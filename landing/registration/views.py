from django.shortcuts import render, redirect
from .handlers import bot



def index(request):

    if request.method == 'POST':
        cap_name = request.POST['captain']
        cap_pro_potok = request.POST['captain-group']

        mem2 = request.POST['member-2']
        mem2_pro_potok = request.POST['member-2-group']
        mem3 = request.POST['member-3']
        mem3_pro_potok = request.POST['member-3-group']
        mem4 = request.POST['member-4']
        mem4_pro_potok = request.POST['member-4-group']
        mem5 = request.POST['member-5']
        mem5_pro_potok = request.POST['member-5-group']
        mem6 = request.POST['member-6']
        mem6_pro_potok = request.POST['member-6-group']
        main_text = 'Новая команда\n'

        main_text += f'Капитан\nИмя: {cap_name}\nСпециальность и поток: {cap_pro_potok}\n\n'
        main_text += f'Второй участник: {mem2}, {mem2_pro_potok}\n' \
                     f'Третий участник: {mem3}, {mem3_pro_potok}\n' \
                     f'Четвёртый участник: {mem4}, {mem4_pro_potok}\n' \
                     f'Пятый участник: {mem5}, {mem5_pro_potok}\n' \
                     f'Шестой участник: {mem6}, {mem6_pro_potok}'
        bot.send_message(-1001892934814, main_text)



    return render(request, 'index.html')




def done(request):
    return render(request, 'index.html')


