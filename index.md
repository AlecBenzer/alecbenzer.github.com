---
layout: page
title: "Alec Benzer"
---
# Posts

{% for post in site.posts %}
  <div class="post-div">
  <span class="date">{{post.date | date: "%m/%d/%y" }}</span>
  <a href="{{post.url}}">{{post.title}}</a>
  <div class="post-preview">{{post.content | strip_html | truncatewords: 60}}</div>
  </div>
{% endfor %}
