const express = require('express');
const router = express.Router(); // Renamed to 'router' for convention

// GET route for the root path
router.route('/').get((req, res) => {
    res.send('get all records..................');
});

// Chained GET and DELETE routes for the '/12' path
router.route('/12')
    .get((req, res) => {
        res.send('hello 12');
    })
    .delete((req, res) => {
        res.send('bye data');
    });

// Correctly export the router object
module.exports = router;