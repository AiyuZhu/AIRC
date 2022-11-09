class ExecuteAction(object):
    def __init__(self, component_id, robot_namespace):
        self.comp_id = component_id
        self.robot = robot_namespace

    def execute_move(self, node_name, target_pose, robot_namespace):
        # start execution
        # subscribe move_base server
        print('Construction task for: ', self.comp_id)
        print('The execution robot is: ', robot_namespace)
        print('Current task is: ', node_name)
        print("Waiting for move_base action server...")
        # waiting for server connection
        print('Connected to move_base')
        # set target
        print("The goal is: ", target_pose)
        print("Going to: " + str(target_pose))
        # print result
        print("Arrived to target!")

    def positioning_action(self, node_name, target_pose, robot_namespace):
        # start execution
        # subscribe move_base server
        print('Construction task for: ', self.comp_id)
        print('The execution robot is: ', robot_namespace)
        print('Current task is: ', node_name)
        print("Waiting for moveit action server...")
        # waiting for server connection
        print('Connected to moveit')
        # set target
        print("The goal is: ", target_pose)
        # print result
        print("Move to positioning target!")

    def picking_action(self, node_name, target_pose, robot_namespace):
        # start execution
        # subscribe move_base server
        print('Construction task for: ', self.comp_id)
        print('The execution robot is: ', robot_namespace)
        print('Current task is: ', node_name)
        print("Waiting for moveit action server...")
        # waiting for server connection
        print('Connected to moveit')
        # set target
        print("The pick goal for ee is: ", target_pose)
        # print result
        print("Executed!")

    def assembly_action(self, node_name, target_pose, robot_namespace):
        # start execution
        # subscribe move_base server
        print('Construction task for: ', self.comp_id)
        print('The execution robot is: ', robot_namespace)
        print('Current task is: ', node_name)
        print("Waiting for moveit action server...")
        # waiting for server connection
        print('Connected to moveit')
        # set target
        print("The assembly goal for ee is: ", target_pose)
        # print result
        print("Executed!")

    def action_selector(self, node_name, activities):
        if node_name == 'move_to_component':
            target = activities[node_name]
            robot = self.robot[node_name]
            self.execute_move(node_name, target, robot)
        elif node_name == 'positioning_for_pickup':
            target = activities[node_name]
            robot = self.robot[node_name]
            self.positioning_action(node_name, target, robot)
        elif node_name == 'pickup':
            target = activities[node_name]
            robot = self.robot[node_name]
            self.picking_action(node_name, target, robot)
        elif node_name == 'transfer':
            target = activities[node_name]
            robot = self.robot[node_name]
            self.execute_move(node_name, target, robot)
        elif node_name == 'positioning_for_assembly':
            target = activities[node_name]
            robot = self.robot[node_name]
            self.positioning_action(node_name, target, robot)
        elif node_name == 'assembly':
            target = activities[node_name]
            robot = self.robot[node_name]
            self.assembly_action(node_name, target, robot)


if __name__ == '__main__':
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

    ea = ExecuteAction('fdsafdas', robot_namespaces).action_selector('positioning_for_pickup', dict_transitions)