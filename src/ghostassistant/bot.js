const discord = require('discord.js');
const client = new discord.Client();
require('dotenv').config()
require('./server')(client)

// Run when the bot sends a ready event
client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);
});

// Run when message event is sent by client - could be used for commands but not something we are going to need it for
client.on('message', msg => {
    if (msg.content == 'test') {
        msg.reply('the bot is working :)');
    }
});

// Run the bot with the token that we store in the .env file
client.login(process.env.BOT_TOKEN);