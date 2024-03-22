from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client

class ClientProjectView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            # Logic to retrieve a list of clients
            clients = Client.objects.all()
            return Response("List of clients")
        else:
            # Logic to retrieve a specific client and its projects
            client = Client.objects.get(pk=pk)
            projects = client.projects.all()  # Assuming related_name is 'projects' in Client model
            return Response(f"Client {pk} and its projects")

    def post(self, request, pk=None):
        if pk is None:
            # Logic to create a new client
            return Response("Client created")
        else:
            # Logic to create a new project for a client
            return Response(f"Project created for client {pk}")

    def put(self, request, pk):
        if pk is not None:
            # Logic to update a specific client
            return Response(f"Client {pk} updated")
        else:
            # Logic to update a specific project
            return Response(f"Project {pk} updated")

    def delete(self, request, pk):
        if pk is not None:
            # Logic to delete a specific client
            return Response(f"Client {pk} deleted")
        else:
            # Logic to delete a specific project
            return Response(f"Project {pk} deleted")
