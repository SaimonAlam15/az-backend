
import os

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response

class DefaultView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        response = Response(f'AZ API v.{os.getenv("API_VERSION", "dev")}')
        response["Content-Type"] = "text/plain"
        return response