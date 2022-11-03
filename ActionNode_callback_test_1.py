from transitions import Machine, State
import uuid


class RobotConstructionActionNode(object):
    def __init__(self):
        self.id = uuid.uuid4()

    def execute_move_action(self):
        print("Moving to target")

    def execute_positioning_action(self):
        print("Doing positioning")

    def execute_pickup_action(self):
        print("Doing pick up work")

    def execute_assemble_action(self):
        print("Doing assembling work")

    def execution_finish(self):
        print("Execution finish!")


robotAction = RobotConstructionActionNode()

# Same states as above, but now we give StateA an exit callback
states = [
    State(name='need construction'),
    State(name='need positioning for picking up', on_enter=['position_pickup_point'], on_exit=['execution_finish']),
    State(name='need pick up'),
]

machine = Machine(robotAction, states=states, initial='need construction')
machine.add_transition('move_to_component', 'need construction', 'need positioning for picking up')
machine.add_transition('position_pickup', 'need positioning for picking up', 'need pick up')

# Callbacks can also be added after initialization using
# the dynamically added on_enter_ and on_exit_ methods.
# Note that the initial call to add the callback is made
# on the Machine and not on the model.
# machine.on_exit_need_construction('position_pickup_point')


if __name__ == '__main__':
    # Test out the callbacks...
    robotAction.move_to_component()
    robotAction.position_pickup()
    print(robotAction.state)
    # machine.set_state('need construction')
