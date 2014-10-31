(ns hackasm.core
  (:use [hackasm.inst :only [gen-ainst gen-cinst]]
        [hackasm.symbol-table :only [init-symbol-table insert-symbol-table]])
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

(defn parse-cinst 
  [expr] 
  (cond 
    (= -1 (.indexOf expr ";")) (parse-cinst (str expr ";null")) 
    (= -1 (.indexOf expr "=")) (parse-cinst (str "null=", expr)) 
    :else 
      (let 
        [[dest calc jump] (string/split expr #"[;=]")] 
        (gen-cinst calc dest jump)))) 

(defn parse-line
  [expr] 
  (cond 
    (re-find #"@" expr) (parse-ainst expr) 
    :else (parse-cinst expr)))

(defn preprocess 
  [expr-lst] 
  (loop [exprs expr-lst res '() line 0] 
    (cond 
      (empty? exprs) (reverse res) 
      :else 
        (let [e (first exprs)] 
          (cond 
            (and (.startsWith e "(") (.endsWith e ")")) 
              (do 
                (insert-symbol-table (subs e 1 (dec (count e))) line) 
                (recur (rest exprs) res line))
            :else 
              (recur (rest exprs) (cons e res) (inc line))))))) 

(defn parse 
  [lines] 
  (let 
    [exprs (filter (fn [l] (< 0 (count l))) 
                   (map remove-comment (map remove-blank lines)))] 
    (init-symbol-table) 
    (map parse-line (preprocess exprs)))) 

