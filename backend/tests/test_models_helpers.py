import mock
import unittest
from app.models_helpers import create_fake_info


class MyTestCase(unittest.TestCase):

    @mock.patch('app.models_helpers')
    def test_random_data_generation(self, mock_db):
        # Make it so that this doesn't use or import the real database
        mock_db.return_value = {}

        fake_info_length = 5
        result = create_fake_info(fake_info_length)
        self.assertEqual(len(result), fake_info_length)
        for fake_info in result:
            self.assertIsNotNone(fake_info.id)
            self.assertIsNotNone(fake_info.username)
            self.assertIsNotNone(fake_info.date)
            self.assertIsNotNone(fake_info.language)
            self.assertIsNotNone(fake_info.stars)
            self.assertIsNotNone(fake_info.number_of_repositories)

        # TODO Here make sure that the DB mock was called fake_info_length times with proper arguments
        mock_db.remove.assert_called_with("any path")


if __name__ == '__main__':
    unittest.main()
