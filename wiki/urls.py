from django.urls import path
from wiki.views import PageListView, PageDetailView, CreateWikiView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('new_wiki/', CreateWikiView.as_view(), name='wiki-new-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    # Make sure have leading and ending slashes when using slaahes or else won't work
    # Slahes matters!
    # new_wiki.html does work, but why?
    
]
