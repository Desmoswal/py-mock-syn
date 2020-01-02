from unittest.mock import Mock
import unittest


class TestRepoMock(unittest.TestCase):

    def test_mock_ReturnsExpectedValue(self):
        mock = Mock()
        mock.Model.get.return_value = "itsworking"
        self.assertEqual(mock.Model.get(), 'itsworking')


if __name__ == '__main__':
    unittest.main()