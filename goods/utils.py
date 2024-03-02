from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector('name', 'description')
    query = SearchQuery(query)

    result = Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    
    result = result.annotate(headline=SearchHeadline(
        "name",
        query,
        start_sel='<span style="background-color: yellow">',
        stop_sel='</span>',
    ))
    result = result.annotate(bodyline=SearchHeadline(
        "description",
        query,
        start_sel='<span style="background-color: yellow">',
        stop_sel='</span>',
    ))
    return result

    # kewbord = [word for word in query.split() if len(word) >2]

    # q_objects = Q()

    # for i in kewbord:
    #     q_objects |= Q(description__icontains=i)
    #     q_objects |= Q(name__icontains=i)

    # return Products.objects.filter(q_objects)