import os
import pdb

a = os.walk('/static/games/')

from birdroadscup import stats_reader, playerstats_to_html, add_stats
add_stats()



for i in range(3):
    print i
    try:
        a = stats_reader('static/teams/teams.csv')
    except IOError:
        continue


    #print playerstats_to_html(a)
