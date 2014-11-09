(ns translator.main 
  (:require [clojure.java.io :as io] 
            [clojure.string :as string] 
            [translator.core :as core]
            [translator.env :as env]) 
  (:gen-class)) 

(defn rm-comment 
  "Remove comment from a line."
  [line]
  (string/replace line #"\s*//.*" "")) 

(defn rm-empty-lines 
  [lines] 
  (filter (fn [l] (not (empty? l))) lines)) 

(defn trim-expr 
  "Remove leading and trailing spaces from expression string." 
  [expr-str] 
  (string/replace expr-str #"(^\s+)|(\s+$)" "")) 

(defn translate-exprs 
  [lines] 
  (->> lines 
       (map rm-comment) 
       (map trim-expr) 
       (rm-empty-lines) 
       (map-indexed vector) 
       (mapcat (fn [args] (apply core/translate-expr args))))) 

(defn -main 
  [file] 
  (env/set-vm-file! file) 
  (with-open [rdr (io/reader file)] 
    (println (string/join "\n" (translate-exprs (line-seq rdr)))))) 

