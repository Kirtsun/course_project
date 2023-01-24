from django.contrib.auth import views as view
from django.urls import path, reverse_lazy

from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", view.LoginView.as_view(next_page='/shop/book_list/'), name="login"),
    path("logout/", view.LogoutView.as_view(), name="logout"),

    path("password_change/", view.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", view.PasswordChangeDoneView.as_view(), name="password_change_done"),

    path("password_reset/", view.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')),
         name="password_reset"),
    path("password_reset/done/", view.PasswordResetDoneView.as_view(), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", view.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("registration/", views.registers, name='registration')
]
