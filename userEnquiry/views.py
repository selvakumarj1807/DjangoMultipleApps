from django.shortcuts import render

# Create your views here.

def enquiryIndex(request):
    return render(request, 'userEnquiry/index.html')