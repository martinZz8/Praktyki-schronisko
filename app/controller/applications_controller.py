from app.model.models import Application

def get_all_app(request):
    app=Application.objects.all()
    return app

def get_app_by_id(request, id_app):
    app = Application.objects.get(ID = id_app)
    return app