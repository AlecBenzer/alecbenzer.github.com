---
title: Git aliases
layout: post
...

Things I use to use git. A combination of actual git aliases and shell
functions.

#### `new`

`new` creates a new branch based on current (i.e., up-to-date) `origin/master`:

```bash
function new() {
    git fetch -q origin master
    git branch "${1:?}" origin/master
    git checkout "${1:?}"
}
```

#### `master`

`master` checks out current `origin/master` (as a detached head). (See also
["Don't checkout master locally"](/dont-checkout-master).)

```bash
function master() {
    git fetch -q origin master
    git checkout origin/master
}
```


#### `stow`/`unstow`

Like a branch-specific "stash". I think many people initially assume `git
stash` will behave kind of like this, but the stash is shared across all
branches.

`stow` either saves your pending changes in a commit with message "stow",
or, if you've already stowed changes, ammends the stow commit with your new
changes.

```bash
function stow() {
    if [[ $(git log -1 --format=%B) == "stowed" ]]; then
        git commit -a --amend --date=now --no-edit
    else
        git commit -a -m stowed
    fi
}
```

`unstow` undoes a stowed commit (by resetting to the commit before it):

```bash
function unstow() {
    if [[ $(git log -1 --format=%B) == stowed ]]; then
        git reset @^
    else
        echo "Nothing to unstow"
    fi
}
```

#### `changes`

What changes have been made from `origin/master`?

```bash
git config --global alias.changes 'diff origin/master...'
```

#### `update`

Rebase your commit(s) onto master:

```bash
git config --global alias.update "pull origin master --rebase"
```

#### `save`

This is kind of similar to [`stow`](#stowunstow). If you don't currently have
a change "in progress", it creates a new commit. Otherwise, it just ammends
the "in progress" commit. "In progress" is defined as "not an ancestor of `origin/master`".

```bash
function save() {
    if git merge-base --is-ancestor HEAD origin/master; then
        git commit -va
    else
        git commit -va --amend --date=now --no-edit
    fi
}
```

_TODO: Make this work better with branch pipeling._

#### `branch-cleanup`

Deletes any branches that have already been merged onto master, where
"merged" means either that the branch has no delta from master, or that a
commit equivalent to the branch's latest is already on master:

```bash
function branch-cleanup() {
    git fetch --all --quiet
    for b in $(git for-each-ref refs/heads --format="%(refname:short)"); do
        if [[ ! $(git cherry -v origin/master "${b:?}" | grep "^+") ]]; then
            git branch -D "${b:?}"
        elif git diff --exit-code --quiet "origin/master...${b:?}"; then
            git branch -D "${b:?}"
        fi
    done
}
```
