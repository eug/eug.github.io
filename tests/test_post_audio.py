import tempfile
import unittest
from pathlib import Path

from main import find_post_audio


class FindPostAudioTests(unittest.TestCase):
    def test_returns_matching_mp3_filename(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            posts_dir = Path(temporary_directory)
            (posts_dir / "20260823-engineerification.mp3").touch()

            result = find_post_audio(
                "20260823-engineerification.md",
                posts_dir=str(posts_dir),
            )

            self.assertEqual(result, "20260823-engineerification.mp3")

    def test_returns_none_without_matching_mp3(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            result = find_post_audio(
                "20260823-engineerification.md",
                posts_dir=temporary_directory,
            )

            self.assertIsNone(result)

    def test_ignores_non_markdown_files(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            posts_dir = Path(temporary_directory)
            (posts_dir / "engineerification.mp3").touch()

            result = find_post_audio(
                "engineerification.txt",
                posts_dir=str(posts_dir),
            )

            self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
