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


print('<!DOCTYPE html>\n<html>\n    <head>\n    <meta charset="utf-8" />\n\
        <title>1000 jours en mars</title>\n\
        <meta name="description" content="1000 jours en mars est un projet\
d\'écriture à mille mains, une fabrique bricolée de mille futurs possibles."\
 />\n\
        <meta name="keywords" content="1000joursenmars, écriture, collaborative,\
 nuitdebout, nuit, debout, futur, lutte, désincarcerer, zanzibar" />\n\
        <link rel="stylesheet" href="stylesheetWIP.css" />\n\
    </head>\n\n    <body>\n')


with open('main.html', 'r') as main:
    for line in main:
        print(line.strip('\n'))


print('<div id="main" class="cols">')

with open('padimport.txt', 'r') as pad1000:
    for line in pad1000:
        day = line.split(' ', 1)[0]

        if len(line.split()) > 4:
            if isLineInt(day):
                dateToPrint = marsToDate(day)

                print('    </div>')
                print('</div>')
                print('<div class="day">')
                print('    <h5><span id="show">' + day + ' mars</span> <span\
 id="hide">' + dateToPrint + '</span></h5>')
                text = line.split(' ', 3)[3]
                print('    <div class="texte">')
                print('    <p>' + text.strip('\n') + '</p>')
            else:
                print('    <p class="plusdeP">' + line.strip('\n') + '</p>')


print('</div>\n</div>')

print('        <footer>\n\
        <p>1000 jours en mars est lancé par le collectif \
<a href="http://zanzibar.zone/" target="_blank">Zanzibar</a>. \
Tout ce qui en retombe vous appartient. Si vous savez quoi en faire, prenez \
sans demander : il n\'y a rien à voler. <a href="http://1000joursenmars.space">\
1000joursenmars.space</a></p>\n\
        </footer>')

print('        <script src="test.js"></script>')
print('    </body>\n</html>')
