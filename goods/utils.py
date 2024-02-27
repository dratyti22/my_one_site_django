from django.db.models import Q

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <=5:
        return Products.objects.filter(id=int(query))
    
    kewbord = [word for word in query.split() if len(word) >2]

    q_objects = Q()

    for i in kewbord:
        q_objects |= Q(description__icontains=i)
        q_objects |= Q(name__icontains=i)
    
    return Products.objects.filter(q_objects)
