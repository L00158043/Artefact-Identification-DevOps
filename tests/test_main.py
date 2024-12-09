import unittest
from src.main import identify_artifact, return_artifact

class TestArtifactFunctions(unittest.TestCase):
    def test_identify_artifact(self):
        self.assertEqual(
            identify_artifact("Golden Idol"),
            "Artifact 'Golden Idol' identified successfully!"
        )

    def test_return_artifact(self):
        self.assertEqual(
            return_artifact("Ancient Temple"),
            "Artifact returned to Ancient Temple!"
        )

if __name__ == "__main__":
    unittest.main()
