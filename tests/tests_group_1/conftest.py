import pytest


@pytest.fixture(scope="package", autouse=True)
def package_1_setup(request):
    print("Package 1 setup started")

    def package_1_teardown():
        print("Package 1 teardown started")

    request.addfinalizer(finalizer=package_1_teardown)
