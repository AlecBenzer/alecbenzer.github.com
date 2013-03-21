---
layout: page
---
{% for post in site.posts %}
  <div class="post-div">
  <span class="date">{{post.date | date: "%m/%d/%y" }}&nbsp;&nbsp;&nbsp;</span>
  <a href="{{post.url}}">{{post.title | truncate:40 | strip_html}}</a>
  <!--<div class="post-preview">{{post.content | strip_html | truncatewords: 60}}</div>-->
  </div>
{% endfor %}
