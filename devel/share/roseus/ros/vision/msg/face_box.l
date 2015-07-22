;; Auto-generated. Do not edit!


(when (boundp 'vision::face_box)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'face_box (find-package "VISION")))
(unless (find-package "VISION::FACE_BOX")
  (make-package "VISION::FACE_BOX"))

(in-package "ROS")
;;//! \htmlinclude face_box.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass vision::face_box
  :super ros::object
  :slots (_top_left _width_height ))

(defmethod vision::face_box
  (:init
   (&key
    ((:top_left __top_left) (instance geometry_msgs::Point :init))
    ((:width_height __width_height) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _top_left __top_left)
   (setq _width_height __width_height)
   self)
  (:top_left
   (&rest __top_left)
   (if (keywordp (car __top_left))
       (send* _top_left __top_left)
     (progn
       (if __top_left (setq _top_left (car __top_left)))
       _top_left)))
  (:width_height
   (&rest __width_height)
   (if (keywordp (car __width_height))
       (send* _width_height __width_height)
     (progn
       (if __width_height (setq _width_height (car __width_height)))
       _width_height)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Point _top_left
    (send _top_left :serialization-length)
    ;; geometry_msgs/Point _width_height
    (send _width_height :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Point _top_left
       (send _top_left :serialize s)
     ;; geometry_msgs/Point _width_height
       (send _width_height :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Point _top_left
     (send _top_left :deserialize buf ptr-) (incf ptr- (send _top_left :serialization-length))
   ;; geometry_msgs/Point _width_height
     (send _width_height :deserialize buf ptr-) (incf ptr- (send _width_height :serialization-length))
   ;;
   self)
  )

(setf (get vision::face_box :md5sum-) "9bdccc133bdc2e2db906756187d7a6f5")
(setf (get vision::face_box :datatype-) "vision/face_box")
(setf (get vision::face_box :definition-)
      "geometry_msgs/Point top_left
geometry_msgs/Point width_height
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :vision/face_box "9bdccc133bdc2e2db906756187d7a6f5")


