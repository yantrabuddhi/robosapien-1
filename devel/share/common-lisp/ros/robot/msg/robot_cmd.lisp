; Auto-generated. Do not edit!


(cl:in-package robot-msg)


;//! \htmlinclude robot_cmd.msg.html

(cl:defclass <robot_cmd> (roslisp-msg-protocol:ros-message)
  ((cmd
    :reader cmd
    :initarg :cmd
    :type cl:string
    :initform "")
   (duration_10ms
    :reader duration_10ms
    :initarg :duration_10ms
    :type cl:fixnum
    :initform 0))
)

(cl:defclass robot_cmd (<robot_cmd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <robot_cmd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'robot_cmd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot-msg:<robot_cmd> is deprecated: use robot-msg:robot_cmd instead.")))

(cl:ensure-generic-function 'cmd-val :lambda-list '(m))
(cl:defmethod cmd-val ((m <robot_cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot-msg:cmd-val is deprecated.  Use robot-msg:cmd instead.")
  (cmd m))

(cl:ensure-generic-function 'duration_10ms-val :lambda-list '(m))
(cl:defmethod duration_10ms-val ((m <robot_cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot-msg:duration_10ms-val is deprecated.  Use robot-msg:duration_10ms instead.")
  (duration_10ms m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <robot_cmd>) ostream)
  "Serializes a message object of type '<robot_cmd>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'cmd))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'cmd))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'duration_10ms)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <robot_cmd>) istream)
  "Deserializes a message object of type '<robot_cmd>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cmd) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'cmd) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'duration_10ms)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<robot_cmd>)))
  "Returns string type for a message object of type '<robot_cmd>"
  "robot/robot_cmd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'robot_cmd)))
  "Returns string type for a message object of type 'robot_cmd"
  "robot/robot_cmd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<robot_cmd>)))
  "Returns md5sum for a message object of type '<robot_cmd>"
  "0dc039100dce1fd03db0d90732bfee7d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'robot_cmd)))
  "Returns md5sum for a message object of type 'robot_cmd"
  "0dc039100dce1fd03db0d90732bfee7d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<robot_cmd>)))
  "Returns full string definition for message of type '<robot_cmd>"
  (cl:format cl:nil "string cmd~%uint8 duration_10ms~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'robot_cmd)))
  "Returns full string definition for message of type 'robot_cmd"
  (cl:format cl:nil "string cmd~%uint8 duration_10ms~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <robot_cmd>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'cmd))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <robot_cmd>))
  "Converts a ROS message object to a list"
  (cl:list 'robot_cmd
    (cl:cons ':cmd (cmd msg))
    (cl:cons ':duration_10ms (duration_10ms msg))
))
