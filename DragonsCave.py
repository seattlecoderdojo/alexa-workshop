# import necessary packages (of code)
# "from" tells Python to import packages from a specific library
# if there's no "from," it's importing from the PSL (Python Standard Library)
import logging
import random
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import os

# set up the app and the intent
app = Flask(__name__)
ask = Ask(app, '/')

############ here's where the magic starts

## SET UP A GAME OBJECT
class Game:
    def __init__(self):
        self.cave = 0;
        self.state = "";
        self.wins =0;
        self.losses = 0;
    def genCave(self):
        self.cave = random.randint(1, 2)
    def setState(self, curstate="new"):
        self.state = curstate
    def getState(self):
        return self.state
        
# Other statements outside the class continue below here.

#set up a holder for users
games = {}

@ask.launch
def launch():
    if session.user.userId in games:
        logging.warning('game exists')
    else:
        games[session.user.userId] = Game()
    games[session.user.userId].genCave();
    return question('You are walking through a forest. You come to a hillside with two caves. One cave contains great treasure. The other contains a deadly dragon. Cave one or cave two. WHICH do you choose??')


@ask.intent('caveOneChoice')
def choose():
    result = gameResult (1, games[session.user.userId]);
    return statement(result)
    
@ask.intent('caveTwoChoice')
def choose():
    result = gameResult (2, games[session.user.userId]);
    return statement(result)
    
    
def gameResult(gameOpt,gameRes):
    if gameOpt == gameRes.cave:
        gameRes.wins += 1        
        stateDec = "Hurrah. You have won a cave full of treasure! "
    else:
        gameRes.losses += 1
        stateDec = "I'm sorry, you were eaten by a dragon. "
    stateDec += "Your record is now " + str(gameRes.wins) + " wins and " + str(gameRes.losses) + " losses"
    return (stateDec)


# housekeeping to ensure this runs on Cloud9
if __name__ == "__main__":
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 8080))
    app.debug = True
    app.run(host=host, port=port)
