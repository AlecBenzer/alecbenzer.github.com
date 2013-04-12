---
layout: page
title: Alec Benzer
---
<div id="bio">
<p>
<a href="http://cs.uiuc.edu">cs</a>/<a href="http://math.uiuc.edu">math</a> student @ <a href="http://uiuc.edu">uiuc</a><br />
former/future sre intern @ <a href="http://www.google.com/about">google</a>
<br />
<br />
Follow <a href="http://twitter.com/alecbenzer">@alecbenzer</a> on twitter
</p>
</div>

<hr />

## posts

{% for post in site.posts %}
  <div class="post-div">
  <!--<span class="date">{{post.date | date: "%m/%d/%y" }}&nbsp;&nbsp;&nbsp;</span>-->
  <a href="{{post.url}}">{{post.title}}</a>
  </div>
{% endfor %}
