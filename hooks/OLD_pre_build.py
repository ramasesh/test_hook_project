#!/usr/bin/env python3
"""Pre-build hook that checks that the repo is in an up-to-date state,
and stores the commit hash in a file"""

import os, sys
from git import Repo
from absl import logging

def hook():
  logging.info('Running git-cleanliness hook')
  logging.info('Running git-cleanliness hook 2')

  repo = Repo('.')

  EXIT_CODE = 0

  # check repo is clean
  if len(repo.untracked_files) != 0:
    logging.error('Untracked files found!')
    EXIT_CODE = 1
  if repo.is_dirty():
    logging.error('Repo is dirty!')
    EXIT_CODE = 1
  if EXIT_CODE == 1:
    sys.exit(EXIT_CODE)

  # get commit hash
  commit_hash = repo.commit().hexsha
  print('{"commit": "%s"}' % commit_hash)

if __name__=='__main__':
  hook()
