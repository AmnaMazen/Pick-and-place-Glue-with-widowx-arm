#!/usr/bin/env python


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "widowx_arm"
group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)


# We can get the name of the reference frame for this robot:
planning_frame = group.get_planning_frame()
print "============ Reference frame: %s" % planning_frame

# We can also print the name of the end-effector link for this group:
eef_link = group.get_end_effector_link()
print "============ End effector: %s" % eef_link

# We can get a list of all the groups in the robot:
group_names = robot.get_group_names()
print "============ Robot Groups:", robot.get_group_names()

# Sometimes for debugging it is useful to print the entire state of the
# robot:
print "============ Printing robot state"
print robot.get_current_state()
print ""


# We can get the joint values from the group and adjust some of the values:
joint_goal = group.get_current_joint_values()

############# Position 1: move down #########################################
joint_goal[0] = -0.09357282806102411
joint_goal[1] = 0.4003689856381523
joint_goal[2] = 0.0782330201821677
joint_goal[3] = -0.4387185053352934
joint_goal[4] =  -0.015339807878856412

# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
group.go(joint_goal, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
group.stop()
group.clear_pose_targets()



############# Position 2: Open gripper #####################################

rospy.sleep(2);
group_name2 = "widowx_gripper"
group2 = moveit_commander.MoveGroupCommander(group_name2)
joint_goal2 = group2.get_current_joint_values()
joint_goal2[0] = 0.03
#joint_goal2[1] = 0.03




# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
group2.go(joint_goal2, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
group2.stop()
group2.clear_pose_targets()



############# Position 3: move forward #########################################
# Make default position
rospy.sleep(2);
joint_goal = group.get_current_joint_values()
joint_goal[0] = -0.09510680884890975
joint_goal[1] = 0.5967185264875144
joint_goal[2] = -0.2561747915769021
joint_goal[3] = -0.3313398501832985
joint_goal[4] =  -0.015339807878856412



# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
group.go(joint_goal, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
group.stop()
group.clear_pose_targets()



############# Position 4: Close gripper #####################################

rospy.sleep(2);
group_name2 = "widowx_gripper"
group2 = moveit_commander.MoveGroupCommander(group_name2)
joint_goal2 = group2.get_current_joint_values()
joint_goal2[0] = 0.01373050448397646
#joint_goal2[1] = 0.03




# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
group2.go(joint_goal2, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
group2.stop()
group2.clear_pose_targets()



############# Position 5: Above pen holder #########################################
# Make default position
rospy.sleep(2);
joint_goal = group.get_current_joint_values()
joint_goal[0] = 0.42644665903220824
joint_goal[1] = -0.4678641403051206
joint_goal[2] = 0.9863496466104673
joint_goal[3] = -0.5276893910326605
joint_goal[4] = -0.015339807878856412



# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
group.go(joint_goal, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
group.stop()
group.clear_pose_targets()

############# Position 6: Open gripper #####################################

rospy.sleep(2);
group_name2 = "widowx_gripper"
group2 = moveit_commander.MoveGroupCommander(group_name2)
joint_goal2 = group2.get_current_joint_values()
joint_goal2[0] = 0.03
#joint_goal2[1] = 0.03




# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
group2.go(joint_goal2, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
group2.stop()
group2.clear_pose_targets()


