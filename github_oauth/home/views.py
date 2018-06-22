from django.shortcuts import render
from github import Github


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
    context = {'header': 'My organizations',
               'rows': orgs_names}
    return render(request, 'list_base.html', context=context)
