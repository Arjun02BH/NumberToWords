from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from num2words import num2words  # You may need to install this package with pip

def number_to_words(request):
    if request.method == 'POST':
        number = request.POST['number']
        words = num2words(number)
        return render(request, 'converter/number_to_words.html', {'number': number, 'words': words})
    return render(request, 'converter/number_to_words.html')
