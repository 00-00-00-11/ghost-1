const discord = require('discord.js');
const client = new discord.Client();
require('dotenv').config()
// require('./server')(client)

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);
});

client.on('message', msg => {
    if (msg.content == 'test') {
        msg.reply('the bot is working :)');
    }
});

client.login(process.env.BOT_TOKEN);