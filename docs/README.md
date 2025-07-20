# 🔍 WebPilot

**Automate your browser with AI — just write a prompt and watch it work.**

WebPilot lets you control any browser task using AI agents and natural language. It’s powered by [browser-use](https://github.com/browser-use/browser-use) and large language models like GPT-4o, Claude, Gemini, and DeepSeek.

---

## 🚀 Features

- 🌐 Automate browsing, searching, clicking, form filling, and scraping  
- 🧠 Powered by LLMs: OpenAI, Anthropic, DeepSeek, Grok, Gemini & more  
- ⚙️ Works with Playwright & supports Chromium setup  
- 🔌 Supports [Model Context Protocol (MCP)](https://modelcontext.org/)  
- 🧪 Testable via CLI, Web UI, or Claude Desktop integration  
- ☁️ Try hosted version for cloud-based automation  

---

## 🛠️ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Satyam-Mishra-1/WebPilot.git
cd WebPilot
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
playwright install chromium --with-deps --no-sandbox
```

### 3. Add API Keys to `.env`

Create a `.env` file in the root directory and add your keys:

```
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
# Add more as needed
```

### 4. Run Your First Agent

```python
import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from browser_use.llm import ChatOpenAI

async def main():
    agent = Agent(
        task="Compare prices of GPT-4o and DeepSeek-V3",
        llm=ChatOpenAI(model="o4-mini", temperature=1.0),
    )
    await agent.run()

asyncio.run(main())
```


## 🧠 Example Prompts

* "Find top 5 laptops under ₹50,000 and save links."
* "Check my LinkedIn followers and log new ones to Airtable."
* "Apply to ML jobs listed on Indeed and fill forms automatically."

---

## 🌐 Demo Use Cases

| Task              | Description                                        |
| ----------------- | -------------------------------------------------- |
| 🛒 Add to Cart    | "Add these grocery items and check out."           |
| 📩 LinkedIn → CRM | "Add my latest follower to Salesforce."            |
| 📄 Job Apps       | "Read my resume and apply to jobs automatically."  |
| ✍️ Docs           | "Write a thank you letter to Papa in Google Docs." |

---

## 📄 License

MIT License © 2025

---

> Made with ❤️ using AI + Playwright + Python
