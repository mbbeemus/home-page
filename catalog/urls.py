from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]


urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),

]
