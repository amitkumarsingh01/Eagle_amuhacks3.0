from django.urls import path
from .views import *
from .utils import get_nutrition_data,save_nutrition_data,delete_nutrition_data
from .search_gemini import NutSearch
from django.views.decorators.csrf import csrf_exempt
from .blog import BlogHome
from .med_gemini import *

urlpatterns = [
    path('', Home, name='main-home' ),
    path('tdee/', TdeePage.as_view(), name='main-tdee' ),
    path('nutrition/', NutritionPage.as_view(), name='main-nutrition' ),
    path('api/get-nutrition-data/', get_nutrition_data, name='main-get_nutrition_data'),
    path('api/save_nutrition_data/', save_nutrition_data, name='main-save_nutrition_data'),
    path('api/delete_nutrition_data/<int:item_id>/', delete_nutrition_data, name='main-delete_nutrition_data'),
    path("api/img", csrf_exempt(NutSearch), name="main-api-img"),
    path("blog/", BlogHome.as_view(), name="main-blog"),
    path("api/med/img", csrf_exempt(MedSearch), name="main-api-med-img"),
    path("med/", med_gemini, name="main-med"),
]