from rest_framework.permissions import BasePermission


class IsLoggedInAdmin(BasePermission):
    message = "Acceso denegado"

    def has_permission(self, request, view):
        profile = request.user.perfil
        is_true = ((profile == "Administrador") or request.user.is_superuser)
        return bool(is_true and request.user.is_authenticated)


class IsLoggedInAdminExceptions(BasePermission):
    edit_methods = ("POST", "PUT", "DELETE")

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            profile = request.user.perfil
            is_true = ((profile == "Administrador") or request.user.is_superuser)
            return bool(is_true and request.method in self.edit_methods and request.user.is_authenticated)


class IsLoggedInAdminStudent(BasePermission):
    edit_methods = ("POST", "DELETE")

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            profile = request.user.perfil
            is_true = ((profile == "Administrador") or (profile == "Estudiante") or request.user.is_superuser)
            return bool(is_true and request.method in self.edit_methods and request.user.is_authenticated)


class IsLoggedInAdminProfessor(BasePermission):
    edit_methods = ("GET", "POST", "PUT")

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            profile = request.user.perfil
            is_true = ((profile == "Administrador") or (profile == "Profesor") or request.user.is_superuser)
            return bool(is_true and request.method in self.edit_methods and request.user.is_authenticated)


class IsLoggedInAll(BasePermission):
    message = "Acceso denegado"

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)


class IsLoggedInStudent(BasePermission):
    edit_methods = ("GET", "POST", "PUT")

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            profile = request.user.perfil
            is_true = ((profile == "Estudiante") or request.user.is_superuser)
            return bool(is_true and request.method in self.edit_methods and request.user.is_authenticated)
