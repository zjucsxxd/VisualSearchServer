
# Path to your output directory, where we can store snapshots, prototxts etc.  
# Note that all files will be placed in a subdirectory of this directory, named
# after this file but with '.py' replaced with '_out'.  This means you can
out_dir = '/data/'

# Path to your installation of ImageNet.  If you don't want to
# use ImageNet, see the load_imageset function to see how to replace it.
imagenet_dir = '/data/ILSVRC2012/'

# Optionally, set this to a directory in /dev/shm or another ramdisk.
# This script launches background processes which prefetch data while
# the main process sends them through Caffe.  
# Bizarrely, sending large numpy arrays through a file in ramdisk seems
# to be faster than sending them through a python queue.  If this is
# None, then the data will be sent through a queue, but otherwise batches
# will be saved to this directory and loaded.
tmp_dir = '/dev/shm/deepcontext/'
