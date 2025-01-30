from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
import json

class Converter(View):
    def get(self,request):
        return render(request, 'template.html')
    def post(self,request) :
        data = json.loads(request.body)
        mproperty = data['mproperty']
        value = data['value']
        iunit = data['input_unit']
        ounit = data['output_unit']
        res = 0
        if mproperty == 'length' :
            if iunit == 'centimeter' :
                res = value/(2.54 * (1 if ounit == 'inche' else 12))
            elif iunit == 'inche' :
                res = value*(2.54 if ounit == 'centimeter' else 1/12)
            elif iunit == 'foot' :
                res = value/12*(2.54 if ounit == 'centimeter' else 1)
        elif mproperty == 'weight' :
            if iunit == 'kilogram' :
                res = value*(2.20462 * (1 if ounit == 'pound' else 16))
            elif iunit == 'pound' :
                res = value/(2.20462 if ounit == 'kilogram' else 1/16)
            elif iunit == 'ounce' :
                res = value/16*(2.20462 if ounit == 'kilogram' else 1)
        elif mproperty == 'temperature':
            if iunit == 'celsius':
                if ounit == 'fahrenheit':
                    res = (value * 1.8) + 32
                elif ounit == 'kelvin':
                    res = value + 273.15
            elif iunit == 'fahrenheit':
                if ounit == 'celsius':
                    res = (value - 32) / 1.8
                elif ounit == 'kelvin':
                    res = (value - 32) / 1.8 + 273.15
            elif iunit == 'kelvin':
                if ounit == 'celsius':
                    res = value - 273.15
                elif ounit == 'fahrenheit':
                    res = (value - 273.15) * 1.8 + 32
        return JsonResponse({"result" : round(res, 2)})