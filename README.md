## DiscoBackup

Discord bot for backing up and restoring text channels

# Setup

Put your Discord bot token in a text file with any name in an easy-to-access location (project root directory is most convenient).

Now install the required dependencies to run the project.

```
pip install -r requirements.txt  # For required dependencies
```

# Run

Start up the Discord bot.

```
python -m discobackup <tokenfile>  # To run the application
```

Here's an example of how you would run the application given a token file named `bot_token.txt` located in the root directory of the project, assuming that the current working directory of your terminal is this project.

```
python -m discobackup bot_token.txt
```
