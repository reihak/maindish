from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu
from .forms import MenuForm
from django.views.decorators.http import require_POST
from django.db.models import Q

week_list = [['月','カレー'], ['火','焼きそば'], ['水','手巻き寿司']]

# Create your views here.
def index(request):
    menus = Menu.objects.all().order_by('id')
    return render(request, 'app/index.html', {'menus': menus})

def detail(request, menu_id):
  menu = get_object_or_404(Menu, id=menu_id)
  return render(request, 'app/detail.html', {'menu': menu})


def new_menu(request):
	if request.method == "POST":
		form = MenuForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('app:index')
	else:
		form = MenuForm
	return render(request, 'app/new_menu.html', {'form': form })

@require_POST
def delete_menu(request, menu_id):
	menu = get_object_or_404(Menu, id=menu_id)
	menu.delete()
	return redirect('app:index')

def edit_menu(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = MenuForm(instance=menu)

    return render(request, 'app/edit_menu.html', {'form': form, 'menu':menu })


def weekly(request):
    if request.method == "POST":
        index = 0
        weekly = Menu.objects.all().order_by('?')[:3]

        for i in weekly:
            del week_list[index][1:]
            week_list[index].append(i.title)
            week_list[index].append(i.id)
            week_list[index].append(i.food_stuff)
            index += 1
    else:
        weekly = Menu.objects.all().filter(Q(title=week_list[2][1]) | Q(title=week_list[1][1]) | Q(title=week_list[0][1]))

    return render(request, 'app/weekly.html', {'weekly': weekly, 'week_list':week_list})
