# DS-5100-2022-Final-Project

Matthew Scheffel

Final Project for DS 5100 Fall 2022 - Monte Carlo Simulator

**Install**:

Use the following code: 

pip install -e

**Import**:

Use the following code:

import numpy as np

import pandas as pd


from montecarlo import Die

from montecarlo import Game

from montecarlo import Analyzer


**Create dice objects**:

newdie = Die(np.array([1,2,3,4]))

newdie.change_weight(1, 5.)

newdie.roll_die(5)

newdie.show_current_fw()


**Play game**:

newgame = Game([newdie, newdie, newdie])

newgame.play(20)

newgame.recent_results('Wide')


**Analyse game**:

newanalyzer = Analyzer(newgame)

newanalyzer.jackpot()

newanalyzer.combo()

newanalyzer.face_counts_per_roll()


**Descriptions**:


