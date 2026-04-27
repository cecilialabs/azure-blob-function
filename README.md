# Azure Blob Trigger Function ☁️

This is my first ever Azure project and honestly what a way to start. 📈

It's a serverless Python function that automatically fires whenever a file gets uploaded to Azure Blob Storage. No manual triggers, no polling in a loop, just drop a file and the cloud does the work.

I built this to get my hands dirty with cloud architecture for the first time and understand how event-driven, serverless systems actually work in practice. After this, my understanding of cloud computing reached a new level.

---

## What's actually going on here

The idea is simple. You upload a file to a Blob Storage container, Azure detects that event and the function kicks off automatically. It reads the file, logs what it finds and from there you can plug in whatever processing logic you need.

Think parsing CSVs, transforming JSON, routing files to different containers, writing results to a database. The trigger handles the "when", you just write the "what".

```
File uploaded to Blob Storage
        ↓
Azure detects the event
        ↓
BlobTriggerFunction fires automatically
        ↓
File is read + processed
```

No servers to spin up. No cron jobs. Just an event and a response. That's the beauty of serverless.

---

## Project structure

```
azure-blob-function/
├── function_app.py       # Where the magic happens — blob trigger logic
├── requirements.txt      # Python dependencies
├── host.json             # Azure Functions host config
├── .gitignore            # Keeps the junk out
└── README.md             # You're reading it!
```

> One thing to note 📝 `local.settings.json` is intentionally left out of this repo. It holds your connection strings and secrets, so it should never go anywhere near GitHub.

---

## What you'll need before running this

- Python 3.11+
- Azure Functions Core Tools v4
- VS Code with the Azure Functions extension installed
- Azurite extension (this emulates blob storage locally, super handy!)
- An Azure account (free tier works fine to get started)

---

## Running it locally

**1. Install the dependencies**
```bash
pip install -r requirements.txt
```

**2. Create a `local.settings.json` file in the project root**

This file stays local, don't commit it!

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python"
  }
}
```

**3. Start Azurite**

In VS Code hit `Cmd+Shift+P` and search for `Azurite: Start`

**4. Start the function**
```bash
func start
```

**5. Test it out**

- Open the Azure panel in the VS Code sidebar
- Go to Azurite → Blob Containers
- Create a container called `samples-workitems`
- Upload any file, a `.txt`, `.csv`, whatever's around
- Watch the terminal and you'll see the function fire in real time ✅

---

## The actual function

```python
import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(
    arg_name="myblob",
    path="samples-workitems/{name}",
    connection="AzureWebJobsStorage"
)
def BlobTriggerFunction(myblob: func.InputStream):
    logging.info(
        f"Blob trigger fired!\n"
        f"Name: {myblob.name}\n"
        f"Size: {myblob.length} bytes"
    )

    content = myblob.read()
    logging.info(f"Content preview: {content[:200]}")

    # Processing logic goes here
```

---

## What I learned building this

**Cloud Architecture & Azure**
- Event-driven architecture isn't just theory, it's a practical pattern that eliminates polling and simplifies workflows
- Serverless means you truly stop thinking about infrastructure and focus only on business logic
- Azure Functions v2 Python model is clean and intuitive once you understand decorators and bindings
- Blob Storage triggers are powerful for building reactive systems that respond to file events

**Development & Debugging**
- Local development with Azurite is crucial! test everything before deploying to real Azure
- Understanding TCP ports, process management and system level debugging (lsof, kill commands)
- How to troubleshoot cloud tools - permissions issues, connection strings, environment paths
- The importance of clear `.gitignore` files to protect secrets and local-only files

**Professional Workflow**
- Proper Git workflow with meaningful commit messages that tell the story of development
- Structuring a cloud project correctly from the start - config files, secrets management, clean dependencies
- Writing documentation that's honest and helps others (and future me) understand the project
- Setting up local development environments for cloud tools requires careful project structure

**Problem-Solving**
- Renaming `function.py` to `function_app.py` - learning that Azure Functions has specific file naming requirements
- Fixing permission issues with Homebrew and global package installations
- Understanding how file paths affect local development and Azure tooling
- Reading verbose logs to understand what's actually happening under the hood

First project down. Many more to come.

---

## Tech used

- Azure Functions v4 - Python
- Azure Blob Storage trigger
- Python 3.11
- Azurite for local blob emulation
- VS Code + Azure Functions extension

---

## Author

**Cecilia | @cecilialabs** : [github.com/cecilialabs](https://github.com/cecilialabs)

Always building, always learning. 🧠 🌷 
