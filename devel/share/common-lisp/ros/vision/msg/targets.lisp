; Auto-generated. Do not edit!


(cl:in-package vision-msg)


;//! \htmlinclude targets.msg.html

(cl:defclass <targets> (roslisp-msg-protocol:ros-message)
  ((faces
    :reader faces
    :initarg :faces
    :type (cl:vector vision-msg:face_box)
   :initform (cl:make-array 0 :element-type 'vision-msg:face_box :initial-element (cl:make-instance 'vision-msg:face_box)))
   (ref_img_width
    :reader ref_img_width
    :initarg :ref_img_width
    :type cl:fixnum
    :initform 0)
   (ref_img_height
    :reader ref_img_height
    :initarg :ref_img_height
    :type cl:fixnum
    :initform 0))
)

(cl:defclass targets (<targets>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <targets>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'targets)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-msg:<targets> is deprecated: use vision-msg:targets instead.")))

(cl:ensure-generic-function 'faces-val :lambda-list '(m))
(cl:defmethod faces-val ((m <targets>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-msg:faces-val is deprecated.  Use vision-msg:faces instead.")
  (faces m))

(cl:ensure-generic-function 'ref_img_width-val :lambda-list '(m))
(cl:defmethod ref_img_width-val ((m <targets>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-msg:ref_img_width-val is deprecated.  Use vision-msg:ref_img_width instead.")
  (ref_img_width m))

(cl:ensure-generic-function 'ref_img_height-val :lambda-list '(m))
(cl:defmethod ref_img_height-val ((m <targets>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-msg:ref_img_height-val is deprecated.  Use vision-msg:ref_img_height instead.")
  (ref_img_height m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <targets>) ostream)
  "Serializes a message object of type '<targets>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'faces))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'faces))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ref_img_width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'ref_img_width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ref_img_height)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'ref_img_height)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <targets>) istream)
  "Deserializes a message object of type '<targets>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'faces) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'faces)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'vision-msg:face_box))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ref_img_width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'ref_img_width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ref_img_height)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'ref_img_height)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<targets>)))
  "Returns string type for a message object of type '<targets>"
  "vision/targets")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'targets)))
  "Returns string type for a message object of type 'targets"
  "vision/targets")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<targets>)))
  "Returns md5sum for a message object of type '<targets>"
  "bf92c07c6e3081a4a97a355ceda9b6aa")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'targets)))
  "Returns md5sum for a message object of type 'targets"
  "bf92c07c6e3081a4a97a355ceda9b6aa")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<targets>)))
  "Returns full string definition for message of type '<targets>"
  (cl:format cl:nil "face_box[] faces~%uint16 ref_img_width~%uint16 ref_img_height~%~%================================================================================~%MSG: vision/face_box~%geometry_msgs/Point top_left~%geometry_msgs/Point width_height~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'targets)))
  "Returns full string definition for message of type 'targets"
  (cl:format cl:nil "face_box[] faces~%uint16 ref_img_width~%uint16 ref_img_height~%~%================================================================================~%MSG: vision/face_box~%geometry_msgs/Point top_left~%geometry_msgs/Point width_height~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <targets>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'faces) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <targets>))
  "Converts a ROS message object to a list"
  (cl:list 'targets
    (cl:cons ':faces (faces msg))
    (cl:cons ':ref_img_width (ref_img_width msg))
    (cl:cons ':ref_img_height (ref_img_height msg))
))
