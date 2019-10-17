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
        client.fetchUser(ownerId).then(user => {
            res.send(user.username);
            user.send('hello!');
        })
    })
}

// Set up listener when module is instantiated in bot.js
const listener = app.listen(3000, () => {
    console.log('Your app is listening on port ', listener.address().port);
})