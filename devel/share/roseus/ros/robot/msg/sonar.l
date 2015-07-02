;; Auto-generated. Do not edit!


(when (boundp 'robot::sonar)
  (if (not (find-package "ROBOT"))
    (make-package "ROBOT"))
  (shadow 'sonar (find-package "ROBOT")))
(unless (find-package "ROBOT::SONAR")
  (make-package "ROBOT::SONAR"))

(in-package "ROS")
;;//! \htmlinclude sonar.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass robot::sonar
  :super ros::object
  :slots (_header _distance_cm ))

(defmethod robot::sonar
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:distance_cm __distance_cm) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _distance_cm (round __distance_cm))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:distance_cm
   (&optional __distance_cm)
   (if __distance_cm (setq _distance_cm __distance_cm)) _distance_cm)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32 _distance_cm
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32 _distance_cm
       (write-long _distance_cm s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32 _distance_cm
     (setq _distance_cm (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get robot::sonar :md5sum-) "855619628c5c5c7ec5359ec908324b2b")
(setf (get robot::sonar :datatype-) "robot/sonar")
(setf (get robot::sonar :definition-)
      "Header header
int32 distance_cm

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :robot/sonar "855619628c5c5c7ec5359ec908324b2b")


