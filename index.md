---
layout: page
title: "Alec's Blog"
---
{% for post in site.posts %}
  <div class="post-div"><a href="{{post.url}}">{{post.title}}</a></div>
{% endfor %}
