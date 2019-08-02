import csv
import numpy as np

with open('2009.csv') as Draft09:
  draft = Draft09.readlines()
  for pick in draft:
    a = pick.split(',')
  round_one = []
  round_two = []
  round_three = []
  round_four = []
  round_five = []
  round_six = []
  round_seven = []  
  def round_sorter():
    i = 1
    for pick in draft:
      if i < 32:
        round_one.append(pick)
      elif i < 62:
        round_two.append(pick)
      elif i < 92:
        round_three.append(pick)
      elif i < 122: 
        round_four.append(pick)
      elif i < 152:
        round_five.append(pick)
      elif i < 182:
        round_six.append(pick)
      else:
        round_seven.append(pick)
      i += 1
  round_sorter()
  
  def team_picks():
    picks = []
    for pick in draft:
      a = pick.split(',')
      picks.append(a[1])  
    return picks
  def num_games():
    i = 0
    for pick in draft:
      a = pick.split(',')
      try: 
        i += int(a[8])
      except:
        continue 
    return i
  
  def num_picks():
    i = 0
    for pick in draft:
      i += 1
    return i 
  num_picks()
  def mean_games(dataset):
    av = int(((num_games()) / (num_picks())))
    return 'The mean number of games played in this draft was ' + str(av)

  def pct_games_played(dataset):
    median_set = []
    for pick in draft:
      a = pick.split(',')
      if (a[8] == 'GP'):
        continue
      elif (a[8] == ''):
        continue
      elif (int(a[8]) > 0): 
        median_set.append(a[8])
    pc = int(100 * (len(median_set) / num_picks()))
    return str(pc) + '% of players drafted in this year went on to play a game in the NHL' 
  print(pct_games_played(draft))  
  
  def position_sorter(dataset, position):
    pos = []
    for pick in draft:
      a = pick.split(',')
      if (a[4] == position):
        pos.append(a[4])  
    result = 'There were ' + str(len(pos)) + ' players picked who were listed as ' + position + '.'
    return result
  print(position_sorter(draft, 'D'))
    
with open('2010.csv') as Draft10:
  draft = Draft10.readlines()
  print(mean_games(draft))
  print(pct_games_played(draft))  

with open('2011.csv') as Draft11:
  draft = Draft11.readlines()
  print(mean_games(draft))
  print(pct_games_played(draft))  

with open('2012.csv') as Draft12:
  draft = Draft12.readlines()
  print(mean_games(draft))
  print(pct_games_played(draft))  

with open('2013.csv') as Draft13:
  draft = Draft13.readlines()

  print(mean_games(draft))
  print(pct_games_played(draft))  

with open('2014.csv') as Draft14:
  draft = Draft14.readlines()
  print(mean_games(draft))
  print(pct_games_played(draft))  

with open('2015.csv') as Draft15:
  draft = Draft15.readlines()
  print(mean_games(draft))
  print(pct_games_played(draft))  

with open('2016.csv') as Draft16:
  draft = Draft16.readlines()
  print(mean_games(draft))
  print(pct_games_played(draft))  

with open('2017.csv') as Draft17:
  draft = Draft17.readlines()
  print(mean_games(draft))
  print(pct_games_played(draft))  


