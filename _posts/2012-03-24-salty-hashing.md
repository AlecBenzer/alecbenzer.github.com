---
layout: post
title: Salty Hashing
---
I threw up a stupid little gem the other day for salted hashing. It's called [salty](https://rubygems.org/gems/salty) (I couldn't believe that wasn't taken). Anyway, it's nothing too special, I just got tired of constantly re-implementing password hashing code.

Just `gem install salty` to get it. Or you can just grab the one source file if you want, it's less than 1KB

    $ wget https://raw.github.com/alecbenzer/salty/master/lib/salty.rb

Usage is pretty simple:

{% highlight ruby %}
require 'salty'

password = Salty.hash('thisismypassword')

Salty.check('thisismypassword',password) # => true
Salty.check('notmypassword',password) # => false
{% endhighlight %}

`Salty.hash` does an iterative salted SHA512 hash. The salt is randomly generated and emebded into the output hash, which `Salty.check` then extracts, so you don't need to worry about it yourself.

Do realize though that `Salty.hash` isn't like a normal hash function. Namely, repeated calls to it will generate different outputs (because each call generates a different salt), so things like `Salty.hash(str) == Salty.hash(str)` won't work. You always need to use `Salty.check`.

You can check out the source on [github](https://github.com/alecbenzer/salty).
