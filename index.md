---
layout: page
title: "Alec Benzer"
---
# Posts

{% for post in site.posts %}
  <div class="post-div"><a href="{{post.url}}">{{post.title}}</a>
<span class="date">{{post.date | date: "%B %-d, %Y" }}</span>
</div>
{% endfor %}
