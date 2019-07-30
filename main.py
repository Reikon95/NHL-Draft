#import csv
#import numpy
DO9 = {}
D10 = {}
D11 = {}
D12 = {}
D13 = {}
D14 = {}
D15 = {}
D16 = {}
D17 = {}
D18 = {}



with open('2009.csv') as Draft09:
  draft = Draft09.readlines()
  for pick in draft:
    # print(pick)
    a = pick.split(',')
    # print(a[1])
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
  def num_games():
    i = 0
    for pick in draft:
      a = pick.split(',')
      try: 
        i += int(a[8])
      except:
        continue 
    return i
  print(num_games())

with open('2010.csv') as Draft10:
  draft = Draft10.readlines()
  print(num_games())

with open('2011.csv') as Draft11:
  draft = Draft11.readlines()
  print(num_games())

with open('2012.csv') as Draft12:
  draft = Draft12.readlines()
  print(num_games())

with open('2013.csv') as Draft13:
  draft = Draft13.readlines()
  print(num_games())

with open('2014.csv') as Draft14:
  draft = Draft14.readlines()
  print(num_games())

with open('2015.csv') as Draft15:
  draft = Draft15.readlines()
  print(num_games())

with open('2016.csv') as Draft16:
  draft = Draft16.readlines()
  print(num_games())

with open('2017.csv') as Draft17:
  draft = Draft17.readlines()
  print(num_games())

with open('2018.csv') as Draft18:
  draft = Draft18.readlines()
  print(num_games())
