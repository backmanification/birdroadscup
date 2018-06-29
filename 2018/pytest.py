from birdroadscup import stats_reader, playerstats_to_html, show_profiles
import pdb

c = show_profiles('Magnus_Ahlm')



while True:
    a = stats_reader('static/stats/goaliestats.csv')
    pdb.set_trace()
    b = playerstats_to_html(a)

print playerstats_to_html(stats_reader('static/stats/goaliestats.csv'),'2')
