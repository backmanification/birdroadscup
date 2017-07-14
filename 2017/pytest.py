from birdroadscup import stats_reader, playerstats_to_html


print playerstats_to_html(stats_reader('static/stats/goaliestats.csv'),'2')
