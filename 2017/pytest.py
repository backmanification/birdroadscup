import pdb

infofile = open('static/games/games.csv').read()
infoline = infofile.split('\n')
#print infoline
body = str()
for item in infoline:
    info = item.split(',')
    print info
    if info[0] == "R1/G1":
        pdb.set_trace()
        for i in range(3,len(info)):
            pdb.set_trace()
            body += '<a href="/birdroadscup/games/{{info[0]}}/game'+str(i-2)+'"><p class="score">{{info[i]}}</p></a>'
    
