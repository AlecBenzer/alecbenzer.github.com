---
layout: post
title: Ruby Levenshtein Word Distance
---
A quick ruby function to compute the Levensthein word distance betweeen two strings ([see wikipedia](http://en.wikipedia.org/wiki/Levenshtein_distance) for a description of the algorithm):

    def distance(a,b)
      matrix = Array.new(a.size + 1) { Array.new(b.size + 1) }
      (0..a.size).each { |i| matrix[i][0] = i }
      (0..b.size).each { |j| matrix[0][j] = j }
      (1..a.size).each do |i|
        (1..b.size).each do |j|
          if a[i-1] == b[j-1]
            matrix[i][j] = matrix[i-1][j-1]
          else
            matrix[i][j] = [matrix[i-1][j] + 1,matrix[i][j-1] + 1,matrix[i-1][j-1] + 1].min
          end
        end
      end
      matrix[a.size][b.size]
    end

Here's a [gist](https://gist.github.com/1062009) with the code.
