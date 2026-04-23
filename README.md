# Azure Blob Trigger Function ☁️

This is my first ever Azure project and honestly what a way to start. 📈

It's a serverless Python function that automatically fires whenever a file gets uploaded to Azure Blob Storage. No manual triggers, no polling in a loop, just drop a file and the cloud does the work.

I built this to get my hands dirty with cloud architecture for the first time and understand how event-driven, serverless systems actually work in practice. Cloud computing clicked for me in a whole new way after this one.

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

This being my first Azure project, a lot was new to me and I picked up more than I expected:

- What event-driven architecture actually means in practice, not just as a concept
- How serverless removes the infrastructure layer entirely and lets you just focus on logic
- The Azure Functions v2 Python programming model and how triggers and bindings work
- How to emulate cloud services locally with Azurite so you're not deploying every single change to test it
- How to structure a cloud project properly from the start: config, secrets management, deployment

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
