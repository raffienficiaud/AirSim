#!/usr/bin/env bash
set -e

# in here, we are in a virtual environment with conan installed
# the CONAN_HOME and download cache have already been configured

# variable expansion, see https://stackoverflow.com/a/13864829
if [ -z ${CONAN_HOME+x} ]; then
    echo "[CONAN] the variable 'CONAN_HOME' should have been defined before the call"
    exit 1
fi

if [ ! -d "$CONAN_CENTER_INDEX_SRC" ]; then
    echo "[CONAN] conan-center-index repository folder does not exist."
    exit 1
fi

cd $CONAN_CENTER_INDEX_SRC

conan export --name eigen --version 3.37.0 recipes/eigen/all
conan export --name rpclib --version 2.3.0 recipes/rpclib/all

echo
echo "Known conan packages"
echo

conan list "*"
