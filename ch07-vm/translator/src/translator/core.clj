(ns translator.core
  (:require [clojure.string :as string]
            [translator.code-snippet :as snippet])) 

(def arith-exprs '("add" "sub" "lt" "gt" "eq" "neg" "and" "or")) 

(def memop-exprs '("pop" "push")) 

(defn translate-arith-expr
  [cmd index] 
  (cond 
    (some #(= cmd %) '("add" "sub" "and" "or")) (snippet/binary-arith-code cmd) 
    (some #(= cmd %) '("not" "neg")) (snippet/unary-arith-code cmd) 
    (some #(= cmd %) '("gt" "lt" "eq")) (snippet/binary-cmp-code cmd index)))

(defn translate-memop-expr 
  [cmd seg index] 
  (cond 
    (= cmd "push") 
      (snippet/push-code seg index) 
    (= cmd "pop") 
      (snippet/pop-code seg index))) 

(defn translate-expr
  "Translate a single expression."
  [expr-index expr-str] 
  (let 
    [expr (string/split expr-str #"\s+")] 
    (cond 
      (some #(= (first expr) %) arith-exprs)
        (translate-arith-expr (first expr) expr-index) 
      (some #(= (first expr) %) memop-exprs) 
        (translate-memop-expr (first expr) (fnext expr) (fnext (next expr)))
      :else 
        (println "ERROR undefined type of vm instruction" expr-str)))) 

