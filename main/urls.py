from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('save-comment',views.save_comment,name='save-comment'),
    path('save-upvote',views.save_upvote,name='save-upvote'),
    path('save-downvote',views.save_downvote,name='save-downvote'),
    # User Register
    path('accounts/register/',views.register,name='register'),
    # Ask QUestion
    path('ask-question',views.ask_form,name='ask-question'),
]