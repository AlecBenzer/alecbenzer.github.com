---
layout: page
title: "Alec Benzer"
---
{% for post in site.posts %}
  <div class="post-div"><a href="{{post.url}}">{{post.title}}</a></div>
{% endfor %}
