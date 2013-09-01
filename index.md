---
layout: page
title: Alec Benzer
---
# Alec Benzer
<div id="bio">
<p>
cs student @ <a href="http://cs.uiuc.edu">uiuc</a><br />
sre intern @ <a href="http://www.google.com/about">google</a><br />
<br />
<a href="http://twitter.com/alecbenzer">twitter</a>&nbsp;&middot;&nbsp;<a href="mailto:alecbenzer@gmail.com">email</a>&nbsp;&middot;&nbsp;<a href="/feed.xml">rss</a>
</p>
</div>

## blog posts

{% for post in site.posts %}
  <div class="post-div"><span class="post-date">{{post.date | date:"%m/%d/%y"}}</span>&nbsp;&nbsp;<a href="{{post.url}}">{{post.title}}</a></div>
{% endfor %}
