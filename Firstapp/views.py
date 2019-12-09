# Library imports
import pdb
from django.shortcuts import render
# from django.http import HttpResponse

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from Firstapp import forms

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer


def index(request):
    temp = {'a': 'Hello World'}
    return render(request, 'firstapp/index.html', context=temp)


class ArticleView(APIView):
    def get(self, request):
        print("Thid id get")
        #      pdb.b()
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})


class JWTDemo(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hey these , Python Training is going on'}
        return Response(content)


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success")
            print("Name: " + form.cleaned_data['name'])

    return render(request, 'Firstapp/form_page.html', {'form': form})
