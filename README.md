# Seattle CoderDojo Amazon Alexa Skill Workshop
This workshop was originally presented on May 20, 2018

## Shout Outs

A shout out to StarSwap for their [Instructables tutorial](http://www.instructables.com/id/Make-Alexa-Skills-With-Cloud9-No-Credit-Card-or-Ha/). It convinced me that this could be done. The fact that it's broken in multiple ways less than 4 months after publication is a testament to how fast things move in this industry, but it was inspiring.

## Setting up your development environment

You're going to need two things to complete this tutorial.

1. A web-addressable python server. We'll show how to use a Cloud9 workspace as one in this tutorial, but that's just one of many ways to get one for free. 
2. A developer account on https://developer.amazon.com so you can make Amazon Alexa skills. This is free. Go sign up.

### Setting up your Python server

These instructions assume you followed the instructions we provided to request a Cloud9 account and you signed up.

Login to your Cloud9 account and click "Create a new workspace."

For the workspace name, use whatever you want. You can also use whatever description you want. 

The team should already be selected as "Seattle CoderDojo."

Click "Clone Workspace" and for the workspace select "yiddishninja/alexa-workshop."

Then click the "create workspace" button. It will create a workspace ready to run the Hello World program we'll work with first.

> **FOR OTHER INSTRUCTORS**
>
> You won't be able to clone our workspace. This repository contains all the scripts you'll need. To get the Cloud9 workspace ready to run them, you'll need to run a handful of commands.
>
> ```shell
> sudo -H pip2 install --upgrade pip
> sudo python -m pip install pip==9.0.3 --upgrade --force-reinstall 
> sudo -H pip install 'cryptography<2.2'
> sudo -H pip install flask
> sudo -H pip install flask-ask
> ```
>
> The second line is because the most recent version of `pip` (at the time of this writing) actually breaks the `flask-ask` installation, so after upgrading `pip`  a few versions, you then have to downgrade it one. Then you need to install the `cryptography` package because it's a dependency that doesn't get installed automatically and is needed to handle the encrypted requests from Amazon to your server.

## Making Amazon Alexa say "Hello, World"

An Amazon Alexa skill has two components... an intent and an intent handler. The intent is defined via the Amazon Developers site, where you set up your skill. The intent handler is built with code on your skill server (here that's the code in our Cloud9 workspace).

### What is an intent? 

According to the Amazon Alexa tech writers: "An intent represents an action that fulfills a user's spoken request." Show of hands, who understands that?
			
Let's actually break down the word "intent." Your intent is the the reason you do something, related to the result you want to get. Your intent in coming here was to learn how to make an Alexa skill.

An "intent" in this case is a set of rules and information that help the Amazon Alexa service understand what someone wants to get from talking to Amazon Alexa and then give that to the person. To create a skill, you have to set up the intents it will handle.

### Creating our Hello World intent...

If you're logged into https://developer.amazon.com/home, you'll be in the developer console. In the Amazon Alexa section, choose "Alexa Skills Kit" (the Alexa Voice Service is for building Alexa devices).

In general, you shouldn't have any skills already, assuming this account is new. If you do, we'll ignore them for now. For now you want to click the "Create Skill" button.

You'll be asked to give your skill a name. Obviously something descriptive like MyFirstSkill or HelloWorld is good. Then you'll be asked to select a skill model. Select "Custom" and then click the "Create Skill" button on that page.

Our basic skill template has been created, but we still need to fill in a couple of blanks and add an intent.

First, in the lefthand navigation bar, click "Invocation Name." This is where we'll set thename of our skill so we can call it. I call it "my first talker," but you could call it "hello world" or even "steven universe." **Note** how all of those are lower case.

Now to add an intent. You have 4 already built in for housekeeping purposes, but we don't need to touch those right now. Click the "add" icon at the top of the list.