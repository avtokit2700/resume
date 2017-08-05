import unittest2

"""
runTest("Highest straight flush wins",        "Loss", "2H 3H 4H 5H 6H", "KS AS TS QS JS")
runTest("Straight flush wins of 4 of a kind", "Win",  "2H 3H 4H 5H 6H", "AS AD AC AH JD")
runTest("Highest 4 of a kind wins",           "Win",  "AS AH 2H AD AC", "JS JD JC JH 3D")
runTest("4 Of a kind wins of full house",     "Loss", "2S AH 2H AS AC", "JS JD JC JH AD")
runTest("Full house wins of flush",           "Win",  "2S AH 2H AS AC", "2H 3H 5H 6H 7H")
runTest("Highest flush wins",                 "Win",  "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H")
runTest("Flush wins of straight",             "Win",  "2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C")
runTest("Equal straight is tie", 	  	      "Tie",  "2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S")
runTest("Straight wins of three of a kind",   "Win",  "2S 3H 4H 5S 6C", "AH AC 5H 6H AS")
runTest("3 Of a kind wins of two pair",       "Loss", "2S 2H 4H 5S 4C", "AH AC 5H 6H AS")
runTest("2 Pair wins of pair",                "Win",  "2S 2H 4H 5S 4C", "AH AC 5H 6H 7S")
runTest("Highest pair wins",                  "Loss", "6S AD 7H 4S AS", "AH AC 5H 6H 7S")
runTest("Pair wins of nothing",               "Loss", "2S AH 4H 5S KC", "AH AC 5H 6H 7S")
runTest("Highest card loses",                 "Loss", "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S")
runTest("Highest card wins",                  "Win",  "4S 5H 6H TS AC", "3S 5H 6H TS AC")
runTest("Equal cards is tie",		          "Tie",  "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C")
"""

from poker import PokerHand


class TestPokerCompaire(unittest2.TestCase):
    def setUp(self):
        self.P = PokerHand('2S AH 4H 5S 6C')
        self.P1 = PokerHand("4S 5H 6H TS AC")
        self.P2 = PokerHand("2S 3H 6H 7S 9C")
        self.P3 = PokerHand("2S AH 4H 5S KC")
        pass

    def test_compare_with(self):

        self.assertEqual('Tie', self.P.compare_with('AD 4C 5H 6H 2C'))

        self.assertEqual('Win', self.P1.compare_with("3S 5H 6H TS AC"))

        self.assertEqual('Loss', self.P2.compare_with("7H 3C TH 6H 9S"))

        self.assertEqual('Loss', self.P3.compare_with("AH AC 5H 6H 7S"))

    def test_count_value(self):
        self.assertEqual(True, self.P.count_value(3, 'AAAQ3', 1))

if __name__ == '__main__':
    unittest2.main()