
(cl:in-package :asdf)

(defsystem "vision-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "face_box" :depends-on ("_package_face_box"))
    (:file "_package_face_box" :depends-on ("_package"))
    (:file "targets" :depends-on ("_package_targets"))
    (:file "_package_targets" :depends-on ("_package"))
  ))