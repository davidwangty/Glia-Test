import random
from django.shortcuts import render


def home(request):
    excuses = [
        "It was working in my head",
        "I thought I fixed that",
        "Actually, that is a feature",
        "It works on my machine"
    ]

    view_data = {}
    view_data['excuse'] = random.choice(excuses)

    return render(request, 'index.html', view_data)
