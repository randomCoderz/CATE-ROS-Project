# CATE Project

Cal Poly Pomona Autonomous Transportation Experience Project, which also happens to be my Master's Project.

## Quick Commands

```bash
# Launch RVIZ
roslaunch husky_viz view_robot.launch
 ```

## Reference Material

1. [Husky Tutorial](http://www.clearpathrobotics.com/assets/guides/kinetic/husky/SimulatingHusky.html)
2. [Catkin](http://wiki.ros.org/catkin/workspaces#Source_Space)

## Configurations

1. ROS Melodic
2. Ubuntu 18.04

## Running this Project

Pull the project from Git onto your desktop

```bash
# Build the project
catkin_make
source <your_workspace_path>/ros_project/devel/setup.bash
rospack profile
```

## Launch Gazebo World

```bash
roslaunch simulation cpp.launch
```
