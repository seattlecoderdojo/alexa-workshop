# Seattle CoderDojo Alexa Skill Workshop
This workshop was originally presented on May 20, 2018

## Shout Outs

A shout out to StarSwap for their [Instructables tutorial](http://www.instructables.com/id/Make-Alexa-Skills-With-Cloud9-No-Credit-Card-or-Ha/). It convinced me that this could be done. The fact that it's broken in multiple ways less than 4 months after publication is a testament to how fast things move in this industry, but it was inspiring.

## Setting up your development environment

You're going to need two things to complete this tutorial.

1. A web-addressable python server. We'll show how to use a Cloud9 workspace as one in this tutorial, but that's just one of many ways to get one for free. 
2. A developer account on https://developer.amazon.com so you can make Alexa skills. This is free. Go sign up.

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

## Making Alexa say "Hello, World"

An Alexa skill has two components... an intent and an intent handler. The intent is defined via the Amazon Developers site, where you set up your skill. The intent handler is built with code on your skill server (here that's the code in our Cloud9 workspace).

#### What is an intent? 

According to the Alexa tech writers: "An intent represents an action that fulfills a user's spoken request." Show of hands, who understands that?
			
Let's actually break down the word "intent." Your intent is what you mean to do, the result you want to create... "I intended to do my homework right after dinner, but I got distracted." "You came here with the intent of learning how to make an Alexa skill."

An "intent" in this case is a set of rules and information that help the Alexa service understand what someone wants to get from talking to Alexa and then give that to the person. To create a skill, you have to set up the intents it will handle.