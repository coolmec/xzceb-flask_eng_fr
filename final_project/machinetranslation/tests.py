import unittest
from mytranslator import english_to_french, french_to_english

class TestMyTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Good morning"), "Bonsoir")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonsoir"), "Good night")

if __name__ == "__main__":
    unittest.main()