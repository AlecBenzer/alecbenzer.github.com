---
title: "alecb"
layout: page
...

# alecb

Software engineer @ [Level](https://level.com)  
Formerly [Imagen](https://imagen.ai), [Google](https://google.com/about)

<a href="mailto:hi@alecb.me"><i class="fas fa-envelope"></i></a>
<a href="https://www.linkedin.com/in/alecbenzer"><i class="fab fa-linkedin"></i></a>
<a href="https://news.ycombinator.com/user?id=alecbenzer"><i class="fab fa-hacker-news"></i></a>
<a href="https://instagram.com/martinkittynyc"><i class="fas fa-cat"></i></a>
<a href="/feed.xml"><i class="fas fa-rss"></i></a>
{: .home-icons}

<div style="text-align: center">
    <em>I like to write things sometimes:</em>
    <ul class="fa-ul" style="display: inline-block; text-align: left">
        {% for post in site.posts %}
            {% if post.listed %}
                <li><a href="{{ post.url }}"><span class="fa-li"><i class="fas fa-angle-double-right"></i></span>{{ post.title }}</a></li>
            {% endif %}
        {% endfor %}
    </ul>
</div>
