import pytest


# @pytest.mark.usefixtures('global_setup')
class TestGroup2Number2:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        print("\n")
        print("Setup class group 2 test 2")

    def test_assertion_1(self):
        print("group 2 test 2 assert 1")

    def test_assertion_2(self):
        print("group 2 test 2 assert 2")

    def teardown_class(self):
        print("Teardown class group 2 test 2")
