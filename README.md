# About

As the description of this repository states, this discord bot mimics the character CYN from Murder Drones.

So far, When you talk in the chat, it spits out random quoths directly from the show itself. Very uneventful, but here is my roadmap on this project:

- [] Integrate to llm (ChatGPT, Gemini or Local) instead of picking quoths from the show
- [] Commands with some games (Rock Paper Scissors and such, yeah it's a work in progress) 

# Setup
```bash
# entering the virtual environment
python -m venv ./.venv
source .venv/bin/activate

# installing necessary dependencies
pip instal -r ./requirements.txt


# running the bot:
python ./main
```

> IMPORTANT: In your environment you need to set the `DISCORD_TOKEN` and `DISCORD_GUILD` environment variables in `.env` file. To get those, ask me first

# FAQ:

### Why?
- I got a raspberry PI. Not sure what to do with it, so I made a discord bot

### Why CYN Tho?
- She's so silly :3