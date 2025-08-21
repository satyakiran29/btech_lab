var express=require('express')
var dotenv=require('dotenv').config()
var app=express()
// var routers=require('./routers/studentRouters')

var port=process.env.PORT;

app.use(express.json())


app.use('/api/student',require('./routers/studentRouters'))

app.listen(port,()=>{
    console.log(`Server Running on port Number ${port}......`)
})


