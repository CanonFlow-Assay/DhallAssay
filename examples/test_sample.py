from pathlib import Path
import subprocess
import unittest


class Service(unittest.TestCase):
    def assert_workers(self, expected, exit_code):
        source = Path("service.dhall").read_text()
        assertion = f"let service = ({source}) in assert : service.workers === {expected}\n"
        result = subprocess.run(
            ["dhall", "--plain", "--censor", "normalize"], input=assertion, text=True,
            capture_output=True, timeout=5,
        )
        self.assertEqual(result.returncode, exit_code, result.stderr)

    def test_two_workers_are_required(self):
        self.assert_workers(2, 0)

    def test_a_changed_worker_count_is_rejected(self):
        self.assert_workers(3, 1)


if __name__ == "__main__":
    unittest.main()
