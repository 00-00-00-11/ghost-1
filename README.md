# Ghost

Advanced discord self bot that doesn't abuse Discord API.

## Getting started - Docker version coming soon!

- Go into the `src` folder, rename `.env.sample` to `.env` in both `client` and `ghostassistant`. Fill in all of the required values in both with real api keys and user ids.

Client:

- If you don't already have it installed, install pipenv. MacOS with brew: `brew install pipenv`
- Go into client folder, run `pipenv shell` followed by `pipenv install`. Run `python3 app.py` and you should now have the client up and running!

Server:

- If you do not already have node installed, install it!
- Go into the ghostassistant folder, run `npm install` to get all of the node packages.
- Run `node bot.js` to get the server up and running.

Congrats! You now have a self hosted version of Ghost and Ghost Assistant!