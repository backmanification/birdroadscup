import pdb
from birdroadscup import stats_reader, playerstats_to_html

a = stats_reader('static/teams/teams.txt')
pdb.set_trace()


print playerstats_to_html(a)
