from django.urls import path

from .views import ProfilePageView, ProfileUpdateView, PaymentInfoUpdateView


urlpatterns = [
    path('profile/<int:pk>', ProfilePageView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/payment-info/edit/<int:pk>', PaymentInfoUpdateView.as_view(), name='payment_info_edit'),
]