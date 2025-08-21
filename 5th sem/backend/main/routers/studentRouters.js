var express=require('express')
var routers=express.Router()
const {getStudent,getStudents,insertStudent,updatedStudent,deleteStudents,deleteStudnet}=require('../controller/studentController')

routers.route('/').get(getStudents).post(insertStudent).delete(deleteStudents)

routers.route('/:id').get(getStudent).put(updatedStudent).delete(deleteStudnet)


module.exports=routers