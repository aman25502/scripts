#!/bin/bash
echo "Regenerating FaceUnlock..."

ROOTDIR="$PWD"
CURRENT_DIR="$ROOTDIR/external/motorola/faceunlock/patch"

cd packages/apps/Settings
git am $CURRENT_DIR/0001-Settings-Port-face-unlock-feature-4-4.patch

cd $ROOTDIR/frameworks/base
git am $CURRENT_DIR/0001-base-Port-face-unlock-feature-3-4.patch

cd $ROOTDIR
echo "Done"

