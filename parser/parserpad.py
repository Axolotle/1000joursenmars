from datetime import date, timedelta
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')



def isLineInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def marsToDate(d):
    daysToAdd = eval(day) - 31
    newDate = date(2016, 3, 31) + timedelta(days=daysToAdd)
    dateToPrint = newDate.strftime("%d %B %Y")
    return dateToPrint



with open('main.html', 'r') as main:
    for line in main:
        print(line.strip('\n'))


print('\n<div id="main" class="cols">')

with open('padimport.txt', 'r') as pad1000:
    for line in pad1000:
        day = line.split(' ', 1)[0]

        if len(line.split()) > 4:
            if isLineInt(day):
                dateToPrint = marsToDate(day)

                print('    </div>')
                print('</div>')
                print('<div class="day" id="' + day + '">')
                print('    <h5><span class="show">' + day + ' mars</span> <span\
 class="hide">' + dateToPrint + '</span></h5>')
                text = line.split(' ', 3)[3]
                print('    <div class="texte">')
                print('    <p>' + text.strip('\n') + '</p>')
            else:
                print('    <p class="plusdeP">' + line.strip('\n') + '</p>')


print('</div>\n</div>\n</div>\n')

with open('footer.html', 'r') as footer:
    for line in footer:
        print(line.strip('\n'))
