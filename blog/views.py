


#
# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()


from django.http import HttpResponse


def article_year(request):
    return HttpResponse(f"Displaying articles from the year ")
