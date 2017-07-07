from flask import Flask, render_template, make_response, jsonify, request, abort

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
            for i in range(3,len(info)):
                if info[i] == '':
                    break
                body += '<a href="/games/'+str(info[0])+'/game'+str(i-2)+'" onclick="openInParent("/playofftree")><p class="score">'+info[i]+'</p></a> '
            return render_template('gamesummary.html', info=info, body = body)
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
            return render_template('game.html', info={'team': info[1:3], 'score': info[gamenr+2], 'matchid': matchlist, 'game': game})
    return render_template('child.html')

@app.route('/stats/')
def show_player_stats():
    return render_template('stats.html')

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
    return render_template('playofftree.html')
