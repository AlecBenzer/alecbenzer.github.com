---
layout: page
title: Alec Benzer
---
# Alec Benzer

(soon-to-be) site reliability engineer at [google]  
former [cs] and [math] student at [uiuc]

[alecbenzer@gmail.com](mailto:alecbenzer@gmail.com)  
[rss feed](/feed.xml)

## blog posts

{% for post in site.posts %}
  <div style="margin-bottom: 0.8em;"><a href="{{post.url}}">{{post.title}}</a></div>
{% endfor %}

[google]: http://google.com/about/company
[cs]: http://cs.uiuc.edu
[math]: http://math.uiuc.edu
[uiuc]: http://uiuc.edu
