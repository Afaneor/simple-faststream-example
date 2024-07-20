import logging
from faststream import FastStream
from faststream.rabbit import RabbitBroker
from pydantic import BaseModel

logger = logging.getLogger('faststream')

broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
app = FastStream(broker)


class BaseMessage(BaseModel):
    message: str


@broker.subscriber('test')
async def base_subscriber(message: BaseMessage):
    logger.info(f'Received message: {message}')
