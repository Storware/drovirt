import logging

logger = logging.getLogger(__name__)
from drovirt.models.tasks import TaskStatus

class BaseTask:
    def __init__(self, task):
        self.task = task
        self.task_id = task.get('id', None)
        if not self.task_id:
            raise Exception("Received task without id")
        self.result = {}
        self.status = TaskStatus.ACTIVE

    def start(self):
        logger.info("%s started" % repr(self))

    def finish(self):
        logger.info("%s finished" % repr(self))
        self.status = TaskStatus.COMPLETED

    def main(self):
        import time
        time.sleep(5)

    def run(self):
        self.start()
        self.main()
        self.finish()

    def __repr__(self):
        return "Task {task_id} ({task_class})".format(task_id=self.task_id,
                                        task_class=self.__class__.__name__)