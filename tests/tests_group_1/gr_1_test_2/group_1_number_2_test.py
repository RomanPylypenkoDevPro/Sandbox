import pytest


class TestGroup1Number2:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        print("\n")
        print("Setup class group 1 test 2")

    def test_assertion_1(self):
        print("group 1 test 2 assert 1")

    def test_assertion_2(self):
        print("group 1 test 2 assert 2")

    def teardown_class(self):
        print("Teardown class group 1 test 2")
