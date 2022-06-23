import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from app.models import Person
from django.db.models import Max
from django.db.models import Q


# Create your views here.

"""

    filter return QuerySet containing objects that match the given lookup parameters
    exclude return QuerySet containing objects that do not match the given lookup parameters.
    Change the default ordering of the QuerySet
    The values() method returns a QuerySet containing dictionaries
    The values_list() method returns a QuerySet containing tuples
    date returns a QuerySet containing all available dates in the specified date range
    select_related() Select all related data when executing the query (except many-to-many relationships)
    prefetch_related() Select all related data when executing the query (including many-to-many relationships)
    differ Do not retrieve the named fields from the database. Used to improve query performance on complex datasets
    only Opposite of defer()—return only the named fields
    raw Execute a raw SQL statement
    AND Combine two QuerySets with the SQL AND operator. Using AND (&) is functionally equivalent to using filter() with multiple parameters
    OR Combin two QuerySets with the SQL OR operator
"""
def Return_Queryset(request):

    filter = Person.objects.filter(name = "user1")

    exclude = Person.objects.exclude(name = "user1")

    aggregate = Person.objects.all().aggregate(Max('age'))

    order_by = Person.objects.all().order_by('age')

    values = Person.objects.all().values("age")

    aggregate = Person.objects.all().aggregate(Max('age'))

    order_by = Person.objects.all().order_by('age')

    values = Person.objects.all().values("age")

    values_list = Person.objects.all().values_list("age")

    none = Person.objects.none()

    union = Person.objects.filter(name = "user1").union(Person.objects.exclude(name = "user1"))
    
    intersection = Person.objects.filter(name = "user1").intersection(Person.objects.exclude(name = "user1"))
    
    difference = Person.objects.filter(name = "user1").difference(Person.objects.exclude(name = "user1"))

    difer = Person.objects.defer("age")
    
    only = Person.objects.only("age")
    
    raw = Person.objects.raw('SELECT * FROM Person')
    
    And = Person.objects.filter(name = "user1" , age = 10)
    
    Or = Person.objects.filter(Q(name = "user1") | Q(age = 10))

    filter_str = str(filter)
    
    exclude_str = str(exclude)

    aggregate_str = str(aggregate)

    order_by_str = str(order_by)

    values_str = str(values)

    values_list_str = str(values_list)

    none_str = str(none)

    union_str = str(union)

    intersection_str = str(intersection)

    difference_str = str(difference)

    difer_str = str(difer)

    only_str = str(only)

    raw_str = str(raw)

    And_str = str(And)
    
    Or_str = str(Or)


    data = {
        "filter" : filter_str,
        
        "exclude" : exclude_str,

        "aggregate" : aggregate_str,

        "order_by" : order_by_str,

        "values" : values_str,

        "values_list" : values_list_str,

        "none" : none_str,

        "union" : union_str,
        
        "intersection" : intersection_str,
        
        "difference" : difference_str,

        "difer" : difer_str,

        "only" : only_str,
        
        "raw" : raw_str,

        "And" : And_str,
        
        "Or" : Or_str
    }
    return JsonResponse(data, safe=False)



"""
    get Returns a single object. Throws an error if lookup returns multiple objects
    get_or_create Returns a single object. If the object doesn’t exist, it creates one
    update_or_create()	Updates a single object. If the object doesn’t exist, it creates one
    bulk_create()	Insert a list of objects in the database
    bulk_update()	Update given fields in the listed model instances
    iterator()	Evaluate a QuerySet and return an iterator over the results. Can improve performance and 
        memory use for queries that return a large number of objects
    latest()	Return the latest object in the database table based on the given field(s)
    earliest()	Return the earliest object in the database table based on the given field(s)
    first()	Return the first object matched by the QuerySet
    last()	Return the last object matched by the QuerySet
    exists()	Returns True if the QuerySet contains any results
"""
def No_Return_Queryset(request):

    get = Person.objects.get(pk = 1)

    person, created = Person.objects.get_or_create(name='Leo Tolsthukoy', age=10, address="53",salary=53)

    person, update = Person.objects.update_or_create(name='Leo Tobhjlstoy', age=10, address="53",salary=53)

    bulk_create = Person.objects.bulk_create([
        Person(name='Leo hjTolstoy', age=10, address="53",salary=53),
        Person(name='Leo Tnjfkjnsjkolstoy', age=1780, address="53fndsbu",salary=53),
        Person(name='Leo Tobhjlstoy', age=1870, address="bfdsbfbs",salary=53876),
        Person(name='Leo Tobhlstoy', age=167890, address="vsb53",salary=5783),
    ])

    
    persons = Person.objects.all()
    for person in persons.iterator():
        print(person.name)

    latest = Person.objects.latest("name")

    earliest = Person.objects.earliest("name")

    first = Person.objects.filter(name = "user1").first()

    last = Person.objects.filter(name = "user1").last()

    person = Person.objects.filter(name = "user1")
    if person.exists():
        print("Person exist")


    get = str(get)
    
    created = str(created)

    update = str(update)

    bulk_create = str(bulk_create)

    latest = str(latest)

    earliest = str(earliest)

    first = str(first)

    last = str(last)



    data = {
        "get" : get,
        
        "created" : created,

        "update" : update,

        "bulk_create" : bulk_create,

        "latest" : latest,

        "earliest" : earliest,

        "first" : first,

        "last" : last,
        
    }
    return JsonResponse(data, safe=False)