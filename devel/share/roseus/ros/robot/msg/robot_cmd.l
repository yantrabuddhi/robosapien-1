;; Auto-generated. Do not edit!


(when (boundp 'robot::robot_cmd)
  (if (not (find-package "ROBOT"))
    (make-package "ROBOT"))
  (shadow 'robot_cmd (find-package "ROBOT")))
(unless (find-package "ROBOT::ROBOT_CMD")
  (make-package "ROBOT::ROBOT_CMD"))

(in-package "ROS")
;;//! \htmlinclude robot_cmd.msg.html


(defclass robot::robot_cmd
  :super ros::object
  :slots (_cmd _duration_10ms ))

(defmethod robot::robot_cmd
  (:init
   (&key
    ((:cmd __cmd) "")
    ((:duration_10ms __duration_10ms) 0)
    )
   (send-super :init)
   (setq _cmd (string __cmd))
   (setq _duration_10ms (round __duration_10ms))
   self)
  (:cmd
   (&optional __cmd)
   (if __cmd (setq _cmd __cmd)) _cmd)
  (:duration_10ms
   (&optional __duration_10ms)
   (if __duration_10ms (setq _duration_10ms __duration_10ms)) _duration_10ms)
  (:serialization-length
   ()
   (+
    ;; string _cmd
    4 (length _cmd)
    ;; uint8 _duration_10ms
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _cmd
       (write-long (length _cmd) s) (princ _cmd s)
     ;; uint8 _duration_10ms
       (write-byte _duration_10ms s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _cmd
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _cmd (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint8 _duration_10ms
     (setq _duration_10ms (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get robot::robot_cmd :md5sum-) "0dc039100dce1fd03db0d90732bfee7d")
(setf (get robot::robot_cmd :datatype-) "robot/robot_cmd")
(setf (get robot::robot_cmd :definition-)
      "string cmd
uint8 duration_10ms

")



(provide :robot/robot_cmd "0dc039100dce1fd03db0d90732bfee7d")


