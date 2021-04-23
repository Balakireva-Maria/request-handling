from collections import Counter

from django.shortcuts import render

list_of_transitions = []
list_of_showing = []
counter_transition = Counter(list_of_transitions)
counter_show = Counter(list_of_showing)

def index(request):
    #counter_transition = Counter(list_of_transitions)
    transition = request.GET.get('from-landing')
    if transition == 'original':
        counter_transition['original'] += 1
        list_of_transitions.append(transition)
    elif transition == 'test':
        counter_transition['test'] += 1
        list_of_transitions.append(transition)
    print(counter_transition['original'],  counter_transition['test'])

    return render(request, 'index.html')


def landing(request):
    #counter_show = Counter(list_of_showing)
    land = request.GET.get('ab_test_arg')
    if land == 'original':
        counter_show['original'] += 1
        list_of_showing.append(land)
        response = render(request, 'landing.html')
    elif land == 'test':
        counter_show['test'] += 1
        list_of_showing.append(land)
        response = render(request, 'landing_alternate.html')
    print(list_of_showing)
    print((counter_show['original']), (counter_show['test']))
    return response

def stats(request):

    transition_to_original = counter_transition['original']
    transition_to_test = counter_transition['test']
    showing_of_original =counter_show['original']
    showing_of_test = counter_show['test']

    return render(request, 'stats.html', context={
        'test_conversion': transition_to_test/showing_of_test,
        'original_conversion': transition_to_original/showing_of_original
    })

