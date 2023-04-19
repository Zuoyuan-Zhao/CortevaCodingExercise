from django.urls import path, re_path
from .apis import get_weather_api, get_stats_min_avg, get_stats_max_avg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


generated_schema_view = get_schema_view(
   openapi.Info(
      title="Corteva Code Exercise API",
      default_version='v1',
      description="API description for Corteva Code exercise",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="zuoyuan-zhao@outlook.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    re_path(r'^docs/$', generated_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/', generated_schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  # <-- Here
    path('redoc/', generated_schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  # <-- Here
    path('apis/weather', get_weather_api),
    path('apis/stats/min_avg', get_stats_min_avg),
    path('apis/stats/max_avg', get_stats_max_avg),
]
