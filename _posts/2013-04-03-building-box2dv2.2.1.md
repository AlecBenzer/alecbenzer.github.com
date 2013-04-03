---
layout: "post"
title: "Building Box2D v2.2.1 on linux"
---

The latest release version of Box2D at the time of writing (2.2.1) is kind of a bitch to install. Here's a guide.

Box2D uses premake4 v4.4 to build. To get it, go to [premake's site](http://industriousone.com/premake), click "Download", and grab the **4.4** version tar.gz for linux. The tar contains a single `premake4` binary, which you should just copy to some safe place.

{% highlight text %}
$ tar xvzf premake-4.4-beta4-linux.tar.gz
$ mkdir -p ~/bin
$ mv premake4 ~/bin
{% endhighlight %}

Again, make sure you grab version **4.4** which is (currently) the beta release, not the stable release. If you get 4.3 or something earlier, you'll probably end up with some error about a nil vpath

{% highlight text %}
/path/to/Box2D_v2.2.1/premake4.lua:26: attempt to call global 'vpaths' (a nil value)
{% endhighlight %}

Ok, now that you have premake, grab the Box2D code from [here](http://code.google.com/p/box2d/downloads/detail?name=Box2D_v2.2.1.zip&can=2&q=) (you might want to check if a version more recent than 2.2.1 has been released [here](http://code.google.com/p/box2d/downloads/list), in which case this post may be obsolete). Unzip, go to the main directory, and run premake:

{% highlight text %}
$ unzip Box2D_v2.2.1.zip
$ cd Box2D_v2.2.1
$ ~/bin/premake4 gmake
{% endhighlight %}

This will generate a Makefile along with a bunch of .make files in `Box2D_v2.2.1/Build/gmake/`. You will need to make some changes to these files.

First, open `Box2D_v2.2.1/Build/gmake/HelloWorld.make`, and search for "Helloworld.cpp". There should be only one occurence. This is a typo -- it should be "Hello**W**orld.cpp" (ie, capital 'W'). Make that change, so the line looks like this:

{% highlight text %}
$(OBJDIR)/Helloworld.o: ../../HelloWorld/HelloWorld.cpp
{% endhighlight %}

The next change involves GLUT, and might be system specific. But, on my system, the name of the glut library is `libglut.so`, and so should be linked to with `-lglut`, but Testbed.make links to it with `-lGLUT`. So you'll have to change that in `Testbed.make` -- it appears twice.

{% highlight text %}
LIBS      += bin/Debug/libBox2D.a bin/Debug/libGLUI.a -lX11 -lGL -lGLU -lglut
...
LIBS      += bin/Release/libBox2D.a bin/Release/libGLUI.a -lX11 -lGL -lGLU -lglut
{% endhighlight %}

Obviously, you also have to have glut installed. On Ubuntu 12.10 you can install it with

{% highlight text %}
sudo apt-get install freeglut3-dev
{% endhighlight %}

Package repositories on other distros will probably have freeglut as well. Worse comes to worse, you can just [grab and install freeglut directly](http://freeglut.sourceforge.net/).

After these changes are made, run make from `Box2D_v2.2.1/Build/gmake/`.

{% highlight text %}
$ cd /path/to/Box2D_v2.2.1/Build/gmake/
$ make config="debug"
{% endhighlight %}

You should get a bunch of output (and hopefully no errors) and then you're done! Try running the testbed

{% highlight text %}
$ ./bin/Debug/Testbed
{% endhighlight %}

If something doesn't work, or you had to take some additional steps to get things working, feel free to [let me know](mailto:alecbenzer@gmail.com), and I'll update the post accordingly.
