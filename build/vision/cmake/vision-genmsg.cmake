# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "vision: 2 messages, 0 services")

set(MSG_I_FLAGS "-Ivision:/home/abeni/rob/src/vision/msg;-Istd_msgs:/opt/ros/jade/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/jade/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(vision_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/abeni/rob/src/vision/msg/face_box.msg" NAME_WE)
add_custom_target(_vision_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "vision" "/home/abeni/rob/src/vision/msg/face_box.msg" "geometry_msgs/Point"
)

get_filename_component(_filename "/home/abeni/rob/src/vision/msg/targets.msg" NAME_WE)
add_custom_target(_vision_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "vision" "/home/abeni/rob/src/vision/msg/targets.msg" "vision/face_box:geometry_msgs/Point"
)

#
#  langs = gencpp;geneus;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(vision
  "/home/abeni/rob/src/vision/msg/face_box.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vision
)
_generate_msg_cpp(vision
  "/home/abeni/rob/src/vision/msg/targets.msg"
  "${MSG_I_FLAGS}"
  "/home/abeni/rob/src/vision/msg/face_box.msg;/opt/ros/jade/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vision
)

### Generating Services

### Generating Module File
_generate_module_cpp(vision
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vision
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(vision_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(vision_generate_messages vision_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abeni/rob/src/vision/msg/face_box.msg" NAME_WE)
add_dependencies(vision_generate_messages_cpp _vision_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abeni/rob/src/vision/msg/targets.msg" NAME_WE)
add_dependencies(vision_generate_messages_cpp _vision_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vision_gencpp)
add_dependencies(vision_gencpp vision_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vision_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(vision
  "/home/abeni/rob/src/vision/msg/face_box.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vision
)
_generate_msg_eus(vision
  "/home/abeni/rob/src/vision/msg/targets.msg"
  "${MSG_I_FLAGS}"
  "/home/abeni/rob/src/vision/msg/face_box.msg;/opt/ros/jade/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vision
)

### Generating Services

### Generating Module File
_generate_module_eus(vision
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vision
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(vision_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(vision_generate_messages vision_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abeni/rob/src/vision/msg/face_box.msg" NAME_WE)
add_dependencies(vision_generate_messages_eus _vision_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abeni/rob/src/vision/msg/targets.msg" NAME_WE)
add_dependencies(vision_generate_messages_eus _vision_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vision_geneus)
add_dependencies(vision_geneus vision_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vision_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(vision
  "/home/abeni/rob/src/vision/msg/face_box.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vision
)
_generate_msg_lisp(vision
  "/home/abeni/rob/src/vision/msg/targets.msg"
  "${MSG_I_FLAGS}"
  "/home/abeni/rob/src/vision/msg/face_box.msg;/opt/ros/jade/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vision
)

### Generating Services

### Generating Module File
_generate_module_lisp(vision
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vision
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(vision_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(vision_generate_messages vision_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abeni/rob/src/vision/msg/face_box.msg" NAME_WE)
add_dependencies(vision_generate_messages_lisp _vision_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abeni/rob/src/vision/msg/targets.msg" NAME_WE)
add_dependencies(vision_generate_messages_lisp _vision_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vision_genlisp)
add_dependencies(vision_genlisp vision_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vision_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(vision
  "/home/abeni/rob/src/vision/msg/face_box.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision
)
_generate_msg_py(vision
  "/home/abeni/rob/src/vision/msg/targets.msg"
  "${MSG_I_FLAGS}"
  "/home/abeni/rob/src/vision/msg/face_box.msg;/opt/ros/jade/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision
)

### Generating Services

### Generating Module File
_generate_module_py(vision
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(vision_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(vision_generate_messages vision_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/abeni/rob/src/vision/msg/face_box.msg" NAME_WE)
add_dependencies(vision_generate_messages_py _vision_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/abeni/rob/src/vision/msg/targets.msg" NAME_WE)
add_dependencies(vision_generate_messages_py _vision_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vision_genpy)
add_dependencies(vision_genpy vision_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vision_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vision)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vision
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(vision_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(vision_generate_messages_cpp geometry_msgs_generate_messages_cpp)

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vision)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vision
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
add_dependencies(vision_generate_messages_eus std_msgs_generate_messages_eus)
add_dependencies(vision_generate_messages_eus geometry_msgs_generate_messages_eus)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vision)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vision
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(vision_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(vision_generate_messages_lisp geometry_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(vision_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(vision_generate_messages_py geometry_msgs_generate_messages_py)