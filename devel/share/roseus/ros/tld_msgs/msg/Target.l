;; Auto-generated. Do not edit!


(when (boundp 'tld_msgs::Target)
  (if (not (find-package "TLD_MSGS"))
    (make-package "TLD_MSGS"))
  (shadow 'Target (find-package "TLD_MSGS")))
(unless (find-package "TLD_MSGS::TARGET")
  (make-package "TLD_MSGS::TARGET"))

(in-package "ROS")
;;//! \htmlinclude Target.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass tld_msgs::Target
  :super ros::object
  :slots (_bb _img ))

(defmethod tld_msgs::Target
  (:init
   (&key
    ((:bb __bb) (instance tld_msgs::BoundingBox :init))
    ((:img __img) (instance sensor_msgs::Image :init))
    )
   (send-super :init)
   (setq _bb __bb)
   (setq _img __img)
   self)
  (:bb
   (&rest __bb)
   (if (keywordp (car __bb))
       (send* _bb __bb)
     (progn
       (if __bb (setq _bb (car __bb)))
       _bb)))
  (:img
   (&rest __img)
   (if (keywordp (car __img))
       (send* _img __img)
     (progn
       (if __img (setq _img (car __img)))
       _img)))
  (:serialization-length
   ()
   (+
    ;; tld_msgs/BoundingBox _bb
    (send _bb :serialization-length)
    ;; sensor_msgs/Image _img
    (send _img :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; tld_msgs/BoundingBox _bb
       (send _bb :serialize s)
     ;; sensor_msgs/Image _img
       (send _img :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; tld_msgs/BoundingBox _bb
     (send _bb :deserialize buf ptr-) (incf ptr- (send _bb :serialization-length))
   ;; sensor_msgs/Image _img
     (send _img :deserialize buf ptr-) (incf ptr- (send _img :serialization-length))
   ;;
   self)
  )

(setf (get tld_msgs::Target :md5sum-) "e979efe430ffe5ed7edc21b98ae753b2")
(setf (get tld_msgs::Target :datatype-) "tld_msgs/Target")
(setf (get tld_msgs::Target :definition-)
      "BoundingBox bb
sensor_msgs/Image img

================================================================================
MSG: tld_msgs/BoundingBox
Header header
int32 x
int32 y
int32 width
int32 height
float32 confidence
string tracker_id

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

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of cameara
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

")



(provide :tld_msgs/Target "e979efe430ffe5ed7edc21b98ae753b2")


