; Auto-generated. Do not edit!


(cl:in-package robot-msg)


;//! \htmlinclude sonar.msg.html

(cl:defclass <sonar> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (distance_cm
    :reader distance_cm
    :initarg :distance_cm
    :type cl:integer
    :initform 0))
)

(cl:defclass sonar (<sonar>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sonar>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sonar)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot-msg:<sonar> is deprecated: use robot-msg:sonar instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <sonar>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot-msg:header-val is deprecated.  Use robot-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'distance_cm-val :lambda-list '(m))
(cl:defmethod distance_cm-val ((m <sonar>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot-msg:distance_cm-val is deprecated.  Use robot-msg:distance_cm instead.")
  (distance_cm m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sonar>) ostream)
  "Serializes a message object of type '<sonar>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'distance_cm)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sonar>) istream)
  "Deserializes a message object of type '<sonar>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'distance_cm) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sonar>)))
  "Returns string type for a message object of type '<sonar>"
  "robot/sonar")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sonar)))
  "Returns string type for a message object of type 'sonar"
  "robot/sonar")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sonar>)))
  "Returns md5sum for a message object of type '<sonar>"
  "855619628c5c5c7ec5359ec908324b2b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sonar)))
  "Returns md5sum for a message object of type 'sonar"
  "855619628c5c5c7ec5359ec908324b2b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sonar>)))
  "Returns full string definition for message of type '<sonar>"
  (cl:format cl:nil "Header header~%int32 distance_cm~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sonar)))
  "Returns full string definition for message of type 'sonar"
  (cl:format cl:nil "Header header~%int32 distance_cm~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sonar>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sonar>))
  "Converts a ROS message object to a list"
  (cl:list 'sonar
    (cl:cons ':header (header msg))
    (cl:cons ':distance_cm (distance_cm msg))
))
