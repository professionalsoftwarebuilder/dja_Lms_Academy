from django.urls import include, path
from publisher.views import catalog
from publisher.views import my_publication
from publisher.views import publication

urlpatterns = [
    # Publications(s)
    path('publish', catalog.catalog_page),
    path('publication/<publication_id>', publication.publication_page),
    path('publication/<publication_id>/peer_review_modal', publication.peer_review_modal),
    path('publication/<publication_id>/save_peer_review', publication.save_peer_review),
    path('publication/<publication_id>/delete_peer_review', publication.delete_peer_review),
                       
    # My Publications
    path('my_publications', my_publication.my_publications_page),
    path('refresh_publications_table', my_publication.refresh_publications_table),
    path('my_publication_modal', my_publication.my_publication_modal),
    path('save_publication', my_publication.save_publication),
    path('delete_publication', my_publication.delete_publication),
]
