from fastapi import FastAPI
from file_upload import upload_file_to_drive_url
from fastapi.openapi.models import Info
from pydantic import BaseModel

app = FastAPI()
app.openapi = Info(
    title="Your API Title",
    version="1.0",
    description="Your API description",
    contact={
        "name": "Your Name",
        "url": "https://example.com/contact",
        "email": "your.email@example.com",
    },
)


class FileParams(BaseModel):
    file_path: str


@app.get("/")
async def my_first_get_api():
    return {"message": "First FastAPI example"}


@app.post("/drive/image-client")
async def upload_image_client_to_drive(file: FileParams):
    """
    Upload an image for the image-client category to Google Drive.

    Parameters:
      - file: FileParams - JSON body with the file_path parameter.

    Response:
      - 200: Successful file upload with the file URL.
      - 500: Failed to upload file.
    """
    return upload_file_to_drive_url(file.file_path, "image-client", ['jpg', 'jpeg', 'png'])


@app.post("/drive/image-vihecule")
async def upload_image_vihecule_to_drive(file: FileParams):
    """
    Upload an image for the image-vihecule category to Google Drive.

    Parameters:
      - file: FileParams - JSON body with the file_path parameter.

    Response:
      - 200: Successful file upload with the file URL.
      - 500: Failed to upload file.
    """
    return upload_file_to_drive_url(file.file_path, "image-vihecule", ['jpg', 'jpeg', 'png'])


@app.post("/drive/contract-pdf")
async def upload_pdf_contract_to_drive(file: FileParams):
    """
    Upload a PDF contract to Google Drive.

    Parameters:
      - file: FileParams - JSON body with the file_path parameter.

    Response:
      - 200: Successful file upload with the file URL.
      - 500: Failed to upload file.
    """
    return upload_file_to_drive_url(file.file_path, "contract-pdf", ['pdf'])


@app.post("/drive/driver-licence")
async def upload_image_driver_licence_to_drive(file: FileParams):
    """
    Upload an image for the driver-licence category to Google Drive.

    Parameters:
      - file: FileParams - JSON body with the file_path parameter.

    Response:
      - 200: Successful file upload with the file URL.
      - 500: Failed to upload file.
    """
    return upload_file_to_drive_url(file.file_path, "driver-licence", ['jpg', 'jpeg', 'png'])


@app.post("/drive/national-identity-card")
async def upload_image_national_identity_card_to_drive(file: FileParams):
    """
    Upload an image for the national-identity-card category to Google Drive.

    Parameters:
      - file: FileParams - JSON body with the file_path parameter.

    Response:
      - 200: Successful file upload with the file URL.
      - 500: Failed to upload file.
    """
    return upload_file_to_drive_url(file.file_path, "national-identity-card", ['jpg', 'jpeg', 'png'])
