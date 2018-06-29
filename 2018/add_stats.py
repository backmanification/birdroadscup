import os
import pdb

def tot_stats(statstype):
    tot_stats = open('static/stats/'+statstype+'stats.csv','w')
    text = ''
    cont_games = ['BRC','DF','CF']
    #make base of known unique players
    for x in os.walk('static/games/R1/'):
        try:
            stats_file = open(x[0]+'/'+statstype+'stats.csv','r')
            stats = stats_file.read()
        except IOError:
            continue
        statsrow = stats.split('\n')
        if text == '':
            text = statsrow[0]
        for row in statsrow:
            if row == statsrow[0]:
                continue
            text += '\n'+row
        stats_file.close()
    tot_stats.write(text)
    tot_stats.close()
    text = ''
    print 'text origin', text
    #start adding stats
    tot_stats_file = open('static/stats/'+statstype+'stats.csv','r')    
    tot_stats = tot_stats_file.read()
    tot_stats_file.close()
    tot_statsrows = tot_stats.split('\n')
    tot_items = []
    for row in tot_statsrows:
        tot_items.append(row.split(','))
                        
    for runda in cont_games:
        for x in os.walk('static/games/'+runda+'/'):
            try:
                stats_file = open(x[0]+'/'+statstype+'stats.csv','r')
                stats = stats_file.read()
            except IOError:
                continue
            statsrows = stats.split('\n')

            for row in statsrows:
                if row == statsrows[0]:
                    continue
                item = row.split(',')
                for index in range(len(tot_items)):
                    #print index
                    if tot_items[index][0] =='':
                        continue
                    #print 'new',item
                    #print 'old',tot_items[index]
                    if item[0] == '':
                        continue
                    if item[1] == tot_items[index][1]:
                        for i in range(3,len(tot_items[index])):
                            try:
                                tot_items[index][i] = int(tot_items[index][i])
                                tot_items[index][i] += int(item[i])
                                tot_items[index][i] = str(tot_items[index][i])
                            except ValueError:
                                tot_items[index][i] = 'Error'
                    #print 'sum', tot_items[index]
    for n in tot_items:
        #pdb.set_trace()
        #print n
        for i in range(len(n)):
            if i != len(n)-1:
                text += n[i]+','
            else:
                text += n[i]+'\n'
        #print text
    print 'xxxx'
    #text.encode('utf-8')
    print 'cccc'
    tot_stats_file = open('static/stats/'+statstype+'stats.csv','w')
    tot_stats_file.write(text)
    tot_stats_file.close()

tot_stats('player')
