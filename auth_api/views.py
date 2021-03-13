from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class Auth(View):

    def get(self, request):
        sign_up_context = dict(
            title="Sign Up | Your Data",
            header_hide=True,
            left_sidebar_hide=True,
        )
        return render(request=request,
                      template_name='auth_api/sign_up.html',
                      context=sign_up_context)
