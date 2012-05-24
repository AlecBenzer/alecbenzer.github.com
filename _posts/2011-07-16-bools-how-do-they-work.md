---
layout: post
title: Bools - How do they work?
---
What is it with people doing really stupid things with bools? (and if-statements) For example, the entire purpose of an if-statement is to decide whether or not an expression is true. Effectively, an if-statement is an `== true` test. Why then, do people do things like:

    if(something == true) {
        //do something
    }

Checking for truth is what an if-statement already does by itself. Why would you manually add `== true` yourself?

Worse still, I encountered this in C# once:

    if(something.ToString().Equals("True"))
    {
        //do something
    }
    else if(something.ToString().Equals("False"))
    {
        //do something else
    }

Why?? What was going through your head? Did you not know that there are `true` and `false` literals?

I also see methods like this a lot:

    boolean isGood() {
      if(this.good)
        return true;
      else
        return false;
    }

Now, granted, this could be worse, at least there isn’t `a == true`. But remember that the equality check with true is still really there, it’s just not explicity specified. This code is not completely insane because bools only have two values, but imagine if it were an int instead. That code is equivelant to something like:

    int getAmount() {
      if(this.amt == 0)
        return 0;
      else if(this.amt == 1)
        return 1;
      else if(this.amt == -1)
        return -1;
      else if(this.amt == 2)
        return 2;
      ...
      else if(this.amt == 2147483647)
        return 214783647;
      else
        return -214783647;
    }

Anyone can clearly see that the above should be written as just:

    int getAmount() {
        return this.amt;
    }
And the same goes for the bool example:

    boolean isGood() {
        return this.good;
    }

