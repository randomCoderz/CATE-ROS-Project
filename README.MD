# CATE Project

Cal Poly Pomona Autonomous Transportation Experience Project, which also happens to be my Master's Project.

## Reference Material

If you are new to ROS, then it would be a good idea to study up on the following reference material.

1. [Getting Started with ROS (Clearpath Tutorial)](http://www.clearpathrobotics.com/assets/guides/kinetic/ros/Getting%20Started%20with%20Ubuntu.html) 
2. [Husky Tutorial](http://www.clearpathrobotics.com/assets/guides/kinetic/husky/index.html)
3. [Catkin](http://wiki.ros.org/catkin/workspaces#Source_Space)

## Environment

1. ROS Melodic
2. Ubuntu 18.04
3. Python 2.x
4. C++

## Running this Project

Create catkin specific directory structure on your device, clone the repository inside source, and build.

```bash
# Make a directory, most importantly with the src folder inside
mkdir -p ros_project/src
# Clone this project inside the src folder
git clone https://github.com/randomCoderz/CATE-ROS-Project.git
# Build the project
catkin_make 
# Source the setup script
source <your_workspace_path>/ros_project/devel/setup.bash
rospack profile
```

## Launch Gazebo World

```bash
roslaunch simulation cpp.launch
```

## Rviz

```bash
# Launch RVIZ
roslaunch husky_viz view_robot.launch
 ```