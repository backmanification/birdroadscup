from flask import Flask, render_template, make_response, jsonify, request, abort
import unicodedata as ucd

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

@app.route('/stats/')
def show_player_stats():
    return render_template('stats.html')

@app.route('/awards/')
def show_awards():
    return render_template('awards.html')


"""
@app.route('/games/DF/<matchid>')
def show_game_DF(matchid):
    #get team information
    #matchid = matchid.encode('utf-8')
    infofile = open('static/games/games.csv').read()
    infoline = infofile.split('\n')
    #print infoline
    body = str()
    for item in infoline:
        info = item.split(',')
        if info[0] == "DF/"+matchid:
            for i in range(3,len(info)):
                if info[i] == '':
                    break
                body += '<a href="/birdroadscup/games/{{info[0]}}/game'+str(i-2)+'"><p class="score">{{info['+str(i)+']}}</p></a>'
            return render_template('gamesummary.html', info=info, body = body)
    return render_template('child.html')

@app.route('/games/CF/<matchid>')
def show_game_CF(matchid):
    #get team information
    #matchid = matchid.encode('utf-8')
    infofile = open('static/games/games.csv').read()
    infoline = infofile.split('\n')
    #print infoline
    body = str()
    for item in infoline:
        info = item.split(',')
        if info[0] == "CF/"+matchid:
            for i in range(3,len(info)):
                if info[i] == '':
                    break
                body += '<a href="/birdroadscup/games/{{info[0]}}/game'+str(i-2)+'"><p class="score">{{info['+str(i)+']}}</p></a> '
            return render_template('gamesummary.html', info=info, body = body)
    return render_template('child.html')

@app.route('/games/BRC/<matchid>')
def show_game_BRC(matchid):
    #get team information
    #matchid = matchid.encode('utf-8')
    infofile = open('static/games/games.csv').read()
    infoline = infofile.split('\n')
    #print infoline
    body = str()
    for item in infoline:
        info = item.split(',')
        if info[0] == "BRC/"+matchid:
            for i in range(3,len(info)):
                if info[i] == '':
                    break
                body += '<a href="/birdroadscup/games/{{info[0]}}/game'+str(i-2)+'"><p class="score">{{info['+str(i)+']}}</p></a>'
            return render_template('gamesummary.html', info=info, body = body)
    return render_template('child.html')
"""
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


"""
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('child.html', name=name)
"""

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('child.html', name=name)
