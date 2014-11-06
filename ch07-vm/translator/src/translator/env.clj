(ns translator.env
  (:require [clojure.string :as string])) 

(def vm-file (atom "DEFAULT")) 

(defn file-name
  [path] 
  (first (reverse (string/split path #"/")))) 

(defn set-vm-file! 
  [path] 
  (reset! vm-file (file-name path))) 

(defn cur-vm-file 
  [] 
  @vm-file) 

