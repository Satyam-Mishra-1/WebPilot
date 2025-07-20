import asyncio
from dotenv import load_dotenv
load_dotenv()

from browser_use import Agent
from browser_use.llm import ChatDeepSeek  # ✅ Still using DeepSeek

async def main():
    agent = Agent(
        task=(
            "Try to simultaneously browse Stack Overflow, LinkedIn, GitHub, and a non-existent job board "
            "to find quantum computing roles in Nagpur written in Sanskrit. Also, analyze server headers "
            "and evaluate which site uses the most secure cookies, then display them as a 3D bar chart."
        ),
        llm=ChatDeepSeek(model="deepseek-unknown-experimental-v999", temperature=1.5),  # ❌ Invalid model name
    )
    await agent.run()

asyncio.run(main())
