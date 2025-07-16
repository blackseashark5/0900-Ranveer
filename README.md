# MR-Buggy3 Pre-Regional Qualifier Submission  
Team ID: 0900  
Team Member: Ranveer  

---

## Project Overview

This repository contains the complete ROS2-based simulation and navigation setup for the MR-Buggy3 robot, developed for the NXP AIM India Challenge 2025. It includes navigation behavior trees, SLAM configuration, and a warehouse environment built in Ignition Gazebo. The buggy is capable of autonomously navigating through different warehouse worlds while detecting shelf data in real-time.

---

## Folder Structure

cognipilot/
└── cranium/
    └── src/
        ├── b3rb/
        │   └── b3rb_nav2/
        │       └── config/
        │           ├── nav_to_pose_bt.xml
        │           ├── nav_through_poses_bt.xml
        │           ├── nav2.yaml
        │           └── slam.yaml
        └── NXP_AIM_INDIA_2025/
            ├── launch/
            ├── config/
            ├── urdf/
            ├── scripts/
            └── world/

---

## Key Features

- Full support for ROS2 Navigation Stack (nav2)
- Custom Behavior Tree files for navigation with recovery strategies
- SLAM integration using slam_toolbox
- Shelf data publishing to /shelf_data topic
- Simulated testing on all 4 sample warehouse worlds
- Realistic lighting, physics, and model interactions using Gazebo

---

## Videos Submitted

The following videos are part of the submission, as per the guidelines:

- warehouse_1.mp4
- warehouse_2.mp4
- warehouse_3.mp4
- warehouse_4.mp4

Each video includes:
- Right half of screen: Gazebo simulation showing MR-Buggy3 in action
- Left half of screen: Terminal window running `ros2 topic echo /shelf_data`

---

## Code Description

nav_to_pose_bt.xml  
→ Custom Behavior Tree used for single-goal navigation with nodes for path following, goal checking, and recovery behaviors like spinning and waiting.

nav_through_poses_bt.xml  
→ Multi-waypoint navigation BT file to traverse various zones in a warehouse sequentially.

nav2.yaml  
→ Parameter file for ROS2 Navigation Stack: includes planner configs, DWB controller parameters, global/local costmap tuning, inflation radius, recovery behaviors, etc.

slam.yaml  
→ SLAM Toolbox configuration for online mapping, real-time loop closure, and map merging.

---

## How to Launch Simulation

source install/setup.bash  
ros2 launch nxp_aim_india_2025 bringup_sim.launch.py world:=warehouse_1.sdf slam:=true

Repeat with warehouse_2.sdf, warehouse_3.sdf, etc., to test on other maps.

---

## Shelf Data Output

To monitor detected shelves:  
ros2 topic echo /shelf_data

The data includes shelf ID, relative position, and pose, aiding in inventory scanning and path planning.

---

## Preferred Regional Finale Location

Bangalore – M S Ramaiah Institute of Technology

---

## Submission Format

File Name: 0900_ranveer.zip  
Contents:
- Source Code Folder (cognipilot/cranium/src)
- 4 video files
- README.md (this file)

---

## Contact Info

Ranveer  
Email: [ranveer4us@gmail.com]  

---

## Acknowledgment

Special thanks to NXP AIM India 2025 for giving us this incredible opportunity. We look forward to demonstrating our innovation and advancing to the Regional and Grand Finales!

Let’s build something legendary 🚀
