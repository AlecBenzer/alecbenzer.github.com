---
layout: post
title: "Salty now uses PBKDF2"
---

[Salty](http://github.com/alecbenzer/salty) now uses [PBKDF2](http://en.wikipedia.org/wiki/PBKDF2) via the [pbkdf2 ruby gem](https://rubygems.org/gems/pbkdf2). Usage is still identical, but PBKDF2 should be a bit more secure than the iterated SHA512 that previous versions used.

There's now just a single `salted_hash` function that looks like this:

{% highlight ruby %}
def Salty.salted_hash(str,salt)
  pbkdf2 = PBKDF2.new(:password => str, :salt => salt, :iterations => 1000)
  pbkdf2.hex_string
end
{% endhighlight %}

as opposed to previously:

{% highlight ruby %}
def Salty.hash_fn(str)
  sha512 = Digest::SHA2.new(512)
  sha512.hexdigest(str)
end

def Salty.salted_hash(str,salt)
  res = str
  100.times do
    res = hash_fn(res+salt)
  end
  res
end
{% endhighlight %}

Again, this is all just implementation-level stuff. You still just encrypt with `Salty.hash` and check with `Salty.check` (as described [here](/blog/salty-hashing)).

You'll also notice the number of iterations has been raised from 100 to 1000. I might play around with varying the number of iterations based on the string length, if that does anything for security.

I might also add support for keeping track of what method was used to encrypt a particular string, as to maintain backwards compatibility with older versions, if the encryption method changes again. Right now you should _not_ upgrade to 0.1 from 0.0.&#42;, or else you'll be comparing PBKDF2 output to SHA512 output.
