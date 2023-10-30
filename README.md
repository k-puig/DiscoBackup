# DiscoBackup

Discord bot for backing up and restoring text channels

## Setup

The following instructions assume that the current working directory of your terminal is the project root, but it's not absolutely necessary if you have a unique structure for your filesystem.

- Create a text file containing the bot token.

- Now install the required dependencies to run the project:

```
pip install -r requirements.txt  # For required dependencies
```

## Run

- Start up the Discord bot:

```
python -m discobackup <tokenfile>  # To run the application
```

Here's an example of how you would run the application given a token file named `bot_token.txt` located in the root directory of the project, assuming that the current working directory of your terminal is this project.

```
python -m discobackup bot_token.txt
```
