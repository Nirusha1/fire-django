from django.urls import path

from . import views

#adding namespaces to our URL conf so that Django knows which app view to
# create for a url when using the {% url %} template tag
app_name='test_poll'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results',views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]