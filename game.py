from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from Musica import play, stop

PC = []

PC_check = []

items = []

programs = []

skills = []

power = 0

similarity = 0

sim = 0

power_check_global = 0

class SKFButton(Button): #Класс для кнопок SkillFox/main чтобы при наведении на них менялся цвет
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultImage = self["image"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        if e.widget.winfo_x() == 64 and e.widget.winfo_y() == 160:
            self.Activ = PhotoImage(file=r'Image\ActiveProgrammingButton.png')
            self['image'] = self.Activ
        elif e.widget.winfo_x() == 427 and e.widget.winfo_y() == 160:
            self.Activ = PhotoImage(file=r'Image\ActiveDesignButton.png')
            self['image'] = self.Activ
        elif e.widget.winfo_x() == 790 and e.widget.winfo_y() == 160:
            self.Activ = PhotoImage(file=r'Image\ActiveMarketingButton.png')
            self['image'] = self.Activ
        elif e.widget.winfo_x() == 1155 and e.widget.winfo_y() == 160:
            self.Activ = PhotoImage(file=r'Image\ActiveManagmentButton.png')
            self['image'] = self.Activ
        elif e.widget.winfo_x() == 1520 and e.widget.winfo_y() == 160:
            self.Activ = PhotoImage(file=r'Image\ActiveGamesButton.png')
            self['image'] = self.Activ
        else:
            print(e.widget.winfo_x())
            print(e.widget.winfo_y())
    def on_leave(self, e):
        self['image'] = self.defaultImage


class SFProg(Button): #Класс для кнопок SkillFox/prog  чтобы при наведении на них менялся цвет
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultImage = self["image"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        if e.widget.winfo_x() == 50 and e.widget.winfo_y() == 193 or \
                e.widget.winfo_x() == 708 and e.widget.winfo_y() == 433:
            self.Activ = PhotoImage(file=r'Image\ActivePythonDeveloper.png')
            self['image'] = self.Activ
        elif e.widget.winfo_x() == 728 and e.widget.winfo_y() == 193:
            self.Activ = PhotoImage(file=r'Image\ActiveUnityDeveloper.png')
            self['image'] = self.Activ
        elif e.widget.winfo_x() == 1390 and e.widget.winfo_y() == 193:
            self.Activ = PhotoImage(file=r'Image\ActiveAppsDeveloper.png')
            self['image'] = self.Activ
        elif e.widget.winfo_x() == 50 and e.widget.winfo_y() == 490:
            self.Activ = PhotoImage(file=r'Image\ActiveWebDeveloper.png')
            self['image'] = self.Activ
        else:
            print(e.widget.winfo_x())
            print(e.widget.winfo_y())
    def on_leave(self, e):
        self['image'] = self.defaultImage

########################################
with open('Save files\PC.txt', 'r') as filehandle:
    savefile = filehandle.readlines()
    for line in savefile:
        current_place = line[:-1]
        PC.append(current_place)

with open('Save files\PC_elements.txt', 'r') as filehandle:
    savefile = filehandle.readlines()
    for line in savefile:
        current_place = line[:-1]
        PC_check.append(current_place)

with open('Save files\Items.txt', 'r') as filehandle:
    savefile = filehandle.readlines()
    for line in savefile:
        current_place = line[:-1]
        items.append(current_place)

with open('Save files\Skills.txt', 'r') as filehandle:
    savefile = filehandle.readlines()
    for line in savefile:
        current_place = line[:-1]
        skills.append(current_place)

with open('Save files\Programs.txt', 'r') as filehandle:
    savefile = filehandle.readlines()
    for line in savefile:
        current_place = line[:-1]
        programs.append(current_place)
########################################

PC1 = ['Процессор 1', 'Мат плата 1', 'Видеокарта 1', 'Видеокарта 2', 'ХДД 1', 'ХДД 2', 'Кулер 1', 'Кулер 2', 'ОЗУ 1',
       'ОЗУ 2', 'БП 1', 'БП 2']

PC2 = ['Процессор 2', 'Мат плата 2', 'Видеокарта 2', 'Видеокарта 3', 'ХДД 1', 'ХДД 2', 'Кулер 1', 'Кулер 2', 'БП 2',
       'ОЗУ 3']

########################################

########################################

########################################

########################################

########################################
f = open('Save files\save_variable.txt', 'r')
savefile = f.read().splitlines()

mfc = int(savefile[0]) #Доход за клик
money = int(savefile[1])
level = int(savefile[2])
level_ex = int(savefile[3])
bills = int(savefile[4])

Music = int(savefile[5])
dark_theme = int(savefile[6])

efficiency = int(savefile[7]) #Мощность компьютера
free_memory = int(savefile[8]) #Кол-во свободной памяти
load_memory = int(savefile[9]) #Кол-во занятой памяти

f.close()
########################################

########################################

########################################

########################################

########################################

root = Tk()

root.title('Кликер')
root.attributes('-fullscreen', True)


def slots(variant):
    moneyLabel.place_forget()
    if variant == 'Мат плата':
        NoSlotPhoto = PhotoImage(file=r'Image\no slot motherboard.png')
    elif variant == 'Блок питания':
        NoSlotPhoto = PhotoImage(file=r'Image\no slot power.png')
    elif variant == 'Процессор':
        NoSlotPhoto = PhotoImage(file=r'Image\no slot processor.png')
    elif variant == 'Кулер':
        NoSlotPhoto = PhotoImage(file=r'Image\no slot processor.png')
    elif variant == 'ОЗУ':
        NoSlotPhoto = PhotoImage(file=r'Image\no slot processor.png')
    elif variant == 'Видеокарта':
        NoSlotPhoto = PhotoImage(file=r'Image\no slot videocard.png')
    elif variant == 'ХДД':
        NoSlotPhoto = PhotoImage(file=r'Image\no slot videocard.png')
    no_slots_label = Label(root, image=NoSlotPhoto, bg='#333333', bd=0)
    no_slots_label.place(x=0, y=0)
    root.after(2000, no_slots_label.place_forget)
    root.update()
    root.after(2000, moneyLabel.place(x=10, y=80))
    root.update


def PC_change_sort(item):
    global similarity, power, efficiency, PC_check, PC, load_memory, free_memory
    power_check = 0
    HDD_check = 0
    no = Label(root, text='')
    if 'БП' in PC_check:
        if efficiency <= power:
            if list(item)[0] == 'Б':
                no = Label(root, text='Вы не можете установить данный предмет,\n'
                                      'т.к. предмет такого типа уже установлен')
                no.place(x=100, y=100)
                root.after(1000, no.place_forget)
                root.update()
            elif list(item)[0] == 'В':
                if 'Видеокарта' not in PC_check:
                    PC_check.append('Видеокарта')
                    PC.append(item)
                    similarity = 1
            elif list(item)[0] == 'К':
                if 'Кулер' not in PC_check:
                    PC_check.append('Кулер')
                    PC.append(item)
                    similarity = 1
            elif list(item)[0] == 'М':
                if 'Мат плата' not in PC_check:
                    PC_check.append('Мат плата')
                    PC.append(item)
                    similarity = 1
            elif list(item)[0] == 'О':
                if 'ОЗУ' not in PC_check:
                    PC_check.append('ОЗУ')
                    PC.append(item)
                    similarity = 1
            elif list(item)[0] == 'П':
                if 'Процессор' not in PC_check:
                    PC_check.append('Процессор')
                    PC.append(item)
                    similarity = 1
            elif list(item)[0] == 'Х':
                if 'ХДД' not in PC_check:
                    if load_memory <= free_memory:
                        PC_check.append('ХДД')
                        PC.append(item)
                        similarity = 1
                    else:
                        no = Label(root, text='Вы не можете установить данный предмет,\n'
                                              'т.к. не хватает памяти.')
                        no.place(x=100, y=100)
                        root.after(1000, no.place_forget)
                        root.update()
                        HDD_check = 1
            if similarity == 0 and HDD_check == 0:
                no = Label(root, text='Вы не можете установить данный предмет,\n'
                                      'т.к. предмет такого типа уже установлен')
                no.place(x=100, y=100)
                root.after(1000, no.place_forget)
                root.update()
        else:
            no = Label(root, text='Вы не можете установить данный предмет,\n'
                                  'т.к. не хватает мощности блока питания')
            no.place(x=100, y=100)
            root.after(1000, no.place_forget)
            root.update()
    else:
        if list(item)[0] == 'Б':
            if 'БП' not in PC_check:
                if power >= efficiency:
                    PC_check.append('БП')
                    PC.append(item)
                    similarity = 1
                else:
                    no = Label(root, text='Вы не можете установить этот блок питания,\n'
                                          'т.к. не хватает мощности')
                    power_check = 1
                    no.place(x=100, y=100)
                    root.after(1000, no.place_forget)
                    root.update()
        elif list(item)[0] == 'В':
            if 'Видеокарта' not in PC_check:
                PC_check.append('Видеокарта')
                PC.append(item)
                similarity = 1
        elif list(item)[0] == 'К':
            if 'Кулер' not in PC_check:
                PC_check.append('Кулер')
                PC.append(item)
                similarity = 1
        elif list(item)[0] == 'М':
            if 'Мат плата' not in PC_check:
                PC_check.append('Мат плата')
                PC.append(item)
                similarity = 1
        elif list(item)[0] == 'О':
            if 'ОЗУ' not in PC_check:
                PC_check.append('ОЗУ')
                PC.append(item)
                similarity = 1
        elif list(item)[0] == 'П':
            if 'Процессор' not in PC_check:
                PC_check.append('Процессор')
                PC.append(item)
                similarity = 1
        elif list(item)[0] == 'Х':
            if load_memory <= free_memory:
                PC_check.append('ХДД')
                PC.append(item)
                similarity = 1
            else:
                no = Label(root, text='Вы не можете установить данный предмет,\n'
                                      'т.к. не хватает памяти.')
                no.place(x=100, y=100)
                root.after(1000, no.place_forget)
                root.update()
                HDD_check = 1
        if similarity == 0 and power_check == 0 and HDD_check == 0:
            no = Label(root, text='Вы не можете установить данный предмет,\n'
                          'т.к. предмет такого типа уже установлен')
            no.place(x=100, y=100)
            root.after(1000, no.place_forget)
            root.update()


def PC_change_check(item):
    global similarity
    similarity = 0
    if len(PC) == 0:
        PC_change_sort(item)
        similarity = 1
    else:
        if item not in PC:
            if PC[0] in PC1:
                if item in PC1:
                    PC_change_sort(item)
                else:
                    no = Label(root, text='Этот предмет не подходит для сборки')
                    no.place(x=100, y=100)
                    root.after(1000, no.place_forget)
                    root.update()
            elif PC[0] in PC2:
                if item in PC1:
                    PC_change_sort(item)
                else:
                    no = Label(root, text='Этот предмет не подходит для сборки')
                    no.place(x=100, y=100)
                    root.after(1000, no.place_forget)
                    root.update()
            else:
                no = Label(root, text='Этот предмет не подходит для сборки')
                no.place(x=100, y=100)
                root.after(1000, no.place_forget)
                root.update()


def PC_change():
    Number = len(PC)
    for i in range(Number):
        if PC[i] == 'Видеокарта 1':
            VideoCard1Make['bd'] = 2
            VideoCard1Make['bg'] = '#00ff00'
        elif PC[i] == 'Видеокарта 2':
            VideoCard2Make['bd'] = 2
            VideoCard2Make['bg'] = '#00ff00'
        elif PC[i] == 'Видеокарта 3':
            VideoCard3Make['bd'] = 2
            VideoCard3Make['bg'] = '#00ff00'
        elif PC[i] == 'Видеокарта 4':
            VideoCard4Make['bd'] = 2
            VideoCard4Make['bg'] = '#00ff00'
        elif PC[i] == 'Видеокарта 5':
            VideoCard5Make['bd'] = 2
            VideoCard5Make['bg'] = '#00ff00'
        elif PC[i] == 'Видеокарта 6':
            VideoCard6Make['bd'] = 2
            VideoCard6Make['bg'] = '#00ff00'
        elif PC[i] == 'Видеокарта 7':
            VideoCard7Make['bd'] = 2
            VideoCard7Make['bg'] = '#00ff00'
        elif PC[i] == 'Мат плата 1':
            MotherBoard1Make['bd'] = 2
            MotherBoard1Make['bg'] = '#00ff00'
        elif PC[i] == 'Мат плата 2':
            MotherBoard2Make['bd'] = 2
            MotherBoard2Make['bg'] = '#00ff00'
        elif PC[i] == 'Мат плата 3':
            MotherBoard3Make['bd'] = 2
            MotherBoard3Make['bg'] = '#00ff00'
        elif PC[i] == 'Мат плата 4':
            MotherBoard4Make['bd'] = 2
            MotherBoard4Make['bg'] = '#00ff00'
        elif PC[i] == 'Процессор 1':
            Processor1Make['bd'] = 2
            Processor1Make['bg'] = '#00ff00'
        elif PC[i] == 'Процессор 2':
            Processor2Make['bd'] = 2
            Processor2Make['bg'] = '#00ff00'
        elif PC[i] == 'Процессор 3':
            Processor3Make['bd'] = 2
            Processor3Make['bg'] = '#00ff00'
        elif PC[i] == 'Процессор 4':
            Processor4Make['bd'] = 2
            Processor4Make['bg'] = '#00ff00'
        elif PC[i] == 'ХДД 1':
            HDD1Make['bd'] = 2
            HDD1Make['bg'] = '#00ff00'
        elif PC[i] == 'ХДД 2':
            HDD2Make['bd'] = 2
            HDD2Make['bg'] = '#00ff00'
        elif PC[i] == 'БП 1':
            Power1Make['bd'] = 2
            Power1Make['bg'] = '#00ff00'
        elif PC[i] == 'БП 2':
            Power2Make['bd'] = 2
            Power2Make['bg'] = '#00ff00'
        elif PC[i] == 'Кулер 1':
            Cooler1Make['bd'] = 2
            Cooler1Make['bg'] = '#00ff00'
        elif PC[i] == 'Кулер 2':
            Cooler2Make['bd'] = 2
            Cooler2Make['bg'] = '#00ff00'
        elif PC[i] == 'ОЗУ 1':
            RAM1Make['bd'] = 2
            RAM1Make['bg'] = '#00ff00'
        elif PC[i] == 'ОЗУ 2':
            RAM2Make['bd'] = 2
            RAM2Make['bg'] = '#00ff00'
        elif PC[i] == 'ОЗУ 3':
            RAM3Make['bd'] = 2
            RAM3Make['bg'] = '#00ff00'


def auto_save():
    f = open('Save files\save_variable.txt', 'w')
    f.write(str(mfc) + '\n')
    f.write(str(money) + '\n')
    f.write(str(level) + '\n')
    f.write(str(level_ex) + '\n')
    f.write(str(bills) + '\n')

    f.write(str(Music) + '\n')
    f.write(str(dark_theme) + '\n')

    f.write(str(efficiency) + '\n')

    f.write(str(free_memory) + '\n')
    f.write(str(load_memory) + '\n')

    f.close()

    with open('Save files\PC.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in PC)

    with open('Save files\PC_elements.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in PC_check)

    with open('Save files\Items.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in items)

    with open('Save files\Skills.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in skills)

    with open('Save files\Programs.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in programs)


    print('Сохранение')
    auto_save_timer()


def auto_save_timer():
    root.after(600000, auto_save)
    root.update()



def save():
    f = open('Save files\save_variable.txt', 'w')
    f.write(str(mfc) + '\n')
    f.write(str(money) + '\n')
    f.write(str(level) + '\n')
    f.write(str(level_ex) + '\n')
    f.write(str(bills) + '\n')

    f.write(str(Music) + '\n')
    f.write(str(dark_theme) + '\n')

    f.write(str(efficiency) + '\n')

    f.write(str(free_memory) + '\n')
    f.write(str(load_memory) + '\n')

    f.close()

    with open('Save files\PC.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in PC)

    with open('Save files\PC_elements.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in PC_check)

    with open('Save files\Items.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in items)

    with open('Save files\Skills.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in skills)

    with open('Save files\Programs.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in programs)

    root.destroy()


def full_size(event):
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
    else:
        root.attributes('-fullscreen', True)


root.bind('<F11>', full_size)


def money_sort():
    global money
    moneys = str(money)
    if money > 99999999:
        moneyLabel['text'] = '$' + str(moneys[0] + moneys[1] + moneys[2] + '.' + moneys[3] + moneys[4]) + 'M'
    elif money > 9999999:
        moneyLabel['text'] = '$' + str(moneys[0] + moneys[1] + '.' + moneys[2] + moneys[3]) + 'M'
    elif money > 999999:
        moneyLabel['text'] = '$' + str(moneys[0]+'.' + moneys[1] + moneys[2]) + 'M'
    elif money > 99999:
        moneyLabel['text'] = '$' + str(moneys[0] + moneys[1] + moneys[2] + '.' + moneys[3] + moneys[4]) + 'K'
    elif money > 9999:
        moneyLabel['text'] = '$' + str(moneys[0] + moneys[1] + '.' + moneys[2] + moneys[3]) + 'K'
    elif money > 999:
        moneyLabel['text'] = '$' + str(moneys[0]+'.' + moneys[1] + moneys[2]) + 'K'
    else:
        moneyLabel['text'] = '$' + str(money)



def options_open():
    close_comnata()
    OptionsPhotoLabel.place(x=0, y=0)
    BackButtonOptions.place(x=146, y=25)
    if dark_theme == 0:
        check_mark_theme_False.place(x=1000, y=370)
    else:
        check_mark_theme_True.place(x=1000, y=370)

    if Music == 1:
        check_mark_music_True.place(x=1000, y=190)
    else:
        check_mark_music_False.place(x=1000, y=190)


def back_options():
    comnata()
    OptionsPhotoLabel.place_forget()
    BackButtonOptions.place_forget()

    check_mark_theme_True.place_forget()
    check_mark_theme_False.place_forget()

    check_mark_music_True.place_forget()
    check_mark_music_False.place_forget()



def music_option():
    global Music
    if Music == 1:
        Music = 0
        check_mark_music_True.place_forget()
        check_mark_music_False.place(x=1000, y=190)
        stop()
    else:
        Music = 1
        check_mark_music_True.place(x=1000, y=190)
        check_mark_music_False.place_forget()
        play()


def theme():
    global  dark_theme
    if dark_theme == 0:
        check_mark_theme_False.place_forget()
        check_mark_theme_True.place(x=1000, y=370)
        dark_theme = 1
    else:
        check_mark_theme_True.place_forget()
        check_mark_theme_False.place(x=1000, y=370)
        dark_theme = 0


def CBut():
    global mfc, money, skills
    if money >= 3000:
        if 'C#' not in skills:
            money -= 3000
            skills.append('C#')
            money_sort()
            buy['text'] = 'Поздравляем! Вы прошли курс "Разработка игр на Unity".'
            buy.place(x=500, y=450)
            root.after(2000, buy.place_forget)
            root.update()
        else:
            bought.place(x=750, y=450)
            root.after(2000, bought.place_forget)
            root.update()
    else:
        close.place(x=700, y=400)
        root.after(2000, close.place_forget)
        root.update()


def CCBut():
    global mfc, money, skills
    if money >= 5000:
        if 'C++' not in skills:
            money -= 5000
            skills.append('C++')
            money_sort()
            buy['text'] = 'Поздравляем! Вы прошли курс "Разработка мобильных приложений".'
            buy.place(x=500, y=450)
            root.after(2000, buy.place_forget)
            root.update()
        else:
            bought.place(x=750, y=450)
            root.after(2000, bought.place_forget)
            root.update()
    else:
        close.place(x=700, y=400)
        root.after(2000, close.place_forget)
        root.update()


def JavaScript():
    global mfc, money, skills
    if money >= 18000:
        if 'JavaScript' not in skills:
            money -= 18000
            skills.append('JavaScript')
            money_sort()
            buy['text'] = 'Поздравляем! Вы освоили профессию "Веб-разработчик".'
            buy.place(x=500, y=450)
            root.after(2000, buy.place_forget)
            root.update()
        else:
            bought.place(x=750, y=450)
            root.after(2000, bought.place_forget)
            root.update()
    else:
        close.place(x=700, y=400)
        root.after(2000, close.place_forget)
        root.update()


def timer_JKH():
    root.after(60000, JKH)
    root.update()


def JKH():
    global money, bills
    KolVoItems = len(items)
    money -= bills
    money -= KolVoItems * 10
    money_sort()
    root.after(1, timer_JKH)


def VideoCardOpen():
    back_Market()
    close_comnata()
    BackButtonVideoCard.place(x=142, y=26)
    VideoCardPhotoLabel.place(x=0, y=0)
    moneyLabel.place(x=10, y=80)

    VideoCard1Button.place(x=20, y=200)
    VideoCard2Button.place(x=340, y=200)
    VideoCard3Button.place(x=660, y=200)
    VideoCard4Button.place(x=980, y=200)
    VideoCard5Button.place(x=1300, y=200)
    VideoCard6Button.place(x=1620, y=200)
    VideoCard7Button.place(x=20, y=500)


def VideoCard1_buy():
    global items, money
    number = len(items)
    if 'Видеокарта 1' not in items:
        if money >= 3900:
            if number < 12:
                items.append('Видеокарта 1')
                money -= 3900
                money_sort()
            else:
                slots('Видеокарта')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def VideoCard2_buy():
    global items, VideoCard2_variable, money
    number = len(items)
    if 'Видеокарта 2' not in items:
        if money >= 7000:
            if number < 12:
                items.append('Видеокарта 2')
                money -= 7000
                money_sort()
            else:
                slots('Видеокарта')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def VideoCard3_buy():
    global items, money
    number = len(items)
    if 'Видеокарта 3' not in items:
        if money >= 10100:
            if number < 12:
                items.append('Видеокарта 3')
                money -=10100
                money_sort()
            else:
                slots('Видеокарта')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def VideoCard4_buy():
    global items, money
    number = len(items)
    if 'Видеокарта 4' not in items:
        if money >= 10500:
            if number < 12:
                items.append('Видеокарта 4')
                money -= 10500
                money_sort()
            else:
                slots('Видеокарта')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def VideoCard5_buy():
    global items, money
    number = len(items)
    if 'Видеокарта 5' not in items:
        if money >= 16200:
            if number < 12:
                items.append('Видеокарта 5')
                money -= 16200
                money_sort()
            else:
                slots('Видеокарта')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def VideoCard6_buy():
    global items, money
    number = len(items)
    if 'Видеокарта 6' not in items:
        if money >= 20600:
            if number < 12:
                items.append('Видеокарта 6')
                money -= 20600
                money_sort()
            else:
                slots('Видеокарта')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def VideoCard7_buy():
    global items, money
    number = len(items)
    if 'Видеокарта 7' not in items:
        if money >= 34500:
            if number < 12:
                items.append('Видеокарта 7')
                money -= 34500
                money_sort()
            else:
                slots('Видеокарта')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def back_VideoCard():
    BackButtonVideoCard.place_forget()
    VideoCardPhotoLabel.place_forget()
    moneyLabel.place_forget()

    VideoCard1Button.place_forget()
    VideoCard2Button.place_forget()
    VideoCard3Button.place_forget()
    VideoCard4Button.place_forget()
    VideoCard5Button.place_forget()
    VideoCard6Button.place_forget()
    VideoCard7Button.place_forget()

    Market_open()


def ProcessorOpen():
    back_Market()
    close_comnata()
    moneyLabel.place(x=10, y=80)
    ProcessorMarket.place(x=0, y=0)
    BackButtonProcessor.place(x=142, y=26)

    Processor1Button.place(x=20, y=200)
    Processor2Button.place(x=340, y=200)
    Processor3Button.place(x=660, y=200)
    Processor4Button.place(x=980, y=200)


def Processor1_buy():
    global items, money
    number = len(items)
    if 'Процессор 1' not in items:
        if money >= 2000:
            if number < 12:
                items.append('Процессор 1')
                money -= 2000
                money_sort()
            else:
                slots('Процессор')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def Processor2_buy():
    global items, money
    number = len(items)
    if 'Процессор 2' not in items:
        if money >= 4000:
            if number < 12:
                items.append('Процессор 2')
                money -= 4000
                money_sort()
            else:
                slots('Процессор')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def Processor3_buy():
    global items, money
    number = len(items)
    if 'Процессор 3' not in items:
        if money >= 14000:
            if number < 12:
                items.append('Процессор 3')
                money -= 14000
                money_sort()
            else:
                slots('Процессор')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def Processor4_buy():
    global items, money
    number = len(items)
    if 'Процессор 4' not in items:
        if money >= 19000:
            if number < 12:
                items.append('Процессор 4')
                money -= 19000
                money_sort()
            else:
                slots('Процессор')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def back_Processor():
    ProcessorMarket.place_forget()
    BackButtonProcessor.place_forget()
    Processor1Button.place_forget()
    Processor2Button.place_forget()
    Processor3Button.place_forget()
    Processor4Button.place_forget()

    Market_open()


def PowerOpen():
    back_Market()
    close_comnata()
    moneyLabel.place(x=10, y=80)
    BackButtonPower.place(x=142, y=26)
    PowerMarket.place(x=0, y=0)

    Power1Button.place(x=20, y=200)
    Power2Button.place(x=340, y=200)


def Power1_buy():
    global items, money
    number = len(items)
    if 'БП 1' not in items:
        if money >= 1000:
            if number < 12:
                items.append('БП 1')
                money -= 1000
                money_sort()
            else:
                slots('Блок питания')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def Power2_buy():
    global items, money
    number = len(items)
    if 'БП 2' not in items:
        if money >= 1650:
            if number < 12:
                items.append('БП 2')
                money -= 1650
                money_sort()
            else:
                slots('Блок питания')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def back_power():
    BackButtonPower.place_forget()
    PowerMarket.place_forget()

    Power1Button.place_forget()
    Power2Button.place_forget()

    Market_open()


def MotherBoardOpen():
    back_Market()
    close_comnata()
    moneyLabel.place(x=10, y=80)
    MotherBoardLabel.place(x=0, y=0)
    BackButtonMotherBoard.place(x=142, y=26)
    MotherBoard1Button.place(x=20, y=200)
    MotherBoard2Button.place(x=340, y=200)
    MotherBoard3Button.place(x=660, y=200)
    MotherBoard4Button.place(x=980, y=200)


def MotherBoard1_buy():
    global items, money
    number = len(items)
    if 'Мат плата 1' not in items:
        if money >= 2000:
            if number < 12:
                items.append('Мат плата 1')
                money -= 2000
                money_sort()
            else:
                slots('Мат плата')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def MotherBoard2_buy():
    global items, money
    number = len(items)
    if 'Мат плата 2' not in items:
        if money >= 3100:
            if number < 12:
                items.append('Мат плата 2')
                money -= 3100
                money_sort()
            else:
                slots('Мат плата')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def MotherBoard3_buy():
    global items, money
    number = len(items)
    if 'Мат плата 3' not in items:
        if money >= 5000:
            if number < 12:
                items.append('Мат плата 3')
                money -= 5000
                money_sort()
            else:
                slots('Мат плата')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def MotherBoard4_buy():
    global items, money
    number = len(items)
    if 'Мат плата 4' not in items:
        if money >= 5500:
            if number < 12:
                items.append('Мат плата 4')
                MotherBoard4_variable = 1
                money -= 5500
                money_sort()
            else:
                slots('Мат плата')
        else:
                close.place(x=700, y=400)
                root.after(2000, close.place_forget)
                root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def back_MotherBoard():
    MotherBoardLabel.place_forget()
    BackButtonMotherBoard.place_forget()
    MotherBoard1Button.place_forget()
    MotherBoard2Button.place_forget()
    MotherBoard3Button.place_forget()
    MotherBoard4Button.place_forget()

    Market_open()


def CoolerOpen():
    back_Market()
    close_comnata()
    CoolerMarket.place(x=0, y=0)
    BackButtonCooler.place(x=142, y=26)
    moneyLabel.place(x=10, y=80)

    Cooler1Button.place(x=20, y=200)
    Cooler2Button.place(x=340, y=200)


def Cooler1_buy():
    global items, money
    number = len(items)
    if 'Кулер 1' not in items:
        if money >= 350:
            if number < 12:
                items.append('Кулер 1')
                money -= 350
                money_sort()
            else:
                slots('Кулер')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def Cooler2_buy():
    global items, money
    number = len(items)
    if 'Кулер 2' not in items:
        if money >= 800:
            if number < 12:
                items.append('Кулер 2')
                money -= 800
                money_sort()
            else:
                slots('Кулер')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def back_cooler():
    BackButtonCooler.place_forget()
    CoolerMarket.place_forget()

    Cooler1Button.place_forget()
    Cooler2Button.place_forget()

    Market_open()


def RamOpen():
    back_Market()
    close_comnata()
    RAMMarket.place(x=0, y=0)
    BackButtonRAM.place(x=142, y=26)
    moneyLabel.place(x=10, y=80)

    RAM1Button.place(x=20, y=200)
    RAM2Button.place(x=340, y=200)
    RAM3Button.place(x=660, y=200)


def RAM1_buy():
    global items, money
    number = len(items)
    if 'ОЗУ 1' not in items:
        if money >= 400:
            if number < 12:
                items.append('ОЗУ 1')
                money -= 400
                money_sort()
            else:
                slots('ОЗУ')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def RAM2_buy():
    global items, money
    number = len(items)
    if 'ОЗУ 2' not in items:
        if money >= 1200:
            if number < 12:
                items.append('ОЗУ 2')
                money -= 1200
                money_sort()
            else:
                slots('ОЗУ')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def RAM3_buy():
    global items, money
    number = len(items)
    if 'ОЗУ 3' not in items:
        if money >= 1200:
            if number < 12:
                items.append('ОЗУ 3')
                money -= 1200
                money_sort()
            else:
                slots('ОЗУ')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def back_RAM():
    BackButtonRAM.place_forget()
    RAMMarket.place_forget()

    RAM1Button.place_forget()
    RAM2Button.place_forget()
    RAM3Button.place_forget()

    Market_open()


def HDDOpen():
    back_Market()
    close_comnata()
    HDDMarket.place(x=0, y=0)
    BackButtonHDD.place(x=142, y=26)
    moneyLabel.place(x=10, y=80)

    HDD1Button.place(x=20, y=200)
    HDD2Button.place(x=340, y=200)


def HDD1_buy():
    global items, money
    number = len(items)
    if 'ХДД 1' not in items:
        if money >= 1000:
            if number < 12:
                items.append('ХДД 1')
                money -= 1000
                money_sort()
            else:
                slots('ХДД')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def HDD2_buy():
    global items, money
    number = len(items)
    if 'ХДД 2' not in items:
        if money >= 1800:
            if number < 12:
                items.append('ХДД 2')
                money -= 1800
                money_sort()
            else:
                slots('ХДД')
        else:
            close.place(x=700, y=400)
            root.after(2000, close.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def back_HDD():
    HDDMarket.place_forget()
    BackButtonHDD.place_forget()
    moneyLabel.place_forget()

    HDD1Button.place_forget()
    HDD2Button.place_forget()

    Market_open()


def SoftOpen():
    back_Market()
    close_comnata()

    SoftLabel.place(x=0, y=0)
    BackButtonSoft.place(x=142, y=26)

    SoftPythonButton.place(x=20, y=200)
    SoftCSharpButton.place(x=340, y=200)
    SoftCPlusPlusButton.place(x=660, y=200)
    SoftJavaScriptButton.place(x=980, y=200)


def SoftPython_buy():
    global programs, money, skills, efficiency, mfc, free_memory
    if 'Python IDE' not in programs:
        if 'Python' in skills:
            if efficiency > 20:
                if free_memory >= 5:
                    programs.append('Python IDE')
                    mfc += 1
                    yes = Label(root, text='Вы успешно приобрели "IDE Python"')
                    yes.place(x=750, y=450)
                    root.after(2000, yes.place_forget)
                    root.update()
                    free_memory -= 5
                else:
                    no = Label(root, text='На вашем компьютере недостаточно места')
                    no.place(x=750, y=450)
                    root.after(2000, no.place_forget)
                    root.update()
            else:
                no = Label(root, text='Ваш компьютер не соответствует требованиям')
                no.place(x=750, y=450)
                root.after(2000, no.place_forget)
                root.update()
        else:
            no = Label(root, text='Выши навыки не соответствуют требованиям')
            no.place(x=750, y=450)
            root.after(2000, no.place_forget)
            root.update()
    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def SoftCSharrp_buy():
    global programs, money, skills, efficiency, mfc, free_memory
    if 'Unity' not in programs:
        if money >= 50:
            if 'Unity' in skills:
                if efficiency > 25:
                    if free_memory >= 15:
                        programs.append('Unity')
                        mfc += 1
                        yes = Label(root, text='Вы успешно приобрели "Unity"')
                        yes.place(x=750, y=450)
                        root.after(2000, yes.place_forget)
                        root.update()
                        free_memory -= 15
                    else:
                        no = Label(root, text='На вашем компьютере недостаточно места')
                        no.place(x=750, y=450)
                        root.after(2000, no.place_forget)
                        root.update()
                else:
                    no = Label(root, text='Ваш компьютер не соответствует требованиям')
                    no.place(x=750, y=450)
                    root.after(2000, no.place_forget)
                    root.update()
            else:
                no = Label(root, text='Выши навыки не соответствуют требованиям')
                no.place(x=750, y=450)
                root.after(2000, no.place_forget)
                root.update()
        else:
            no = Label(root, text='У вас недостаточно средств!')
            no.place(x=450, y=450)
            root.after(2000, no.place_forget)
            root.update()

    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def SoftCPlusPlus_buy():
    global programs, money, skills, efficiency, mfc, free_memory
    if 'Apps' not in programs:
        if money >= 50:
            if 'Apps' in skills:
                if efficiency > 30:
                    if free_memory >= 10:
                        programs.append('Apps')
                        mfc += 1
                        yes = Label(root, text='Вы успешно приобрели "IDE C++"')
                        yes.place(x=750, y=450)
                        root.after(2000, yes.place_forget)
                        root.update()
                        free_memory -= 10
                    else:
                        no = Label(root, text='На вашем компьютере недостаточно места')
                        no.place(x=750, y=450)
                        root.after(2000, no.place_forget)
                        root.update()
                else:
                    no = Label(root, text='Ваш компьютер не соответствует требованиям')
                    no.place(x=750, y=450)
                    root.after(2000, no.place_forget)
                    root.update()
            else:
                no = Label(root, text='Выши навыки не соответствуют требованиям')
                no.place(x=750, y=450)
                root.after(2000, no.place_forget)
                root.update()
        else:
            no = Label(root, text='У вас недостаточно средств!')
            no.place(x=450, y=450)
            root.after(2000, no.place_forget)
            root.update()

    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def SoftJavaScript_buy():
    global programs, money, skills, efficiency, mfc, free_memory
    if 'Web' not in programs:
        if money >= 50:
            if 'Web' in skills:
                if efficiency > 35:
                    if free_memory >= 15:
                        programs.append('JavaScript IDE')
                        mfc += 1
                        yes = Label(root, text='Вы успешно приобрели "IDE JavaScript"')
                        yes.place(x=750, y=450)
                        root.after(2000, yes.place_forget)
                        root.update()
                        free_memory -= 15
                    else:
                        no = Label(root, text='На вашем компьютере недостаточно места')
                        no.place(x=750, y=450)
                        root.after(2000, no.place_forget)
                        root.update()
                else:
                    no = Label(root, text='Ваш компьютер не соответствует требованиям')
                    no.place(x=750, y=450)
                    root.after(2000, no.place_forget)
                    root.update()
            else:
                no = Label(root, text='Выши навыки не соответствуют требованиям')
                no.place(x=750, y=450)
                root.after(2000, no.place_forget)
                root.update()
        else:
            no = Label(root, text='У вас недостаточно средств!')
            no.place(x=450, y=450)
            root.after(2000, no.place_forget)
            root.update()

    else:
        bought.place(x=750, y=450)
        root.after(2000, bought.place_forget)
        root.update()


def back_soft():
    SoftLabel.place_forget()
    BackButtonSoft.place_forget()

    SoftPythonButton.place_forget()
    SoftCSharpButton.place_forget()
    SoftCPlusPlusButton.place_forget()
    SoftJavaScriptButton.place_forget()

    Market_open()


def close_but():
    close.place_forget()
    bought.place_forget()
    buy.place_forget()


def back_Market():
    moneyLabel.place_forget()
    MarketPhotoLabel.place_forget()
    BackButtonMarket.place_forget()
    ProcessorButton.place_forget()
    VideoCardButton.place_forget()
    HDDButton.place_forget()
    CoolerButton.place_forget()
    RAMButton.place_forget()
    PowerButton.place_forget()
    MotherBoardButton.place_forget()
    SoftButton.place_forget()
    ScreenOpen()


def no_exit():
    WarningExitLabel.place_forget()
    YesExitButton.place_forget()
    NoExitButton.place_forget()


def warning_exit():
    WarningExitLabel.place(x=0, y=0)
    YesExitButton.place(x=790, y=540)
    NoExitButton.place(x=960, y=555)


def Up_make():
    UP_or_Down = 'UP'
    inventory_make_pc(UP_or_Down)

def Down_make():
    UP_or_Down = 'DOWN'
    inventory_make_pc(UP_or_Down)


def make_computer():
    close_comnata()
    MakePcLabel.place(x=0, y=0)
    BackPcButton.place(x=0, y=0)

    MakeUpButton.place(x=1600, y=80)
    MakeDownButton.place(x=1600, y=1000)

    Up_make()


def VideoCard1_On():
    global similarity, efficiency
    if VideoCard1Make['bd'] == 0:
        if 'Видеокарта' not in PC_check:
            efficiency += 10
            PC_change_check('Видеокарта 1')
            if similarity == 1:
                VideoCard1Make['bd'] = 2
                VideoCard1Make['bg'] = '#00ff00'
            else:
                efficiency -= 10
        else:
            PC_change_check('Видеокарта 1')
    else:
        if 'Видеокарта 1' in PC:
            VideoCard1Make['bd'] = 0
            VideoCard1Make['bg'] = '#333333'
            PC.remove('Видеокарта 1')
            PC_check.remove('Видеокарта')
            efficiency -= 10


def VideoCard2_On():
    global similarity, efficiency
    if VideoCard2Make['bd'] == 0:
        if 'Видеокарта' not in PC_check:
            efficiency += 20
            PC_change_check('Видеокарта 2')
            if similarity == 1:
                VideoCard2Make['bd'] = 2
                VideoCard2Make['bg'] = '#00ff00'
            else:
                efficiency -= 20
        else:
            PC_change_check('Видеокарта 2')
    else:
        if 'Видеокарта 2' in PC:
            VideoCard2Make['bd'] = 0
            VideoCard2Make['bg'] = '#333333'
            PC.remove('Видеокарта 2')
            PC_check.remove('Видеокарта')
            efficiency -= 20


def VideoCard3_On():
    global similarity, efficiency
    if VideoCard3Make['bd'] == 0:
        if 'Видеокарта' not in PC_check:
            efficiency += 30
            PC_change_check('Видеокарта 3')
            if similarity == 1:
                VideoCard3Make['bd'] = 2
                VideoCard3Make['bg'] = '#00ff00'
            else:
                efficiency -= 30
        else:
            PC_change_check('Видеокарта 3')
    else:
        if 'Видеокарта 3' in PC:
            VideoCard3Make['bd'] = 0
            VideoCard3Make['bg'] = '#333333'
            PC.remove('Видеокарта 3')
            PC_check.remove('Видеокарта')
            efficiency -= 30


def VideoCard4_On():
    global similarity, efficiency
    if VideoCard4Make['bd'] == 0:
        if 'Видеокарта' not in PC_check:
            efficiency += 40
            PC_change_check('Видеокарта 4')
            if similarity == 1:
                VideoCard4Make['bd'] = 2
                VideoCard4Make['bg'] = '#00ff00'
            else:
                efficiency -= 40
        else:
            PC_change_check('Видеокарта 4')
    else:
        if 'Видеокарта 4' in PC:
            VideoCard4Make['bd'] = 0
            VideoCard4Make['bg'] = '#333333'
            PC.remove('Видеокарта 4')
            PC_check.remove('Видеокарта')
            efficiency -=40


def VideoCard5_On():
    global similarity, efficiency
    if VideoCard5Make['bd'] == 0:
        if 'Видеокарта' not in PC_check:
            efficiency += 50
            PC_change_check('Видеокарта 5')
            if similarity == 1:
                VideoCard5Make['bd'] = 2
                VideoCard5Make['bg'] = '#00ff00'
            else:
                efficiency -= 50
        else:
            PC_change_check('Видеокарта 5')
    else:
        if 'Видеокарта 5' in PC:
            VideoCard5Make['bd'] = 0
            VideoCard5Make['bg'] = '#333333'
            PC.remove('Видеокарта 5')
            PC_check.remove('Видеокарта')
            efficiency -= 50


def VideoCard6_On():
    global similarity, efficiency
    if VideoCard6Make['bd'] == 0:
        if 'Видеокарта' not in PC_check:
            efficiency += 60
            PC_change_check('Видеокарта 6')
            if similarity == 1:
                VideoCard6Make['bd'] = 2
                VideoCard6Make['bg'] = '#00ff00'
            else:
                efficiency -= 60
        else:
            PC_change_check('Видеокарта 6')
    else:
        if 'Видеокарта 6' in PC:
            VideoCard6Make['bd'] = 0
            VideoCard6Make['bg'] = '#333333'
            PC.remove('Видеокарта 6')
            PC_check.remove('Видеокарта')
            efficiency -= 60


def VideoCard7_On():
    global similarity, efficiency
    if VideoCard7Make['bd'] == 0:
        if 'Видеокарта' not in PC_check:
            efficiency += 70
            PC_change_check('Видеокарта 7')
            if similarity == 1:
                VideoCard7Make['bd'] = 2
                VideoCard7Make['bg'] = '#00ff00'
            else:
                efficiency -= 70
        else:
            PC_change_check('Видеокарта 7')
    else:
        if 'Видеокарта 7' in PC:
            VideoCard7Make['bd'] = 0
            VideoCard7Make['bg'] = '#333333'
            PC.remove('Видеокарта 7')
            PC_check.remove('Видеокарта')
            efficiency -= 70


def MotherBoard1_On():
    global similarity,efficiency
    if MotherBoard1Make['bd'] == 0:
        if 'Мат плата' not in PC_check:
            efficiency += 2
            PC_change_check('Мат плата 1')
            if similarity == 1:
                MotherBoard1Make['bd'] = 2
                MotherBoard1Make['bg'] = '#00ff00'
            else:
                efficiency -= 2
        else:
            PC_change_check('Мат плата 1')
    else:
        if 'Мат плата 1' in PC:
            MotherBoard1Make['bd'] = 0
            MotherBoard1Make['bg'] = '#333333'
            PC.remove('Мат плата 1')
            PC_check.remove('Мат плата')
            efficiency -= 2


def MotherBoard2_On():
    global similarity, efficiency
    if MotherBoard2Make['bd'] == 0:
        if 'Мат плата' not in PC_check:
            efficiency += 5
            PC_change_check('Мат плата 2')
            if similarity == 1:
                MotherBoard2Make['bd'] = 2
                MotherBoard2Make['bg'] = '#00ff00'
            else:
                efficiency -= 5
        else:
            PC_change_check('Мат плата 2')
    else:
        if 'Мат плата 2' in PC:
            MotherBoard2Make['bd'] = 0
            MotherBoard2Make['bg'] = '#333333'
            PC.remove('Мат плата 2')
            PC_check.remove('Мат плата')
            efficiency -= 5


def MotherBoard3_On():
    global similarity, efficiency
    if MotherBoard3Make['bd'] == 0:
        if 'Мат плата' not in PC_check:
            efficiency += 8
            PC_change_check('Мат плата 3')
            if similarity == 1:
                MotherBoard3Make['bd'] = 2
                MotherBoard3Make['bg'] = '#00ff00'
            else:
                efficiency -= 8
        else:
            PC_change_check('Мат плата 3')
    else:
        if 'Мат плата 3' in PC:
            MotherBoard3Make['bd'] = 0
            MotherBoard3Make['bg'] = '#333333'
            PC.remove('Мат плата 3')
            PC_check.remove('Мат плата')
            efficiency -= 8


def MotherBoard4_On():
    global similarity, efficiency
    if MotherBoard4Make['bd'] == 0:
        if 'Мат плата' not in PC_check:
            efficiency += 10
            PC_change_check('Мат плата 4')
            if similarity == 1:
                MotherBoard4Make['bd'] = 2
                MotherBoard4Make['bg'] = '#00ff00'
            else:
                efficiency -= 10
        else:
            PC_change_check('Мат плата 4')
    else:
        if 'Мат плата 4' in PC:
            MotherBoard4Make['bd'] = 0
            MotherBoard4Make['bg'] = '#333333'
            PC.remove('Мат плата 4')
            PC_check.remove('Мат плата')
            efficiency -= 10


def Processor1_On():
    global similarity, efficiency
    if Processor1Make['bd'] == 0:
        if 'Процессор' not in PC_check:
            efficiency += 10
            PC_change_check('Процессор 1')
            if similarity == 1:
                Processor1Make['bd'] = 2
                Processor1Make['bg'] = '#00ff00'
            else:
                efficiency -= 10
        else:
            PC_change_check('Процессор 1')
    else:
        if 'Процессор 1' in PC:
            Processor1Make['bd'] = 0
            Processor1Make['bg'] = '#333333'
            PC.remove('Процессор 1')
            PC_check.remove('Процессор')
            efficiency -= 10


def Processor2_On():
    global similarity, efficiency
    if Processor2Make['bd'] == 0:
        if 'Процессор' not in PC_check:
            efficiency += 15
            PC_change_check('Процессор 2')
            if similarity == 1:
                Processor2Make['bd'] = 2
                Processor2Make['bg'] ='#00ff00'
            else:
                efficiency -= 15
        else:
            PC_change_check('Процессор 2')
    else:
        if 'Процессор 2' in PC:
            Processor2Make['bd'] = 0
            Processor2Make['bg'] = '#333333'
            PC.remove('Процессор 2')
            PC_check.remove('Процессор')
            efficiency -= 15


def Processor3_On():
    global similarity, efficiency
    if Processor3Make['bd'] == 0:
        if 'Процессор' not in PC_check:
            efficiency += 30
            PC_change_check('Процессор 3')
            if similarity == 1:
                Processor3Make['bd'] = 2
                Processor3Make['bg'] ='#00ff00'
            else:
                efficiency -= 30
        else:
            PC_change_check('Процессор 3')
    else:
        if 'Процессор 3' in PC:
            Processor3Make['bd'] = 0
            Processor3Make['bg'] = '#333333'
            PC.remove('Процессор 3')
            PC_check.remove('Процессор')
            efficiency -= 30


def Processor4_On():
    global similarity, efficiency
    if Processor4Make['bd'] == 0:
        if 'Процессор' not in PC_check:
            efficiency += 45
            PC_change_check('Процессор 4')
            if similarity == 1:
                Processor4Make['bd'] = 2
                Processor4Make['bg'] ='#00ff00'
            else:
                efficiency -= 45
        else:
            PC_change_check('Процессор 4')
    else:
        if 'Процессор 4' in PC:
            Processor4Make['bd'] = 0
            Processor4Make['bg'] = '#333333'
            PC.remove('Процессор 4')
            PC_check.remove('Процессор')
            efficiency -= 45


def HDD1_On():
    global similarity, free_memory, load_memory
    if HDD1Make['bd'] == 0:
        if 'ХДД' not in PC_check:
            free_memory = 120
            PC_change_check('ХДД 1')
            if similarity == 1:
                HDD1Make['bd'] = 2
                HDD1Make['bg'] ='#00ff00'
                free_memory -= load_memory
            else:
                free_memory = 0
        else:
            PC_change_check('ХДД 1')
    else:
        if 'ХДД 1' in PC:
            HDD1Make['bd'] = 0
            HDD1Make['bg'] = '#333333'
            PC.remove('ХДД 1')
            PC_check.remove('ХДД')


def HDD2_On():
    global similarity, free_memory, load_memory
    if HDD2Make['bd'] == 0:
        if 'ХДД' not in PC_check:
            free_memory = 500
            PC_change_check('ХДД 2')
            if similarity == 1:
                HDD2Make['bd'] = 2
                HDD2Make['bg'] ='#00ff00'
                free_memory -= load_memory
            else:
                free_memory = 0
        else:
            PC_change_check('ХДД 2')
    else:
        if 'ХДД 2' in PC:
            HDD2Make['bd'] = 0
            HDD2Make['bg'] = '#333333'
            PC.remove('ХДД 2')
            PC_check.remove('ХДД')


def Power1_On():
    global similarity, power
    if Power1Make['bd'] == 0:
        if 'БП' not in PC_check:
            power = 35
            PC_change_check('БП 1')
            if similarity == 1:
                Power1Make['bd'] = 2
                Power1Make['bg'] ='#00ff00'
            else:
                power = 0
        else:
            PC_change_check('БП 1')
    else:
        if 'БП 1' in PC:
            Power1Make['bd'] = 0
            Power1Make['bg'] = '#333333'
            PC.remove('БП 1')
            PC_check.remove('БП')
            power = 0


def Power2_On():
    global similarity, power
    if Power2Make['bd'] == 0:
        if 'БП' not in PC_check:
            power = 50
            PC_change_check('БП 2')
            if similarity == 1:
                Power2Make['bd'] = 2
                Power2Make['bg'] ='#00ff00'
            else:
                power = 0
        else:
            PC_change_check('БП 2')
    else:
        if 'БП 2' in PC:
            Power2Make['bd'] = 0
            Power2Make['bg'] = '#333333'
            PC.remove('БП 2')
            PC_check.remove('БП')
            power = 0


def Cooler1_On():
    global similarity
    if Cooler1Make['bd'] == 0:
        PC_change_check('Кулер 1')
        if similarity == 1:
            Cooler1Make['bd'] = 2
            Cooler1Make['bg'] ='#00ff00'
    else:
        if 'Кулер 1' in PC:
            Cooler1Make['bd'] = 0
            Cooler1Make['bg'] = '#333333'
            PC.remove('Кулер 1')
            PC_check.remove('Кулер')


def Cooler2_On():
    global similarity
    if Cooler2Make['bd'] == 0:
        PC_change_check('Кулер 2')
        if similarity == 1:
            Cooler2Make['bd'] = 2
            Cooler2Make['bg'] ='#00ff00'
    else:
        if 'Кулер 2' in PC:
            Cooler2Make['bd'] = 0
            Cooler2Make['bg'] = '#333333'
            PC.remove('Кулер 2')
            PC_check.remove('Кулер')


def RAM1_On():
    global similarity, efficiency
    if RAM1Make['bd'] == 0:
        if 'ОЗУ' not in PC_check:
            efficiency += 1
            PC_change_check('ОЗУ 1')
            if similarity == 1:
                RAM1Make['bd'] = 2
                RAM1Make['bg'] ='#00ff00'
            else:
                efficiency -= 1
        else:
            PC_change_check('ОЗУ 1')
    else:
        if 'ОЗУ 1' in PC:
            RAM1Make['bd'] = 0
            RAM1Make['bg'] = '#333333'
            PC.remove('ОЗУ 1')
            PC_check.remove('ОЗУ')
            efficiency -= 1


def RAM2_On():
    global similarity, efficiency
    if RAM2Make['bd'] == 0:
        if 'ОЗУ' not in PC_check:
            efficiency += 4
            PC_change_check('ОЗУ 2')
            if similarity == 1:
                RAM2Make['bd'] = 2
                RAM2Make['bg'] ='#00ff00'
            else:
                efficiency -= 4
        else:
            PC_change_check('ОЗУ 2')
    else:
        if 'ОЗУ 2' in PC:
            RAM2Make['bd'] = 0
            RAM2Make['bg'] = '#333333'
            PC.remove('ОЗУ 2')
            PC_check.remove('ОЗУ')
            efficiency -= 4


def RAM3_On():
    global similarity, efficiency
    if RAM3Make['bd'] == 0:
        if 'ОЗУ' not in PC_check:
            efficiency += 4
            PC_change_check('ОЗУ 3')
            if similarity == 1:
                RAM3Make['bd'] = 2
                RAM3Make['bg'] ='#00ff00'
            else:
                efficiency -= 4
        else:
            PC_change_check('ОЗУ 3')
    else:
        if 'ОЗУ 3' in PC:
            RAM3Make['bd'] = 0
            RAM3Make['bg'] = '#333333'
            PC.remove('ОЗУ 3')
            PC_check.remove('ОЗУ')
            efficiency -= 4


def inventory_make_pc(UP_or_Down):
    global items
    NumberOfElements = len(items)
    Number = len(items)
    items1 = items.copy()
    IndexItems = 0
    cordx = 0
    cordy = 0
    if UP_or_Down == 'UP':
        clear_make()
        if NumberOfElements <= 6:
            while NumberOfElements != 0:
                Name = items1.pop()
                IndexItems += 1
                if IndexItems == 1:
                    cordx = 1360
                    cordy = 160
                elif IndexItems%2 == 0:
                    cordx += 290
                    cordy = cordy
                elif (IndexItems%2) != 0 and (IndexItems <= 6):
                    cordx = 1360
                    cordy += 300
                inventory_sort_make_pc(cordx, cordy, Name)
                NumberOfElements -= 1
        else:
            while NumberOfElements != Number-6:
                Name = items1.pop()
                IndexItems += 1
                if IndexItems == 1:
                    cordx = 1360
                    cordy = 160
                elif IndexItems%2 == 0:
                    cordx += 290
                    cordy = cordy
                elif (IndexItems%2) != 0 and (IndexItems <= 6):
                    cordx = 1360
                    cordy += 300
                inventory_sort_make_pc(cordx, cordy, Name)
                NumberOfElements -= 1
    else:
        if NumberOfElements > 6:
            clear_make()
            for i in range(6):
                items1.pop()
            while NumberOfElements != 6:
                Name = items1.pop()
                IndexItems += 1
                if IndexItems == 1:
                    cordx = 1360
                    cordy = 160
                elif IndexItems%2 == 0:
                    cordx += 290
                    cordy = cordy
                elif (IndexItems%2) != 0 and (IndexItems <= 6):
                    cordx = 1360
                    cordy += 300
                inventory_sort_make_pc(cordx, cordy, Name)
                NumberOfElements -= 1


def inventory_sort_make_pc(cordx, cordy, Name):
        if Name == 'Видеокарта 1':
            VideoCard1Make.place(x=cordx, y=cordy)
        elif Name == 'Видеокарта 2':
            VideoCard2Make.place(x=cordx, y=cordy)
        elif Name == 'Видеокарта 3':
            VideoCard3Make.place(x=cordx, y=cordy)
        elif Name == 'Видеокарта 4':
            VideoCard4Make.place(x=cordx, y=cordy)
        elif Name == 'Видеокарта 5':
            VideoCard5Make.place(x=cordx, y=cordy)
        elif Name == 'Видеокарта 6':
            VideoCard6Make.place(x=cordx, y=cordy)
        elif Name == 'Видеокарта 7':
            VideoCard7Make.place(x=cordx, y=cordy)
        elif Name == 'Мат плата 1':
            MotherBoard1Make.place(x=cordx, y=cordy)
        elif Name == 'Мат плата 2':
            MotherBoard2Make.place(x=cordx, y=cordy)
        elif Name == 'Мат плата 3':
            MotherBoard3Make.place(x=cordx, y=cordy)
        elif Name == 'Мат плата 4':
            MotherBoard4Make.place(x=cordx, y=cordy)
        elif Name == 'Процессор 1':
            Processor1Make.place(x=cordx, y=cordy)
        elif Name == 'Процессор 2':
            Processor2Make.place(x=cordx, y=cordy)
        elif Name == 'Процессор 3':
            Processor3Make.place(x=cordx, y=cordy)
        elif Name == 'Процессор 4':
            Processor4Make.place(x=cordx, y=cordy)
        elif Name == 'БП 1':
            Power1Make.place(x=cordx, y=cordy)
        elif Name == 'БП 2':
            Power2Make.place(x=cordx, y=cordy)
        elif Name == 'Кулер 1':
            Cooler1Make.place(x=cordx, y=cordy)
        elif Name == 'Кулер 2':
            Cooler2Make.place(x=cordx, y=cordy)
        elif Name == 'ОЗУ 1':
            RAM1Make.place(x=cordx, y=cordy)
        elif Name == 'ОЗУ 2':
            RAM2Make.place(x=cordx, y=cordy)
        elif Name == 'ОЗУ 3':
            RAM3Make.place(x=cordx, y=cordy)
        elif Name == 'ХДД 1':
            HDD1Make.place(x=cordx, y=cordy)
        elif Name == 'ХДД 2':
            HDD2Make.place(x=cordx, y=cordy)


def clear_make():
    VideoCard1Make.place_forget()
    VideoCard2Make.place_forget()
    VideoCard3Make.place_forget()
    VideoCard4Make.place_forget()
    VideoCard5Make.place_forget()
    VideoCard6Make.place_forget()
    VideoCard7Make.place_forget()

    MotherBoard1Make.place_forget()
    MotherBoard2Make.place_forget()
    MotherBoard3Make.place_forget()
    MotherBoard4Make.place_forget()

    Processor1Make.place_forget()
    Processor2Make.place_forget()
    Processor3Make.place_forget()
    Processor4Make.place_forget()

    Power1Make.place_forget()
    Power2Make.place_forget()

    Cooler1Make.place_forget()
    Cooler2Make.place_forget()

    RAM1Make.place_forget()
    RAM2Make.place_forget()
    RAM3Make.place_forget()

    HDD1Make.place_forget()
    HDD2Make.place_forget()


def simi():
    Number = len(PC)
    for i in range(Number):
        if PC[i] == 'Видеокарта 1':
            VideoCard1Make['bd'] = 0
            VideoCard1Make['bg'] = '#333333'
        elif PC[i] == 'Видеокарта 2':
            VideoCard2Make['bd'] = 0
            VideoCard2Make['bg'] = '#333333'
        elif PC[i] == 'Видеокарта 3':
            VideoCard3Make['bd'] = 0
            VideoCard3Make['bg'] = '#333333'
        elif PC[i] == 'Видеокарта 4':
            VideoCard4Make['bd'] = 0
            VideoCard4Make['bg'] = '#333333'
        elif PC[i] == 'Видеокарта 5':
            VideoCard5Make['bd'] = 0
            VideoCard5Make['bg'] = '#333333'
        elif PC[i] == 'Видеокарта 6':
            VideoCard6Make['bd'] = 0
            VideoCard6Make['bg'] = '#333333'
        elif PC[i] == 'Видеокарта 7':
            VideoCard7Make['bd'] = 0
            VideoCard7Make['bg'] = '#333333'
        elif PC[i] == 'Мат плата 1':
            MotherBoard1Make['bd'] = 0
            MotherBoard1Make['bg'] = '#333333'
        elif PC[i] == 'Мат плата 2':
            MotherBoard2Make['bd'] = 0
            MotherBoard2Make['bg'] = '#333333'
        elif PC[i] == 'Мат плата 3':
            MotherBoard3Make['bd'] = 0
            MotherBoard3Make['bg'] = '#333333'
        elif PC[i] == 'Мат плата 4':
            MotherBoard4Make['bd'] = 0
            MotherBoard4Make['bg'] = '#333333'
        elif PC[i] == 'Процессор 1':
            Processor1Make['bd'] = 0
            Processor1Make['bg'] = '#333333'
        elif PC[i] == 'Процессор 2':
            Processor2Make['bd'] = 0
            Processor2Make['bg'] = '#333333'
        elif PC[i] == 'Процессор 3':
            Processor3Make['bd'] = 0
            Processor3Make['bg'] = '#333333'
        elif PC[i] == 'Процессор 4':
            Processor4Make['bd'] = 0
            Processor4Make['bg'] = '#333333'
        elif PC[i] == 'ХДД 1':
            HDD1Make['bd'] = 0
            HDD1Make['bg'] = '#333333'
        elif PC[i] == 'ХДД 2':
            HDD2Make['bd'] = 0
            HDD2Make['bg'] = '#333333'
        elif PC[i] == 'БП 1':
            Power1Make['bd'] = 0
            Power1Make['bg'] = '#333333'
        elif PC[i] == 'БП 2':
            Power2Make['bd'] = 0
            Power2Make['bg'] = '#333333'
        elif PC[i] == 'Кулер 1':
            Cooler1Make['bd'] = 0
            Cooler1Make['bg'] = '#333333'
        elif PC[i] == 'Кулер 2':
            Cooler2Make['bd'] = 0
            Cooler2Make['bg'] = '#333333'
        elif PC[i] == 'ОЗУ 1':
            RAM1Make['bd'] = 0
            RAM1Make['bg'] = '#333333'
        elif PC[i] == 'ОЗУ 2':
            RAM2Make['bd'] = 0
            RAM2Make['bg'] = '#333333'
        elif PC[i] == 'ОЗУ 3':
            RAM3Make['bd'] = 0
            RAM3Make['bg'] = '#333333'



def backpc():
    global efficiency, free_memory
    MakePcLabel.place_forget()
    BackPcButton.place_forget()

    MakeUpButton.place_forget()
    MakeDownButton.place_forget()

    if len(PC) < 7:
        simi()
        PC.clear()
        PC_check.clear()
        efficiency = 0
        free_memory = -1

    clear_make()

    comnata()


def Inventory_open():
    global items
    NumberOfElements = len(items)
    items1 = items.copy()
    close_comnata()
    InventoryLabel.place(x=0, y=0)
    BackButtonInventory.place(x=142, y=26)
    IndexItems = 0
    while NumberOfElements != 0:
        IndexItems += 1
        Name = items1.pop()
        if IndexItems == 1:
            cordx = 20
            cordy = 300
        elif IndexItems <= 6:
            cordx += 320
            cordy = 300
        elif (IndexItems > 6) and (IndexItems < 13):
            if IndexItems == 7:
                cordx = 20
                cordy = 650
            else:
                cordx += 320
                cordy = 650
        Inventory_sort(cordx, cordy, Name)
        NumberOfElements -= 1


def Inventory_sort(cordx, cordy, Name):
    if Name == 'Видеокарта 1':
        VideoCard1Label.place(x=cordx, y=cordy)
    elif Name == 'Видеокарта 2':
        VideoCard2Label.place(x=cordx, y=cordy)
    elif Name == 'Видеокарта 3':
        VideoCard3Label.place(x=cordx, y=cordy)
    elif Name == 'Видеокарта 4':
        VideoCard4Label.place(x=cordx, y=cordy)
    elif Name == 'Видеокарта 5':
        VideoCard5Label.place(x=cordx, y=cordy)
    elif Name == 'Видеокарта 6':
        VideoCard6Label.place(x=cordx, y=cordy)
    elif Name == 'Видеокарта 7':
        VideoCard7Label.place(x=cordx, y=cordy)
    elif Name == 'Мат плата 1':
        MotherBoard1Label.place(x=cordx, y=cordy)
    elif Name == 'Мат плата 2':
        MotherBoard2Label.place(x=cordx, y=cordy)
    elif Name == 'Мат плата 3':
        MotherBoard3Label.place(x=cordx, y=cordy)
    elif Name == 'Мат плата 4':
        MotherBoard4Label.place(x=cordx, y=cordy)
    elif Name == 'Процессор 1':
        Processor1Label.place(x=cordx, y=cordy)
    elif Name == 'Процессор 2':
        Processor2Label.place(x=cordx, y=cordy)
    elif Name == 'Процессор 3':
        Processor3Label.place(x=cordx, y=cordy)
    elif Name == 'Процессор 4':
        Processor4Label.place(x=cordx, y=cordy)
    elif Name == 'БП 1':
        Power1Label.place(x=cordx, y=cordy)
    elif Name == 'БП 2':
        Power2Label.place(x=cordx, y=cordy)
    elif Name == 'Кулер 1':
        Cooler1Label.place(x=cordx, y=cordy)
    elif Name == 'Кулер 2':
        Cooler2Label.place(x=cordx, y=cordy)
    elif Name == 'ОЗУ 1':
        RAM1Label.place(x=cordx, y=cordy)
    elif Name == 'ОЗУ 2':
        RAM2Label.place(x=cordx, y=cordy)
    elif Name == 'ОЗУ 3':
        RAM3Label.place(x=cordx, y=cordy)
    elif Name == 'ХДД 1':
        HDD1Label.place(x=cordx, y=cordy)
    elif Name == 'ХДД 2':
        HDD2Label.place(x=cordx, y=cordy)


def back_Inventory():
    BackButtonInventory.place_forget()
    InventoryLabel.place_forget()

    VideoCard1Label.place_forget()
    VideoCard2Label.place_forget()
    VideoCard3Label.place_forget()
    VideoCard4Label.place_forget()
    VideoCard5Label.place_forget()
    VideoCard6Label.place_forget()
    VideoCard7Label.place_forget()

    MotherBoard1Label.place_forget()
    MotherBoard2Label.place_forget()
    MotherBoard3Label.place_forget()
    MotherBoard4Label.place_forget()

    Processor1Label.place_forget()
    Processor2Label.place_forget()
    Processor3Label.place_forget()
    Processor4Label.place_forget()

    Power1Label.place_forget()
    Power2Label.place_forget()

    Cooler1Label.place_forget()
    Cooler2Label.place_forget()

    RAM1Label.place_forget()
    RAM2Label.place_forget()
    RAM3Label.place_forget()

    HDD1Label.place_forget()
    HDD2Label.place_forget()

    comnata()


def Market_open():
    close_comnata()
    moneyLabel.place(x=10, y=80)
    MarketPhotoLabel.place(x=0, y=0)
    MarketButton.place_forget()

    ProcessorButton.place(x=20, y=400)
    VideoCardButton.place(x=20, y=200)
    HDDButton.place(x=400, y=400)
    CoolerButton.place(x=780, y=400)
    RAMButton.place(x=400, y=150)
    PowerButton.place(x=780, y=150)
    SoftButton.place(x=1160, y=180)
    MotherBoardButton.place(x=1160, y=400)

    BackButtonMarket.place(x=142, y=26)


def SkillFox_check():
    if 'Python' in skills:
        SkillFoxPythonDeveloperPhoto['file'] = r'Image\BoughtPythonDeveloper.png'
    if 'Unity' in skills:
        SkillFoxUnityDeveloperPhoto['file'] = r'Image\BoughtUnityDeveloper.png'
    if 'Apps' in skills:
        SkillFoxAppsDeveloperPhoto['file'] = r'Image\BoughtAppsDeveloper.png'
    if 'Web' in skills:
        SkillFoxWebDeveloperPhoto['file'] = r'Image\BoughtWebDeveloper.png'


def SkillFox_open():
    close_comnata()
    SkillFoxLabel.place(x=0, y=0)
    MarketButton.place_forget()

    SkillFoxProgButton.place(x=64, y=160)
    SkillFoxDesignButton.place(x=427, y=160)
    SkillFoxMarketingButton.place(x=790, y=160)
    SkillFoxManagmentButton.place(x=1155, y=160)
    SkillFoxGamesButton.place(x=1520, y=160)

    SkillFoxPythonDeveloperButton.place(x=708, y=433)

    BackButtonSkillFox.place(x=142, y=26)



def SkillFoxProgOpen():
    back_SkillFox()
    close_comnata()

    SkillFoxProgBackButton.place(x=142, y=26)

    SkillFoxProgLabel.place(x=0, y=0)

    SkillFoxPythonDeveloperButton.place(x=50, y=193)
    SkillFoxUnityDeveloperButton.place(x=728, y=193)
    SkillFoxAppsDeveloperButton.place(x=1390, y=193)
    SkillFoxWebDeveloperButton.place(x=50, y=490)




def SkillFoxProg_back():
    SkillFoxProgBackButton.place_forget()

    SkillFoxProgLabel.place_forget()

    SkillFoxPythonDeveloperButton.place_forget()
    SkillFoxUnityDeveloperButton.place_forget()
    SkillFoxAppsDeveloperButton.place_forget()
    SkillFoxWebDeveloperButton.place_forget()

    SkillFox_open()


def SkillFoxPythonDeveloper():
    global money, skills
    if money >= 250:
        if 'Python' not in skills:
            money -= 250
            skills.append('Python')
            money_sort()
            buy['text'] = 'Поздравляем! Вы освоили профессию "Python-разработчик".'
            SkillFoxPythonDeveloperPhoto['file'] = r'Image\BoughtPythonDeveloper.png'
            buy.place(x=500, y=450)
            root.after(2000, buy.place_forget)
            root.update()
    else:
        close.place(x=700, y=400)
        root.after(2000, close.place_forget)
        root.update()


def SkillFoxUnityDeveloper():
    global money, skills
    if money >= 3000:
        if 'Unity' not in skills:
            money -= 3000
            skills.append('Unity')
            money_sort()
            buy['text'] = 'Поздравляем! Вы прошли курс "Разработка игр на Unity".'
            SkillFoxUnityDeveloperPhoto['file'] = r'Image\BoughtUnityDeveloper.png'
            buy.place(x=500, y=450)
            root.after(2000, buy.place_forget)
            root.update()
    else:
        close.place(x=700, y=400)
        root.after(2000, close.place_forget)
        root.update()


def SkillFoxAppsDeveloper():
    global money, skills
    if money >= 5000:
        if 'Apps' not in skills:
            money -= 5000
            skills.append('Apps')
            money_sort()
            buy['text'] = 'Поздравляем! Вы прошли курс "Разработка мобильных приложений".'
            SkillFoxAppsDeveloperPhoto['file'] = r'Image\BoughtAppsDeveloper.png'
            buy.place(x=500, y=450)
            root.after(2000, buy.place_forget)
            root.update()
    else:
        close.place(x=700, y=400)
        root.after(2000, close.place_forget)
        root.update()


def SkillFoxWebDeveloper():
    global money, skills
    if money >= 18000:
        if 'Web' not in skills:
            money -= 18000
            skills.append('Web')
            money_sort()
            buy['text'] = 'Поздравляем! Вы освоили профессию "Веб-разработчик".'
            SkillFoxWebDeveloperPhoto['file'] = r'Image\BoughtWebDeveloper.png'
            buy.place(x=500, y=450)
            root.after(2000, buy.place_forget)
            root.update()
    else:
        close.place(x=700, y=400)
        root.after(2000, close.place_forget)
        root.update()


def back_SkillFox():
    SkillFoxLabel.place_forget()
    BackButtonSkillFox.place_forget()
    comnata()

    SkillFoxProgButton.place_forget()
    SkillFoxDesignButton.place_forget()
    SkillFoxMarketingButton.place_forget()
    SkillFoxManagmentButton.place_forget()
    SkillFoxGamesButton.place_forget()

    SkillFoxPythonDeveloperButton.place_forget()


def click_balance():
    global money, mfc, efficiency
    global level, level_ex
    if mfc != 0 and efficiency > 0:
        money += mfc
        level_ex += 1
        ProgressBarLevel['value'] = level_ex
        get_cash.place(x=100, y=50)
        root.after(1000, get_cash.place_forget)
        root.update()
        money_sort()
        if level_ex == 1000:
            level += 1
            level_ex = 0
            levelLabel['text'] = str(level)
            ProgressBarLevel['value'] = level_ex
    elif efficiency == 0:
        no = Label(root, text='Ваш компьютер разобран')
        no.place(x=450, y=450)
        root.after(1000, no.place_forget)
        root.update()


def close_comnata():
    moneyLabel['bg'] = '#333333'
    moneyLabel['fg'] = '#FFFFFF'
    moneyLabel.place_forget()
    ProgressBarLevel.place_forget()
    click.place_forget()
    SkillFox.place_forget()
    MarketButton.place_forget()
    InventoryButton.place_forget()
    levelLabel.place_forget()
    Information_Label.place_forget()
    options.place_forget()
    ClockLabel.place_forget()
    ComputerButton.place_forget()
    LevelPlaceLabel.place_forget()
    levelLabel.place_forget()
    exitbutton.place_forget()


def comnata():
    moneyLabel['bg'] = '#FFFFFF'
    moneyLabel['fg'] = '#000000'
    click.place(x=0, y=0)
    SkillFox.place(x=1720, y=0)
    MarketButton.place(x=1720, y=50)
    InventoryButton.place(x=1720, y=100)

    ClockLabel.place(x=25, y=90)
    ComputerButton.place(x=1215, y=846)
    LevelPlaceLabel.place(x=40, y=40)
    levelLabel.place(x=70, y=72)
    ProgressBarLevel.place(x=140, y=78)
    ProgressBarLevel['value'] = level_ex

    Information_Label.place(x=2, y=2)
    options.place(x=25, y=18)
    exitbutton.place(x=280, y=18)
    moneyLabel.place(x=105, y=27)


one_monitor = PhotoImage(file=r'Image\Room_one.png')
click = Button(root, image=one_monitor, command=click_balance, bg='#333333', fg='black', height=1080, width=1920, bd=0,
               relief='sunken', activebackground='#333333')


check_mark_True = PhotoImage(file=r'Image\Check_mark_1.png')
check_mark_False = PhotoImage(file=r'Image\Check_mark_0.png')
options_photo = PhotoImage(file=r'Image\Options_photo.png')
option_photo = PhotoImage(file=r'Image\Optons.png')

clockPhoto = PhotoImage(file='Часы\Часы0.png')

WarningExitPhoto = PhotoImage(file=r'Image\WarningExit.png')
WarningYesPhoto = PhotoImage(file=r'Image\YesExit.png')
WarningNoPhoto = PhotoImage(file=r'Image\NoExit.png')

ComputerPhoto = PhotoImage(file=r'Image\Компьютер кнопка.png')

MakePcPhoto = PhotoImage(file=r'Image\Сборка ПК.png')
BackMakePcPhoto = PhotoImage(file=r'Image\back make pc.png')

LevelPlacePhoto = PhotoImage(file=r'Image\level place.png')
information_of_player = PhotoImage(file=r'Image\Information of player.png')
KillBoxButton = PhotoImage(file=r'Image\KillBoxButton.png')
MarketButtonDark = PhotoImage(file=r'Image\MarketNutton_dark_theme.png')
StorageButtonDark = PhotoImage(file=r'Image\Storage_dark_theme.png')
marketPhoto = PhotoImage(file=r'Image\Brauzer_market.png')
nomoneyPhoto = PhotoImage(file=r'Image\Нет денег.png')
InventoryPhoto = PhotoImage(file=r'Image\Инвентарь.png')
KillBoxProgPhoto = PhotoImage(file=r'Image\KillBoxProg.png')

SkillFoxPhoto = PhotoImage(file=r'Image\SkillFox_main.png')
SkillFoxProgrammingPhoto = PhotoImage(file=r'Image\SkillFox_Programming.png')

SkillFoxProgButtonPhoto = PhotoImage(file=r'Image\ProgrammingButton.png')
SkillFoxPythonDeveloperPhoto = PhotoImage(file=r'Image\PythonDeveloper.png')
SkillFoxUnityDeveloperPhoto = PhotoImage(file=r'Image\UnityDeveloper.png')
SkillFoxAppsDeveloperPhoto = PhotoImage(file=r'Image\AppsDeveloper.png')
SkillFoxWebDeveloperPhoto = PhotoImage(file=r'Image\WebDeveloper.png')

SkillFoxDesignButtonPhoto = PhotoImage(file=r'Image\DesignButton.png')
SkillFoxMarketingButtonPhoto = PhotoImage(file=r'Image\MarketingButton.png')
SkillFoxManagmentButtonPhoto = PhotoImage(file=r'Image\ManagmentButton.png')
SkillFoxGamesButtonPhoto = PhotoImage(file=r'Image\GamesButton.png')

MakeUpPhoto = PhotoImage(file=r'Image\Up make.png')
MakeDownPhoto = PhotoImage(file=r'Image\Down make.png')

VideoCardPhoto = PhotoImage(file=r'Image\Видеокарта.png')
VideoCardMarketPhoto = PhotoImage(file=r'Image\Видеокарты.png')
VideoCard1Photo = PhotoImage(file=r'Image\Видеокарта 1.png')
VideoCard2Photo = PhotoImage(file=r'Image\Видеокарта 2.png')
VideoCard3Photo = PhotoImage(file=r'Image\Видеокарта 3.png')
VideoCard4Photo = PhotoImage(file=r'Image\Видеокарта 4.png')
VideoCard5Photo = PhotoImage(file=r'Image\Видеокарта 5.png')
VideoCard6Photo = PhotoImage(file=r'Image\Видеокарта 6.png')
VideoCard7Photo = PhotoImage(file=r'Image\Видеокарта 7.png')

MotherBoardPhoto = PhotoImage(file=r'Image\МатПлата.png')
MotherBoardMarketPhoto = PhotoImage(file=r'Image\Материнские платы.png')
MotherBoard1Photo = PhotoImage(file=r'Image\Мат плата 1.png')
MotherBoard2Photo = PhotoImage(file=r'Image\Мат плата 2.png')
MotherBoard3Photo = PhotoImage(file=r'Image\Мат плата 3.png')
MotherBoard4Photo = PhotoImage(file=r'Image\Мат плата 4.png')

ProcessorPhoto = PhotoImage(file=r'Image\Процессор.png')
ProcessorMarketPhoto = PhotoImage(file=r'Image\Процессоры.png')
Processor1Photo = PhotoImage(file=r'Image\Процессор 1.png')
Processor2Photo = PhotoImage(file=r'Image\Процессор 2.png')
Processor3Photo = PhotoImage(file=r'Image\Процессор 3.png')
Processor4Photo = PhotoImage(file=r'Image\Процессор 4.png')

PowerPhoto = PhotoImage(file=r'Image\БлокПитания.png')
PowerMarketPhoto = PhotoImage(file=r'Image\Блоки питания.png')
Power1Photo = PhotoImage(file=r'Image\БП 1.png')
Power2Photo = PhotoImage(file=r'Image\БП 2.png')

CoolerPhoto = PhotoImage(file=r'Image\Кулер.png')
CoolerMarketPhoto = PhotoImage(file=r'Image\Кулеры маркет.png')
Cooler1Photo = PhotoImage(file=r'Image\Кулер 1.png')
Cooler2Photo = PhotoImage(file=r'Image\Кулер 2.png')

RAMPhoto = PhotoImage(file=r'Image\ОЗУ.png')
RAMBrauzerPhoto = PhotoImage(file=r'Image\Озу браузер.png')
RAM1Photo = PhotoImage(file=r'Image\Оперативка 1.png')
RAM2Photo = PhotoImage(file=r'Image\Оперативка 2.png')
RAM3Photo = PhotoImage(file=r'Image\ОЗУ 3.png')

HDDPhoto = PhotoImage(file=r'Image\HDD.png')
HDDMarketPhoto = PhotoImage(file=r'Image\HDD&SSD MArket.png')
HDD1Photo = PhotoImage(file=r'Image\HDD 1.png')
HDD2Photo = PhotoImage(file=r'Image\HDD 2.png')

SoftPhoto = PhotoImage(file=r'Image\Soft.png')
SoftMarketPhoto = PhotoImage(file=r'Image\SoftMarket.png')
SoftPythonPhoto = PhotoImage(file=r'Image\Python soft.png')
SoftUnityPhoto = PhotoImage(file=r'Image\UnitySoft.png')
CPlusPlusPhoto = PhotoImage(file=r'Image\C++Soft.png')
JavaScriptPhoto = PhotoImage(file=r'Image\JavaScriptSoft.png')

back = PhotoImage(file=r'Image\back.png')

ExitPhoto = PhotoImage(file=r'Image\Exit.png')

get_cash = Label(root, text='+1', font=('Helvetica, 24'), bg='#c1bb76', fg='white')

MarketPhotoLabel = Label(root, image=marketPhoto, height=1080, width=1920, borderwidth=0)

#SKILLFOX
SkillFoxLabel = Label(root, image=SkillFoxPhoto, bd=0)
SkillFoxProgLabel = Label(root, image=SkillFoxProgrammingPhoto, bd=0)
BackButtonSkillFox = Button(root, image=back, command=back_SkillFox, relief='flat', bd=0, bg='#e6e1e5',
                            activebackground='#e6e1e5')

SkillFoxProgButton = SKFButton(root, image=SkillFoxProgButtonPhoto, bd=0, bg='#333333', relief='sunken',
                               command=SkillFoxProgOpen, activebackground='#333333')

SkillFoxPythonDeveloperButton = SFProg(root, image=SkillFoxPythonDeveloperPhoto, bd=0, bg='#333333', relief='sunken',
                                       activebackground='#333333', command=SkillFoxPythonDeveloper)
SkillFoxUnityDeveloperButton = SFProg(root, image=SkillFoxUnityDeveloperPhoto, bd=0, bg='#333333', relief='sunken',
                                      activebackground='#333333', command=SkillFoxUnityDeveloper)
SkillFoxAppsDeveloperButton = SFProg(root, image=SkillFoxAppsDeveloperPhoto,  bd=0, bg='#333333', relief='sunken',
                                     activebackground='#333333', command=SkillFoxAppsDeveloper)
SkillFoxWebDeveloperButton = SFProg(root, image=SkillFoxWebDeveloperPhoto, bd=0, bg='#333333', relief='sunken',
                                    activebackground='#333333', command=SkillFoxWebDeveloper)

SkillFoxProgBackButton = Button(root, image=back, command=SkillFoxProg_back, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')

SkillFoxDesignButton = SKFButton(root, image=SkillFoxDesignButtonPhoto, bd=0, bg='#333333', relief='sunken',
                                 activebackground='#333333')
SkillFoxMarketingButton = SKFButton(root, image=SkillFoxMarketingButtonPhoto, bd=0, bg='#333333', relief='sunken',
                                    activebackground='#333333')
SkillFoxManagmentButton = SKFButton(root, image=SkillFoxManagmentButtonPhoto, bd=0, bg='#333333', relief='sunken',
                                    activebackground='#333333')
SkillFoxGamesButton = SKFButton(root, image=SkillFoxGamesButtonPhoto, bd=0, bg='#333333', relief='sunken',
                                activebackground='#333333')

InventoryLabel = Label(root, image=InventoryPhoto, height=1080, width=1920, borderwidth=0)

KillBoxProgLabel = Label(root, image=KillBoxProgPhoto, height=1080, width=1920, borderwidth=0)

MotherBoardLabel = Label(root, image=MotherBoardMarketPhoto, height=1080, width=1920, borderwidth=0)

OptionsPhotoLabel = Label(root, image=options_photo, bd=0)

MakePcLabel = Label(root, image=MakePcPhoto, bd=0)

BackPcButton = Button(root, image=BackMakePcPhoto, bd=0, bg='#333333', activebackground='#333333', command=backpc)

MakeUpButton = Button(root, image=MakeUpPhoto, bd=0, bg='#333333', activebackground='#333333', relief='sunken',
                      command=Up_make)
MakeDownButton = Button(root, image=MakeDownPhoto, bd=0, bg='#333333', activebackground='#333333', relief='sunken',
                        command=Down_make)

marketLabel = Label(root, text='Маркет', font=('Helvetica, 24'), justify='center')

MarketingButton = Button(root, text='Маркетинг', font=('Minion Pro', '16'), bg='#333333', borderwidth=0,
                         fg='white', activebackground='#333333', activeforeground='white')

ManagmentButton = Button(root, text='Управление', font=('Minion Pro', '16'), bg='#333333', borderwidth=0,
                         fg='white', activebackground='#333333', activeforeground='white')

GamesButton = Button(root, text='Игры', font=('Minion Pro', '16'), bg='#333333', borderwidth=0,
                     fg='white', activebackground='#333333', activeforeground='white')

#Видеокарты
VideoCardPhotoLabel = Label(root, image=VideoCardMarketPhoto, height=1080, width=1920, borderwidth=0)
VideoCardButton = Button(root, image=VideoCardPhoto, bg='#333333', borderwidth=0, command=VideoCardOpen,
                         activebackground='#333333')

VideoCard1Button = Button(root, image=VideoCard1Photo, bg='#333333', borderwidth=0, command=VideoCard1_buy,
                          activebackground='#333333')
VideoCard1Make = Button(root, image=VideoCard1Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=VideoCard1_On, relief='sunken')
VideoCard1Label = Label(root, image=VideoCard1Photo, borderwidth=0)


VideoCard2Button = Button(root, image=VideoCard2Photo, bg='#333333', borderwidth=0, command=VideoCard2_buy,
                          activebackground='#333333')
VideoCard2Make = Button(root, image=VideoCard2Photo, bg='#333333', bd=0, activebackground='#333333',
                        command=VideoCard2_On, relief='sunken')
VideoCard2Label = Label(root, image=VideoCard2Photo, bg='#333333', borderwidth=0)


VideoCard3Button = Button(root, image=VideoCard3Photo, bg='#333333', borderwidth=0, command=VideoCard3_buy,
                          activebackground='#333333')
VideoCard3Make = Button(root, image=VideoCard3Photo, bg='#333333', bd=0, activebackground='#333333',
                        command=VideoCard3_On, relief='sunken')
VideoCard3Label = Label(root, image=VideoCard3Photo, bg='#333333', borderwidth=0)


VideoCard4Button = Button(root, image=VideoCard4Photo, bg='#333333', borderwidth=0, command=VideoCard4_buy,
                         activebackground='#333333')
VideoCard4Make = Button(root, image=VideoCard4Photo, bg='#333333', bd=0, activebackground='#333333',
                        command=VideoCard4_On, relief='sunken')
VideoCard4Label = Label(root, image=VideoCard4Photo, bg='#333333', borderwidth=0)


VideoCard5Button = Button(root, image=VideoCard5Photo, bg='#333333', borderwidth=0, command=VideoCard5_buy,
                       activebackground='#333333')
VideoCard5Make = Button(root, image=VideoCard5Photo, bg='#333333', bd=0, activebackground='#333333',
                        command=VideoCard5_On, relief='sunken')
VideoCard5Label = Label(root, image=VideoCard5Photo, bg='#333333', borderwidth=0)


VideoCard6Button = Button(root, image=VideoCard6Photo, bg='#333333', borderwidth=0, command=VideoCard6_buy,
                          activebackground='#333333')
VideoCard6Make = Button(root, image=VideoCard6Photo, bg='#333333', bd=0, activebackground='#333333',
                        command=VideoCard6_On, relief='sunken')
VideoCard6Label = Label(root, image=VideoCard6Photo, bg='#333333', borderwidth=0)


VideoCard7Button = Button(root, image=VideoCard7Photo, bg='#333333', borderwidth=0, command=VideoCard7_buy,
                          activebackground='#333333')
VideoCard7Make = Button(root, image=VideoCard7Photo, bg='#333333', bd=0, activebackground='#333333',
                        command=VideoCard7_On, relief='sunken')
VideoCard7Label = Label(root, image=VideoCard7Photo, bg='#333333', borderwidth=0)

#Софт
SoftButton = Button(root, image=SoftPhoto, bg='#333333', bd=0, command=SoftOpen, activebackground='#333333')

SoftLabel = Label(root, image=SoftMarketPhoto, bd=0)

SoftPythonButton = Button(root, image=SoftPythonPhoto, bg='#333333', bd=0, command=SoftPython_buy,
                          activebackground='#333333')

SoftCSharpButton = Button(root, image=SoftUnityPhoto, bg='#333333', bd=0, command=SoftCSharrp_buy,
                          activebackground='#333333')

SoftCPlusPlusButton = Button(root, image=CPlusPlusPhoto, bg='#333333', bd=0, command=SoftCPlusPlus_buy,
                          activebackground='#333333')

SoftJavaScriptButton = Button(root, image=JavaScriptPhoto, bg='#333333', bd=0, command=SoftJavaScript_buy,
                          activebackground='#333333')

#Мат платы
MotherBoardButton = Button(root, image=MotherBoardPhoto, bg='#333333', bd=0, command=MotherBoardOpen,
                           activebackground='#333333')


MotherBoard1Button = Button(root, image=MotherBoard1Photo, bg='#333333', bd=0, command=MotherBoard1_buy,
                            activebackground='#333333')
MotherBoard1Make = Button(root, image=MotherBoard1Photo, bg='#333333', bd=0, activebackground='#333333',
                          command=MotherBoard1_On, relief='sunken')
MotherBoard1Label = Label(root, image=MotherBoard1Photo, bg='#333333', bd=0)


MotherBoard2Button = Button(root, image=MotherBoard2Photo, bg='#333333', bd=0, command=MotherBoard2_buy,
                            activebackground='#333333')
MotherBoard2Make = Button(root, image=MotherBoard2Photo, bg='#333333', bd=0, activebackground='#333333',
                          command=MotherBoard2_On, relief='sunken')
MotherBoard2Label = Label(root, image=MotherBoard2Photo, bg='#333333', bd=0)


MotherBoard3Button = Button(root, image=MotherBoard3Photo, bg='#333333', bd=0, command=MotherBoard3_buy,
                            activebackground='#333333')
MotherBoard3Make = Button(root, image=MotherBoard3Photo, bg='#333333', bd=0, activebackground='#333333',
                          command=MotherBoard3_On, relief='sunken')
MotherBoard3Label = Label(root, image=MotherBoard3Photo, bg='#333333', bd=0)


MotherBoard4Button = Button(root, image=MotherBoard4Photo, bg='#333333', bd=0, command=MotherBoard4_buy,
                            activebackground='#333333')
MotherBoard4Make = Button(root, image=MotherBoard4Photo, bg='#333333', bd=0, activebackground='#333333',
                          command=MotherBoard4_On, relief='sunken')
MotherBoard4Label = Label(root, image=MotherBoard4Photo, bg='#333333', bd=0)


#Проыессоры
ProcessorButton = Button(root, image=ProcessorPhoto, bg='#333333', borderwidth=0, command=ProcessorOpen,
                         activebackground='#333333')

ProcessorMarket = Label(root, image=ProcessorMarketPhoto, bd=0)


Processor1Button = Button(root, image=Processor1Photo, bg='#333333', borderwidth=0, command=Processor1_buy,
                          activebackground='#333333')
Processor1Make = Button(root, image=Processor1Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=Processor1_On, relief='sunken')
Processor1Label = Label(root, image=Processor1Photo, bd=0)


Processor2Button = Button(root, image=Processor2Photo,  bg='#333333', bd=0, command=Processor2_buy,
                          activebackground='#333333')
Processor2Make = Button(root, image=Processor2Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=Processor2_On, relief='sunken')
Processor2Label = Label(root, image=Processor2Photo, bd=0)


Processor3Button = Button(root, image=Processor3Photo,  bg='#333333', bd=0, command=Processor3_buy,
                          activebackground='#333333')
Processor3Make = Button(root, image=Processor3Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=Processor3_On, relief='sunken')
Processor3Label = Label(root, image=Processor3Photo, bd=0)


Processor4Button = Button(root, image=Processor4Photo,  bg='#333333', bd=0, command=Processor4_buy,
                          activebackground='#333333')
Processor4Make = Button(root, image=Processor4Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=Processor4_On, relief='sunken')
Processor4Label = Label(root, image=Processor4Photo, bd=0)

#HDD
HDDButton = Button(root, image=HDDPhoto, bg='#333333', borderwidth=0, command=HDDOpen, activebackground='#333333')

HDDMarket = Label(root, image=HDDMarketPhoto, bd=0)

HDD1Button = Button(root, image=HDD1Photo, bg='#333333', bd=0, command=HDD1_buy, activebackground='#333333')
HDD1Make = Button(root, image=HDD1Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=HDD1_On, relief='sunken')
HDD1Label = Label(root, image=HDD1Photo, bd=0)

HDD2Button = Button(root, image=HDD2Photo, bg='#333333', bd=0, command=HDD2_buy, activebackground='#333333')
HDD2Make = Button(root, image=HDD2Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=HDD2_On, relief='sunken')
HDD2Label = Label(root, image=HDD2Photo, bd=0)

#БП
PowerButton = Button(root, image=PowerPhoto, bg='#333333', borderwidth=0, command=PowerOpen, activebackground='#333333')

PowerMarket = Label(root, image=PowerMarketPhoto, bd=0)

Power1Button = Button(root, image=Power1Photo, bg='#333333', bd=0, command=Power1_buy, activebackground='#333333')
Power1Make = Button(root, image=Power1Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=Power1_On, relief='sunken')
Power1Label = Label(root, image=Power1Photo, bd=0)

Power2Button = Button(root, image=Power2Photo, bg='#333333', bd=0, command=Power2_buy, activebackground='#333333')
Power2Make = Button(root, image=Power2Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=Power2_On, relief='sunken')
Power2Label = Label(root, image=Power2Photo, bd=0)

#Кулер
CoolerMarket = Label(root, image=CoolerMarketPhoto, bd=0)

CoolerButton = Button(root, image=CoolerPhoto, bg='#333333', bd=0, command=CoolerOpen, activebackground='#333333')

Cooler1Button = Button(root, image=Cooler1Photo, bg='#333333', bd=0, command=Cooler1_buy, activebackground='#333333')
Cooler1Make = Button(root, image=Cooler1Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=Cooler1_On, relief='sunken')
Cooler1Label = Label(root, image=Cooler1Photo, bd=0)

Cooler2Button = Button(root, image=Cooler2Photo, bg='#333333', bd=0, command=Cooler2_buy, activebackground='#333333')
Cooler2Make = Button(root, image=Cooler2Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=Cooler2_On, relief='sunken')
Cooler2Label = Label(root, image=Cooler2Photo, bd=0)

#ОЗУ
RAMButton = Button(root, image=RAMPhoto, bg='#333333', borderwidth=0, command=RamOpen, activebackground='#333333')

RAMMarket = Label(root, image=RAMBrauzerPhoto, bd=0)

RAM1Button = Button(root, image=RAM1Photo, bg='#333333', bd=0, command=RAM1_buy, activebackground='#333333')
RAM1Make = Button(root, image=RAM1Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=RAM1_On, relief='sunken')
RAM1Label = Label(root, image=RAM1Photo, bd=0)

RAM2Button = Button(root, image=RAM2Photo, bg='#333333', bd=0, command=RAM2_buy, activebackground='#333333')
RAM2Make = Button(root, image=RAM2Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=RAM2_On, relief='sunken')
RAM2Label = Label(root, image=RAM2Photo, bd=0)

RAM3Button = Button(root, image=RAM3Photo, bg='#333333', bd=0, command=RAM3_buy, activebackground='#333333')
RAM3Make = Button(root, image=RAM3Photo, bg='#333333', borderwidth=0, activebackground='#333333',
                        command=RAM3_On, relief='sunken')
RAM3Label = Label(root, image=RAM3Photo, bd=0)



SkillFox = Button(root, image=KillBoxButton, command=SkillFox_open, relief='solid', bd=0, bg='#6a6a6a',
                 activebackground='#6a6a6a')
MarketButton = Button(root, image=MarketButtonDark, command=Market_open, relief='solid', bd=0, bg='#6a6a6a',
                      activebackground='#6a6a6a')
InventoryButton = Button(root, image=StorageButtonDark, command=Inventory_open, relief='solid', bd=0, bg='#6a6a6a',
                         activebackground='#6a6a6a')

check_mark_music_True = Button(root, image=check_mark_True, relief='sunken', bd=0, command=music_option, bg='#333333',
                               fg='#333333', activebackground='#333333')
check_mark_music_False = Button(root, image=check_mark_False, relief='sunken', bd=0, command=music_option, bg='#333333',
                                fg='#333333', activebackground='#333333')

check_mark_theme_True = Button(root, image=check_mark_True, relief='sunken', bd=0, command=theme, bg='#333333',
                               fg='#333333', activebackground='#333333')
check_mark_theme_False = Button(root, image=check_mark_False, relief='sunken', bd=0, command=theme, bg='#333333',
                                fg='#333333', activebackground='#333333')

BackButtonMarket = Button(root, image=back, command=back_Market, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')
BackButtonVideoCard = Button(root, image=back, command=back_VideoCard, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')
BackButtonInventory = Button(root, image=back, command=back_Inventory, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')
BackButtonMotherBoard = Button(root, image=back, command=back_MotherBoard, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')
BackButtonProcessor = Button(root, image=back, command=back_Processor, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')
BackButtonOptions = Button(root, image=back, command=back_options, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')
BackButtonPower = Button(root, image=back, command=back_power, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')
BackButtonCooler = Button(root, image=back, command=back_cooler, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')
BackButtonRAM = Button(root, image=back, command=back_RAM, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')
BackButtonHDD = Button(root, image=back, command=back_HDD, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')
BackButtonSoft = Button(root, image=back, command=back_soft, relief='flat', bd=0, bg='#e6e1e5',
                                activebackground='#e6e1e5')

ClockLabel = Label(image=clockPhoto, bd=0)

ComputerButton = Button(image=ComputerPhoto, bd=0, relief='solid', command=make_computer)

LevelPlaceLabel = Label(image=LevelPlacePhoto, bd=0)

levelLabel = Label(root, text=str(level), font=('Borsok, 18'), fg='white', bg='#636363', justify='center',
                   width=5)

StyleLevelBar = ttk.Style()
StyleLevelBar.theme_use('default')
StyleLevelBar.configure("blue.Horizontal.TProgressbar", background='black')

ProgressBarLevel = Progressbar(root, orient="horizontal", mode="determinate", style='black.Horizontal.TProgressbar',
                               maximum=1000, value=0, length=100)

Information_Label = Label(image=information_of_player, bd=0)

close = Label(root, image=nomoneyPhoto, borderwidth=0)

bought = Label(root, text='Это улучшение уже куплено', font=('Helvetica, 24'), bg='white', width=25)

buy = Label(root, text='', font=('Helvetica, 24'), bg='white')

options = Button(root, image=option_photo, bd=0, relief='solid', bg='white', command=options_open)
exitbutton = Button(root, image=ExitPhoto, bd=0, relief='solid', bg='white', command=warning_exit)

moneyLabel = Label(root, text='$' + str(money) + 'K', font=('Borsok, 18'), bg='white', fg='black', justify='center',
                   width=10)

WarningExitLabel = Label(root, image=WarningExitPhoto, bd=0, width=1920, height=1080)
YesExitButton = Button(root, image=WarningYesPhoto, command=save, bd=0, relief='sunken', bg='black',
                       activebackground='black')
NoExitButton = Button(root, image=WarningNoPhoto, command=no_exit, bd=0, relief='sunken', bg='black',
                      activebackground='black')

money_sort()

comnata()

timer_JKH()

PC_change()


def start_music():
    if Music == 1:
        play()
    else:
        pass


start_music()

auto_save_timer()

SkillFox_check()

root.protocol("WM_DELETE_WINDOW", save)


root.mainloop()