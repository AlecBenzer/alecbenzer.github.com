---
title: "alecb"
layout: page
...

# alecb

Software engineer @ [Level](https://level.com)  
Formerly [Imagen](https://imagen.ai), [Google](https://google.com/about)

<div style="text-align: center">
    <ul class="fa-ul" style="display: inline-block; text-align: left">
        <li><a href="mailto:alec@alecb.me"><span class="fa-li"><i class="far fa-envelope"></i></span>alec@alecb.me</a></li>
        <li><a href="https://twitter.com/AlecBenzer"><span class="fa-li"><i class="fab fa-twitter"></i></span>@AlecBenzer</a></li>
        <li><a href="https://www.linkedin.com/in/AlecBenzer"><span class="fa-li"><i class="fab fa-linkedin"></i></span>LinkedIn</a></li>
        <li><a href="/feed.xml"><span class="fa-li"><i class="fas fa-rss"></i></span>Feed</a></li>
        <li><a href="https://instagram.com/martinkittynyc"><span class="fa-li"><i class="fas fa-cat"></i></span>Martin</a></li>
    </ul>
</div>

---
{: .short}

*I like to write things sometimes:*

{% for post in site.posts %}

    {% if post.listed %}
[{{ post.title }}]({{ post.url }})
    {% endif %}

{% endfor %}
