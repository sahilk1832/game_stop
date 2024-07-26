from django.urls import path
from gamestopapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('create_product',views.create_product),
    path('read_product',views.read_product),
    path('delete_product/<rid>',views.delete_product),
    path('update_product/<rid>',views.update_product),
    path('register',views.user_reg),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('create_cart/<rid>',views.create_cart),
    path('read_cart',views.read_cart),
    path('delete_cart/<rid>',views.delete_cart),
    path('update_cart/<rid>/<q>', views.update_cart),
    path('create_order/<rid>', views.create_order),
    path('read_order', views.read_order),
    path('create_review/<rid>', views.create_review),
    path('read_product_detail/<rid>', views.read_product_detail),
    path('forgot_password', views.forgot_password),
    path('otp_verification', views.otp_verification),
    path('new_password', views.new_password),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)