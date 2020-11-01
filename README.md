# discord-py-quickstart

You can use this project to create your own basic [discord.py][discord.py] bot project.

This project sets up Python logging. It includes several extensions that can
load and unload cogs. These extensions include simple examples of:

* A listener (log a little info about each message)
* A command handler (ping)
* Hot reloading
* A way to reference secrets without checking them into source control

## Getting Started

Check out the [Introduction][intro] from the [discord.py][discord.py] documentation.

Now take a look at the [Quickstart][quickstart] section. This section will link to the
documentation on how to [Create a Bot Account][create-account]. Don't forget to save
your bot token.

You can use this project as a [template][template] to create your own bot. Once you've
got your own copy of the project, you'll need to [clone][clone] it onto your own
computer.

Now, you need to add an `authsecrets.py` file in the same directory as this `README.md`
file.

The contents of the `authsecrets.py` file should look like this:

```
BOT_TOKEN='paste your bot token here'
```

## Building and running with Docker

```
docker build --tag discord-py-quickstart:latest .
docker run --rm discord-py-quickstart:latest
```

[clone]: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[create-account]: https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro
[discord.py]: https://discordpy.readthedocs.io/en/latest/index.html
[intro]: https://discordpy.readthedocs.io/en/latest/intro.html
[quickstart]: https://discordpy.readthedocs.io/en/latest/quickstart.html
[template]: https://github.com/binduwavell/discord-py-quickstart/generate
