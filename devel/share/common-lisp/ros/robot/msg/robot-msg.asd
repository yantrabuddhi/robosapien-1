
(cl:in-package :asdf)

(defsystem "robot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "gesture_r" :depends-on ("_package_gesture_r"))
    (:file "_package_gesture_r" :depends-on ("_package"))
    (:file "sonar" :depends-on ("_package_sonar"))
    (:file "_package_sonar" :depends-on ("_package"))
    (:file "compass" :depends-on ("_package_compass"))
    (:file "_package_compass" :depends-on ("_package"))
    (:file "robot_cmd" :depends-on ("_package_robot_cmd"))
    (:file "_package_robot_cmd" :depends-on ("_package"))
  ))