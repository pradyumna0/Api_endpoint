from django.http import JsonResponse, HttpResponse
from .tasks import fetch_cat_fact
from django.core.cache import cache

temp=False
def health_check(request):
    if temp:
        return JsonResponse({'status':'OK,Application is running'})
    else:
        return JsonResponse({'status': temp,'error':'application is not running'})

def index(request):
    return HttpResponse("Hello")
def fetch_fact(request):
    global temp
    try:
        temp = True
        fetch_cat_fact.send()
        return JsonResponse({'success': True})
    except Exception as e:
        temp=False
        return JsonResponse({'success': False, 'error': str(e)})

def get_fact(request):
    try:
        last_cat_fact = fetch_cat_fact()
        if last_cat_fact:
            return JsonResponse({'success': True, 'fact': last_cat_fact})
        else:
            return JsonResponse({'success': False, 'error': 'No task has been queued yet'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
