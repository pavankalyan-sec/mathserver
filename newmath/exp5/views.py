from django.shortcuts import render
from http.server import BaseHTTPRequestHandler, HTTPServer
def index(request):
    result = None
    current = ''
    resistance = ''
    
    if request.method == 'POST':
        try:
            current = float(request.POST.get('current', 0))
            resistance = float(request.POST.get('resistance', 0))
            result = current ** 2 * resistance
            print(f"Current = {current}")
            print(f"Resistance = {resistance}")
            print(f"Calculated Power = {result} watts")
        except ValueError:
            result = 'Invalid input. Please enter numeric values.'
    


    
    return render(request, 'index.html', {
        'result': result,
        'current': current,
        'resistance': resistance})
   