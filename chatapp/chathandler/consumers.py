from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer

class ChatHandler(AsyncConsumer):

    async def websocket_connect(self,event):
        print("connected !!")

        await self.send(
            {
                "type" : "websocket.accept",
            }
        )



    async def websocket_receive(self,event):
        data = event["text"]
        print(data)
        await self.send({
            "type" : "websocket.receive",
            "text" : "Message recieved on server !!"
        }
        )


    async def websocket_disconnect(self,event):
        print("Connection closed !!")
        await self.send({
            "type": "websocket.dissconnect",
            "text" : "You are good one !!"
        }
        )
        raise StopConsumer()
