---
title: "alecb"
layout: page
...

# alecb

Software engineer @ [Level](https://level.com)  
Formerly [Imagen](https://imagen.ai), [Google](https://google.com/about)

<a href="https://twitter.com/AlecBenzer"><i class="fab fa-twitter-square"></i></a>
<a href="https://www.linkedin.com/in/alecbenzer"><i class="fab fa-linkedin"></i></a>
<a href="mailto:alec@alecb.me"><i class="fas fa-envelope-open-text"></i></a>
<a href="https://instagram.com/martinkittynyc"><i class="fas fa-cat"></i></a>
<a href="/feed.xml"><i class="fas fa-rss-square"></i></a>
{: .contact}

---
{: .short}

I like to write things sometimes:

{% for post in site.posts %}

    {% if post.listed %}
[{{ post.title }}]({{ post.url }})
    {% endif %}

{% endfor %}
