(ns translator.env
  (:require [clojure.string :as string])) 

(def vm-file    (atom "DEFAULT")) 
(def func-name  (atom "__MAIN__"))

(defn file-name
  [path] 
  (-> path 
      (string/split #"/")
      (reverse) 
      (first) 
      (string/split #"\.") 
      (first))) 

(defn set-vm-file! 
  [path] 
  (reset! vm-file (file-name path))) 

(defn set-cur-func!
  [fname] 
  (reset! func-name fname)) 

(defn cur-vm-file 
  "The current file name being parsed."
  [] 
  @vm-file) 

(defn cur-func-name 
  "The current function name being parsed."
  [] 
  @func-name) 
