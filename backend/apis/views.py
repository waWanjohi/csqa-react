from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Answer, Question, AnswerSerializer, QuestionSerializer


@api_view(['GET'])
def index(request):
    question_api_urls = {
        'Questions API  Routes': '',
        'List': 'questions/',
        'Detail': 'question-detail/',
        'Create': 'question-create/',
        'Update': 'question-update/',
        'Delete': 'question-delete/',
    }

    comment_api_urls = {
        'Comments API Routes': '',
        'List': 'answers/',
        'Detail': 'answer-detail/',
        'Create': 'answer-create/',
        'Update': 'answer-update/',
        'Delete': 'answer-delete/',
    }

    return Response((question_api_urls, comment_api_urls))


@api_view(['GET'])
def questionList(request):
    """
    docstring
    """
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def questionDetail(request, pk):
    """
    docstring
    """
    questions = Question.objects.get(id=pk)
    serializer = QuestionSerializer(questions, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def questionCreate(request):
    serializer = QuestionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def questionUpdate(request, pk):
    question = Question.objects.get(id=pk)
    serializer = QuestionSerializer(instance=question, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def questionDelete(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()

    return Response('Question Deleted!')


#  Handle Answers API

@api_view(['GET'])
def answerList(request):
    """
    docstring
    """
    answers = Answer.objects.all()
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def answerDetail(request, pk):
    """
    docstring
    """
    answers = Answer.objects.get(id=pk)
    serializer = AnswerSerializer(answers, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def answerCreate(request):
    serializer = AnswerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def answerUpdate(request, pk):
    answer = Answer.objects.get(id=pk)
    serializer = AnswerSerializer(instance=answer, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def answerDelete(request, pk):
    answer = Answer.objects.get(id=pk)
    answer.delete()

    return Response('Answer Deleted!')
