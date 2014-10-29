(ns hackasm.main
  (:require 
    [hackasm.core :as core])
  (:gen-class))

(defn -main
  []
  (core/foo "Mengyu Zhang")) 

