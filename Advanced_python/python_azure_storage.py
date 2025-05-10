import io
import os
from azure.storage.blob import BlobServiceClient
from PIL import Image
# Azure Storage connection details (replace with your actual values)
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = "images"  # Name of your container
# Function trigger and bindings
def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()
        # Extract the blob name from the request body (adjust based on your trigger setup)
    try:
        blob_name = req_body.get('blob_name') 
        if not blob_name:
            return func.HttpResponse(
                "Please pass a blob name in the request body",
                status_code=400
            )
    except ValueError:
        return func.HttpResponse(
             "Invalid JSON format in request body",
             status_code=400
        )
    # Create a BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # Download the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    image_data = blob_client.download_blob().readall()
    try:
        # Resize the image
        image = Image.open(io.BytesIO(image_data))
        resized_image = image.resize((500, 500))  # Example resize to 500x500 pixels

        # Save the resized image to an in-memory buffer
        output_buffer = io.BytesIO()
        resized_image.save(output_buffer, format="JPEG")  # Adjust format if needed
        output_buffer.seek(0)
        # Upload the resized image (e.g., to a "resized" folder in the same container)
        resized_blob_name = f"resized/{blob_name}" 
        resized_blob_client = blob_service_client.get_blob_client(container=container_name, blob=resized_blob_name)
        resized_blob_client.upload_blob(output_buffer, overwrite=True)
        return func.HttpResponse(f"Image '{blob_name}' resized and saved as '{resized_blob_name}'")
    except Exception as e:
        return func.HttpResponse(f"Error processing image: {str(e)}", status_code=500)