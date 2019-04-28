---
title: My git aliases
layout: post
...

### `new` & `master`

`git new` creates a new branch based on current (i.e., up-to-date) `origin/master`:

```bash
git fetch -q origin master
git branch ${1:?} origin/master
git checkout ${1:?}
```

`git master` checks out current `origin/master` (as a detached head). (See
also ["Don't checkout master locally"](/dont-checkout-master).)

```bash
git fetch -q origin master
git checkout origin/master
```

Copy/paste:

```bash
git config --global alias.new '!f(){ git fetch -q origin master && git branch ${1:?} origin/master && git checkout ${1:?};};f'
git config --global alias.master '!f(){ git fetch -q origin master && git checkout origin/master;};f'
```

### `stow`/`unstow`

Like a branch-specific "stash". I think many people initially assume `git
stash` will behave kind of like this, but the stash is shared across all
branches.

`git stow` either saves your pending changes in a commit with message "stow",
or, if you've already stowed changes, ammends the stow commit with your new
changes.

```bash
if [[ $(git log -1 --format=%B) == stowed ]]; then
  git commit -a --amend --no-edit
else
  git commit -a -m stowed
fi
```

`git unstow` undoes a stowed commit (by resetting to the commit before it):

```bash
if [[ $(git log -1 --format=%B) == stowed ]]; then
  git reset @^
else
  echo "Nothing to unstow"
fi
```

Copy/paste:

```bash
git config --global alias.stow '!f(){ if [[ $(git log -1 --format=%B) == "stowed" ]]; then git commit -a --amend --no-edit; else git commit -a -m stowed; fi;};f'
git config --global alias.unstow '!f(){ if [[ $(git log -1 --format=%B) == stowed ]]; then git reset @^; else echo \"Nothing to unstow\"; fi;};f'
```

### `changes`

What changes have been made from `origin/master`?

```bash
git config --global alias.changes 'diff origin/master...'
```

### `update`

Rebase your commit(s) onto master:

```bash
git config --global alias.update "pull origin master --rebase"
```

### `save`

This is kind of similar to [`stow`](#stowunstow). If you don't currently have
a change "in progress", it creates a new commit. Otherwise, it just ammends
the "in progress" commit. "In progress" is defined as "not an ancestor of `origin/master`".

```bash
if git merge-base --is-ancestor HEAD origin/master; then
  git commit -va
else
  git commit -va --amend --no-edit
fi
```

Copy/paste:

```bash
git config --global alias.save '!f(){ if git merge-base --is-ancestor HEAD origin/master; then git commit -va; else git commit -va --amend --no-edit; fi;};f'
```
