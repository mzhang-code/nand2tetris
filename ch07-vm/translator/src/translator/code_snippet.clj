(ns translator.code-snippet
  (:require [translator.env :as env])) 

(defn init-code 
  [] 
  '("@256" "D=A" "@SP" "M=D")) 

(defn push-code 
  [seg index]
  (let 
    [assignment '("@SP" 
                  "A=M" 
                  "M=D"
                  "@SP" 
                  "M=M+1")] 
    (concat 
      (cond 
        (= seg "constant") `(~(str "@" index) 
                             "D=A")
        (= seg "argument") `("@ARG"
                             "D=M" 
                             ~(str "@" index) 
                             "A=D+A" 
                             "D=M")
        (= seg "local")    `("@LCL"
                             "D=M" 
                             ~(str "@" index) 
                             "A=D+A" 
                             "D=M")
        (= seg "this")     `("@THIS"
                             "D=M" 
                             ~(str "@" index) 
                             "A=D+A" 
                             "D=M")
        (= seg "that")     `(~(str "@THAT") 
                             "D=M" 
                             ~(str "@" index) 
                             "A=D+A" 
                             "D=M")
        (= seg "pointer")   `(~(cond (= index "0") "@THIS" :else "@THAT") 
                              "D=M")

        (= seg "temp")      `("@R5"
                              "D=A" 
                              ~(str "@" index) 
                              "A=D+A" 
                              "D=M")
        (= seg "static")    `(~(str "@" (env/cur-vm-file) "." index) 
                              "D=M"))
      assignment)))

(defn pop-code 
  [seg index] 
  (let 
    [assignment `("D=M" 
                  ~(str "@" index) 
                  "D=D+A" 
                  "@R13" 
                  "M=D" 
                  "@SP" 
                  "AM=M-1" 
                  "D=M" 
                  "@R13" 
                  "A=M" 
                  "M=D")] 
      (cond 
        (= seg "local")     (concat '("@LCL")      assignment)    
        (= seg "argument")  (concat '("@ARG")      assignment)
        (= seg "this")      (concat '("@THIS")     assignment) 
        (= seg "that")      (concat '("@THAT")     assignment)
        (= seg "pointer")   `("@SP" 
                              "AM=M-1" 
                              "D=M" 
                              ~(cond (= index "0") "@THIS" :else "@THAT")
                              "M=D")

        (= seg "temp")      `("@R5" 
                              "D=A"
                              ~(str "@" index)
                              "D=D+A"
                              "@R13" 
                              "M=D" 
                              "@SP" 
                              "AM=M-1" 
                              "D=M" 
                              "@R13" 
                              "A=M"
                              "M=D") 

        (= seg "static")    `("@SP" 
                              "AM=M-1"
                              "D=M" 
                              ~(str "@" (env/cur-vm-file) "." index) 
                              "M=D")))) 

(defn unary-arith-code 
  [cmd] 
  (let 
    [access-oprand '("@SP"
                     "A=M-1")] 
    (concat access-oprand 
            (cond 
              (= cmd "not") '("M=!M") 
              (= cmd "neg") '("D=0"
                              "M=D-M"))))) 

(defn binary-arith-code 
  [cmd] 
  (let 
    [access-oprands '("@SP" 
                      "AM=M-1" 
                      "D=M"
                      "A=A-1")] 
    (concat access-oprands 
            (cond 
              (= cmd "add") '("M=M+D") 
              (= cmd "sub") '("M=M-D") 
              (= cmd "and") '("M=M&D") 
              (= cmd "or")  '("M=M|D"))))) 

(defn get-cmp-op 
  [cmp] 
  (cond 
    (= cmp "gt") "JLE" 
    (= cmp "lt") "JGE" 
    (= cmp "eq") "JNE")) 

(defn binary-cmp-code 
  [cmd index] 
  (let 
    [op (get-cmp-op cmd)] 
    `("@SP" 
      "AM=M-1"
      "D=M" 
      "A=A-1"
      "D=M-D"
      ~(str "@FALSE-" (env/cur-vm-file) "." index) 
      ~(str "D;" op)
      "@SP" 
      "A=M-1" 
      "M=-1"
      ~(str "@CONTINUE-" (env/cur-vm-file) "." index) 
      "0;JMP" 
      ~(str "(FALSE-" (env/cur-vm-file) "." index ")")
      "@SP" 
      "A=M-1" 
      "M=0"
      ~(str "(CONTINUE-" (env/cur-vm-file) "." index ")"))))

