from django.shortcuts import redirect

class LoginStaffMixin(object):
    def dispatch(self, request, *args, **kargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kargs)
        return redirect('/')

