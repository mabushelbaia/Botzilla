# Botzilla - Discord bot built using [Pycord v2.4](https://pycord.dev/)
## Installation
**Clone the repository**
```bash
git clone https://github.com/mabushelbaia/Botzilla
```
**Install dependencies**
```bash
pip install -r requirements.txt
```
**Create a file called `.env` in the root directory and paste your bot token into it**

## Features

- [X] Team Management
- [X] Random Generators
- [X] Basic Moderation
- [x] Server Statistics **Channels**
## Commands
- `/split` [channel] [team1] [team2] - Splits the members of the voice channel into two teams
- `/roll` - Rolls a random number between 1 and 6
- `/flip` - Flips a coin with a prompt
- `/coin` - Flips a coin without a prompt
- `/server` - Displays server statistics
- `/kick` [member] - Kicks a member from the server
- `/ban` [member] - Bans a member from the server
- `/disconnect` - Disconnects a member from the voice channel
- `/clear` [amount] - Clears a certain amount of messages from the channel
- `/about` [member] - Displays information about a member
- `/ping` - Displays the bot's latency
