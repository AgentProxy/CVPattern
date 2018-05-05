#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/patternCaffe
DATA=data/patternCaffe
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/patternproducts_train_lmdb \
  $DATA/patternproducts_mean.binaryproto

echo "Done."
#  examples/DogsCatsKaggle/