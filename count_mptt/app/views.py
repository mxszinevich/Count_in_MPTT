from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Topic
from .serializers import TopicSerializer


class TopicsView(APIView):

    def get(self, request):
        topics = Topic.objects.filter(parent=None)
        self.count = 0
        self.count_child_easy(topics)
        print(self.count)
        representation = TopicSerializer(topics, many=True)
        return Response(representation.data)

    def count_child_easy(self, topics):
        for topic in topics:
            if topic.type == 1: # условие
                self.count += 1
            if topic.parent == None:
                children = topic.get_children()
                self.count_child_easy(children)
                topic.count = self.count
                self.count = 0
            else:
                if topic.get_descendant_count() != 0:
                    children = topic.get_children()
                    self.count_child_easy(children)

























