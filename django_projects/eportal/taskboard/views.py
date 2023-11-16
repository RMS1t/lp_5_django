from django.shortcuts import render


# Create your views here.
def index(request):
    # Create your views here.

    # Generate counts of some of the main objects
    num_books = 1
    num_instances = 1

    # Available books (status = 'a')
    num_instances_available = 1

    # The 'all()' is implied by default.
    num_authors = 1  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': 1,
    }

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', context=context)

