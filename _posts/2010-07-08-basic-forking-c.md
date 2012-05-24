---
layout: post
title: Basic Forking in C
---
Here's a quick intro to some basic multithreading in C using forks. This is by no means the best way to achieve forking (using a 3rd party library would probably be a lot more practical), but I like knowing the more basic, low-level methods for doing things.

Note that the functions we'll be using are standard for UNIX systems. If you're on windows you'll have to use something like [CygWin](http://www.cygwin.com/) to get this working.

## Forking

Forking in C is done with the `fork()` function, declared in `unistd.h`. `fork()` takes no arguments and returns a `pid_t`. When `fork()` is called, a copy is made of the current process of the program. The only difference between the original parent process and the forked child process is the return value from the `fork()`. For the child process, `fork()` returns `0`, which simply tells the child process that it is the child. For the parent process, `fork()` returns the pid of the newly created child process. If there is an error, `fork()` will return `-1`.

Here's a quick example:

{% highlight cpp %}
    #include <stdio.h>
    #include <unistd.h>

    int main()
    {
      pid_t pid = fork();
      if(pid == -1)
        fprintf(stderr,"There was an error\n");
      else if(pid == 0)
        printf("I am the child. I do not know my pid.\n");
      else
        printf("I am the parent. The child's pid is %d.\n",pid);

      return 0;
    }
{% endhighlight %}

Running this program gives this output:

    I am the parent. The child's pid is 2955.
    I am the child. I do not know my pid.

## Piping

We use piping to allow our two process to have some basic communication. Piping is done using the `pipe()` function, also declared in `unistd.h`. `pipe()` takes as its single parameter an array of two integers. If the pipe is established successfully, the first element in the array will contain a file descriptor for reading from the pipe, and the second element will contain a file descriptor for writing to the pipe. You can read up a bit on file descriptors here. In the example we'll be writing and reading to the pipe using the file descriptors and the `read()` and `write()` functions declared in `stdio.h`.

Here's some code that demonstrates piping:

{% highlight cpp %}
    #include <stdio.h>
    #include <string.h>
    #include <unistd.h>

    int main()
    {
      int pip[2];

      if(pipe(pip) == -1)
      {
        fprintf(stderr,"There was an error establishing the pipe.\n");
        return 1;
      }

      pid_t pid = fork();
      if(pid == -1)
      {
        fprintf(stderr,"There was an error forking.\n");
        return 1;
      }

      char buffer[80];

      if(pid == 0)
      {
        char* msg = "This is a message from the child: Hello!";
        write(pip[1],msg,strlen(msg)+1);
      }
      else
      {
        read(pip[0],buffer,sizeof(buffer));
        printf("The parent received this string from the child: \"%s\"\n",buffer);
      }
      return 0;
    }
{% endhighlight %}
