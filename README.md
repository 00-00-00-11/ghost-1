# Ghost

Advanced discord self bot that doesn't abuse Discord API.

## Getting started - Docker version coming soon

- Go into the `src` folder, rename `.env.sample` to `.env` in both `client` and `ghostassistant`. Fill in all of the required values in both with real api keys and user ids.

Client:

- If you don't already have it installed, install pipenv. MacOS with brew: `brew install pipenv`
- Go into client folder, run `pipenv shell` followed by `pipenv install`. Run `python3 app.py` and you should now have the client up and running!

Server:

- If you do not already have node installed, install it!
- Go into the ghostassistant folder, run `npm install` to get all of the node packages.
- Run `node bot.js` to get the server up and running.

Web:

- If you do not have Postgres installed, install it!
- Go into `src/web/` and rename .env.example to .env and fill out the appropriate fields.
- From there, go to `web/` and open `settings.py`.
- Go down to the `DATABASES` option.
- Edit the user to be your postgres user.
- Run `psql` in your terminal once you have postgres installed, and then run `CREATE DATABASE ghostsite OWNER name;` with name being your postgres user.
- Run `python3 manage.py migrate` and then run `python3 manage.py runserver` and the webserver should be up and running.
- For more information on how to get the postgres database setup, refer to [this](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/) website tutorial.

Congrats! You now have a self hosted version of Ghost and Ghost Assistant!

## Need to change for deployment

- Discord redirect URL to real url
- Change URL in django all-auth social application
