# MCP Server (S3 Access Tool)

This Model Context Protocol (MCP) server integrates with Claude Desktop to list and interact with AWS S3 buckets using Britive.

---

## Prerequisites

1. **Python 3.13+ installed**
   - Check: `python3 --version`
   - On macOS: Hight recommended to use a **virtual environment** (details below)

2. **Claude Desktop installed**
   - Download from: [https://claude.ai](https://claude.ai)
   - Open the app and make sure you can see **Settings → Developer Mode**. Close it now.
  
<img width="1146" height="640" alt="image" src="https://github.com/user-attachments/assets/b836fc5a-f123-446e-b0f6-d4b3f5299776" />




3. **Britive API Token**
   - Generate a Britive token for your service identity and add it to a Britive policy that has **at least `s3:ListAllMyBuckets`** permission.

---

## Required Python Packages

Install dependencies:

pip install boto3 requests fastmcp

If using a virtual environment:

python3 -m venv venv

source venv/bin/activate

pip install boto3 requests fastmcp

---

##

Copy the included MCP server python file to your machine.  Try running the python file and it should run.

python mcp-s3-buckets.py

or

python3.13 mcp-s3-buckets.py (depending on how the virtual env was setup)


<pre>



╭─ FastMCP 2.0 ──────────────────────────────────────────────────────────────╮
│                                                                            │
│        _ __ ___ ______           __  __  _____________    ____    ____     │
│       _ __ ___ / ____/___ ______/ /_/  |/  / ____/ __ \  |___ \  / __ \    │
│      _ __ ___ / /_  / __ `/ ___/ __/ /|_/ / /   / /_/ /  ___/ / / / / /    │
│     _ __ ___ / __/ / /_/ (__  ) /_/ /  / / /___/ ____/  /  __/_/ /_/ /     │
│    _ __ ___ /_/    \__,_/____/\__/_/  /_/\____/_/      /_____(_)____/      │
│                                                                            │
│                                                                            │
│                                                                            │
│    🖥️  Server name:     Britive API MCP                                     │
│    📦 Transport:       STDIO                                               │
│                                                                            │
│    📚 Docs:            https://gofastmcp.com                               │
│    🚀 Deploy:          https://fastmcp.cloud                               │
│                                                                            │
│    🏎️  FastMCP version: 2.10.5                                              │
│    🤝 MCP version:     1.11.0                                              │
│                                                                            │
╰────────────────────────────────────────────────────────────────────────────╯


[07/14/25 13:16:42] INFO     Starting MCP server 'Britive API MCP' with transport 'stdio'




Open Claude, go to developer settings, edit config, and then open the claude_desktop_config.json file. 
You should see following 

{
  "mcpServers": {
    "s3agent9": {
      "command": "/Users/shahzadali/Library/CloudStorage/OneDrive-britive,Inc/Britive_Github/Agentic AI MCP S3 Access Tool/venv/bin/python",
      "args": ["/Users/shahzadali/Library/CloudStorage/OneDrive-britive,Inc/Britive_Github/Agentic AI MCP S3 Access Tool/mcp-s3-buckets.py"],
      "env": {
        "BRITIVE_API_KEY": "Your Key"
      }
    }
  }
}

</pre>

Use the provided example, and customize file paths for Mac or PC.

Restart Claude, and ask it "What s3 buckets do I have"

## Reference to use Python Virtual Environment 

<pre>

Create a virtual environment for your project:
# Navigate to your project directory (Mac Example)
cd "/Users/shahzadali/Library/CloudStorage/OneDrive-britive,Inc/Britive_Github/Agentic AI MCP S3 Access Tool"

# Create a virtual environment
python3.13 -m venv venv

# Activate it
source venv/bin/activate

# Install your dependencies
pip install fastmcp requests boto3

# Run your script
python mcp-s3-buckets.py

When you're done working, you can deactivate the virtual environment:
deactivate

</pre>
