cmake_minimum_required(VERSION 2.8.3)
project(fake_odom)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  roscpp
  rospy
  std_msgs
  sensor_msgs
  tf
)

catkin_package(
  CATKIN_DEPENDS geometry_msgs nav_msgs roscpp rospy std_msgs tf sensor_msgs
)

include_directories(${catkin_INCLUDE_DIRS})

add_executable(fake_odom_node_tf src/fake_odom_node_tf.cpp)
add_executable(fake_odom_node_no_tf src/fake_odom_node_no_tf.cpp)
target_link_libraries(fake_odom_node_tf ${catkin_LIBRARIES})
target_link_libraries(fake_odom_node_no_tf ${catkin_LIBRARIES})

install(PROGRAMS
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(TARGETS fake_odom_node_tf fake_odom_node_no_tf
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
