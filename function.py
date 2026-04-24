import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(
    arg_name="myblob",
    path="samples-workitems/{name}",
    connection="AzureWebJobsStorage"
)
def blob_trigger_function(myblob: func.InputStream):
    logging.info(
        f"Blob trigger fired!\n"
        f"Name: {myblob.name}\n"
        f"Size: {myblob.length} bytes"
    )

    content = myblob.read()
    logging.info(f"Content preview: {content[:200]}")

    # Processing logic goes here