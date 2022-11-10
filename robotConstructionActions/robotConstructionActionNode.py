from datetime import datetime
import uuid
import time
from transitions import Machine
from robotConstructionActions import execute_simulation as es


class RobotConstructionActionStates(object):
    def __init__(self, node_name):
        self.name = node_name
        self.success = False
        self.ts_finish = None
        self.ts_start = None
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


class RobotConstructionActionNode(object):
    def __init__(self, component_guid, node_name, activities, robots=None):
        self.id = uuid.uuid4()
        self.component_guid = component_guid
        self.node_name = node_name
        self.activities = activities
        if robots is None:
            self.robots = {'move_to_component': 'mobile_base',
                           'position_for_picking': 'manipulator',
                           'pick': 'gripper',
                           'transfer': 'mobile_base',
                           'position_for_installing': 'manipulator',
                           'install': 'gripper'}
        else:
            self.robots = robots

    def execute_state_only(self):
        comp_state = RobotConstructionActionStates(self.node_name)
        comp_state.start_execution()
        comp_state.finish_execution()
        return comp_state.state

    # position_set should query by component_id
    def execute_robot_simulation(self):
        comp_state = RobotConstructionActionStates(self.node_name)
        comp_state.start_execution()
        es.ExecuteAction(self.component_guid, self.robots).action_selector(self.node_name, self.activities)
        comp_state.finish_execution()
        return comp_state.state

    # position_set should query by component_id
    def execute_robot(self, position_set, exe_func):
        from robotConstructionActions import target_generator as tg
        target_generator = tg.target_pose_generator(self.component_guid, self.node_name, position_set)
        comp_state = RobotConstructionActionStates(self.node_name)
        action = exe_func
        comp_state.start_execution()
        if action.execute(target_generator.move_to_component()) == 'success':
            comp_state.finish_execution()
            return comp_state.state


if __name__ == '__main__':
    # oneNode = RobotConstructionActionStates('move_action')
    # print(oneNode.state)
    # oneNode.start_execution()
    # print(oneNode.state)
    # time.sleep(2)
    # oneNode.finish_execution()
    # print(oneNode.state)
    # print(oneNode.execution_duration())
    dict_transitions = {'move_to_component': [1, 2, 3],
                        'positioning_for_pickup': [2, 3, 4],
                        'pickup': [3, 4, 5],
                        'transfer': [4, 5, 6],
                        'positioning_for_assembly': [5, 6, 7],
                        'assembly': [7, 8, 9]}

    robot_namespaces = {'move_to_component': 'mobile_base',
                        'positioning_for_pickup': 'manipulator',
                        'pickup': 'gripper',
                        'transfer': 'mobile_base',
                        'positioning_for_assembly': 'manipulator',
                        'assembly': 'gripper'}

    rsan = RobotConstructionActionNode('ghjgjkgkh', 'move_to_component', dict_transitions)
    rsan.execute_robot_simulation()
