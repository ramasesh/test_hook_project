"""Pre-build hook that checks that the repo is in an up-to-date state,
and stores the commit hash in a file"""

import os, sys
from git import Repo


def hook():
  print('Running git-cleanliness hook')

  repo = Repo('.')

  EXIT_CODE = 0

  # check repo is clean
  if len(repo.untracked_files) != 0:
    print('Untracked files found!')
    EXIT_CODE = 1
  if repo.is_dirty():
    print('Repo is dirty!')
    EXIT_CODE = 1
  if EXIT_CODE == 1:
    sys.exit(EXIT_CODE)

  # get commit hash
  commit_hash = repo.commit().hexsha
  print(f"Latest commit: {commit_hash}")

if __name__=='__main__':
  hook()
