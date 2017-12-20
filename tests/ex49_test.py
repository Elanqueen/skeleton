#coding=utf-8
import unittest
import NAME.ex49

class TestParseSentence(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print("down")

    def test_peek(self):
        self.assertEqual(NAME.ex49.peek([("direction","north")]),"direction")
        self.assertEqual(NAME.ex49.peek([]),None)

    def test_match(self):
        self.assertEqual(NAME.ex49.match([("direction","north")],"direction"),("direction","north"))
        self.assertEqual(NAME.ex49.match([("direction","north")],"verb"),None)
        self.assertEqual(NAME.ex49.match([],"south"),None)

    def test_skip(self):
        self.assertEqual(NAME.ex49.skip([("direction","north")],"stop"),None)
        self.assertEqual(NAME.ex49.skip([("stop","the"),("direction", "north")], "stop"), None)

    def test_parse_verb(self):
        self.assertEqual(NAME.ex49.parse_verb([("verb","go")]),("verb","go"))
        with self.assertRaises(NAME.ex49.ParserError):
            NAME.ex49.parse_verb([("noun","bear")])

    def test_parse_object(self):
        self.assertEqual(NAME.ex49.parse_object([("direction","north")]), ("direction","north"))
        self.assertEqual(NAME.ex49.parse_object([("noun","door"),("direction", "north")]), ("noun","door"))
        with self.assertRaises(NAME.ex49.ParserError):
            NAME.ex49.parse_object([("verb", "go")])

        self.assertRaises(NAME.ex49.ParserError,NAME.ex49.parse_object,[("verb", "go")])

    def test_parse_subject(self):
        sentence = NAME.ex49.Sentence(("noun","bear"),("verb","go"),("direction","north"))
        self.assertEqual(NAME.ex49.parse_subject([("verb","go"),("direction","north")],("noun","bear")).object,
                         sentence.object)

    def test_parse_sentence(self):
        sentence = NAME.ex49.Sentence(("noun","bear"),("verb","go"), ("noun", "north"))
        self.assertEqual(NAME.ex49.parse_sentence([("noun","bear"),("verb","go"),
                                                   ("stop","the"),("noun", "north")]).object,sentence.object)
        sentence = NAME.ex49.Sentence(("noun", "player"),("verb", "go"),("noun","door"))
        self.assertEqual(NAME.ex49.parse_sentence([("verb", "go"),("stop","the"),("noun","door")]).object, sentence.object)

if __name__=="__main__":
    unittest.main()