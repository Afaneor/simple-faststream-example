import logging

from faststream import FastStream
from faststream.rabbit import RabbitBroker
from pydantic import BaseModel

logger = logging.getLogger('faststream')

broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
app = FastStream(broker)


class BaseMessage(BaseModel):
    message: str


@app.after_startup
async def setup(*args, **kwargs):
    await broker.publish(BaseMessage(message='Hello, World!'), 'test', )
