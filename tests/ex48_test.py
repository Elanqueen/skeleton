#coding=utf-8
import unittest
from NAME.ex48 import Lexicon

class TestLexicon(unittest.TestCase):
    def setUp(self):
        print("start!")


    def tearDown(self):
        print("teardown!")

    def test_directions(self):
        lexicon = Lexicon()
        self.assertEqual(lexicon.scan("north"),[('direction','north')])
        result = lexicon.scan("north south east")
        self.assertEqual(result,[('direction','north'),
                                 ('direction','south'),
                                 ('direction','east')])

    def test_verbs(self):
        lexicon = Lexicon()
        self.assertEqual(lexicon.scan("go"),[('verb','go')])
        result = lexicon.scan("go kill eat")
        self.assertEqual(result,[('verb','go'),
                                 ('verb','kill'),
                                 ('verb','eat')])

    def test_stops(self):
        lexicon = Lexicon()
        self.assertEqual(lexicon.scan("the"),[('stop','the')])
        result = lexicon.scan("the in of")
        self.assertEqual(result,[('stop','the'),
                                 ('stop','in'),
                                 ('stop','of')])

    def test_numbers(self):
        lexicon = Lexicon()
        self.assertEqual(lexicon.scan("1234"),[('number',1234)])
        result = lexicon.scan("3 91234")
        self.assertEqual(result,[('number',3),
                                 ('number',91234)])

    def test_errors(self):
        lexicon = Lexicon()
        self.assertEqual(lexicon.scan("ASDFAFASDF"),[('error','ASDFAFASDF')])
        result = lexicon.scan("bear IAS princess")
        self.assertEqual(result,[('noun','bear'),
                                 ('error','IAS'),
                                 ('noun','princess')])

if __name__ == '__main__':
    unittest.main()