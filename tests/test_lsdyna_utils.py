import unittest
import os

from fem_utils import lsdyna_utils


class TestLsdynaUtils(unittest.TestCase):
    def setUp(self):
        self._model_dir = os.path.join(os.path.dirname(__file__), 'data', 'dyna(.k)')

    def get_model_path(self, fname):
        return os.path.join(self._model_dir, fname)

    def test_is_nastran_file_by_content(self):
        list_fileNname_isLsdyna = [
            ["quad_noK", True],
            ["quad.k", True]
        ]

        for file_name, is_lsdyna in list_fileNname_isLsdyna:
            self.assertEqual(
                lsdyna_utils.is_lsdyna_file_by_content(self.get_model_path(file_name)),
                is_lsdyna,
                msg='Check Error with file: %s' % file_name
            )

if __name__ == '__main__':
    unittest.main()