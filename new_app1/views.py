from django.shortcuts import render
from .models import Destination
from collections import Counter

# Create your views here.
def index(request):
    data = Destination.objects.all().order_by("-id")[:10]

    # For pie chart
    data_log = Destination.objects.order_by('Log_Category').values('Log_Category')
    d_lst = []
    for d in data_log:
        if d not in d_lst:
            d_lst.append(d)
    u_value = set(val for dic in d_lst for val in dic.values())
    # print(len(u_value))
    log_values = {}
    for x in u_value:
        count = Destination.objects.filter(Log_Category__contains=x).count()
        log_values[x] = count
    print(len(log_values))


    # For Line chart
    data_date = Destination.objects.order_by('Date_Time').values('Date_Time')
    date_lst = []
    for d in data_date:
        date_lst.append(d)
    # print(date_lst[0].values())
    new_lst = []
    for x in date_lst:
        d_item = x.values()
        new_lst.append(str(d_item)[14:20])


    date_count = Counter(new_lst)
    date_keys = list(date_count.keys())
    date_vals = list(date_count.values())



    context = {
        'data': data,
        'log_values_keys': log_values.keys(),
        'log_values_value': log_values.values(),
        'date_keys': date_keys,
        'date_vals': date_vals,

    }
    return render(request, 'new_app1/index.html', context)
