# **Lesson 2: Exploring the Dragon's Cave**

Now that you've got your server set up and have successfully ran your first Hello World, let's make Amazon Alexa play a simple game... The Dragon's Cave.

Since we're doing this in Python, I thought it would be great to borrow one of the early games from Al Sweigart's amazing book "[Invent Your Own Computer Games with Python, 4th Edition](https://inventwithpython.com/#invent)." He calls it "Dragon Realm," but it's a classic game I recall by another name.

In the game you are an adventurer who has come to a clearing where there are the mouths of two caves, In one is a lot of treasure. In the other is a nasty dragon who will eat you. You select the cave you want to go into, the computer flips a coin behind the scenes, and boom... you're either rich or dead.

## Setting up your Amazon Alexa Skill

Let's go back to developer.amazon.com and [go to your skills console](https://developer.amazon.com/alexa/console/ask). Create a new skill and  name it Dragon's Cave, select a custom skill, and create it. When we get to the main control panel, we have a few things to set up...

### Invocation name

Let's go with "dragon's cave".

Now because we'll be opening the skill with its invocation name instead of asking for it to do something by proxy, we don't need a launcher intent.

### Intent 1: caveOneChoice

This is where players will be able to select the first cave. But what might they call it? Let's set up a bunch of sample utterances for it... "one, cave one, left, left cave, the first one, first cave the first."



### Intent 2: caveTwoChoice

We'll do a similar thing here... "Second one, second cave, second, right, tight cave two cave two."



### Set the Endpoint and Build it

Use the same endpoint you used for Hello World. Then build the skill.