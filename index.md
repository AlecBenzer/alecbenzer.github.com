---
layout: page
title: Alec Benzer
---
# Alec Benzer

site reliability engineer at [google]  
former [cs] and [math] student at [uiuc]

[alecbenzer@gmail.com](mailto:alecbenzer@gmail.com)

## blog posts

{% for post in site.posts %}
{{post.date | date: "%b, %-d %Y"}}&nbsp;&nbsp;•&nbsp;&nbsp;[{{post.title}}]({{post.url}})
{% endfor %}

[google]: http://google.com/about/company
[cs]: http://cs.uiuc.edu
[math]: http://math.uiuc.edu
[uiuc]: http://uiuc.edu
