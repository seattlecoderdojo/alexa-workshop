# Seattle CoderDojo Amazon Alexa Skill Workshop
This workshop was originally presented on May 20, 2018

## Shout Outs

A shout out to StarSwap for their [Instructables tutorial](http://www.instructables.com/id/Make-Alexa-Skills-With-Cloud9-No-Credit-Card-or-Ha/). It convinced me that this could be done. The fact that it's broken in multiple ways less than 4 months after publication is a testament to how fast things move in this industry, but it was inspiring.

Shout out also to mentor Nick Peters who dogfooded the Hello World! project and provided some valuable contributions to this document. 

## Setting up your development environment

You're going to need two things to complete this tutorial.

1. A web-addressable python server. We'll show how to use a Cloud9 workspace as one in this tutorial, but that's just one of many ways to get one for free. 
2. A developer account on https://developer.amazon.com so you can make Amazon Alexa skills. This is free. Go sign up.

### Setting up your Python server

These instructions assume you followed the instructions we provided to request a Cloud9 account and you signed up. We exceeded our 50 team members, but at last check, while new sign-ups got an error message about that, they still got a free account set-up.

**Login to your Cloud9 account and click "Create a new workspace."**

For the workspace name, use "Seattle CoderDojo Alexa Class".  Leave the Description blank. 

Select a Hosted Workspace. Leave it public.

In the "Clone from Git or Mercurial URL" enter the URL for this repository:

​	https://github.com/seattlecoderdojo/alexa-workshop.git

**Select the Python template.**

Then click the "create workspace" button. It will create a workspace.

### Setting up your Python Workspace

We still need to install the Python components you'll need.

In the bash terminal in the lower part of your screen, type 

​	`sudo sh install.sh` 

## Making Amazon Alexa say "Hello, World"

Amazon Alexa skills have two components… intents and intent handlers. An intent is defined via the Amazon Developers site, where you set up your skill. Intent handlers are built with code on your skill server (for this tutorial, the server is your Cloud9 workspace).

### What is an intent? 

According to the Amazon Alexa tech writers: "An intent represents an action that fulfills a user's spoken request." Show of hands, who understands that?
			
Let's actually break down the word "intent." Your intent is what you want to do or the result you want to get. Your *intent* in coming here was to learn how to make an Alexa skill. Maybe you *intend* to go get ice cream after this.

An "intent," in the case of an Amazon Alexa skill, is a set of rules and information that help the Amazon Alexa service understand what someone wants to get from talking to Amazon Alexa and then give that to them. To create a skill, you have to set up the intents it will handle.

### Creating our Hello World intent...

If you're logged into https://developer.amazon.com/home, you'll be in the developer console. In the Amazon Alexa section, choose "Alexa Skills Kit" (the Alexa Voice Service is for building Alexa devices).

In general, you shouldn't have any skills already, assuming this account is new. If you do, we'll ignore them for now. 

**Click the "Create Skill" button.**

You'll be asked to give your skill a name. Obviously something descriptive like MyFirstSkill or HelloWorld is good. 

**Select "Custom" as the skill model, then click the "Create Skill" button.**

Our basic skill template has been created, but we still need to fill in a couple of blanks and add an intent.

**In the lefthand navigation bar, click "Invocation Name."** 

This is where we'll set thename of our skill so we can call it. I call it "my first talker," but you could call it "hello world" or even "steven universe." **Note** how all of those are lower case.

**Click the "Save Model" button near the top of the page.**

Now to add an intent. You have 4 already built in for housekeeping purposes, but we don't need to touch those right now. 

**Click the "add" icon at the top of the intent list.**

Give it the name "HelloWorld" and click the "Create Custom Intent" button to go to the next screen.

At this point it asks for "sample utterances." These are things a user might say to convey this intent. For this we'll go with two. 

**In the Sample Utterances box, type "say hello to me" and then click the plus symbol in the right side of the box to add it. Then type "greet me" and do the same to add your second sample utterance. Finally add "say hello."**

You're done configuring your intent and your skill will be able to respond to all three utterances.  All that's left is to tell Alexa where to find your skill handler.

**Switch over to Cloud 9. **

**Open the HelloWorld.py file. **

**Right click on the file and select "Run."**

You'll get a message in the terminal window stating "Your code is running at https://[workspace name]-[user name].c9users.io."

**Copy that URL. **

**Go back to the Amazon Developers site. ** **Click the "Endpoint" tab on the left.** 

**Select HTTPS as the service endpoint type.**

**In the Default Region, paste the URL you copied from Cloud9.**

**In the box that says "Select SSL certificate type," choose the option that begins with "My development endpoint is a sub-domain of a domain that has a wildcard certificate..."**

**Click the "Save Model" button.**

You'll notice a message pops up saying "If you make any new changes, you will need to rebuild your model for them to take effect." This means we have saved the configuration for our skill, but we still need to build the model of our skill.

**Click on your "HelloWorld" intent from the intents list.** **Click on "Build Model."**

### Testing your skill

Now that everything is running, filled in, and built, it is time to test your skill.

Click on the test tab in the upper menu. If it says "test is disabled for this skill," click the toggle button next to that.

Clicking on the microphone symbol may cause the browser to ask you for permission to access the microphone. Approve it.

Now you can test your skill. 

**Click the microphone and say "ask [skill invocation name] to say hello" or type it in the text box and hit enter.**

If you just ask Amazon Alexa to "say hello," that's all she says. But if you tell Alexa to ask "my first talker" or "steven universe" or whatever name you used to "say hello," you should get back "Hello World."

**To make this more interesting, change "Hello, World" to some other reply.**

And that's the end of this set-up tutorial. Next, let's look at some of the other skill-making lessons by picking another .md file from our repository.

**To make this even more interesting, add another intent and another function for replying to it.**

Tell Alexa to ask your skill to do something else like say she's a teapot and have it get her to respond "I'm a little teapot, short and stout. My handle and spout are virtual."

## All Done?

Have no fear... well, maybe a little. In our next skill, you'll go looking for treasure, but there may be dragons around.

