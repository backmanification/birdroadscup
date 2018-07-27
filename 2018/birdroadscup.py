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
            try:
                goalietable = playerstats_to_html(stats_reader('static/games/'+str(internet)+'goaliestats.csv'),'2')
            except IOError:
                goalietable = 'TBD'
            for i in range(3,len(info)):
                if info[i] == '':
                    break
                body += '<a href="/games/'+str(info[0])+'/game'+str(i-2)+'" onclick="openInParent("/playofftree")><p class="score">'+info[i]+'</p></a> '
            return render_template('gamesummary.html', info=info, body = body, table=table, goalietable=goalietable)
    return render_template('child.html')

@app.route('/profiles/<name>')
def show_profiles(name):
    Ahlm = {'name': 'Magnus Ahlm',
            'solo': { 'BOS': {'name':'BOS', 'games': ['R1-G6'], 'results': ['-OTT 2-3(L)']},
                      'CBJ': {'name':'CBJ', 'games': ['R1-G8'], 'results': ['-PIT 1-3(L)']},
                      'MIN': {'name':'MIN', 'games': ['R1-G2'], 'results': ['-STL 1-3(L)']},
                      'MTL': {'name':'MTL', 'games': ['DF-G3'], 'results': ['-OTT 2-3(L)']} },
            'dble': { 'MTL': {'name':'MTL', 'games': ['R1-G5'], 'results': ['-NYR 3-0(W)'], 'other_member': 'Niklas_Wiberg','teamname': 'Team Rest'},
                      'CGY': {'name':'CGY', 'games': ['R1-G3'], 'results': ['-ANA 0-3(L)'], 'other_member': 'Filip_Backman','teamname': 'Team Chaffinch'} },
            'awards': {'2017': {'prizes': [''], 'as':['']}}}
    
    Backman = {'name': 'Filip Backman',
               'solo': { 'SJS': {'name':'SJS', 'games': ['R1-G4'], 'results': ['-EDM 2-3(L)']},
                         'STL': {'name':'STL', 'games': ['R1-G2','DF-G1','CF-G1'], 'results': ['-MIN 3-1(W)','-CHI 3-1(W)','-ANA 3-1(W)']},
                         'WSH': {'name':'WSH', 'games': ['R1-G7','DF-G4','CF-G2'], 'results': ['-TOR 3-1(W)','-PIT 3-1(W)','-OTT 3-0(W)']} },
               'dble': { 'CGY': {'name':'CGY', 'games': ['R1-G3'], 'results': ['-ANA 0-3(L)'], 'other_member': 'Magnus_Ahlm','teamname': 'Team Chaffinch'},
                         'NYR': {'name':'NYR', 'games': ['R1-G5'], 'results': ['-MTL 0-3(L)'], 'other_member': 'Filip_Edstrom','teamname': 'Team Filip'} },
               'awards': {'2017': {'prizes': ['Bird Roads Cup','Conn Smirk Trophy','Steve Icerman Trophy','Dominik Hasek Award'], 'as':['Filip Backman','Vladimir Tarasenko', 'Karl Alzner', 'Braden Holtby']}}}
    
    Edstrom = {'name': 'Filip Edstrom',
               'solo': { 'CHI': {'name':'CHI', 'games': ['R1-G1','DF-G1'], 'results': ['-NAS 3-1(W)','-STL 1-3(L)']},
                         'EDM': {'name':'EDM', 'games': ['R1-G4','DF-G2'], 'results': ['-SJS 3-2(W)','-ANA 1-3(L)']},
                         'PIT': {'name':'PIT', 'games': ['R1-G8','DF-G4'], 'results': ['-CBJ 3-1(W)','-WSH 1-3(L)']} },
               'dble': { 'ANA': {'name':'ANA', 'games': ['R1-G3','CF-G1'], 'results': ['-CGY 3-0(W)','-STL 1-3(L)'], 'other_member': 'Niklas_Wiberg','teamname': 'Team Thrush'},
                         'NYR': {'name':'NYR', 'games': ['R1-G5'], 'results': ['-MTL 0-3(L)'], 'other_member': 'Filip_Backman','teamname': 'Team Filip'} },
               'awards': {'2017': {'prizes': [''], 'as':['']}}}
    
    NWiberg = {'name': 'Niklas Wiberg',
              'solo': { 'NAS': {'name':'NAS', 'games': ['R1-G1'], 'results': ['-CHI 1-3(L)']},
                        'OTT': {'name':'OTT', 'games': ['R1-G6','DF-G3','CF-G2'], 'results': ['-BOS 3-2(W)','-MTL 3-2(W)','-WSH 0-3(L)']},
                        'TOR': {'name':'TOR', 'games': ['R1-G7'], 'results': ['-WSH 1-3(L)']},
                        'ANA': {'name':'ANA', 'games': ['DF-G2'], 'results': ['-EDM 3-1(W)']} },
              'dble': { 'ANA': {'name':'ANA', 'games': ['R1-G3','CF-G1'], 'results': ['-CGY 3-0(W)','-STL 1-3(L)'], 'other_member': 'Filip_Edstrom','teamname': 'Team Thrush'},
                        'MTL': {'name':'MTL', 'games': ['R1-G5'], 'results': ['-NYR 3-0(W)'], 'other_member': 'Magnus_Ahlm','teamname': 'Team Rest'} },
              'awards': {'2017': {'prizes': [''], 'as':['']}}}

    VWiberg = {'name': 'Viktor Wiberg',
              'solo': { 'NAS': {'name':'NAS', 'games': ['R1-G1'], 'results': ['-CHI 1-3(L)']},
                        'OTT': {'name':'OTT', 'games': ['R1-G6','DF-G3','CF-G2'], 'results': ['-BOS 3-2(W)','-MTL 3-2(W)','-WSH 0-3(L)']},
                        'TOR': {'name':'TOR', 'games': ['R1-G7'], 'results': ['-WSH 1-3(L)']},
                        'ANA': {'name':'ANA', 'games': ['DF-G2'], 'results': ['-EDM 3-1(W)']} },
              'dble': { 'ANA': {'name':'ANA', 'games': ['R1-G3','CF-G1'], 'results': ['-CGY 3-0(W)','-STL 1-3(L)'], 'other_member': 'Filip_Edstrom','teamname': 'Team Thrush'},
                        'MTL': {'name':'MTL', 'games': ['R1-G5'], 'results': ['-NYR 3-0(W)'], 'other_member': 'Magnus_Ahlm','teamname': 'Team Rest'} },
              'awards': {'2017': {'prizes': [''], 'as':['']}}}

    players = [Ahlm, Backman, Edstrom, NWiberg, VWiberg]
    name = name.replace('_',' ')
    name.decode('utf-8')
    for player in players:
        if player['name'] == name:
            solo_body = '<div class="container">'
            solo_body +='<h1>'+player['name']+'</h1><div class="row"><div class="col-xs-6"><h3>Solo Teams</h3></div><div class="col-xs-6"><h3>Solo Matches</h3></div></div>'
            for team in player['solo'].keys():
                solo_team_info = '<div class="row">'
                solo_team_info += '<div class="col-xs-6"><p class="teams"><img src="/static/teams/'+player['solo'][team]['name']+'/'+player['solo'][team]['name']+'logo.png" height="25pt" ><a href="/teams/'+player['solo'][team]['name']+'">'+player['solo'][team]['name']+'</p></a></div>'
                solo_team_info += '<div class="col-xs-6"><p class="teams">'
                for gameno in range(len(player['solo'][team]['games'])):
                    solo_team_info += '<a href="/games/'+player['solo'][team]['games'][gameno]+'/">'+player['solo'][team]['name']+player['solo'][team]['results'][gameno]+'</a>    '
                solo_team_info += '</p></div></div>'
                solo_body += solo_team_info
            solo_body += '</div>'

            dbl_body = '<div class="container">'
            dbl_body +='<div class="row"><div class="col-xs-6"><h3>Double Teams</h3></div><div class="col-xs-6"><h3>Double Matches</h3></div></div>'
            for team in player['dble'].keys():
                dbl_team_info = '<div class="row">'
                dbl_team_info += '<div class="col-xs-6"><p class="teams"><img src="/static/teams/'+player['dble'][team]['name']+'/'+player['dble'][team]['name']+'logo.png" height="25pt" ><a href="/teams/'+player['dble'][team]['name']+'/">'+player['dble'][team]['name']+'</a> together with <a href="/profiles/'+player['dble'][team]['other_member']+'">'+player['dble'][team]['other_member'].replace('_',' ')+'</a> as '+player['dble'][team]['teamname']+'</p></div>'
                dbl_team_info += '<div class="col-xs-6"><p class="teams">'
                for gameno in range(len(player['dble'][team]['games'])):
                    dbl_team_info += '<a href="/games/'+player['dble'][team]['games'][gameno]+'/">'+player['dble'][team]['name']+player['dble'][team]['results'][gameno]+'</a>   '
                dbl_team_info += '</p></div></div>'
                dbl_body += dbl_team_info
            dbl_body += '</div>'
            
            #print solo_body
            awards_text = '<div class="container">'
            awards_text += '<div class="row"><h3>Awards</h3><div class="col-xs-4"><h4>Year:</h4></div><div class="col-xs-4"><h4>Award:</h4></div><div class="col-xs-4"><h4>As:</h4></div></div>'
            for year in player['awards'].keys():
                awards_text += '<div class="row"><div class="col-xs-4"><p>'+year+':</p></div>'
                prize_text = '<div class="col-xs-4">'
                winner_text = '<div class="col-xs-4">'
                for no in range(len(player['awards'][year]['prizes'])):
                    prize_text += '<p>'+player['awards'][year]['prizes'][no]+'</p>'
                    winner_text += '<p>'+player['awards'][year]['as'][no]+'</p>'
                awards_text += prize_text + '</div>' + winner_text + '</div></div></div>'

                     
            return render_template('profiles.html',player=player, solobody=solo_body, dblbody = dbl_body, awardsbody=awards_text)



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
            if len(matchlist)>1:
                try:
                    open('static/games/'+matchlist[0]+'/'+matchlist[1]+'/'+game+'/events2.jpg')
                    events2 = '<img src="/static/games/'+matchlist[0]+'/'+matchlist[1]+'/'+game+'/events2.jpg" width="700pt" class="centering"></img>'
                except IOError:
                    True
            else:
                try:
                    open('static/games/'+matchlist[0]+'/'+game+'/events2.jpg')
                    events2 = '<img src="/static/games/'+matchlist[0]+'/'+game+'/events2.jpg" width="700pt" class="centering"></img>'
                except IOError:
                    True

            return render_template('game.html', info={'team': info[1:3], 'score': info[gamenr+2], 'matchid': matchlist, 'game': game}, events2 = events2)
    return render_template('child.html')

