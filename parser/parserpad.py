# with open('data.txt', 'r') as pad1000:
#     for line in pad1000:
#         day = line.split(' ', 1)[0]
#  
#         print('<div id="mars' + day + '" class="day">')
#         print('    <h5>' + day + ' mars</h5>')
#        
#         if len(line.split()) > 3:
#             text = line.split(' ', 3)[3]
#             print('    <p>' + text.strip('\n') + '</p>')
#         print('</div>')

def isLineInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

print('<!DOCTYPE html>\n<html>\n    <head>\n    <meta charset="utf-8" />\n\
        <title>1000 jours en mars</title>\n\
        <meta name="description" content="1000 jours en mars est un projet\
d\'écriture à mille mains, une fabrique bricolée de mille futurs possibles."\
 />\n\
        <meta name="keywords" content="1000joursenmars, écriture, collaborative,\
 nuitdebout, nuit, debout, futur, lutte, désincarcerer, zanzibar" />\n\
        <link rel="stylesheet" href="test.css" />\n\
    </head>\n\n    <body>\n')

with open('main.html', 'r') as main:
    for line in main:
        print(line.strip('\n'))

print('<div id="main">')

with open('padimport.txt', 'r') as pad1000:
    for line in pad1000:
        day = line.split(' ', 1)[0]

#        if isLineInt(day):
#            print('</div>')
#            print('<div id="mars' + day + '" class="day">')
#            print('    <h5>' + day + ' mars</h5>')
#       
#            if len(line.split()) > 3:
#                text = line.split(' ', 3)[3]
#                print('    <p>' + text.strip('\n') + '</p>')
#        else:
#            print('    <p class="plusdeP">' + line.strip('\n') + '</p>')

# Si un texte est attaché au jour, print le jour et son texte
        if len(line.split()) > 4:
            if isLineInt(day):
                print('</div>')
                print('<div id="mars' + day + '" class="day">')
                print('    <h5>' + day + ' mars</h5>')
                text = line.split(' ', 3)[3]
                print('    <p>' + text.strip('\n') + '</p>')
            else:
                print('    <p class="plusdeP">' + line.strip('\n') + '</p>')



print('</div>\n</div>')
print('    </body>\n</html>')
