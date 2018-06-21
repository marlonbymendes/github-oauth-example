from django.shortcuts import render

def debug(a, b):
    print('{} = {}'.format(a, b))
    print('type({}) = {}'.format(a, type(b)))

def debug_dict(a, b):
    print('\n({}) = '.format(a))
    for key, value in b.items():
        print('[{}] = {}'.format(key, value))

def home(request):
    print('\n' * 5)
#    debug_dict('request.meta', request.META)
    debug_dict('request.session', request.session)

    user = request.user
    if user.is_authenticated:
        print('\nAuthentic!\n')
        social = user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
        debug('access_token', access_token)
    else:
        print('\nNOT Authentic!\n')

    return render(request, 'home.html')
