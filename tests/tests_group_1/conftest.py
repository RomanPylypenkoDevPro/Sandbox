import pytest


@pytest.fixture(scope="package", autouse=True)
def package_1_setup():  # request):
    print("\n")
    print("Package 1 setup started")
    yield
    print("\n")
    print("Package 1 teardown started")

    # def package_1_teardown():
    #     print("\n")
    #     print("Package 1 teardown started")
    #
    # request.addfinalizer(package_1_teardown)
