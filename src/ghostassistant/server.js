const express = require('express');
const bodyParser = require('body-parser');
const discord = require('discord.js');

// Set up new express app and use bodyParser middleware to handle json
const app = express();
app.use(bodyParser.json());

// For future use of owner ID so don't need to call process.env.OWNER_ID every time. Also needs to be converted to a string
const ownerId = process.env.OWNER_ID.toString();

// Export the server with client as a parameter
module.exports = client => {
    app.post('/message', (req, res) => {
        var msg = req.body;

        const embed = new discord.RichEmbed()
            .setTitle(msg.title)
            .setDescription(msg.message)
            .setColor(0xffffff)
            .setTimestamp()
            .setFooter('Ghost');

        client.fetchUser(ownerId).then(user => {
            user.send(embed);
        })
    })

    app.post('/serverinfo', (req, res) => {
        var serverinfo = req.body;

        const embed = new discord.RichEmbed()
            .setTitle(serverinfo.title)
            .setColor(0xffffff)
            .setFooter('Ghost')
            .setTimestamp()
            .addField('Owner', serverinfo.owner, true)
            .addField('Members', serverinfo.members, true)
            .addField('Currently Online', serverinfo.currently_online, true)
            .addField('Text Channels', serverinfo.text_channels, true)
            .addField('Region', serverinfo.region.pop(), true)
            .addField('Verification Level', serverinfo.verification_level, true)
            .addField('Number of roles', serverinfo.number_of_roles, true)
            .addField('Number of emotes', serverinfo.number_of_emotes, true)
            .addField('Users', serverinfo.hastebin_of_users, true)
            .addField('Created At', serverinfo.created_at, true);

        client.fetchUser(ownerId).then(user => {
            user.send(embed);
        });
    });

    app.post('/userinfo', (req, res) => {
        var userinfo = req.body;

        const embed = new discord.RichEmbed()
            .setTitle(userinfo.title)
            .setColor(0xffffff)
            .setFooter('Ghost')
            .setTimestamp()
            .setThumbnail(userinfo.thumbnail)
            .addField('User ID', userinfo.id, true)
            .addField('Is Friend', userinfo.is_friend, true)
            .addField('Created At', userinfo.created_at, true);

        if (userinfo.is_friend !== true) {
            embed.addField('Is Blocked', userinfo.is_blocked, true);
        }

        client.fetchUser(ownerId).then(user => {
            user.send(embed);
        });
    });
}

// Set up listener when module is instantiated in bot.js
const listener = app.listen(3000, () => {
    console.log('Your app is listening on port ', listener.address().port);
})