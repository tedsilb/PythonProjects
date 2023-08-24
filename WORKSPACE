load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

SHA = "5868e73107a8e85d8f323806e60cad7283f34b32163ea6ff1020cf27abef6036"

VERSION = "0.25.0"

http_archive(
    name = "rules_python",
    sha256 = SHA,
    strip_prefix = "rules_python-{}".format(VERSION),
    url = "https://github.com/bazelbuild/rules_python/releases/download/{}/rules_python-{}.tar.gz".format(VERSION, VERSION),
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()
