---
title: "How to value startup equity"
layout: post
listed: false
...

The standard answer is "value it at $0".

This is dumb and obviously wrong. *No one* values their startup equity at $0. Here's how to check: ask someone if they'll give you their startup equity in exchange for $0. If they won't, they value their equity at more than $0.

Maybe ask them if they'll give it up for $1? They still won't, so they must value it at more than $1. $1,000? For most people, still no. $1,000,000? For a lot of people, yes.

I'm being cranky; I get that the ethos behind "value startup equity at $0" is something like "don't *expect* that your equity will be worth anything" or "there's a high, probably >50% chance that your equity will be worth $0".

This is true, but "value your equity at $0" is a bad general way of phrasing this. When you're trying to see if you can afford to buy a house this year, yes, startup equity is worth $0. If you're trying to decide if you're being shafted by accepting 0.001% equity in a startup you're set on joining, startup equity is not worth $0.

## Break-even valuations

(The rest of this post is mostly about VC-backed startups.)

In general, you value equity based on how successful you think the company will be. I try to look specifically at opportunity costs and break-even points:

- I could be making $A working at some large tech company
- Instead, a startup is offering me $B and X% equity
- $B is probably less than $A, so you have an opportunity cost of $A - $B
    - If it's not, go to [levels.fyi](https://www.levels.fyi/), convince yourself you could probably get a job at a big tech co if you put your mind to it, and use that number instead
- Now, see what value the startup would have to be worth for your X% equity to cover that cost, decide how likely you think that is, and make a decision based on that.

For example:

- [An L3 at Google makes about $180k/year](https://www.levels.fyi/salary/Google/SE/L3/)
    - (This includes stock, but that's fine, because Google stock is basically just cash, unlike a startup's stock.)
- Say a startup offers you $80k/year, plus .01% equity *over 4 years*
    - That's .01% / 4 = .0025% equity per year
- Your opportunity cost per year is $180k - $80k = $100k
- In order for your .0025% to cover that $100k, the company would need to be worth $100k / .0025% = $4 billion
- How likely do you think it is that this company will be worth at least $4 billion?
    - Remember that this is the *break-even* point. You're taking a risk by joining the startup, so ideally your return is better than break-even.

On the other hand, if the company offered you:

- .1% equity, your break-even is $400 million
- 1% equity, $40 million
- 5% equity, $8 million

Similarly, if they kept the equity at .01% but raised the salary to:

- $100,000, your break-even is $3.2 billion
- $120,000, $2.4 billion
- $170,000, $400 million
- $175,000, $200 million

At $180,000, you've already broke even, because at that point you have "no risk". Of course that's not quite true, a startup is always going to carry more risk than a stable company (i.e., that you'll lose your job suddenly).
{: .info}

This model isn't perfect, but I like it, mostly because it boils down to a
single number (the break-even valuation) before having to introduce any
probabilistic reasoning. It doesn't tell you anything about how to decide if
a company is actually going to be worth $X, but at least quantifies the
situation in a way that I think makes things more accessible and easier to
reason about.

The break-even valuation is what people are calculating when they infer valuations based on venture capital investment. If a VC invests $X for Y% of a company, their "valuation" of the company is $X / Y%. A startup employee's "valuation" in this way is almost always going to be way higher than the VC valuation (the VC is getting a better deal than employees).
{: .info}

One thing I skipped: usually, startups aren't giving you shares directly but are giving you [options](https://www.investopedia.com/terms/s/stockoption.asp): the option to buy a share at some set price/share $X, the "strike price". You should in theory factor this into your math, but the opportunity costs are usually so much higher than the strike that it doesn't change things too much.
{: .info}

## Dilution

Unfortunately, another probabilistic factor you need to account for is [dilution](https://www.investopedia.com/terms/d/dilution.asp).

When a company says they're giving you X%, what they mean is that they're
giving you an amount of shares that, *as of right now*, represents X% of the
company. But the total number of shares can increase over time, which means
the % that your shares represent goes down.

The main way new shares get created is during fundraising: the company wants
money from investors, investors want shares in the company, so the company
creates new shares to give to the investors.

How much you get diluted, then, has to do with:

1. How much money the company needs/wants.
2. How highly investors value the company.

Which in turn has to do with how well the company is doing and how old it is.

Keeping with the "staying away from telling you how to value a company" thing, my rule of thumb is just to assume 
