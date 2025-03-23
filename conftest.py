from app.models.xdist_scheduler import CustomScheduler


def pytest_configure(config):
    print("test conftest.py")

def pytest_xdist_make_scheduler(config, log):
    print("test pytest_xdist_make_scheduler")
    return CustomScheduler(config, log)