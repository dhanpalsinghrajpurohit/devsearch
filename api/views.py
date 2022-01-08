from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project, Review

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
# @permission_classes([IsAuthenticated])
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    projects = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    review, created = Review.objects.get_or_create(
        owner = user,
        project=projects,
    )
    review.value = data['value']
    review.save()
    print('DATA : ',data)
    serializer = ProjectSerializer(projects, many=False)
    return Response(serializer.data)