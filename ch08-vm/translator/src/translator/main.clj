(ns translator.main 
  (:require [clojure.java.io          :as io] 
            [clojure.string           :as string] 
            [translator.core          :as core]
            [translator.env           :as env]
            [translator.code-snippet  :as code-snippet]) 
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

(defn translate-vm-file
  [file] 
  (with-open [rdr (io/reader file)] 
    (env/set-vm-file! file) 
    (let 
      [exprs (->> rdr
                  (line-seq) 
                  (map rm-comment)
                  (map trim-expr) 
                  (rm-empty-lines) 
                  (map-indexed vector))] 
      (doall (mapcat #(apply core/translate-expr %) exprs))))) 

(defn -main 
  [proj-dir] 
  (let 
    [files (.list (io/file proj-dir))] 
    (->> files 
         (filter #(.endsWith % ".vm")) 
         (map #(str proj-dir "/" %)) 
         (mapcat #(translate-vm-file %)) 
         (concat (code-snippet/init-code)) 
         (string/join "\n") 
         (println)))) 

