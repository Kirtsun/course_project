from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

User = get_user_model()


@login_required
def my_profile(request):
    user = get_object_or_404(User, pk=request.user.id)
    return render(request, 'myprofile/myprofile.html', {'user': user})


class UpdateProfile(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ["username", "email"]
    template_name = 'myprofile/update_profile.html'
    success_url = reverse_lazy("userprofile:my_profile")
    success_message = "Profile updated"

    def get_object(self, queryset=None):
        user = self.request.user
        return user
