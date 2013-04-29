# What is it?

A bot that takes your google talk bot name, then forwards any message to an HTTP endpoint and replies with whatever comes back.

# Usage

You need to set 3 (or 4) environment variables for this bot to work.  They are,

* BOT_NAME - the name of your bot, defaults to 'HTTP Bot'
* BOT_URL - the URL that your bot GET's messages to
* BOT_GTALK_USER - the GTalk user ID for your bot
* BOT_GTALK_PASSWORD - the GTalk password for your bot

If you want to use Foreman, then put these into a file called '.env' and then just run

	$ foreman start

Easy.

# Why?

For Alex!
