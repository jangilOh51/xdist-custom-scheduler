import pytest
from app.models.xdist_scheduler import worker_to_udid



class TestXdist:
    @pytest.fixture(autouse=True, scope="session", params=["android_udid", "ios_udid"])
    def setup(self):
        pass


    def test_xdist_001(self, request):
        worker_id = request.config.workerinput.get('workerid', 'master')
        udid = worker_to_udid[worker_id]
        test_name = request.node.name
        print(f"udid: {udid}, test_name: {test_name}")
        assert udid in test_name
        

    def test_xdist_002(self, request):
        worker_id = request.config.workerinput.get('workerid', 'master')
        udid = worker_to_udid[worker_id]
        test_name = request.node.name
        print(f"udid: {udid}, test_name: {test_name}")
        assert udid in test_name
        

    def test_xdist_003(self, request):
        worker_id = request.config.workerinput.get('workerid', 'master')
        udid = worker_to_udid[worker_id]
        test_name = request.node.name
        print(f"udid: {udid}, test_name: {test_name}")
        assert udid in test_name
    
    def test_xdist_004(self, request):
        worker_id = request.config.workerinput.get('workerid', 'master')
        udid = worker_to_udid[worker_id]
        test_name = request.node.name
        print(f"udid: {udid}, test_name: {test_name}")
        assert udid in test_name
    