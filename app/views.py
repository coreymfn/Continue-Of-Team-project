from django.shortcuts import render

# Create your views here.
def team_list(request):
    teams = [
        'Management',
        'Procurement',
        'Community',
        'Documentation'
    ]

    return render(request, 'app/team_list.html', {'teams': teams})

def management(request):
    context = {
        'team_name': 'Management',
        'members': [
            'Tristan H',
            'Christopher L',
            'Brian S',
        ]
    }

    return render(request, 'app/management.html', context)
def procurement(request):
    context = {
        'team_name': 'Procurement',
        'members': [
            'Tristan H',
            'Christopher L',
            'Brian S',
        ]
    }

    return render(request, 'app/procurement.html', context)
def community(request):
    context = {
        'team_name': 'Community',
        'members': [
            'Tyler V',
            'Tyler J',
            'Germaine R',
            'Corey N',
        ]
    }

    return render(request, 'app/community.html', context)
def documentation(request):
    context = {
        'team_name': 'Documentation',
        'members': [
            'Tyler V',
            'Tyler J',
            'Germaine R',
            'Corey N',
        ]
    }

    return render(request, 'app/documentation.html', context)