from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'api'


# 'api/'
urlpatterns = [
	path('', views.home, name="home"), #api/
	path('tasks/', views.task_list, name="task-list"),
	path('tasks/<int:pk>/', views.task_detail, name="task-detail"),
]


# apiview = [
#     path('articles/', views.ArticleAPIView.as_view(), name="articles"),
#     path('articles/<int:pk>', views.ArticleDetail.as_view(), name="article-detail"),
# ]

# urlpatterns += apiview


# mixinview = [
#     path('articles/', views.ArticleListMixin.as_view(), name="articles"),
#     path('articles/<int:pk>', views.ArticleDetailMixin.as_view(), name="article-detail"),
# ]
# urlpatterns += mixinview


genericview = [
    path('articles/', views.ArticleListCreate.as_view(), name="articles"),
    path('articles/<int:pk>', views.ArticleRetrieveUpdateDestroy.as_view(), name="article-detail"),
]

urlpatterns += genericview


urlpatterns = format_suffix_patterns(urlpatterns)