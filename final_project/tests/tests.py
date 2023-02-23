import machinetranslation.translator as tr
import unittest

class TestMain(unittest.TestCase):
    def test_eng_to_fr_test_check_equal(self):
        self.assertEqual("Bonjour", tr.english_to_french("Hello")['translation'])

    def test_eng_to_fr_test_check_notequal(self):
        self.assertNotEqual("Mister", tr.english_to_french("Hello")['translation'])

    def test_fr_to_eng_test_check_equal(self):
        self.assertEqual("Hello", tr.french_to_english("Bonjour")['translation'])

    def test_fr_to_eng_test_check_notequal(self):
        self.assertNotEqual("Mister", tr.french_to_english("Bonjour")['translation'])    
    
    if __name__ == '__main__':
        unittest.main()