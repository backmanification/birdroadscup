from PIL import Image, ImageOps, ImageFilter, ImageEnhance
import pytesseract
import os
import pdb
#from birdroadscup import stats_reader

def img_convert(pathtofile, outputpath):
    text = 'POS '
    
    img = Image.open(pathtofile).crop((120, 220, 1220, 850))
    img = ImageOps.invert(img)#(0,0,300,580/14))

    img.save('temp.jpg')

    text += pytesseract.image_to_string(img)
    text = text.replace('1-]','+/')
    text = text.replace('+I-','+/-')
    text = text.replace('F1','R')
    text = text.replace('. ','.')
    text = text.replace(': ','.')
    text = text.replace(', ','.')
    text = text.replace('8.','S.')
    text = text.replace('.8','.S')
    text = text.replace(' D ',' 0 ')
    text = text.replace(' O ',' 0 ')
    text = text.replace('PLAVER','PLAYER')
    text = text.encode('utf-8')
    for i in range(10):
        text = text.replace(str(i)+'O',str(i)+'0')
        text = text.replace(str(i)+'D',str(i)+'0')
    csvtext = text.replace(' ',',')
    
    try:
        text_file = open(outputpath,'r')
        text_file_text = text_file.read()
        text_file.close()
    except IOError:
        text_file = open(outputpath,'w')
        text_file.write(csvtext)
        text_file.close()
        return True

    temp_file = open ('temp.csv','w')
    temp_file.write(csvtext)
    temp_file.close()
    text_file = open(outputpath,'w')

    for text_file_row in text_file_text.split('\n'):
        matched = False
        if len(text_file_row)<2:
            continue
        for row in csvtext.split('\n'):
            if len(row)<2:
                continue
            if text_file_row == row:
                matched = True
            if matched:
                continue
        if not matched:
            csvtext += '\n'+text_file_row
    text_file.write(csvtext)
    text_file.close()
    
def menu():
    success = False
    while True:
        statstype = raw_input('goalie or player stats? ')
        if statstype == 'goalie' or statstype == 'player':
            break
        print 'try again'
    while True:
        try:
            filepath = raw_input('Path to file to process: ')
            open(filepath)
        except IOError:
            print 'There is no such file...'
            continue
        break
    while True:
        outputpath = raw_input('Path to save directory (starting from /static/games/): ')
        outputpath = '2017/static/games/'+outputpath
        for x in os.walk('2017/static/games'):
            print x[0]
            if x[0] == outputpath:
                return True, statstype, filepath, outputpath
            
        answer = raw_input('Are you sure about that path?[y/n] ')
        if answer == 'y':
            print 'youre wrong...'
            continue
            #return True, statstype, filepath, outputpath
        else:
            continue
while True:
    riddle = raw_input('Do you want standard? ')
    if riddle == 'y':
        success = True
        statstype = 'player'
        filepath = 'leksaker/WSH-OTT/stats1.jpg'
        outputpath = '2017/static/games/CF/G2'
        break
    success, statstype, filepath, outputpath = menu()
    if not success:
        continue
    while True:
        print 'Player or Goalie stats: ', statstype
        print 'File to process: ', filepath
        print 'Save Location: ', outputpath
        yesno = raw_input('Are you sure?[y/n] ')
        if yesno == 'y':
            break
        elif yesno == 'n':
            menu()
        else:
            print 'Are you even trying?'
    break

outputpath = outputpath+'/'+statstype+'stats.csv'
print outputpath
img_convert(filepath, outputpath)
