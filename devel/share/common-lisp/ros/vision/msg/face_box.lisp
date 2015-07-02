; Auto-generated. Do not edit!


(cl:in-package vision-msg)


;//! \htmlinclude face_box.msg.html

(cl:defclass <face_box> (roslisp-msg-protocol:ros-message)
  ((top_left
    :reader top_left
    :initarg :top_left
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (width_height
    :reader width_height
    :initarg :width_height
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point)))
)

(cl:defclass face_box (<face_box>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <face_box>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'face_box)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-msg:<face_box> is deprecated: use vision-msg:face_box instead.")))

(cl:ensure-generic-function 'top_left-val :lambda-list '(m))
(cl:defmethod top_left-val ((m <face_box>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-msg:top_left-val is deprecated.  Use vision-msg:top_left instead.")
  (top_left m))

(cl:ensure-generic-function 'width_height-val :lambda-list '(m))
(cl:defmethod width_height-val ((m <face_box>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-msg:width_height-val is deprecated.  Use vision-msg:width_height instead.")
  (width_height m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <face_box>) ostream)
  "Serializes a message object of type '<face_box>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'top_left) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'width_height) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <face_box>) istream)
  "Deserializes a message object of type '<face_box>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'top_left) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'width_height) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<face_box>)))
  "Returns string type for a message object of type '<face_box>"
  "vision/face_box")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'face_box)))
  "Returns string type for a message object of type 'face_box"
  "vision/face_box")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<face_box>)))
  "Returns md5sum for a message object of type '<face_box>"
  "9bdccc133bdc2e2db906756187d7a6f5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'face_box)))
  "Returns md5sum for a message object of type 'face_box"
  "9bdccc133bdc2e2db906756187d7a6f5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<face_box>)))
  "Returns full string definition for message of type '<face_box>"
  (cl:format cl:nil "geometry_msgs/Point top_left~%geometry_msgs/Point width_height~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'face_box)))
  "Returns full string definition for message of type 'face_box"
  (cl:format cl:nil "geometry_msgs/Point top_left~%geometry_msgs/Point width_height~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <face_box>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'top_left))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'width_height))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <face_box>))
  "Converts a ROS message object to a list"
  (cl:list 'face_box
    (cl:cons ':top_left (top_left msg))
    (cl:cons ':width_height (width_height msg))
))
