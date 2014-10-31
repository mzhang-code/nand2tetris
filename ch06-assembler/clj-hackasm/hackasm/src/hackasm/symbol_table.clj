(ns hackasm.symbol-table) 

(def symbol-table (atom {})) 

(defn clear-symbol-table 
  [] 
  (reset! symbol-table {})) 

(defn init-symbol-table 
  [] 
  (clear-symbol-table) 
  (doseq [i (range 16)] 
    (swap! symbol-table assoc (keyword (format "R%d" i)) i)
  (swap! symbol-table merge {:alloc   16
                             :SP      0
                             :LCL     1 
                             :ARG     2
                             :THIS    3 
                             :THAT    4 
                             :SCREEN  16384
                             :KBD     24576}))) 

(defn insert-symbol-table 
  [sym & args] 
  (cond 
    (= 0 (count args)) 
      (let 
        [addr (:alloc @symbol-table)]
        (swap! symbol-table assoc (keyword sym) addr)
        (swap! symbol-table update-in [:alloc] inc)
        addr) 
    :else 
      (swap! symbol-table assoc (keyword sym) (first args)))) 

(defn query-symbol-table 
  [sym] 
  (cond 
    (contains? @symbol-table (keyword sym)) ((keyword sym) @symbol-table)
    :else (insert-symbol-table sym))) 

