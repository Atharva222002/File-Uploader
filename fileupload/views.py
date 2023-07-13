from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UploadedFile
from django.shortcuts import get_object_or_404
import os
from django.http import FileResponse, Http404


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def file_list(request):
    '''
        `Description`: Retrieve a list of files uploaded by the authenticated user.

        `Method`: GET

        `Parameters`:
            - request (HttpRequest): The HTTP request object.

        `Response` : Returns a JSON response containing file information for each uploaded file,
        including the file name, upload timestamp, and download URL.

        Requires the user to be authenticated with a valid token.

        `Example`:
            {
                "file_name": "example.txt",
                "uploaded_at": "2023-07-14T12:34:56Z",
                "download_url": "/download/1/"
            }
    '''
    files = UploadedFile.objects.filter(uploader=request.user)
    file_list = []
    for file in files:
        file_info = {
            'file_name': file.file.name,
            'uploaded_at': file.uploaded_at,
            'download_url': f'/download/{file.id}/'
        }
        file_list.append(file_info)
    return Response(file_list)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def file_upload(request):
    '''        
        `Description`: Uploads a file provided in the request body to the server storage,
        associating it with the authenticated user. Returns a JSON response
        indicating a successful upload.

        Requires the user to be authenticated with a valid token.

        `Method`: POST

        `Parameters`:
            - request (HttpRequest): The HTTP request object containing the file.

        `Returns`:
            Response: A JSON response indicating a successful file upload.

        `Example`:
            {
                "message": "File uploaded successfully"
            }
    '''
    file = request.FILES['file']
    uploaded_file = UploadedFile(uploader=request.user)
    uploaded_file.file.save(file.name, file, save=True)
    return Response({'message': 'File uploaded successfully'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_file(request, file_id):
    '''
        `Description` : Downloads the file identified by the given `file_id`, which is associated
        with the authenticated user. The file is returned as a response with appropriate
        headers for file download.

        Requires the user to be authenticated with a valid token and be the uploader of the file.

        `Method`: GET
        
        `Parameters`:
            - request (HttpRequest): The HTTP request object.
            - file_id (int): The ID of the file to be downloaded.

        `Returns`:
            FileResponse: The file to be downloaded as the HTTP response.

        `Raises`:
            `Http404`: If the file does not exist or if the authenticated user is not the uploader.

        `Example`:
            N/A (Binary file response)
    '''
    uploaded_file = get_object_or_404(UploadedFile, id=file_id)
    if uploaded_file.uploader != request.user:
        raise Http404()

    file_path = uploaded_file.file.name
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="' + os.path.basename(file_path) + '"'
    return response