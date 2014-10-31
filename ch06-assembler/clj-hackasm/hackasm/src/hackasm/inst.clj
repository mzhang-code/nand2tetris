(ns hackasm.inst 
  (:require [clojure.string :as string]
            [hackasm.symbol-table :refer :all])) 

(def word-length 16) 

(defn int-to-bits
  [x] 
  (cond 
    (> x 0) (cons (mod x 2) (int-to-bits (quot x 2)))
    :else '())) 

(defn zfill 
  [s, len] 
  (cond 
    (< (count s) len) (str (apply str (repeat (- len (count s)) "0")) s) 
    :else s)) 

(defn gen-ainst
  [addr] 
  (let 
    [imm (read-string addr)]
    (cond 
      ; addr is imm 
      (integer? imm) 
        (zfill (string/reverse (apply str (int-to-bits imm))) word-length) 
      ; addr is LABEL 
      :else (gen-ainst (str (query-symbol-table addr)))))) 

(def ctype-calc-table {:0     "0101010", 
                       :1     "0111111", 
                       :-1    "0111010", 
                       :D     "0001100",
                       :A     "0110000", 
                       :!D    "0001101",
                       :!A    "0110001", 
                       :-D    "0001111", 
                       :-A    "0110011", 
                       :D+1   "0011111", 
                       :A+1   "0110111", 
                       :D-1   "0001110", 
                       :A-1   "0110010",  
                       :D+A   "0000010",  
                       :D-A   "0010011",  
                       :A-D   "0000111", 
                       :D&A   "0000000", 
                       :D|A   "0010101", 
                       :M     "1110000",   
                       :!M    "1110001",   
                       :-M    "1110011",    
                       :M+1   "1110111",    
                       :M-1   "1110010",    
                       :D+M   "1000010",    
                       :D-M   "1010011",    
                       :M-D   "1000111",   
                       :D&M   "1000000",   
                       :D|M   "1010101"})

(def ctype-jump-table {:null  "000", 
                       :JGT   "001",  
                       :JEQ   "010", 
                       :JGE   "011", 
                       :JLT   "100", 
                       :JNE   "101", 
                       :JLE   "110", 
                       :JMP   "111"}) 

(def ctype-dest-table {:null  "000", 
                       :M     "001", 
                       :D     "010",  
                       :MD    "011",  
                       :A     "100", 
                       :AM    "101", 
                       :AD    "110", 
                       :AMD   "111"}) 

(defn gen-cinst
  [calc dest jump] 
  (let 
    [calc-str ((keyword calc) ctype-calc-table) 
     dest-str ((keyword dest) ctype-dest-table) 
     jump-str ((keyword jump) ctype-jump-table)] 

    (str "111" calc-str dest-str jump-str))) 

