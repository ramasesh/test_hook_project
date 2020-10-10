import numpy as np

from absl import app, flags

FLAGS = flags.FLAGS
FLAGS.DEFINE_string('string_arg', 'Default', 'Argument of type string')
FLAGS.DEFINE_string('float_arg', 'Default', 'Argument of type float')

def main(argv):
  print("----ARGUMENTS----")
  print("FLAGS.string_arg:")
  print(FLAGS.string_arg)

  print("FLAGS.float_arg:")
  print(FLAGS.float_arg)

