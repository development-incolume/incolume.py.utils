import pytest


def sum(a, b):
    return a + b


class TestCase0:
    @pytest.fixture
    def input_dict(self):
        return {"a": 1}

    def test_fixture(self, input_dict):
        assert input_dict["a"] == 1, f"Check fixture {input_dict}"


class TestCaseExamples:
    """Test Case Examples."""

    def test_mock_builtins(self, mocker):
        mocker.patch("__main__.ord", return_value=67)
        print(ord("c"))

    def test_sum1(self, mocker):
        mocker.patch(__name__ + ".sum", return_value=9)
        assert sum(2, 3) == 9

    def test_sum2(self, mocker):
        def crazy_sum(a, b):
            return b + b

        mocker.patch(__name__ + ".sum", side_effect=crazy_sum)
        assert sum(2, 3) == 6
