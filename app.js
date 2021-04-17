
const express = require('express')
const mqtt = require('mqtt')

const app = express()

const mongo = require("mongoose");
const { request, response } = require('express');
mongo.connect('mongodb+srv://sun:5JHb!gagy9CkJzZ@cluster0.dycgj.mongodb.net/Test?retryWrites=true&w=majority', {useNewUrlParser: true, useUnifiedTopology: true});

const db = mongo.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  console.log("connected to mongoDB")
});

const bookbankSchema = new mongo.Schema({
    name: String,
    author: String
})
bookbankSchema.methods.details = function(){
    console.log(`Name: ${this.name}, Author: ${this.author}`)
}

const bookbank = mongo.model("BookBank",bookbankSchema)

function CreateBook(name,writer){
  var b = new bookbank({
    name:name,
    author:writer
  })
  b.save((e,d)=>{
    if (!(e)){
        var worker = mqtt.connect('mqtt://localhost:1883')
        worker.on("connect",()=>{
            worker.subscribe("message",(err)=>{
                if (!err){
                    worker.publish("message",String(d._id))
                    console.log(`setRecord Successful for ${d._id}`)
                }
            })
        })
    }
    else {
        console.log(e)
    }
  })
}

// MQTT PART
//


app.get('/setRecord',(request,response)=>{
    var book = request.query.book
    var author = request.query.author
    var d = CreateBook(book,author)
    response.send("saved")
})

app.get("/getRecord",(request,response)=>{
    var id = request.query.id
    bookbank.findById(id , {__v:0 ,_id:0} , (error,data)=>{
        response.send(data)
    })
})


console.log("Server Start!")
console.log("waiting for mongoDB to start")
app.listen(3000)