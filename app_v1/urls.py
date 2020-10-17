from django.urls import path
from django.views.generic import TemplateView

from app_v1.views import SubmitFormView, AdviceView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('submit/', SubmitFormView.as_view()),
    path('advice/', AdviceView.as_view()),
]