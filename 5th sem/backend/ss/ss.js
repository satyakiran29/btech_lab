var express=require('express') //obj
var dotenv=express('dotenv').config//npm install express dotevn
var app=express() // mini module
var port=3000

var port=express.env.port;

app.get('/api/student',(req,res)=>[
    res.send('get all records..................')
])

app.listen(port,()=>[
    console.log("running on dotenv $[port]")
])