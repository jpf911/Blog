from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView,AddCommentView,Posts

urlpatterns = [
    # path('', HomeView.as_view(),name='home'),
    path('', login_required(HomeView.as_view(),login_url='/members/login/'),name='home'),
    path('posts/', Posts.as_view(), name='posts'),
    path('article/<int:pk>', ArticleDetailView.as_view(),name='article-detail'),
    path('add_post/', AddPostView.as_view(),name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(),name='update_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(),name='add_comment'),
    path('article/<int:pk>/remove', DeletePostView.as_view(),name='delete_post'),
    path('add_category/', AddCategoryView.as_view(),name='add_category'),
    path('category/<str:cats>/', CategoryView,name='category'),
    path('category-list/', CategoryListView,name='category_list'),
    path('like/<int:pk>', LikeView,name='like_post'),
]
