from datetime import datetime
import uuid
import time
from transitions import Machine


class RobotConstructionActionNode(object):
    def __init__(self, node_name):
        self.ts_finish = None
        self.ts_start = None
        self.id = uuid.uuid4()
        self.name = node_name
        self.states = [
            {'name': 'not working', 'on_exit': 'start_time'},
            {'name': 'working', 'on_exit': 'finish_time'},
            {'name': 'executed'},
        ]
        self.transitions = [
            {'trigger': 'start_execution', 'source': 'not working', 'dest': 'working'},
            {'trigger': 'finish_execution', 'source': 'working', 'dest': 'executed'},
        ]
        self.state_machine = Machine(model=self, states=self.states, transitions=self.transitions,
                                     initial='not working', ignore_invalid_triggers=True)

    def start_time(self):
        # Getting the current date and time
        dt_start = datetime.now()

        # getting the timestamp
        self.ts_start = datetime.timestamp(dt_start)

        print('The task: {} start working'.format(self.name))
        print('The start time is:', dt_start)

        return self.ts_start

    def finish_time(self):
        # Getting the current date and time
        dt_finish = datetime.now()

        # getting the timestamp
        self.ts_finish = datetime.timestamp(dt_finish)

        print('The task: {} is executed'.format(self.name))
        print('The finish time is:', dt_finish)

        return self.ts_finish

    def execution_duration(self):
        return self.ts_finish - self.ts_start


if __name__ == '__main__':
    oneNode = RobotConstructionActionNode('move_action')
    print(oneNode.state)
    oneNode.start_execution()
    print(oneNode.state)
    time.sleep(2)
    oneNode.finish_execution()
    print(oneNode.state)
    print(oneNode.execution_duration())

