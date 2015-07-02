;; Auto-generated. Do not edit!


(when (boundp 'vision::targets)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'targets (find-package "VISION")))
(unless (find-package "VISION::TARGETS")
  (make-package "VISION::TARGETS"))

(in-package "ROS")
;;//! \htmlinclude targets.msg.html


(defclass vision::targets
  :super ros::object
  :slots (_faces _ref_img_width _ref_img_height ))

(defmethod vision::targets
  (:init
   (&key
    ((:faces __faces) (let (r) (dotimes (i 0) (push (instance vision::face_box :init) r)) r))
    ((:ref_img_width __ref_img_width) 0)
    ((:ref_img_height __ref_img_height) 0)
    )
   (send-super :init)
   (setq _faces __faces)
   (setq _ref_img_width (round __ref_img_width))
   (setq _ref_img_height (round __ref_img_height))
   self)
  (:faces
   (&rest __faces)
   (if (keywordp (car __faces))
       (send* _faces __faces)
     (progn
       (if __faces (setq _faces (car __faces)))
       _faces)))
  (:ref_img_width
   (&optional __ref_img_width)
   (if __ref_img_width (setq _ref_img_width __ref_img_width)) _ref_img_width)
  (:ref_img_height
   (&optional __ref_img_height)
   (if __ref_img_height (setq _ref_img_height __ref_img_height)) _ref_img_height)
  (:serialization-length
   ()
   (+
    ;; vision/face_box[] _faces
    (apply #'+ (send-all _faces :serialization-length)) 4
    ;; uint16 _ref_img_width
    2
    ;; uint16 _ref_img_height
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; vision/face_box[] _faces
     (write-long (length _faces) s)
     (dolist (elem _faces)
       (send elem :serialize s)
       )
     ;; uint16 _ref_img_width
       (write-word _ref_img_width s)
     ;; uint16 _ref_img_height
       (write-word _ref_img_height s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; vision/face_box[] _faces
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _faces (let (r) (dotimes (i n) (push (instance vision::face_box :init) r)) r))
     (dolist (elem- _faces)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; uint16 _ref_img_width
     (setq _ref_img_width (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _ref_img_height
     (setq _ref_img_height (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get vision::targets :md5sum-) "bf92c07c6e3081a4a97a355ceda9b6aa")
(setf (get vision::targets :datatype-) "vision/targets")
(setf (get vision::targets :definition-)
      "face_box[] faces
uint16 ref_img_width
uint16 ref_img_height

================================================================================
MSG: vision/face_box
geometry_msgs/Point top_left
geometry_msgs/Point width_height
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :vision/targets "bf92c07c6e3081a4a97a355ceda9b6aa")


