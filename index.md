---
title: "alecb"
layout: page
...

<style>
    h1.title {
        margin-bottom: 0px;
    }
</style>

writes software @ [stripee](https://stripe.com/about)  
formerly [some](https://level.com) [startups](https://imagen.ai), [google](https://google.com/about)

<a href="mailto:hi@alecb.me"><i class="fas fa-envelope"></i></a>
<a href="https://linkedin.com/in/alecbz"><i class="fab fa-linkedin"></i></a>
<a href="https://twitter.com/alecbzr"><i class="fab fa-twitter-square"></i></a>
<a href="https://github.com/alecbz"><i class="fab fa-github"></i></a>
<a href="/feed.xml"><i class="fas fa-rss"></i></a>
{: .home-icons}

<div id="post-list">
    <ul class="fa-ul" style="margin-left: 35px; display: inline-block; text-align: left">
        <li>
            <span class="fa-li"><i class="fas fa-pen-alt"></i></span>
            <em>also writes words:</em>
            <ul class="fa-ul" style="display: inline-block; text-align: left; margin-left: 32px">
                {% for post in site.posts %}
                    {% if post.listed %}
                        <li><a href="{{ post.url }}"><span class="fa-li"><i class="fas fa-angle-double-right"></i></span>{{ post.title }}</a></li>
                    {% endif %}
                {% endfor %}
            </ul>
        </li>
    </ul>
</div>
