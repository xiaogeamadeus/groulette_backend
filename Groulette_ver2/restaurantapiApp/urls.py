from django.urls import path
from . import views

urlpatterns = [
    # ex: /getRequest/restaurantAPI?genre=[]&mode=oni&userid=21234xy
    path('restaurantAPI', views.restaurantAPI),
    path('getRouteLinkAPI', views.getRouteLinkAPI)

    # path('', views.index, name='index'),
    #
    # # ex: /getRequest/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    #
    # # ex: /getRequest/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    #
    # # ex: /getRequest/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]