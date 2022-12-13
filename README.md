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


class Die:
    
    '''
    Creates a die that has N sides, or “faces”, and W weights, and which can be rolled to select a face.

    W defaults to 1.0 for each face but can be changed after the object is created.
    The die has one behavior, which is to be rolled one or more times. 
    '''
    
    Parameters: 
    
    array_faces: array of the die faces (integer or str)
    
    face_val: value of a die face (integer or float or str)
    
    new_weight: new weight vale for die (float)
    
    roll_count: count of tiems die is rolled (integer)
    
    
    Return values:
    
    outcomes: list of outcomes from rolling the die
    
    def __init__(self, array_faces):
        '''
        Initializes the class Die.
        
        Takes an array of faces as an argument.
        The array's data type (dtype) may be strings or numbers.
        The faces must be unique; no duplicates.
        Internally initializes the weights to 1.0 for each face.
        Saves faces and weights in a private dataframe that is to be shared by the other methods.
        '''
        
    Parameters: array_faces
    
    Return values: None.
    
    def change_die_weight(self, face_val, new_weight):
        '''
        Changes the weight of a single side of the die.
        
        Takes two arguments: the face value to be changed and the new weight.
        Checks to see if the face is valid.
        Checks to see if the weight is valid.
        '''
        
    Parameters: face_val, new_weight
    
    Return values: None.
    
    def roll_die(self, roll_count=1):
        '''
        Rolls the die one or more times.
        
        Takes a parameter of how many times the die is to be rolled; defaults to 1.
        This is essentially a random sample from the vector of faces according to the weights.
        Returns a list of outcomes.
        Does not store results internally.
        '''
        
    Parameters: roll_count
    
    Return values: outcomes
    
    def show_current_fw(self):
        '''
        Shows the user the die’s current set of faces and weights (since the latter can be changed).
        
        Returns the dataframe created in the initializer but possibly updated by the weight changing method.
        '''
        
    Parameters: None.
    
    Return values: self.die_one (a dataframe with current sets of faces and wieghts)

class Game:
    '''
    Creates a game that consists of rolling of one or more dice of the same kind one or more times.

    Each game is initialized with a list of one or more of similarly defined dice (Die objects).
    By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and set of faces, 
    but each die object may have its own weights.
    The class has a behavior to play a game, i.e. to roll all of the dice a given number of times.
    The class keeps the results of its most recent play.
    '''
    
    Parameters: 
    
    similar_die: list of already instantiated similar die objects 
    
    rolls: specifies how many times the die should be rolled (integer)
    
    format_w_n: determines if dataframe is retunred in wide or narrow form
    
    Return values:
    
    self.game_one: retruns the results of the most recent game (dataframe)
    
    def __init__(self, similar_die):
        '''
        Initializes the class Game.
        
        Takes a single parameter, a list of already instantiated similar Die objects.
        '''
        
    Parameters: similar_die
    
    Return values: None.
    
    def play(self, rolls):
        '''
        Takes a parameter to specify how many times the dice should be rolled.
        
        Saves the result of the play to a private dataframe of shape N rolls by M dice. 
        Each cell should show the resulting face for the die on the roll. 
        '''
        
    Parameters: rolls
    
    Return values: None.
    
    def recent_results(self, format_w_n = 'Wide'):
        '''
        Shows the user the results of the most recent play.
        
        Takes a parameter to return the dataframe in narrow or wide form.
        This parameter raises an exception if the user passes an invalid option.
        '''
        
    Parameters: format_w_n
    
    Return values: self.game_one
    
class Analyzer:
    '''
    An analyzer that takes the results of a single game and computes various descriptive statistical properties about it.
    '''
    
    Parameters: 
    
    game_object: object from Game class is the input
    
    Return values:
    
    resultsDF: stores the results of a Game (dataframe)
    
    countDF: stores the results of the counts function
    
    jackpotDF: stores the results of the jackpot function during a game
    
    jackpot_times: returns the number of times a jackpot is rolled (int)
    
    comboDF: stores the results of the combos function during a game
    
    def __init__(self, game_object):
        '''
        Initializes the class Analyzer.
        
        Takes a game object as its input parameter.
        At initialization time, it also infers the data type of the die faces used.
        '''
        
    Parameters: game_object
    
    Return values: resultsDF
    
    def face_counts_per_roll(self):
        '''
        A face counts per roll method to compute how many times a given face is rolled in each event.
        
        Stores the results as a dataframe in a public attribute.
        '''
        
    Parameters: None.
    
    Return values: countDF
    
    def jackpot(self):
        '''
        A jackpot method to compute how many times the game resulted in all faces being identical.
        
        Returns an integer for the number times to the user.
        Stores the results as a dataframe of jackpot results in a public attribute.
        '''
        
    Parameters: None.
    
    Return values: jackpotDF, jackpot_times
    
    def combo(self):
        '''
        A combo method to compute the distinct combinations of faces rolled, along with their counts.

        Combinations are sorted and saved as a multi-columned index.
        Stores the results as a dataframe in a public attribute.
        '''
        
    Parameters: None.
    
    Return values: comboDF
