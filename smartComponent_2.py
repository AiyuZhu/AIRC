import uuid
from transitions import Machine
from robotConstructionActions import robotConstructionActionNode as rcan


class SmartComponentStates(object):
    def __init__(self, states):
        self.id = uuid.uuid4()
        self.success = False
        self.state_machine = Machine(model=self, states=states, initial=states[0]['name'],
                                     ignore_invalid_triggers=True)
        self.state_machine.add_ordered_transitions()

    def is_execution_success(self, execute_result):
        if execute_result == 'executed':
            self.success = True
        print('The execute result is', self.success)
        return self.success

    def reset_success(self):
        self.success = False


class SmartComponent(object):
    def __init__(self, component_guid, states, activities):
        self.guid = component_guid
        self.states = states
        self.activities = activities
        self.component_stateMachine = SmartComponentStates(self.states)
        self.current_state = self.component_stateMachine.state

    def start_construction(self):
        while self.current_state != 'constructed':
            for activity in self.activities:
                while self.component_stateMachine.success is False:
                    activity_state = rcan.RobotConstructionActionNode(self.guid, activity)
                    self.component_stateMachine.is_execution_success(activity_state.execute_state_only())
                self.component_stateMachine.next_state()
                self.current_state = self.component_stateMachine.state
                self.component_stateMachine.reset_success()
                print('\n')


if __name__ == '__main__':
    states_test = [
        {'name': 'need construction'},
        {'name': 'need positioning for picking up'},
        {'name': 'need pick up'},
        {'name': 'need transfer to target'},
        {'name': 'need positioning for assembling'},
        {'name': 'need assembly'},
        {'name': 'constructed'},
    ]
    transitions = [
        'move_to_component',
        'positioning_for_pickup',
        'pickup',
        'transfer',
        'positioning_for_assembly',
        'assembly',
    ]


    # smartComponent = SmartComponentStates(states_test)
    #
    # while smartComponent.state != 'constructed':
    #     for i in transitions:
    #         while smartComponent.success is False:
    #             # need package
    #             comp_state = rcan.RobotConstructionActionNode('hjghjgkgk', i)
    #             smartComponent.is_execution_success(comp_state.execute_state_only())
    #         smartComponent.next_state()
    #         smartComponent.reset_success()
    #         print(smartComponent.state)
    #         print('\n')

    component_list = {'fdsafasdfdfadf213': 'need construction'}

    comp_1 = SmartComponent('267VPu8ab9991QBA3MI1qr', states_test, transitions)
    comp_1.start_construction()
    print(comp_1.current_state)
