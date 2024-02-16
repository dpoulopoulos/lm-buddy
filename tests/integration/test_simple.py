import ray

from lm_buddy.jobs._entrypoints.simple import get_magic_number
from lm_buddy.jobs.configs import SimpleJobConfig


def test_simple_remote_task():
    config = SimpleJobConfig(magic_number=42)
    result = ray.get(get_magic_number.remote(config))
    assert result == 42
