from github import Github


def debug(a, b):
    print('{} = {}'.format(a, b))
    print('type({}) = {}'.format(a, type(b)))

g = Github('marlonbymendes', 'n0lr4m55')
user = g.get_user()
orgs = user.get_orgs()

debug('orgs', orgs)
for org in orgs:
    debug('org', org)
    print('login = ', org.login)

    for repo in org.get_repos(type='public'):
        tab = ' ' * 8
        print(tab + repo.name)
