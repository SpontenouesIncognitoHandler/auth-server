from rest_framework import generics
from .models import User, Organization
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, OrgSerializer, OrgTokenSerializer
from rest_framework.views import APIView


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrgSerializer

class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrgSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # The serializer now handles linking the user to the organization
        user = serializer.save()
        user.generate_user_token()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VerifyOrgTokenView(APIView):
    def post(self, request):
        serializer = OrgTokenSerializer(data=request.data)
        if serializer.is_valid():
            org_id = serializer.validated_data['org_id']
            token = serializer.validated_data['token']

            try:
                organization = Organization.objects.get(org_id=org_id)
                user = User.objects.filter(organization=organization, user_token=token).first()

                if user:
                    return Response({"message": "Valid org_id and token."}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Invalid org_id or token."}, status=status.HTTP_404_NOT_FOUND)
            except Organization.DoesNotExist:
                return Response({"message": "Organization not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)