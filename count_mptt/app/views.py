from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Topic
from .serializers import TopicSerializer


class TopicsView(APIView):

    def get(self, request):
        topics = Topic.objects.filter()
        topics_parent_none = Topic.objects.filter(parent=None)
        self.count_child_easy(topics_parent_none)
        representation = TopicSerializer(topics, many=True)
        return Response(representation.data)

    def count_child_easy(self, topics, parent=False):

        for topic in topics:

            if topic.parent is None or parent:  # тип родителей
                self.count_r = 0
                children = topic.get_children()
                self.count_child_easy(children)
                topic.count = self.count_r
                topic.save(update_fields=['count'])  # Подсчитали признак у родителя
                for ch in topic.get_children():  # потомки - родители
                    self.count_child_easy(children, parent=True)

            else:
                if topic.type == 1:  # условие в задаче это TYPE магазина
                    self.count_r += 1

                if topic.get_descendant_count() != 0:
                    children = topic.get_children()
                    self.count_child_easy(children)

























