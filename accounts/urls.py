from django.urls import path
from accounts.views import SignUpView, Sayhi

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup-page'),
    # path('hi', Sayhi.as_view(), name="test"), 
]
