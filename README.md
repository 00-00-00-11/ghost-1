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
- Run `psql` in your terminal once you have postgres installed, and then run `CREATE DATABASE ghostsite OWNER name;` with name being your postgres user. This will create the database that the website will use.
- Run `python3 manage.py migrate` and then run `python3 manage.py runserver` and the webserver should be up and running.
- For more information on how to get the postgres database setup, refer to [this](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/) tutorial. Reach out to me if you have any other problems and I will do my best to troubleshoot them.

Congrats! You now have a self hosted version of Ghost and Ghost Assistant!

## Need to change for deployment

- Discord redirect URL to real url
- Change URL in django all-auth social application

## Stuff to Do

- [ ] Refactor all .env files into one .env file for easier management.
- [ ] Improve this README with better documentation that will make for an easier deploy down the line.
- [ ] Allow a user to spin up a new self bot under their user account from the website that allows them to manage it.
- [ ] Implement self-moderation / aditional commands
- [ ] Rate-limit the purge command as to not be detected.
- [ ] Refactor how I do sessions when posting data to the webserver to make everything run faster.
- [ ] Create user dashboard where users can manage their account.
- [ ] Figure out how the fuck I am going to deploy all 3 applications at the same time easily. Docker? Kuberneties? Microservices? Idk will figure it out when the time comes lmao.
- [ ] Create a flag to run everything in 'development' rather than production mode so that I do not have to manually change all settings from production to development.
- [ ] Maybe split requirements for each app up? This would be done when I dockerize the applciation. Would be nice for it to be modular.
- [ ] Create a way to spin everything up locally with 1 command, probably going to use docker for this.
- [ ] Create template overrides for default templates that are used by django-allauth package.
- [ ] Figure out a better way to use postgres than psycopg2 because I know it is going to be a bitch and a half to deploy.
