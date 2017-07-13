from flask import Flask, render_template, make_response, jsonify, request, abort
import os
import pdb

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('startsite.html')

@app.route('/games/')
@app.route('/games/<matchseries>/')
def show_game_summary(matchseries):
    #get team information
    #matchid = matchid.encode('utf-8')
    infofile = open('static/games/games.csv').read()
    infoline = infofile.split('\n')
    #print infoline
    body = ''
    for item in infoline:
        info = item.split(',')
        if info[0] == matchseries:
            folder = info[0].split('-')
            internet = ''
            for ink in folder:
                internet += ink+'/'
            try:
                table=playerstats_to_html(stats_reader('static/games/'+str(internet)+'playerstats.csv'))
            except IOError:
                table='TBD'
            for i in range(3,len(info)):
                if info[i] == '':
                    break
                body += '<a href="/games/'+str(info[0])+'/game'+str(i-2)+'" onclick="openInParent("/playofftree")><p class="score">'+info[i]+'</p></a> '
            return render_template('gamesummary.html', info=info, body = body, table=table)
    return render_template('child.html')

@app.route('/games/<matchseries>/<game>')
def show_game_details(matchseries, game):
    try:
        gamenr = game[4]
        gamenr = int(gamenr)
    except ValueError:
        return render_template('child.html')
    
    infofile = open('static/games/games.csv').read()
    infoline = infofile.split('\n')
    for item in infoline:
        info = item.split(',')
        if info[0] == matchseries:
            matchseries = matchseries.encode('utf-8')
            matchlist = matchseries.split('-')
            events2 = ''
            try:
                open('static/games/'+matchlist[0]+'/'+matchlist[1]+'/'+game+'/events2.jpg')
                events2 = '<img src="/static/games/'+matchlist[0]+'/'+matchlist[1]+'/'+game+'/events2.jpg" width="700pt" class="centering"></img>'
            except IOError:
                True
            return render_template('game.html', info={'team': info[1:3], 'score': info[gamenr+2], 'matchid': matchlist, 'game': game}, events2 = events2)
    return render_template('child.html')

@app.route('/stats/')
def show_player_stats():
    playertable = playerstats_to_html(stats_reader('static/stats/playerstats.csv'))
    #goalietable = playerstats_to_html(stats_reader('static/stats/goaliestats.csv'),'2')
    return render_template('stats.html', playertable=playertable)#, goalietable=goalietable)

@app.route('/awards/')
def show_awards():
    return render_template('awards.html')

@app.route('/draft/')
def show_draft():
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
            dbl[inprog[0]] = inprog
    solodrafttext = ''
    for i in range(1,len(solo)+1):
        solodrafttext += '<div class="row"><div class="col-xs-4"><p class="finalscore">'+solo[str(i)][0]+'</p></div><div class="col-xs-4"><h2>'+solo[str(i)][3]+'</h2><h3>'+solo[str(i)][4]+'</h3></div><div class="col-xs-4"><img src="/static/teams/'+solo[str(i)][2]+'/'+solo[str(i)][2]+'logo.png" width="100%" ></img></div></div>'
    dbldrafttext = ''
    for i in range(1,len(dbl)+1):
        dbldrafttext += '<div class="row"><div class="col-xs-4"><p class="finalscore">'+dbl[str(i)][0]+'</p></div><div class="col-xs-4"><h2>'+dbl[str(i)][3]+'</h2><h3>'+dbl[str(i)][4]+'</h3></div><div class="col-xs-4"><img src="/static/teams/'+dbl[str(i)][2]+'/'+dbl[str(i)][2]+'logo.png" width="100%" ></img></div></div>'

    return render_template('draft.html', info={'solo': solo, 'dbl': dbl, 'solotext': solodrafttext, 'dbltext': dbldrafttext})

@app.route('/teams/')
@app.route('/teams/<teamname>')
def show_team_profile(teamname):
    #get team information
    teamname = teamname.encode('utf-8')
    infofile = open('static/teams/teams.txt').read()
    infoline = infofile.split('\n')
    #print infoline
    for item in infoline:
        info = item.split(',')
        if info[0] == teamname:
            return render_template('teams.html', team=info)
    return render_template('child.html', team=[type(teamname),info[0],type(info[0]),teamname])

@app.route('/playofftree')
def show_playofftree():
    infofile = open('static/games/games.csv').read()
    infoline = infofile.split('\n')
    for item in infoline:
        info = item.split(',')
        if info[0] == 'BRC':
            count = 0
            body = ''
            home=0
            away=0
            gameinfo = ''
            for i in range(3,len(info)):
                if info[i] == '':
                    break
                gameinfo = info[i].split('-')
                if gameinfo[0]>gameinfo[1]:
                    home +=1
                else:
                    away +=1
                body += '<div class="row"><div class="col-xs-2"></div><div class="col-xs-2"><p class="score">'+gameinfo[0]+'</p></div><div class="col-xs-4"><a href="/games/BRC/game'+str(i-2)+'"><p class="score">Game '+str(i-2)+'</p></a></div><div class="col-xs-2"><p class="score">'+gameinfo[1]+'</p></div><div class="col-xs-2"></div></div>'
            
            return render_template('playofftree.html', final={'teaminfo': info[1:3], 'gameinfo': gameinfo, 'body': body, 'series': [home, away]})



def stats_reader(pathtostatsfile):
    infofile = open(pathtostatsfile).read()
    infoline = infofile.split('\n')
    stats =[]
    for item in infoline:
        if item != '':
            stats.append( item.split(',') )
    return stats

def playerstats_to_html(stats, idchanger=''):
    #creating the table
    html_string='<table id="example'+idchanger+'" class="table table-striped table-bordered" width="100%" cellspacing="0">'
    #creating the head
    html_string+='<thead><tr>'
    for item in stats[0]:
        html_string+='<th>'+item+'</th>'
    html_string+='</tr></thead>'
    #starting the body
    html_string += '<tbody>'
    #looping over all players adding a row
    for line in stats:
        if line == stats[0]:
            continue
        html_string+='<tr>'
        for item in line:
            html_string+='<td>'+item+'</td>'
        html_string+='</tr>'
    #closing the body and table
    html_string +='</tbody></table>'
    return html_string

def add_stats():
    stats =[]
    for x in os.walk('static/games'):
        if len(x[0]) > 16:
            continue
        for i in x[1]:
            if len(i) < 4:
                try:
                    pdb.set_trace()
                    stats.append(stats_reader(x[0]+'/'+i+'/stats.csv'))
                except IOError:
                    True
    for seriesstats in stats:
        if seriesstats == stats[0]:
            continue
        
    #har borjar additionsdelen

    #sok igenom alla mappar i matchseries efter en fil som heter stats.csv, hoppa over forsta raden (headern), kolla om nagra namn matchar, isf adera ihop resterande kolumner, gor en gang i borjan, sen later man sidan rulla
