from django.urls import path, include

urlpatterns = [
    path('account/', include('backend.account.urls'))
]