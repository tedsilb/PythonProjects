# Python Projects

[![CodeFactor](https://www.codefactor.io/repository/github/tedsilb/pythonprojects/badge)](https://www.codefactor.io/repository/github/tedsilb/pythonprojects) [![Total alerts](https://img.shields.io/lgtm/alerts/g/tedsilb/PythonProjects.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tedsilb/PythonProjects/alerts/)

Various Python projects I work on from time to time.

## Building

Projects are built using [Bazel](https://bazel.build).

- To build all projects:
  - `bazel build ...`
- To run a specific project:
  - `bazel run projects:{project} {args}`
- For example:
  - `bazel run projects:Magic8Ball`

## Formatting

Files are formatted with [yapf](https://github.com/google/yapf).
