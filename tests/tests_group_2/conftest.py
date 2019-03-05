import pytest


@pytest.fixture(scope="package", autouse=True)
def package_2_setup():  # request):
    print("\n")
    print("Package 2 setup started")
    yield
    print("\n")
    print("Package 2 teardown started")

    # def package_2_teardown():
    #     print("\n")
    #     print("Package 2 teardown started")
    #
    # request.addfinalizer(package_2_teardown)
