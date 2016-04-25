#!/usr/bin/env python3

from datetime import date, timedelta
from urllib.request import urlopen
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')

#DIR = '/var/www/1000joursenmars/'
DIR = '/home/univers-b/dev/1000joursenmars/'


def isLineInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def marsToDate(d):
    daysToAdd = eval(d) - 31
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



def generateHTML() :
    html = [ ]

    with open(DIR + 'parser/main.html', 'r') as main:
        for line in main:
            html.append(line.strip('\n'))


    html.append('\n<div id="main" class="cols">')

    with urlopen('https://strasbourg.nuitdebout.fr/pad/p/1000joursenmars/export/txt') as pad1000:
        first = True
        for _ in range(24):
            next(pad1000)
        for line in pad1000:
            line = line.decode('utf-8')
            day = line.split(' ', 1)[0]

            if len(line.split()) > 4:
                if isLineInt(day):
                    dateToPrint = marsToDate(day)
                    if (first):
                        first = False
                    else:
                        html.append('        </div>')
                        html.append('    </div>')

                    html.append('    <div class="day" id="' + day + '">')
                    html.append('        <h5><span class="show">' + day + ' mars</span> <span class="hide">' + dateToPrint + '</span></h5>')
                    text = line.split(' ', 3)[3]
                    text = orthoTypo(text, rules)
                    html.append('        <div class="texte">')
                    html.append('            <p>' + text.strip('\n') + '</p>')
                else:
                    text = orthoTypo(line, rules)
                    html.append('            <p class="plusdeP">' + text.strip('\n') + '</p>')


    html.append('        </div>\n    </div>\n</div>\n')

    with open(DIR + 'parser/footer.html', 'r') as footer:
        for line in footer:
            html.append(line.strip('\n'))

    return html

def main():
    html = generateHTML()
    html = '\n'.join(html)

    with open(DIR + "index.html","w") as output :
        output.write(html)


main()
