#!/usr/bin/env python3
from absl import app
from absl import flags
import json
import docker

FLAGS = flags.FLAGS
flags.DEFINE_string('container_id', None, 'ID of Docker container to use')


def get_hash_from_image(container_id):
  """Load git hash from docker image label."""
  client = docker.from_env()
  labels = client.images.get(container_id).labels
  try:
    return labels['commit']
  except KeyError as e:
    logging.error(f'Docker image {container_id} does not contain a git commit label.')
    raise e
     

def main(argv):
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

  commit_hash = get_hash_from_image(FLAGS.container_id)
  
  print('{"commit": "%s"}' % commit_hash)

if __name__ == '__main__':
  app.run(main)
