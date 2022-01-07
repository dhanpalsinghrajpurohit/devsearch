from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET':'api/projects'},
        {'GET': 'api/projects/id'},
        {'GET': 'api/projects/id/vote'},
        {'GET': 'api/users/token'},
    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    print("ldsfdksf")
    project = Project.objects.get(id=pk)
    print(project)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)