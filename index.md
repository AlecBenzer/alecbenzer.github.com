---
title: "alecb"
layout: page
...

# alecb

Software engineer @ [Level](https://level.com)  
Formerly [Imagen](https://imagen.ai), [Google](https://google.com/about)

[@AlecBenzer](https://twitter.com/AlecBenzer) · [LinkedIn](https://www.linkedin.com/in/alecbenzer/) · <alec@alecb.me>

---
{: .short}

I like to write things sometimes:

{% for post in site.posts %}

{% if post.listed %}
[{{ post.title }}]({{ post.url }})
{% endif %}

{% endfor %}
