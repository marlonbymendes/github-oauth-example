from django.shortcuts import render
import github
from github import Github

def debug(a, b):
    print('{} = {}'.format(a, b))
    print('type({}) = {}'.format(a, type(b)))

def debug_dict(a, b):
    print('\n({}) = '.format(a))
    for key, value in b.items():
        print('[{}] = {}'.format(key, value))

def get_access_token(request):
    user = request.user
    social = user.social_auth.get(provider='github')
    access_token = social.extra_data['access_token']
    return access_token

def home(request):
    return render(request, 'home.html')

def repos(request):
    token = get_access_token(request)
    g = Github(token)

    user = g.get_user()
    repo_names = [repo.full_name for repo in user.get_repos(type='all')]
    context = {'header': 'My repositories',
               'rows': repo_names}
    return render(request, 'list_base.html', context=context)

def organizations(request):
    token = get_access_token(request)
    g = Github(token)

    user = g.get_user()
    orgs = user.get_orgs()
    orgs_names = [org.login for org in orgs]
    debug('names', orgs_names)
    context = {'header': 'My organizations',
               'rows': orgs_names}
    return render(request, 'list_base.html', context=context)

def get_user_organizations(user):
    assert isinstance(user, github.AuthenticatedUser.AuthenticatedUser)

    orgs = []
    obj = user.get_orgs()
    if isinstance(obj, github.PaginatedList.PaginatedList):
        orgs += [org for org in obj]
    elif isinstance(obj, github.Organization.Organization):
        orgs += [obj]
    else:
        raise Exception
    return orgs

def get_repos(request):
    token = get_access_token(request)
    g = Github(token)
    debug('g', g)

    user = g.get_user()

    print('\n')
    for repo in user.get_repos():
        print('repo.name = {}'.format(repo.full_name))

    #orgs = get_user_organizations(user)
    orgs = g.get_organizations()

    for org in orgs:
        debug('org', org)
        print('url = {}'.format(org.url))
        print('\n')
