import pytest


@pytest.fixture(scope="session", autouse=False)
def global_setup(request):
    print("\n")
    print("Super global setup started")

    def global_teardown():
        print("\n")
        print("Super global teardown started")

    request.addfinalizer(global_teardown)
