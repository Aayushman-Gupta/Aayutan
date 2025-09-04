from django.shortcuts import render
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .constants import DEGREE_SPECIALIZATION_MAPPING



@csrf_exempt  # Only if you're testing with JavaScript and haven't configured CSRF properly ye
def get_motivational_quote(request):
    if request.method == "GET":
        quote = random.choice(MOTIVATIONAL_QUOTES)
        return JsonResponse({'quote': quote})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_mentalwellness_quote(request):
    if request.method == "GET":
        quote = random.choice(MENTAL_WELLNESS_QUOTES)
        return JsonResponse({'quote': quote})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def generate_tags_from_specialty(specialty_text):
    tags = set()
    specialty_text = specialty_text.lower()
    for degree, data in DEGREE_SPECIALIZATION_MAPPING.items():
        for keyword in data["keywords"]:
            if keyword.lower() in specialty_text:
                tags.add(data["field"])
                tags.update(data["keywords"])
    return list(tags)
