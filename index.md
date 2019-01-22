---
title: "alecb"
layout: page
---
# alecb

I'm a software engineer at [Imagen](https://imagen.ai). ([Come work with me](https://imagen.ai/careers)!)

Before that, I was an [SRE](https://google.com/sre) at  [Google](https://google.com/about).

<i class="fa fa-envelope" aria-hidden="true"></i> <alec@alecb.me>  

---

{% for post in site.posts %}
  [{{ post.title }}]({{ post.url }}) - <i>{{ post.date | date: "%Y-%m-%d"}}</i>
{% endfor %}
