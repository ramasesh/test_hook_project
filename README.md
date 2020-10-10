# Caliban hook test project

Idea: add hook functionality to [Caliban](https://github.com/google/caliban)

## Design questions

1. Should both bash and python hooks be supported?
2. If a hook is a bash hook, how should we deal with collecting output?

## Potential hooks to test

### Hook 1: Git cleaniness and reproducibility

Check that prior to building a container, the repository is in a clean git
state, meaning:
1. No untracked files
2. No changes staged for commit but not committed
3. No unstaged changes

This can be done either with Python (through the `gitpython` package) or with
shell script.

If the repository is not clean, do not allow Caliban to build.  This can be done
by returning with a non-zero exit code (can Python do this? probably), meaning
the Caliban pre-build hook-processing script will have to be written so that if the hook returns with a non-zero exit code, the container build does not occur.

### Hook 2: Argument formatting check

Check that the arguments are specified correctly.

A common frustration with running cloud jobs is that if an argument specified
by the user (me) is formatted incorrectly (say I added a extra parentheses to an
array, for example), I won't fint out about this until 5-10 minutes later when
the cloud job starts.  A potential fix is to run a pre-run hook which checks
that all the arguments are formatted correctly (by running an argparse script,
for example)
