from xdist.scheduler import LoadScheduling
from xdist.workermanage import WorkerController


worker_to_udid = {
            "gw0":"android_udid" ,
            "gw1" : "ios_udid"
        }





class CustomScheduler(LoadScheduling):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
    def _send_tests(self, node:WorkerController, num:int)-> None:
        tests_per_node=[]
        remaining_pending = []
        for index in self.pending:
            test_name = self.collection[index]
            assigned_worker = None
            for worker_id,udid in worker_to_udid.items():
                if udid in test_name:
                    assigned_worker = worker_id
                    break
        
            if assigned_worker==node.workerinfo["id"]:
                tests_per_node.append(index)
            else:
                remaining_pending.append(index)

        self.pending = remaining_pending

        if tests_per_node:
            self.node2pending[node].extend(tests_per_node)
            node.send_runtest_some(tests_per_node)

