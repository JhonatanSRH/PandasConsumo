import unittest
import main

class TestMyModule(unittest.TestCase):
    
    data = {
        'region': 'Asia',
        'name': 'Afghanistan',
        'languages': [
            {'iso639_1': 'ps', 'iso639_2': 'pus', 'name': 'Pashto', 'nativeName': 'پښتو'}, 
            {'iso639_1': 'uz', 'iso639_2': 'uzb', 'name': 'Uzbek', 'nativeName': 'Oʻzbek'}, 
            {'iso639_1': 'tk', 'iso639_2': 'tuk', 'name': 'Turkmen', 'nativeName': 'Türkmen'}
        ]
    }
    
    def test_encode(self):
        self.assertIsInstance(main.encode_lang(str([language['name'] for language in self.data['languages']])), str)
        
    def test_make(self):
        self.assertEqual(main.make_row(self.data), {'region':'Asia','country_name':'Afghanistan', 'language': '22affb95d075ac04514eafffc275ec38529fe456'})
        
if __name__ == "__main__":
    unittest.main()