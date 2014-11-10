(ns translator.core
  (:require [clojure.string           :as string]
            [translator.env           :as env] 
            [translator.code-snippet  :as snippet])) 

(def arith-exprs '("add" "sub" "lt" "gt" "eq" "neg" "not" "and" "or")) 

(def memop-exprs '("pop" "push")) 

(def fcall-exprs '("call" "function" "return")) 

(def flowc-exprs '("label" "goto" "if-goto")) 

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

(defn translate-fcall-expr 
  [index cmd & args] 
  (cond 
    (= cmd "call") 
      (let 
        [[fname argc] args] 
        (snippet/call-code index fname argc)) 
    (= cmd "function") 
      (let 
        [[fname localc] args] 
        (env/set-cur-func! fname) 
        (snippet/func-code fname localc)) 
    (= cmd "return") 
      (snippet/return-code))) 

(defn translate-flowc-expr 
  [cmd target] 
  (cond 
    (= cmd "label") 
      (snippet/label-code target) 
    (= cmd "goto") 
      (snippet/goto-code target) 
    (= cmd "if-goto") 
      (snippet/if-goto-code target))) 
           
(defn translate-expr
  "Translate a single expression."
  [expr-index expr-str] 
  (let 
    [expr (string/split expr-str #"\s+")] 
    (cond 
      (some #(= (first expr) %) arith-exprs)
        (translate-arith-expr (first expr) expr-index) 
      (some #(= (first expr) %) memop-exprs) 
        (apply translate-memop-expr expr)
      (some #(= (first expr) %) fcall-exprs) 
        (apply translate-fcall-expr (cons expr-index expr))
      (some #(= (first expr) %) flowc-exprs) 
        (apply translate-flowc-expr expr)
      :else 
        (println "ERROR undefined type of vm instruction" expr-str))))

