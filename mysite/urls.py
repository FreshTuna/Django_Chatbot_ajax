
from django.contrib import admin
from django.urls import path

from mysite.views import home, get_response, question_add, QuestionAPI, get_sentence

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('get-message/', get_response),
    path('get-sentence/<sentence>', get_sentence),
    path('question-add/', question_add, name="question_add"),
    path('api/qs/', QuestionAPI.as_view())
]

if settings.DEBUG == True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)