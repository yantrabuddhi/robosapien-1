# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "robot: 3 messages, 0 services")

set(MSG_I_FLAGS "-Irobot:/home/abeni/rob/src/robot/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(robot_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/abeni/rob/src/robot/msg/sonar.msg" NAME_WE)
add_custom_target(_robot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot" "/home/abeni/rob/src/robot/msg/sonar.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/abeni/rob/src/robot/msg/robot_cmd.msg" NAME_WE)
add_custom_target(_robot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot" "/home/abeni/rob/src/robot/msg/robot_cmd.msg" ""
)

get_filename_component(_filename "/home/abeni/rob/src/robot/msg/compass.msg" NAME_WE)
add_custom_target(_robot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot" "/home/abeni/rob/src/robot/msg/compass.msg" "std_msgs/Header"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(robot
  "/home/abeni/rob/src/robot/msg/sonar.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot
)
_generate_msg_cpp(robot
  "/home/abeni/rob/src/robot/msg/robot_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot
)
_generate_msg_cpp(robot
  "/home/abeni/rob/src/robot/msg/compass.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot
)

### Generating Services

### Generating Module File
_generate_module_cpp(robot
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(robot_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(robot_generate_messages robot_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abeni/rob/src/robot/msg/sonar.msg" NAME_WE)
add_dependencies(robot_generate_messages_cpp _robot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abeni/rob/src/robot/msg/robot_cmd.msg" NAME_WE)
add_dependencies(robot_generate_messages_cpp _robot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abeni/rob/src/robot/msg/compass.msg" NAME_WE)
add_dependencies(robot_generate_messages_cpp _robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_gencpp)
add_dependencies(robot_gencpp robot_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(robot
  "/home/abeni/rob/src/robot/msg/sonar.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot
)
_generate_msg_lisp(robot
  "/home/abeni/rob/src/robot/msg/robot_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot
)
_generate_msg_lisp(robot
  "/home/abeni/rob/src/robot/msg/compass.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot
)

### Generating Services

### Generating Module File
_generate_module_lisp(robot
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(robot_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(robot_generate_messages robot_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abeni/rob/src/robot/msg/sonar.msg" NAME_WE)
add_dependencies(robot_generate_messages_lisp _robot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abeni/rob/src/robot/msg/robot_cmd.msg" NAME_WE)
add_dependencies(robot_generate_messages_lisp _robot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abeni/rob/src/robot/msg/compass.msg" NAME_WE)
add_dependencies(robot_generate_messages_lisp _robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_genlisp)
add_dependencies(robot_genlisp robot_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(robot
  "/home/abeni/rob/src/robot/msg/sonar.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot
)
_generate_msg_py(robot
  "/home/abeni/rob/src/robot/msg/robot_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot
)
_generate_msg_py(robot
  "/home/abeni/rob/src/robot/msg/compass.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot
)

### Generating Services

### Generating Module File
_generate_module_py(robot
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(robot_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(robot_generate_messages robot_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abeni/rob/src/robot/msg/sonar.msg" NAME_WE)
add_dependencies(robot_generate_messages_py _robot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abeni/rob/src/robot/msg/robot_cmd.msg" NAME_WE)
add_dependencies(robot_generate_messages_py _robot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abeni/rob/src/robot/msg/compass.msg" NAME_WE)
add_dependencies(robot_generate_messages_py _robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_genpy)
add_dependencies(robot_genpy robot_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(robot_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(robot_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(robot_generate_messages_py std_msgs_generate_messages_py)
