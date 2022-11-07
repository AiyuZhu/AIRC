#! /usr/bin/env python3
# encoding: utf-8

import rospy
import actionlib
from actionlib_msgs.msg import *  
from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


class ExecuteMovingAction(object):
    def __init__(self, node_name, component_id):
        self.node_name = node_name
        self.comp_id = component_id

        # create the ros node
        rospy.init_node(self.node_name, anonymous=True)

    def execute(self, target_pose):
        # start execution
        # subscribe move_base server
        move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("Waiting for move_base action server...")
        # waiting for server connection
        while move_base.wait_for_server(rospy.Duration(5.0)) == 0:
            rospy.loginfo("Connected to move base server")

        # set target
        x = target_pose[0][0]
        y = target_pose[0][1]
        z = target_pose[0][2]
        o_x = target_pose[1][0]
        o_y = target_pose[1][1]
        o_z = target_pose[1][2]
        w = target_pose[1][3]
        target = Pose(Point(x, y, z), Quaternion(o_x, o_y, o_z, w))
        goal = MoveBaseGoal()
        goal.target_pose.pose = target
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()

        rospy.loginfo("Going to: " + str(target))
        move_base.send_goal(goal)

        finished_within_time = move_base.wait_for_result(rospy.Duration(300))

        if not finished_within_time:
            move_base.cancel_goal()
            rospy.loginfo("Timed out achieving goal")
        else:
            state = move_base.get_state()
            if state == GoalStatus.SUCCEEDED:
                rospy.loginfo("Goal succeeded!")
                return 'success'
            else:
                rospy.loginfo("Goal failed！ ")
        rospy.sleep(2)
