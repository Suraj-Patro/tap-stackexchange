"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_standard_tap_tests

from tap_stackexchange.tap import TapStackExchange

SAMPLE_CONFIG = {
    "site": "stackoverflow",
    "tags": [
        "meltano",
        "singer-io",
    ],
    "metrics_log_level": "debug",
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapStackExchange, config=SAMPLE_CONFIG)
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
