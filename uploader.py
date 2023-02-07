import os
import azure.storage.blob as azureblob
import config

def upload_file(file_path, container_name):
    blob_service = azureblob.BlockBlobService(
        account_name=config.STORAGE_ACCOUNT_NAME,
        account_key=config.STORAGE_ACCOUNT_KEY
    )
    blob_name = os.path.basename(file_path)
    blob_service.create_blob_from_path(container_name, blob_name, file_path)
