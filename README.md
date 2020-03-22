<!--
title: Serverless Telegram Bot
description: Serverless Framework boilerplate for a telegram chat-bot.
layout: Doc
framework: v1
platform: AWS
language: Python
authorLink: 'https://github.com/demondehellis'
authorName: 'Dmitry G'
-->

### Installing
```
# Install the Serverless Framework
$ npm install serverless -g

# Install the necessary plugins
$ npm install

# Get a bot from Telegram, sending this message to @BotFather
$ /newbot

# Put the token received into a file called serverless.env.yml, like this
$ cat serverless.env.yml
TELEGRAM_TOKEN: <your_token>

# Deploy it!
$ serverless deploy

# With the URL returned in the output, configure the Webhook
$ curl -X POST https://<your_url>.amazonaws.com/dev/set_webhook
```

Now, just start a conversation with the bot.
