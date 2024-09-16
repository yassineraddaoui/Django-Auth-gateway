import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCandidate
from .serializers import UserSerializer

# Helper function to handle response
def handle_response(response):
    if response.status_code == 200:
        if response.json():
            return JsonResponse(response.json(), status=response.status_code, safe=False)
        else:
            return JsonResponse({'message': 'No content found'}, status=204)
    else:
        return JsonResponse({'error': response.text}, status=response.status_code)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsCandidate])
def proxy_to_microservice_all(request):
    microservice_url = "http://localhost:8080/candidat/all"
    try:
        if request.method == 'GET':
            response = requests.get(microservice_url, params=request.GET)
        elif request.method == 'POST':
            response = requests.post(microservice_url, json=request.data)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)

        return handle_response(response)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET', 'POST'])
def proxy_to_microservice_by_id(request, id):
    microservice_url = f"http://localhost:8080/candidat/{id}"
    try:
        if request.method == 'GET':
            response = requests.get(microservice_url, params=request.GET)
        elif request.method == 'POST':
            response = requests.post(microservice_url, json=request.data)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)

        return handle_response(response)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
def some_other_api(request):
    microservice_url = "http://localhost:8080/another-endpoint"
    try:
        response = requests.get(microservice_url)
        return handle_response(response)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
