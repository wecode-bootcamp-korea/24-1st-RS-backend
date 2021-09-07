from django.http import JsonResponse
from django.views import View

from .models import Category

class CategoryView(View):
    def get(self, request, category):
        try:
            if category.startswith("약주") or category.endswith("청주"):
                category = "약주"
                category = Category.objects.get(name__istartswith=category)

                result = {
                    "id"          : "5,6",
                    "name"        : "약주,청주",
                    "description" : category.description,
                    "image_url"   : category.image_url,
                }
                return JsonResponse({"Result": result}, status=200)
            
            category = Category.objects.get(name__istartswith=category)
            result = {
                    "id"          : category.id,
                    "name"        : category.name,
                    "description" : category.description,
                    "image_url"   : category.image_url,
                }
            return JsonResponse({"Result": result}, status=200)

        except Category.DoesNotExist:
            return JsonResponse({"Result": "CATEGORY_DOES_NOT_EXIST"}, status=400)