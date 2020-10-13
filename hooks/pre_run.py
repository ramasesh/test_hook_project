#!/usr/bin/env python3
from absl import app
from absl import flags
import json

FLAGS = flags.FLAGS
flags.DEFINE_string('container_id', None, 'ID of Docker container to use')

def main(argv):
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

  FILE = '.container_info.json'
  with open(FILE, 'r') as f:
    data = json.load(f)
  commit_hash = data[FLAGS.container_id]['commit']
  print('{"commit": "%s"}' % commit_hash)

if __name__ == '__main__':
  app.run(main)
