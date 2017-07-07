import pdb

infofile = open('static/draft.txt').read()
infosolodbl = infofile.split('dubbel\n')
solo = {}
dbl = {}
for item in infosolodbl[0].split('\n'):
    if item != '':
        inprog = item.split(',')
        solo[inprog[0]] = inprog
for item in infosolodbl[1].split('\n'):
    if item != '':
        inprog = item.split(',')
        dbl[int(inprog[0])] = inprog
solodrafttext = ''
for i in range(1,len(solo)+1):
    solodrafttext += '<div class="row"><div class="col-xs-4"><p class="finalscore">'+solo[str(i)][0]+'</p></div><div class="col-xs-4"><h2>'+solo[str(i)][3]+'</h2><h3>'+solo[str(i)][4]+'</h3></div><div class="col-xs-4"><img src="/static/teams/'+solo[str(i)][2]+'/'+solo[str(i)][2]+'logo.png" width="100%" ></img></div></div>'
    pdb.set_trace()
print solodrafttext
