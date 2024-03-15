import django_filters
from exams.models.questions import Question

class QuestionsFilter(django_filters.FilterSet):
    exam_title = django_filters.CharFilter("exam__title", lookup_expr='icontains')
    exam_id = django_filters.CharFilter("exam__id", lookup_expr='exact')


    class Meta:
        model = Question
        fields = ['exam_title', 'exam_id']
