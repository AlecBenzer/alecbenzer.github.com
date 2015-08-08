---
layout: page
title: Alec Benzer
---
# Alec Benzer

site reliability engineer at [google]  
former [cs] and [math] student at [uiuc]

[alecbenzer@gmail.com](mailto:alecbenzer@gmail.com)&nbsp;&nbsp;&middot;&nbsp;&nbsp;[feed](/feed.xml)

## blog posts

{% for post in site.posts %}
{{post.date | date: "%m/%d/%Y"}}&nbsp;&nbsp;•&nbsp;&nbsp;[{{post.title}}]({{post.url}})
{% endfor %}

[google]: http://google.com/about/company
[cs]: http://cs.uiuc.edu
[math]: http://math.uiuc.edu
[uiuc]: http://uiuc.edu
