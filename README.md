# discord-py-quickstart

You can use this project to [create][template] your own basic
[discord.py][discord.py] bot project.

This project sets up Python logging. It includes several extensions that can
load and unload cogs. These extensions include simple examples of:

* A listener - log a little info about each member message
* A command handler - ping/pong
* Hot reloading - attempts to reload extensions when you save an edit
* A way to reference secrets without checking them into source control
* How to use Docker to run your bot

As an alternative to this project, there is a way to have discord.py stamp out a new
very basic bot for you.

```shell
> python -m discord newbot -h
usage: discord newbot [-h] [--prefix <prefix>] [--sharded] [--no-git] name [directory]

positional arguments:
  name               the bot project name
  directory          the directory to place it in (default: .)

optional arguments:
  -h, --help         show this help message and exit
  --prefix <prefix>  the bot prefix (default: $)
  --sharded          whether to use AutoShardedBot
  --no-git           do not create a .gitignore file
```

## Getting Started

Check out the [Introduction][intro] in the [discord.py][discord.py] documentation.

Now take a look at the [Quickstart][quickstart] section. This section will link to the
documentation on how to [Create a Bot Account][create-account]. Don't forget to save
your bot token.

NOTE: This assumes you have `git`, a version of `python3` (version 3.5.3 or higher)
and a c/c++ compiler that python can use to to compile native modules on your
computer. If necessary you can run the bot in a Docker container that has python3
and a c/c++ compiler. Instructions later in this doc.

You can use this project as a [template][template] to create your own bot. Once you've
got your own copy of the project, you'll need to [clone][clone] it onto your own
computer.

Now, you need to add an `authsecrets.py` file in the src directory. The contents of
this file should look like this:

```python
BOT_TOKEN='paste your bot token here'
```

## Local development

Setup a python virtual environment, and then install the required dependencies:

<details>
<summary>Mac/Unix</summary>

```shell
python3 -m venv .env
source .env/Scripts/activate
pip install -r requirements.txt
```

</details>

<details>
<summary>Windows</summary>

```shell
python3 -m venv .env
.env/Scripts/activate.exe
pip install -r requirements.txt
```

</details>

Once you have things setup you can start the bot like this:

```shell
python src/bot.py
```

With the hot reloading feature, you should be able to make edits to
the existing command and the changes should be picked up when you
save your file. If you add or remove commands, you will need to
restart the bot.

If you start a new shell you will need to re-activate the virtual
environment with the activate script.

## Building and running with Docker

Following are some basic instructions for creating a Docker image that
will run your bot. This uses a rather heavy python base image in order
to not need to manage installing a C++ compiler. For a production
deployment you will likely want to create an image based on a more
streamlined base image.

```shell
docker build --tag discord-py-quickstart .
docker run -it --rm discord-py-quickstart
```

If you don't wish to use a local install of python, it is possible to
live mount the source code of this project with a volume into the
Docker container. This then allows interactive development without
relying on a local install of python.

<details>
<summary>Mac/Unix</summary>

```shell
docker run -it --rm -v $PWD/src:/usr/src/app discord-py-quickstart
```

</details>

<details>
<summary>Windows</summary>

```shell
docker run -it --rm -v %CD%\src:/usr/src/app discord-py-quickstart
```

There are some more official Docker images for discord.py [here][docker].

</summary>

[clone]: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[create-account]: https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro
[discord.py]: https://discordpy.readthedocs.io/en/latest/index.html
[docker]: https://github.com/Gorialis/discord.py-docker
[intro]: https://discordpy.readthedocs.io/en/latest/intro.html
[quickstart]: https://discordpy.readthedocs.io/en/latest/quickstart.html
[template]: https://github.com/binduwavell/discord-py-quickstart/generate
