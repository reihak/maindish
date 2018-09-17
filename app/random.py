
from models import Menu
from forms import MenuForm
from django.views.decorators.http import require_POST

list = []


weekly = Menu.objects.all().order_by('?')
list.append(weekly.id)
print(list)
