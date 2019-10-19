---
title: "alecb"
layout: page
...

# alecb

Getting computers to read x-rays @ [Imagen](https://imagen.ai)

Previously [SRE](https://google.com/sre)'d @ [Google](https://google.com/about)

[@AlecBenzer](https://twitter.com/AlecBenzer) · <alec@alecb.me>

---

{% for post in site.posts %}

{% if post.listed %}
[{{ post.title }}]({{ post.url }})
{% endif %}

{% endfor %}
