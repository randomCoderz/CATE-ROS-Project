# CATE Project

Cal Poly Pomona Autonomous Transportation Experience Project, which also happens to be my Master's Project.

## Assumptions & Reference Material

It is assumed that the user has a decent understanding of Linux (Using the terminal) and is comfortable with ROS.
If you are new to ROS or Linux, then it would be a good idea to study up on the following reference material:

1. [Getting Started with ROS (Clearpath Tutorial)](http://www.clearpathrobotics.com/assets/guides/kinetic/ros/Getting%20Started%20with%20Ubuntu.html)
2. [Husky Tutorial](http://www.clearpathrobotics.com/assets/guides/kinetic/husky/index.html)
3. [Catkin](http://wiki.ros.org/catkin/workspaces#Source_Space)

## Environment

1. ROS Melodic
2. Ubuntu 18.04
3. Python 2
4. C++
5. Bash
6. Husky Packages

## Assumptions

1. Decent understanding of how to use the Linux Terminal
2. Some knowledge of bash

## Installing/Configuring ROS/Husky simulator

Now install Husky Melodic packages

```bash
# If you upgrade to ROS Neotic+, assuming it's supported replace melodic with neotic
sudo apt-get install ros-melodic-husky-desktop
sudo apt-get install ros-melodic-husky-simulator
sudo apt-get install ros-melodic-husky-navigation
```

## Install libraries

Install OpenCV 3 for Python.

```python
pip install opencv-python==3.4.2.17
```

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

This particular husky is customized to use a camera. We need to add an environment variable to the "custom_description.urdf.xacro" file in order to load the husky with the custom configurations.

```bash
vim ~/.bashrc
# Add the following, but modify accordingly
export HUSKY_URDF_EXTRAS=/<your path>/CATE-ROS-PROJECT/husky_customization/husky_custom_descrption/urdf/custom_description.urdf.xacro
source ~/.bashrc
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

## PS4 Controller Configurations for Simulation

In certain cases, you may want to run the robot via a controller. The method I used to get the controller to work with the simulation is not ideal. By default, Gazebo/Husky simulation tries to find the remote /dev/input/ps4. This would be fine, but the problem is that by default (at least with Ubuntu 18.04, ROS Melodic, and current ds4drv driver) the controller mounts to /dev/input/js0. That means when you spin up the simulation, the bot is trying to look for the ps4 in the wrong location. In theory, we should be able to override this config when we launch the simulation:

```bash
# Example, this did not work for me!!!
roslaunch simulation cpp.launch joy_node/dev=/dev/input/js0
```

This for some reason did not work. So I had to manually override the config file to force it to use the right folder.
Ideally, if you found a way to override the parameter use that. Otherwise, this is a hacky kind of solution.

1. Install [ds4drv](https://github.com/chrippa/ds4drv)
2. Once that's installed, plug in the PS4 controller via cable or connect with bluetooth.
    - Note, I never tested it with bluetooth, but theoretically it should work fine. There is an extra step where you need to connect it via ds4drv command. See their readme on how to connect the controller via bluetooth.
3. Change the read write permissions of whereever the controler is being mounted to.
    - /dev/input/js0 is the current default, but could change. You can verify that it is still the default location by running the ``` ds4drv ```  command in bash.
    - You will see something along the line of "created devices /dev/input/whatever (joystick)". If it's changed, just use this new line, instead of /dev/input/js0.

```bash
# Check if mounted
ls -l /dev/input/js0

# Change the read-write permission. 
# Remember, you will need to do this everytime you plug/unplug the controller!!!
sudo chmod a+rw /dev/input/js0
```

Now, once that's done you need to change modify the default yaml file to match where the controller is being mounted. Do the following:

```bash
# Go to the directory for husky_control
roscd husky_control/config

# Copy teleop_ps4.yaml as a backup
sudo cp teleop_ps4.yaml teleop_ps4.yaml.old

# Override the configurations...
# Scroll to the bottom and look for the following line "dev: /dev/input/ps4"
# Replace this with "dev: /dev/input/js0" or whatever the ps4 mount point is. Then save the file.
sudo vim teleop_ps4.yaml

# Finally, launch the simulation and assuming you didn't unplug the controller (in which case, you'll need to change the read-write permission), things should work. You will not see an error for /dev/input/ps4.

roslaunch simulation cpp.launch
```
