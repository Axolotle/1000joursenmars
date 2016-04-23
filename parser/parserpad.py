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

def orthoTypo(text, rules):
    for i, j in rules.items(): 
        text = text.replace(i, j)
    return text


rules = { " ;": "&nbsp;;", 
          " :": "&nbsp;:",
          " ?": "&nbsp;?",
          " !": "&nbsp;!",
          "« ": "«&nbsp;",
          " »": "&nbsp;»",
          " -": "&nbsp;-",
          "'" : "´" }



with open('main.html', 'r') as main:
    for line in main:
        print(line.strip('\n'))


print('\n<div id="main" class="cols">')

with open('padimport.txt', 'r') as pad1000:
    first = True
    for _ in range(24):
        next(pad1000)
    for line in pad1000:
        day = line.split(' ', 1)[0]

        if len(line.split()) > 4:
            if isLineInt(day):
                dateToPrint = marsToDate(day)
                if (first):
                    first = False
                else:
                    print('        </div>')
                    print('    </div>')

                print('    <div class="day" id="' + day + '">')
                print('        <h5><span class="show">' + day + ' mars</span> \
<span class="hide">' + dateToPrint + '</span></h5>')
                text = line.split(' ', 3)[3]
                text = orthoTypo(text, rules)
                print('        <div class="texte">')
                print('            <p>' + text.strip('\n') + '</p>')
            else:
                text = orthoTypo(line, rules)
                print('            <p class="plusdeP">' + text.strip('\n') + '</p>')


print('</div>\n</div>\n</div>\n')

with open('footer.html', 'r') as footer:
    for line in footer:
        print(line.strip('\n'))
