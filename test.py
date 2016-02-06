# Author: Mirko Pizii
# Email: info@mirkopizii.com
# Website: www.mirkopizii.com
# License: WTFPL
import unittest
import farfallino


class TestCorrectTranslation(unittest.TestCase):
    def test_lowerVovelToFarfallino(self):
        self.assertEqual(farfallino.farfallino_transform('a'), 'afa')
        self.assertEqual(farfallino.farfallino_transform('e'), 'efe')
        self.assertEqual(farfallino.farfallino_transform('i'), 'ifi')
        self.assertEqual(farfallino.farfallino_transform('o'), 'ofo')
        self.assertEqual(farfallino.farfallino_transform('u'), 'ufu')
        self.assertEqual(farfallino.farfallino_transform('y'), 'yfy')

    def test_upperVovelToFarfallino(self):
        self.assertEqual(farfallino.farfallino_transform('A'), 'AfA')
        self.assertEqual(farfallino.farfallino_transform('E'), 'EfE')
        self.assertEqual(farfallino.farfallino_transform('I'), 'IfI')
        self.assertEqual(farfallino.farfallino_transform('O'), 'OfO')
        self.assertEqual(farfallino.farfallino_transform('U'), 'UfU')
        self.assertEqual(farfallino.farfallino_transform('Y'), 'YfY')

    def test_wordToFarfallino(self):
        self.assertEqual(farfallino.farfallino_transform('casa'), 'cafasafa')
        self.assertEqual(farfallino.farfallino_transform('lago'), 'lafagofo')
        self.assertEqual(farfallino.farfallino_transform('stella'), 'stefellafa')
        self.assertEqual(farfallino.farfallino_transform('re'), 'refe')
        self.assertEqual(farfallino.farfallino_transform('cercare'), 'cefercafarefe')

    def test_phraseToFarfallino(self):
        self.assertEqual(farfallino.farfallino_transform('Questo è un esempio'), 'Qufuefestofo è ufun efesefempifiofo')
        self.assertEqual(farfallino.farfallino_transform('Hello, my name is Bobby!'), 'Hefellofo, myfy nafamefe ifis Bofobbyfy!')


if __name__ == '__main__':
    unittest.main()
