# Pick-and-place-Glue-with-widowx-arm
In this tutorial, I will show you how to pick and place a Glue using Widowx arm. 

Author name: Amna Mazen Ali

I uploded a video about step by step tutorial on Youtube:

In this tutorial, I will use package created before in the following github link:
https://github.com/AmnaMazen/Widowx-arm-Move-Group-Python-Interface

* To implement a pick and place scenario, you should divide you task into a sequence of moves that the arm can do. 

# Widowx arm's sequence of moves:

 * I divided this task into 6 steps:

1) Move gripper to be at the same level of the glue (same z-axis)
2) Open gripper.
3) Move widowx arm in x-axis to make glue inside the gripper.
4) Close the gripper on Glue.
5) Move the gripper above the position of pen holder.
6) Open the gripper.

* In every step, you should record the joints positions using the following command:

$ rostopic echo /joints_states -n1

* There is a trick here since position output is not in the regular sequence [joint_1, joint_2,joint_3,joint_4,joint_5, gripper]. Instead it is [joint_3,joint_4,joint_5,gripper_joint,joint_1,joint_2]

* In each step, you should decide "group_name" to use. In widowx arm we have two groups: "widowx_arm" which contains joints starting from joint_1 up to joint_5 and "widowx_gripper" which contains the gripper joints.



# Implementation steps:

1) Download "PickPlaceGlue.py" file from here.
2) Copy the file and paste it inside "src" folder of "move_group_python_interface" package.
3) Make this file as an executable file using the following command:

$ sudo chmod +x PickPlaceGlue.py

5) Launch moveit package for widowx arm using the following command:

$sudo chmod 777 /dev/ttyUSB0

$ cd ~/widowx_arm

$ source devel/setup.bash

$ roslaunch widowx_arm_bringup arm_moveit.launch sim:=false sr300:=false

4) Run the executable file that have the 6 steps discussed earlier:

$ rosrun move_group_python_interface PickPlaceGlue.py


# Note

* In this tutorial, the position of Glue, pen holder, start position of arm are fixed.
