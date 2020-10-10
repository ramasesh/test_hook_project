"""Pre-build hook that checks that the repo is in an up-to-date state,
and stores the commit hash in a file"""

import os
from git import Repo
import json

COMMIT_HASH_FILE = ".container_hashes.json"

def hook():
  repo = Repo('..')

  # check repo is clean
  assert len(repo.untracked_files) == 0
  assert not repo.is_dirty()

  # get commit hash
  commit_hash = repo.commit().hexsha
  

  if not os.path.exists(COMMIT_HASH_FILE):
    json.dum
