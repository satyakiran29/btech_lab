var fs=require('fs')

var getStudents=(req,res)=>{
    // res.send('Get all Records....')
    fs.readFile(__dirname+'/'+'data.json','utf8',(err,data)=>{
        if(err)
            res.status(500).json({message:'Bad Request.........'})
        else
            res.send(data)
    })
}

var getStudent=(req,res)=>{
    // res.send(`Get the record with id ${req.params.id}`)
     fs.readFile(__dirname+'/'+'data.json','utf8',(err,data)=>{
        if(err)
            res.status(500).json({message:'Bad Request.........'})
        else{
         const result=JSON.parse(data).users
         const user=result.filter(item=>item.id===parseInt(req.params.id))
         if(Object.keys(user).length==0)
            res.status(404).json({error:'Record not found.....'})
        else
             res.send(user) 
        }
    })
}

var insertStudent=(req,res)=>{
    const newUser=req.body
    // res.send('New Record Created Successfully......')
   fs.readFile(__dirname+'/data.json','utf8',(err,data)=>{
    if(err)
        res.status(500).json({error:"Couldn't read the data....... "})

    const users=JSON.parse(data).users

    if(!newUser.name || !newUser.email ) 
        res.status(404).json({error:'Provide the data for all parameters......'})

    newUser.id=users.length?users[users.length-1].id+1:1

    users.push(newUser)

    fs.writeFile(__dirname+'/data.json',JSON.stringify({users},null,2),(err)=>{
        if(err)
            res.status(404).json({error:'Insertion Unsuccessfull.....'})
        else{
            res.status(201).json({message:'Insertion Successfulll....',
                newUser
            })
        }
    })


   })
}

var updatedStudent=(req,res)=>{
    // res.send(`Recored ${req.params.id} updated Successfully....`)
    const uid=parseInt(req.params.id)
    const {name,email,age,gender,isActive}=req.body
    fs.readFile(__dirname+'/data.json','utf8',(err,data)=>{
        if(err)
            res.status(500).json({error:"Couldn't read the data....."})

        const users=JSON.parse(data).users
        const user=users.find(u=>u.id===uid)

        if(!user)
            res.status(404).json({error:'User not existed.......'})

        if(name) user.name=name
        if(email) user.email=email
        if(age) user.age=age
        if(gender) user.gender=gender
        if(isActive) user.isActive=isActive

        fs.writeFile(__dirname+'/data.json',JSON.stringify({users},null,2),(err)=>{
            if(err)
                res.status(400).json({error:'Updation Unscessfully......'})
            else{
                res.status(201).json({message:'Updataion Successfully Completed....',
                    users
                })
            }
        })

    })
}

var deleteStudents=(req,res)=>{
    res.send('All Record deleted Successfully......')
}

var deleteStudnet=(req,res)=>{
    // res.send(`Record ${req.params.id} is deleted Successfully......`)
    const uid=parseInt(req.params.id)
    fs.readFile(__dirname+'/data.json','utf8',(err,data)=>{
        if(err)
            res.status(500).json({error:"Couldn't read data from file......"})

        const users=JSON.parse(data).users
        const index=users.findIndex(u=>u.id===uid)
        if(index==-1)
            res.status(404).json({error:'Record not found....'})

        const deleted=users.splice(index,1)[0]

        fs.writeFile(__dirname+'/data.json',JSON.stringify({users},null,2),(err)=>{
            if(err)
                res.status(404).json({error:'Record Deletion Unseccessfull.....'})
            else{
                res.status(201).json({message:`Deleted the record with ${uid} Successfully....`,
                deleted
                })
            }
        })
    })
}

module.exports={getStudent,getStudents,insertStudent,updatedStudent,deleteStudents,deleteStudnet}