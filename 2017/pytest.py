import pdb
infofile = open('static/games/games.csv').read()
infoline = infofile.split('\n')
for item in infoline:
    info = item.split(',')
    if info[0] == 'BRC':
        count = 0
        body = ''
        for i in range(3,len(info)):
            if info[i] == '':
                break
            gameinfo = info[i].split('-')
            body += '<div class="row"><div class="col-xs-3"><p class="score">'+gameinfo[0]+'</p></div><div class="col-xs-3"><p class="score">Game '+str(i-2)+'</p></div><div class="col-xs-3"><p class="score">'+gameinfo[1]+'</p></div></div>'
        pdb.set_trace()
