import asyncio
import mqttools


HOST = 'test.mosquitto.org'
PORT = 1883


async def main():
    client = mqttools.Client(HOST, PORT, 'incrementer')
    await client.start()
    print(f'Connected to {HOST}:{PORT}.')
    await client.subscribe('/mqttools/incrementer/value/request', 0)

    print('Subscribed to topic /mqttools/incrementer/value/request.')

    while True:
        _, message = await client.messages.get()
        count = int(message)
        print(f'Request count:  {count}')
        count += 1
        print(f'Response count: {count}')
        await client.publish('/mqttools/counter-client/value/response',
                             str(count).encode('ascii'),
                             0)


asyncio.run(main())
