# Django File Uploader

This is a Django application that provides a REST API for uploading and managing files securely.

## Features

- Token-based authentication for API access.
- Secure and private file storage.
- APIs to upload files, list uploaded files and download files.
- File encryption for sensitive documents (remaining).

## Installation

1. Clone the repository

2. Install the required dependencies

3. Apply the database migrations

4. Run the development server


## API Endpoints

### Obtain Token

**URL**: `http://localhost:8000/api/obtain_token/`  
**Method**: POST  
**Parameters**:
- `username`: User's username
- `password`: User's password

**Response**: JSON containing the token on success or error message on failure.

### List Files

**URL**: `http://localhost:8000/api/list/`  
**Method**: GET  
**Authentication**: Token-based authentication  
**Response**: JSON array of uploaded files' information.  

### Upload File

**URL**: `http://localhost:8000/api/upload/`  
**Method**: POST  
**Authentication**: Token-based authentication  
**Parameters**:
- `file`: The file to be uploaded.

**Response**: JSON message indicating successful file upload.

### Download File

**URL**: `http://localhost:8000/api/download/{file_id}/`  
**Method**: GET  
**Authentication**: Token-based authentication  
**Response**: The file to download.  

## Contributing

Contributions are welcome! Please fork the repository and create a pull request.
