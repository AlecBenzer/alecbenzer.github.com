---
layout: post
title: "A nice little metaphor for the halting problem"
---
Imagine a company that employs a man named Bob. This company is interested in finding out how people will react to seeing particular images, and they use Bob to figure this out. Bob is given a picture of a person and a second picture, and Bob somehow is able to determine how the pictured person will react to seeing the other picture.

Now, in this universe, "react" has a precise, somewhat odd meaning. When a person is shown a picture, they begin to reflect on it. Sometimes, after reflecting, a person will decide they like the picture, and sometimes they will decide they do not like it. However, there is no guarentee that they will ever come to either decision. Some people might just be so confused or enthralled or whatever by a picture that they see that they will never really be able to come up with an opinion on it.

So now back to Bob. Bob gets these pairs of pictures and has to decide how the pictured person will react to the other picture. The company employs Bob for this position not only because he is always right, but because he can never become confused. It might take him a while, but when shown a pair of pictures, Bob can _always_ determine how the pictured person will react to the other picture, even if the reaction is "they will remain confused by the picture indefinitely".

One day, the company's interests change. Now, instead of giving Bob a picture of a person and some random other picture, they give him a single picture of a person, and they ask Bob how the pictured person will react to viewing their own picture. Bob has no trouble with this, since there's nothing particularlly special about a picture that _happens_ to also be a picture of person.

So Bob goes on with his assignments. Bob likes his job very much. He likes it to the extent that he dislikes all other pictures except pictures related to his job (that is, pictures of people). Furthermore, Bob is saddened by people that do not like their own pictures. Therefore, whenever Bob sees a picture of someone who would not like seeing their own picture, Bob in turn also dislikes that picture. On the other hand, Bob is happy when he sees a picture of someone that would enjoy seeing their own picture.

Now, this is when things get interesting. The company assigns Bob a manager, John. John is a blind man, and thus, can form no opinions of pictures just by looking at them. Instead, when presented with a picture, John passes the picture along to Bob. Bob looks at the picture, and Bob tells John whether the picture makes him happy or sad. John, however, does not like Bob. Bob's happiness makes John sad, and Bob's saddness makes John happy. Bob knows this. In fact, because of Bob's seemingly magic ability to know how people react to pictures, Bob _must_ know this about John, because otherwise, Bob would not be able to predict how John would react to a picture.

Now one day, John gets curious, and decides to take a picture of himself. He does so, and attempts to react to it. But, being blind, John must give the picture to Bob so that John can know his own reaction to the picture. So he does.

What does Bob say?

On the one hand, Bob might say that John would react positively to his own picture. If this were the case, however, then Bob himself would be made happy by looking at John's picture. And John, being the spiteful man that he is, would then become sad, which would render Bob's prediction incorrect.

On the other hand, Bob might say that John would react negatively to his own picture. But if this were the case, Bob would be made sad from looking at John's picture, which would in turn make John happy. So Bob's prediction is still incorrect.

This logical paradox is a metaphor for the following theorem: There is no program (turing machine) that can take as input another program (turing machine) and input to feed into that program, and then determine whether the program will accept the input it is given. In other words, Bob cannot exist.

The fundamental issue here has something to do with looping. If indefinite looping was not allowed (ie, if people always had to arrive at a conclusive opinion about a picture they saw), then we could construct a program like the one described in the paragraph above. All we would have to do is run through the program we're given, simulating it, and then see what happens when it stops.

The problem is that we don't know whether or not any given program will loop forever when presented with a particular input. This problem is known as [the halting problem](http://en.wikipedia.org/wiki/Halting_problem). If you digested everything above, it's actually very easy to prove that the halting problem can't be solved by any program.

The entire story with Bob and John proves that there cannot be any program that, given another program and input to that program, determines whether or not that program "accepts" its input. This is because if such a program did exist, we would arrive at a logical contradiction. But a few paragraphs above, I explained how, if it is possible to make a program that solves the halting problem, then we can also make a program that solves the problem of deciding whether a particular program likes a particular input (ie, Bob's problem). Since we know there can't be any program that solves Bob's problem, we also know that there can't be any program that solves the halting problem.
