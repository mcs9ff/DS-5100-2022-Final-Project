import pandas as pd
import numpy as np
import random
import itertools

class Die:
    '''
    Creates a die that has N sides, or “faces”, and W weights, and which can be rolled to select a face.

    W defaults to 1.0 for each face but can be changed after the object is created.
    The die has one behavior, which is to be rolled one or more times. 
    '''
    die_one = 0
    weights = []
    
    def __init__(self, array_faces):
        '''
        Initializes the class Die.
        
        Takes an array of faces as an argument.
        The array's data type (dtype) may be strings or numbers.
        The faces must be unique; no duplicates.
        Internally initializes the weights to 1.0 for each face.
        Saves faces and weights in a private dataframe that is to be shared by the other methods.
        '''
        self.array_faces = array_faces.tolist()
        self.weights = np.ones(len(self.array_faces))
        #np.ones returns array filled with ones
        
        self.die_one = pd.DataFrame({'Faces':self.array_faces,
                                   'Weights':self.weights.tolist()})
        
    def change_die_weight(self, face_val, new_weight):
        '''
        Changes the weight of a single side of the die.
        
        Takes two arguments: the face value to be changed and the new weight.
        Checks to see if the face is valid.
        Checks to see if the weight is valid.
        '''
        if face_val not in self.die_one.values:
            print("Die does not contain that value. Please try another value.")
            return
        elif face_val in self.die_one.values:
            try:
                float(new_weight)
            except ValueError:
                print("Weight values need to be able to convert to Float.")
                return
        
        self.die_one.loc[self.die_one['Faces'] == face_val, 'Weights'] = new_weight
    
    def roll_die(self, roll_count=1):
        '''
        Rolls the die one or more times.
        
        Takes a parameter of how many times the die is to be rolled; defaults to 1.
        This is essentially a random sample from the vector of faces according to the weights.
        Returns a list of outcomes.
        Does not store results internally.
        '''
        
        type(roll_count) == int

        outcomes = []

        while roll_count > 0:
            
            weight = self.die_one['Weights']
            face = self.die_one['Faces']
            odds = [i/sum(weight) for i in weight]
            outcomes = [random.choices(face, odds) for i in range(roll_count)]
            outcomes = [i[0] for i in outcomes]
            return outcomes

    def show_current_fw(self):
        '''
        Shows the user the die’s current set of faces and weights (since the latter can be changed).
        
        Returns the dataframe created in the initializer but possibly updated by the weight changing method.
        '''
        return self.die_one
    
class Game:
    '''
    Creates a game that consists of rolling of one or more dice of the same kind one or more times.

    Each game is initialized with a list of one or more of similarly defined dice (Die objects).
    By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and set of faces, 
    but each die object may have its own weights.
    The class has a behavior to play a game, i.e. to roll all of the dice a given number of times.
    The class keeps the results of its most recent play.
    '''
    game_one = []

    def __init__(self, similar_die):
        '''
        Initializes the class Game.
        
        Takes a single parameter, a list of already instantiated similar Die objects.
        '''
        self.similar_die = similar_die
        
    def play(self, rolls):
        '''
        Takes a parameter to specify how many times the dice should be rolled.
        
        Saves the result of the play to a private dataframe of shape N rolls by M dice. 
        Each cell should show the resulting face for the die on the roll. 
        '''
        
        for i in self.similar_die:
        
            type(rolls) == int
        
            die_play = [Die.roll_die(self.similar_die[i], rolls)
                            for i in range(len(self.similar_die))]
            self.game_one = pd.DataFrame(die_play)
            #change index name?
        
    def recent_results(self, format_w_n = 'Wide'):
        '''
        Shows the user the results of the most recent play.
        
        Takes a parameter to return the dataframe in narrow or wide form.
        This parameter raises an exception if the user passes an invalid option.
        '''
        if (format_w_n != 'Wide') & (format_w_n != 'Narrow'):
            raise Exception('Format must be wide or narrow.')
        else:
            if format_w_n == 'Wide':
                return self.game_one
            if format_w_n == 'Narrow':
                return self.game_one.stack()

class Analyzer:
    '''
    An analyzer that takes the results of a single game and computes various descriptive statistical properties about it.
    '''
    resultsDF = pd.DataFrame([])
    countDF = pd.DataFrame([])
    jackpotDF = pd.DataFrame([])
    comboDF = pd.DataFrame([])
    
    def __init__(self, game_object):
        '''
        Initializes the class Analyzer.
        
        Takes a game object as its input parameter.
        At initialization time, it also infers the data type of the die faces used.
        '''
        self.game_object = game_object
        self.resultsDF = self.game_object.recent_results()
        
    def face_counts_per_roll(self):
        '''
        A face counts per roll method to compute how many times a given face is rolled in each event.
        
        Stores the results as a dataframe in a public attribute.
        '''
        countDF = pd.DataFrame([])
        countDF = self.resultsDF.T.apply(pd.Series.value_counts, axis=1).fillna(0)
        return countDF
        
    def jackpot(self):
        '''
        A jackpot method to compute how many times the game resulted in all faces being identical.
        
        Returns an integer for the number times to the user.
        Stores the results as a dataframe of jackpot results in a public attribute.
        '''
        
        jackpot_times = 0
        for i in range(0,len(self.resultsDF.columns)):
            col_list = self.resultsDF[i].tolist()
        
            True_False = False
            element = col_list[0]
            for j in range(len(col_list)):
                if element == col_list[j]:
                    True_False = True
                    j += 1
                    
                else:
                    True_False = False
                    j += 1
                    break
            
            if True_False == True:
                jackpot_times += 1
                col_list.insert(0, i)
                self.jackpotDF = pd.concat([self.jackpotDF, pd.DataFrame(col_list).T])
                
            i += 1

        self.jackpotDF = self.jackpotDF.set_index(0, drop=True)
        self.jackpotDF.index.name = 'Roll Number'
        display(self.jackpotDF)
        return jackpot_times
        
    def combo(self):
        '''
        A combo method to compute the distinct combinations of faces rolled, along with their counts.

        Combinations are sorted and saved as a multi-columned index.
        Stores the results as a dataframe in a public attribute.
        '''
        results_transposed = self.resultsDF.T
        comboDF = results_transposed.apply(lambda x: pd.Series
                                          (sorted(x)), 1).value_counts().to_frame('n')
        return comboDF