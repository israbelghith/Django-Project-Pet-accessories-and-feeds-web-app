from django.urls  import path
from .views import *
urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('my_products/',user_products,name="my_products"),
    path('my_categories/',user_categories,name="my_categories"),
    path('add_product/',AddProduct.as_view(),name="add_product"),
    path('add_categorie/',AddCategory.as_view(),name="add_categorie"),
    path('update_categorie/<int:pk>',UpdateCategory.as_view(),name="update_categorie"),
    path('update_article/<int:pk>',UpdateArticle.as_view(),name="update_article"),
   # path('delete_article/<int:pk>',DeleteArticle.as_view(),name="delete_article"),
   # path('delete_article/<int:pk>', DeleteArticle.as_view(), name='delete_article'),
    path('my_articles/delete_article/<int:pk>', DeleteArticle.as_view(), name='delete_article'),
    path('my_categories/delete_categorie/<int:pk>', DeleteCategory.as_view(), name='delete_categorie'),
    path('update_prod/<int:pk>',UpdateProduct.as_view(),name="update_prod"),
    path('my_products/delete_product/<int:pk>', DeleteProduct.as_view(), name='delete_product'),
    path('read_prod/<int:pk>',ReadProduct.as_view(),name="read_prod"),
]