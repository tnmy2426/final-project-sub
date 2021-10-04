import six
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def group_required(group, login_url="/accounts/login/", raise_exception=False):
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group,)
        else:
            groups = group

        if user.groups.filter(name__in=groups).exists():
            return True
        if raise_exception:
            return PermissionDenied

        return False
    return user_passes_test(check_perms, login_url=login_url)