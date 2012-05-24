---
layout: post
title: Estimating Pi with Clojure
---
The following is a quick clojure program to compute the value of PI using a monte carlo method. Essentially, the program pretends it has a "dart board" inscribed in a square. It then randomly "fires" darts at the square, and records how many actually hit the dart board. With good random numbers, the ratio of dart board hits to total shots should be the ratio of the areas of the circle and the square, which is equal to `(pi * r^2)/((2r)^2) = pi/4`. So if we find the ratio and multiply it by four, we will have an estimate for pi. The average of 100 runs each with 1,000,000 shots gets within 0.005% of pi pretty consistently (runs in around 10 seconds on my 3GHz machine).

{% highlight clj %}
(defn circle-test [x y]
 (not ( > ( + (* (- x 0.5) (- x 0.5)) (* (- y 0.5) (- y 0.5))) 0.25)))

(defn error [est]
 (Math/abs (* (/ (- Math/PI est) Math/PI) 100)))

(defn pi [n]
 (loop [hits 0 total 0]
  (let [x (rand) y (rand)]
   (if (< total n)
    (recur (if (circle-test x y) (inc hits) hits) (inc total))
    (* (/ hits total) 4.0)))))

(defn estimate-pi [shots runs]
 (loop [r 0 vals ()]
  (let [est (pi shots)]
   (if (= r runs)
    (/ (reduce + vals) (count vals))
    (recur (inc r) (conj vals est))))))

(defn print-estimate [est]
 (println est)
 (println (str (error est) "%")))
{% endhighlight %}