@app.route('/calendar/')
def show_calendar():
    return render_template('calendar.html')

@app.route('/stats/')
def show_player_stats():
    playertable = playerstats_to_html(stats_reader('static/stats/playerstats.csv'))
    goalietable = playerstats_to_html(stats_reader('static/stats/goaliestats.csv'),'2')
    return render_template('stats.html', playertable=playertable, goalietable=goalietable)

@app.route('/awards/')
def show_awards():
    return render_template('awards.html')

@app.route('/draft/')
def show_draft():
    infofile = open('static/draft.txt').read()
    try:
        infosolodbl = infofile.split('dubbel\n')
        dbl = {}
    except:
        infosolodbl = [infofile]
    solo = {}
    for item in infosolodbl[0].split('\n'):
        if item != '':
            inprog = item.split(',')
            solo[inprog[0]] = inprog
    try:
        for item in infosolodbl[1].split('\n'):
            if item != '':
                inprog = item.split(',')
                dbl[inprog[0]] = inprog
    except:
        True
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
            home="1"
            away="2"
            gameinfo = ''
            for i in range(3,len(info)):
                if info[i] == '':
                    break
                gameinfo = info[i].split('-')
                """
                try:
                    if gameinfo[0]>gameinfo[1]:
                        home +=1
                    else:
                        away +=1
                except IndexError:
                    home = 1
                    away = 2
                """
                body += '<div class="row"><div class="col-xs-2"></div><div class="col-xs-2"><p class="score">'+gameinfo[0]+'</p></div><div class="col-xs-4"><a href="/games/BRC/game'+str(i-2)+'"><p class="score">Game '+str(i-2)+'</p></a></div><div class="col-xs-2"><p class="score">'+gameinfo[1]+'</p></div><div class="col-xs-2"></div></div>'
            
            return render_template('playofftree.html', final={'teaminfo': info[1:3], 'gameinfo': gameinfo, 'body': body, 'series': [home, away]})

