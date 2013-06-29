---
layout: page
title: Alec Benzer
---
## Alec Benzer
<div id="bio">
<p>
sre intern @ <a href="http://www.google.com/about">google</a><br />
cs student @ <a href="http://cs.uiuc.edu">uiuc</a><br />
<br />
<a href="http://twitter.com/alecbenzer">twitter</a> &middot; <a href="mailto:alecbenzer@gmail.com">email</a> &middot; <a href="/feed.xml">rss</a>
</p>
</div>

## blog posts

{% for post in site.posts %}
  <div class="post-div"><a href="{{post.url}}">{{post.title}}</a></div>
{% endfor %}
