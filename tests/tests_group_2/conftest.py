import pytest


@pytest.fixture(scope="package", autouse=True)
def package_2_setup(request):
    print("Package 2 setup started")

    def package_2_teardown():
        print("Package 2 teardown started")

    request.addfinalizer(finalizer=package_2_teardown)
