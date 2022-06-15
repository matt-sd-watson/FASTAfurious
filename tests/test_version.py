import subprocess
import pytest
from fastafurious import __version__

def test_version_detection():
    results = subprocess.check_output(
        ['fastafurious', 'version'])
    assert "This is FASTAfurious: v{}".format(__version__) in results.decode('utf-8').splitlines()
    