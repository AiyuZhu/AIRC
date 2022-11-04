import robotConstructionActionNode as rcan
import rospy
import actionlib
from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


class ExecuteMovingAction(rcan.RobotConstructionActionNode):
    def __init__(self, node_name, component_id):
        super(ExecuteMovingAction, self).__init__(node_name)
        self.node_name = node_name
        self.comp_id = component_id

        # create the ros node
        self.rospy.init_node(self.node_name, anonymous=True)

    def execute(self, target_pose):
        # start execution
        # subscribe move_base server
        move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("Waiting for move_base action server...")
        # waiting for server connection
        while move_base.wait_for_server(rospy.Duration(5.0)) == 0:
            rospy.loginfo("Connected to move base server")

        # set target
        target = Pose(Point(target_pose[0]), Quaternion(target_pose[1]))
        goal = MoveBaseGoal()
        goal.target_pose.pose = target
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()

        rospy.loginfo("Going to: " + str(target))
        self.state_machine.start_execution()
        move_base.send_goal(goal)

        finished_within_time = move_base.wait_for_result(rospy.Duration(300))

        if not finished_within_time:
            move_base.cancel_goal()
            rospy.loginfo("Timed out achieving goal")
        else:
            state = move_base.get_state()
            if state == GoalStatus.SUCCEEDED:
                rospy.loginfo("Goal succeeded!")
                self.state_machine.finish_execution()
            else:
                rospy.loginfo("Goal failed！ ")
        rospy.sleep(5)
