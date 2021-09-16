from django.urls import path
from .views import Movies_Worth_WatchingList, Movies_Worth_WatchingDetail

urlpatterns = [
  path('', Movies_Worth_WatchingList.as_view(), name='movies_worth_watchingList_list'),
  path('<int:pk>/', Movies_Worth_WatchingDetail.as_view(), name='movies_worth_watchingDetail_detail')
]
