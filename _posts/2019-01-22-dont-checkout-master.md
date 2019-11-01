---
title: Don't checkout master locally
layout: post
listed: false
---

_tl;dr_: Don’t `git checkout master`; use topic branches and detached heads.

## Topic branches

It’s good to use so-called “topic” or “feature” branches to organize your work
into individual features, instead of committing onto what I’ll call “mainline”
or “persistent” branches directly. This is a fairly common practice, and I won’t
go into full detail on why I think it’s important, but a few good reasons:

* Ensures you have an easy way of getting back to a known good state that’s not in the middle of some new feature.
* Logically groups individual features/bug fixes.
* Easy to manage multiple concurrent changes.

## Referring to master

Even if we don’t commit directly onto a local master branch, we still often need
to refer to the _remote_ master branch to do things like:

* Start new feature branches off of master.
* Take changes that have been made to master and pull them into a feature branch.
* Do diffs against master.

So if we don’t checkout master locally, how do we these things? Easy -- git
already allows you to refer to remote branches directly, via [remote tracking
branches](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches), like
`origin/master`.

* Need to do a diff against master? `git diff origin/master`
* Need to pull in changes from master? `git merge origin/master` (usually after a `git fetch origin`; or just do `git pull origin master` in one step)
* Need to start a new branch based on master? `git branch my-new-branch origin/master`

There’s no reason to have a local master branch to do any of these things.

## Detached head

Sometimes we need more direct access to the content at master. E.g., maybe we
want to just do a build at master, without necessarily starting a new topic
branch.

We can do this using [detached
heads](https://git-scm.com/docs/git-checkout#_detached_head). In addition to
checking out branches, git lets you check out arbitrary commits. So you can
just checkout a remote tracking branch directly, with `git checkout
origin/master`.

## Why not just checkout master?

Because it’s simpler not to:

* If you checkout master locally, you now need to mentally deal with your local
  view of the remote master (`origin/master`) and your local copy of master
  (`master`), which can diverge.
* Merging with master is easier: you can just `git pull origin master`. If you
  have a local copy of master (and you don’t want it to become stale), you’d
  instead need to:

  ```bash
  git checkout master
  git pull origin master
  git checkout my-branch
  git merge master
  ```
