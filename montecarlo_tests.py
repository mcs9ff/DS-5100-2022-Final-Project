import unittest

class MonteCarloTests(unittest.TestCase):
    '''
    Tests Die, Game, and Analyzer classes.
    
    '''
    
    def test_change_die_weight(self):
        '''
        Tests the method change_weight() in Die class.
       
        '''
        test = Die(np.array([1, 2, 3]))
        test.change_die_weight(3, 4)
        actual = test.show_current_fw().to_dict()
        placeholder = pd.DataFrame({'Faces':[1, 2, 3], 'Weights':[1., 1., 4.]})
        expected = placeholder.to_dict()
        self.assertEqual(actual, expected)

    def test_roll_die(self):
        '''
        Tests the method roll_die() in Die class.
        
        '''
        test = Die(np.array([1, 2, 3]))
        results = test.roll_die(5)
        actual = len(results)
        expected = 5
        self.assertEqual(actual, expected)
        
    def test_show_current_fw(self):
        '''
        Tests the method show_faces_and_weights() in Die class.
       
        '''
        test = Die(np.array([1, 2, 3]))
        actual = test.show_current_fw()
        expected = pd.DataFrame({'Faces':[1, 2, 3], 'Weights':[1., 1., 1.]})
        self.assertEqual(actual.to_dict(), expected.to_dict())
        
    def test_play(self):
        '''
        Tests the method play() in Game class.
        
        '''
        test = Die(np.array([1, 2, 3]))
        test2 = Die(np.array([1, 2, 3]))
        test3 = Die(np.array([1, 2, 3]))
        result = Game([test, test2, test3])
        result.play(2)
        x = result.recent_results()
        actual = len(x)
        expected = 3
        self.assertEqual(actual, expected)
        
    def test_recent_results(self):
        '''
        Tests the method recent_results() in Game class.
        
        '''
        test = Die(np.array([1, 2, 3]))
        test2 = Die(np.array([1, 2, 3]))
        test3 = Die(np.array([1, 2, 3]))
        result = Game([test, test2, test3])
        result.play(2)
        x = result.recent_results('Narrow')
        actual = len(x)
        expected = 6
        self.assertEqual(actual, expected)
        
    def test_face_counts_per_roll(self):
        '''
        Tests the method face_counts_per_roll() in Analyzer class.
        
        '''
        number = True
        message = "Test value is not false"
        test = Die(np.array([1, 2, 3]))
        test2 = Die(np.array([1, 2, 3]))
        test3 = Die(np.array([1, 2, 3]))
        result = Game([test, test2, test3])
        result.play(20)
        analyzer1 = Analyzer(result)
        df = analyzer1.face_counts_per_roll()
        if len(df.columns) < len(df):
            number = False
        self.assertFalse(number, message)
    
    def test_jackpot(self):
        '''
        Tests the method jackpot() in Analyzer class.
        
        '''
        test = Die(np.array([1, 2, 3]))
        test2 = Die(np.array([1, 2, 3]))
        test3 = Die(np.array([1, 2, 3]))
        result = Game([test, test2, test3])
        result.play(20)
        analyzer = Analyzer(result)
        analyzer.jackpot()
        df = analyzer.jackpotDF
        actual = len(df.columns)
        expected = 3
        self.assertEqual(actual, expected)
        
    def test_combo(self):
        '''
        Tests the method combo() in Analyzer class.
        
        '''
        number = True
        message = "Test value is not false"
        test = Die(np.array([1, 2, 3]))
        test2 = Die(np.array([1, 2, 3]))
        test3 = Die(np.array([1, 2, 3]))
        result = Game([test, test2, test3])
        result.play(20)
        analyzer = Analyzer(result)
        df = analyzer.combo()
        if len(df.columns) < len(df):
            number = False
        self.assertFalse(number, message)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)