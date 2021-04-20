from collections import Counter

from django.shortcuts import render

list_of_transitions = []
list_of_showing = []


def index(request):
    transition = request.GET.get('from-landing')
    if transition == 'original':
        counter_click = Counter(list_of_transitions)
        list_of_transitions.append(transition)
    elif transition == 'test':
        counter_click = Counter(list_of_transitions)
        list_of_transitions.append(transition)
    print(list_of_transitions)

    return render(request, 'index.html')


def landing(request):
    land = request.GET.get('ab_test_arg')
    if land == 'original':
        counter_show = Counter(list_of_showing)
        list_of_showing.append(land)
        response = render(request, 'landing.html')
    elif land == 'test':
        counter_show = Counter(list_of_showing)
        list_of_showing.append(land)
        response = render(request, 'landing_alternate.html')
    print(list_of_showing)
    print(dict(counter_show))
    return response

def stats(request):

    transition_to_original = int(dict(counter_click)['original'])
    transition_to_test = int(dict(counter_click)['test'])
    showing_of_original = int(dict(counter_show)['original'])
    showing_of_test = int(dict(counter_show)['test'])

    return render(request, 'stats.html', context={
        'test_conversion': transition_to_test/showing_of_test,
        'original_conversion': transition_to_original/showing_of_original
    })

