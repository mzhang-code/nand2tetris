(ns hackasm.core
  (:use [hackasm.inst :only [gen-ainst gen-cinst insert-symbol-table]])
  (:require [clojure.string :as string]))

(defn remove-blank 
  [s]
  (string/replace s #"\s+" "")) 

(defn remove-comment
  [s]
  (string/replace s #"//\S+" "")) 

(defn parse-ainst 
  [expr] 
  (gen-ainst (subs expr 1))) 

(defn parse-line 
  [line] 
  (let 
    [expr (remove-comment s)] 
    (cond 
      (re-find #"@" expr) (parse-ainst expr) 
      :else (parse-cinst expr)))) 