@app.route('/humanstats')
def show_human_stats():
    solotable = playerstats_to_html(stats_reader('static/stats/individual_stats/indstats.csv'))
    dbltable = playerstats_to_html(stats_reader('static/stats/individual_stats/teamstats.csv'),'2')
    tottable = playerstats_to_html(stats_reader('static/stats/individual_stats/totstats.csv'),'3')
    return render_template('human_stats.html', stats={'solo': solotable, 'team':dbltable, 'tot':tottable})
    
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
        if item == stats[0][0]:
            item = 'POS'
        html_string+='<th>'+item+'</th>'
    html_string+='</tr></thead>'
    #starting the body
    html_string += '<tbody>'
    #looping over all players adding a row
    for line in stats:
        if line == stats[0]:
            continue
        if line == ['\x00']:
            continue
        html_string+='<tr>'
        for item in line:
            html_string+='<td>'+item+'</td>'
        html_string+='</tr>'
    #closing the body and table
    html_string +='</tbody></table>'
    return html_string
        
    #har borjar additionsdelen

    #sok igenom alla mappar i matchseries efter en fil som heter stats.csv, hoppa over forsta raden (headern), kolla om nagra namn matchar, isf adera ihop resterande kolumner, gor en gang i borjan, sen later man sidan rulla

#"table table-striped table-bordered"
