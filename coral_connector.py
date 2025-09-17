import asyncio
from mcp.client import sse_connect
from mcp.types import Request

CORAL_SERVER_URL = "http://localhost:5555/devmode/exampleApplication/privkey/session1/sse"

async def main():
    # Connect to the Coral server via SSE
    async with sse_connect(CORAL_SERVER_URL) as (reader, writer):
        print("✅ Connected to Coral Server")

        # Example: send a simple "ping" request
        req = Request(method="echo", params={"message": "hello from my agent"})
        await writer.send(req)

        # Listen for messages from the server
        async for event in reader:
            print("📩 Event from Coral:", event)

if __name__ == "__main__":
    asyncio.run(main())
