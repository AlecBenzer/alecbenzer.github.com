---
title: Don't checkout master locally
layout: post
...

It’s common to use short-lived branches to organize your work into individual
features, instead of committing directly onto persistent "mainline" branches
like `master`. This:

* Ensures you have an easy way of getting back to a known good state that’s not in the middle of some new feature
* Logically groups individual features/bug fixes
* Makes it easy to manage multiple concurrent changes

But even if you don’t commit directly onto a local master branch, you still
often need to refer to the _remote_ master branch to do things like:

* Start new feature branches off of master.
* Take changes that have been made to master and pull them into a feature branch.
* Do diffs against master.

You don't need to have a locally checked out master branch to do any of that:
git already allows you to refer to remote branches directly, via [remote
tracking branches](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches), like
`origin/master`.

* Need to do a diff against master? `git diff origin/master`
* Need to pull in changes from master? `git merge origin/master` (usually after a `git fetch origin`; or just do `git pull origin master` in one step)
* Need to start a new branch based on master? `git branch my-new-branch origin/master`

Sometimes you need more direct access to the content at master. E.g., maybe
you want to just do a build at master, without necessarily starting a new
topic branch.

You can do this using [detached
heads](https://git-scm.com/docs/git-checkout#_detached_head). In addition to
checking out branches, git lets you check out arbitrary commits. So you can
just checkout a remote tracking branch directly, with `git checkout
origin/master`.

Why not just checkout master? Because it’s simpler not to: If you checkout
master locally, you now need to mentally deal with your local view of the
remote master (`origin/master`) and your local copy of master (`master`),
which can diverge.

E.g., without a local master branch, bringing in changes from master is `git
pull origin master`. If you have a local copy of master (and you don’t want
it to become stale), you’d instead need to:

```bash
# starting with a feature branch checked out
git checkout master
git pull origin master
git checkout -
git merge master
```
