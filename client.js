const mqtt = require('mqtt')
var worker = mqtt.connect('mqtt://localhost:1883')


worker.on("connect",()=>{
    worker.subscribe("message",(err)=>{
        if (!err){
            console.log("Started MQTT Listener!")

        }
    })
})

worker.on("message", (topic,message)=>{
    console.log(`setRecord: ID: ${message.toString()} : completed.`)
})