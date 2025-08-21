var express=require('express') //obj
var app=express() // mini module
// var dontenv=express('dotenv').config


// var port=express.env.PORT;

var port=2929
//crud operations, delete
app.get('/api/student',(req,res)=>[
    res.send('get all records..................')
])

app.get('/api/student/12',(req,res)=>{
    
    res.send('hello 12')
})

app.post('/api/student/post',(req,res)=>{
    
    res.send('hello post')
})
app.put('/api/student/12',(req,res)=>{
    
    res.send('hello data update')
})
app.delete('/api/student'),(req,res)=>{
    res.send('bye data')
}
app.listen(port,()=>[

    console.log('hello world running on port ' + port)

])