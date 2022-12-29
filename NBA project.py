# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 15:51:02 2022

@author: xz_an
"""
import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players


def Menu():
  user = str(
    input(
      "Welcome user, enter a NBA player's name to see their point statistics!\n"
    ))
  player = [player for player in player_dict if player['full_name'] == user][0]

  return player


def Season(player):
  season_id = str(input("What season would you like to see? (ex: 2019-20)\n"))
  gamelog_user = playergamelog.PlayerGameLog(player_id=player['id'],
                                             season=season_id)
  gamelog_user_df = gamelog_user.get_dict()
  pts = []
  ind = []
  counter = 0
  for i in range(len(gamelog_user_df['resultSets'][0]['rowSet'])):
      pts.append(gamelog_user_df['resultSets'][0]['rowSet'][i][24])
      counter += 1
      ind.append(counter)
  #print(pts)
  temp = player['full_name']
  plt.scatter(ind, pts, s = 50, cmap='Green', edgecolor='black') 
  plt.title(f"{temp} {season_id}")
  plt.xlabel('Regular Season Games Played')
  plt.ylabel('Points Scored')

player_name = ""
player_dict = players.get_players()
player = Menu()

Statistics = Season(player)
