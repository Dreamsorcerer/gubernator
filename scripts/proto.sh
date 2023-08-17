#!/bin/bash

# Copyright 2018-2022 Mailgun Technologies Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Make sure the script fails fast.
set -eux

SCRIPT_PATH=$(dirname "$0")                  # relative
REPO_ROOT=$(cd "${SCRIPT_PATH}/.." && pwd )  # absolutized and normalized
PROTO_DIR=$REPO_ROOT/proto
PYTHON_DST_DIR=$REPO_ROOT/python/gubernator
GOLANG_DST_DIR=$REPO_ROOT

# Build Golang stabs


go install \
  google.golang.org/protobuf/cmd/protoc-gen-go \
  google.golang.org/grpc/cmd/protoc-gen-go-grpc \
  github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway \
  github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2
GOPATH=$(go env GOPATH)
export PATH=$PATH:$GOPATH/bin

GOOGLE_APIS_DIR=$REPO_ROOT/googleapis
if [ -d $GOOGLE_APIS_DIR ]
then
    pushd $GOOGLE_APIS_DIR
    git pull
    popd
else
    git clone https://github.com/googleapis/googleapis $GOOGLE_APIS_DIR
fi

protoc -I=$PROTO_DIR \
    -I=$GOOGLE_APIS_DIR \
    --go_out=$GOLANG_DST_DIR \
    --go_opt=paths=source_relative \
    --go-grpc_out=$GOLANG_DST_DIR \
    --go-grpc_opt=paths=source_relative \
    $PROTO_DIR/*.proto

protoc -I=$PROTO_DIR \
    -I=$GOOGLE_APIS_DIR \
    --grpc-gateway_out=$GOLANG_DST_DIR \
    --grpc-gateway_opt=logtostderr=true \
    --grpc-gateway_opt=paths=source_relative \
    --grpc-gateway_opt=generate_unbound_methods=true \
    $PROTO_DIR/*.proto

# Build Python stabs
pip install -r "${REPO_ROOT}/python/requirements.txt"
python3 -m grpc.tools.protoc \
    -I=$PROTO_DIR \
    -I=$GOOGLE_APIS_DIR \
    --python_out=$PYTHON_DST_DIR \
    --pyi_out=$PYTHON_DST_DIR \
    --grpc_python_out=$PYTHON_DST_DIR \
    --mypy_grpc_out=$PYTHON_DST_DIR \
    $PROTO_DIR/*.proto
# Rewrite imports to import from package
sed -i'' -e 's/import gubernator_pb2/from gubernator import gubernator_pb2/' "${PYTHON_DST_DIR}/"gubernator_pb2_grpc.py*
sed -i'' -e 's/import gubernator_pb2/from gubernator import gubernator_pb2/' "${PYTHON_DST_DIR}/"peers_pb2.py*
sed -i'' -e 's/import peers_pb2/from gubernator import peers_pb2/' "${PYTHON_DST_DIR}/"peers_pb2_grpc.py*
