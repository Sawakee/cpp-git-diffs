# cpp-git-diffs

Integrate `diffsitter` with `git difftool` to review only files with semantic differences.

## Prerequisite

Install [diffsitter](https://github.com/afnanenayet/diffsitter):

```bash
cargo install diffsitter --bin diffsitter --version 0.9.0
```

## Usage

```bash
git difftool -x "diffsitter --config /path/to/config.json5"
```

## Integration with `git diff`

Insert the information from `gitconfig_example` into your `.gitconfig`.
You can then use `git diffs` just like `git diff`.
Be sure to update `/path/to` to match your environment.

## Example

Executin `git diffs origin/example` in this repository to check differences in `example` dir.

### Codes in origin/master

`example/main.cpp`

```c++
#include <iostream>

// This is a simple C++ program that prints "Hello, World!" to the console.
int main() {
  // Print a greeting message
  std::cout << "Hello, World!" << std::endl;
  // Return 0 to indicate successful execution
  return 0;
}
```

`example/sub.cpp`

```c++
int add(int a, int b) { return a + b; }
```

### Codes in origin/example

`example/main.cpp`

```c++
#include <iostream>

int main() {
  std::cout << "Hello, World!" << std::endl;
  return 0;
}
```

`example/sub.cpp`

```c++
int add(int a, int b, int c) { return a + b + c; }
```

### Result

Difference exists only in `sub.cpp`

```bash
$ git diffs origin/example

FILENAME: example/sub.cpp

0:
--
-int add(int a, int b, int c) { return a + b + c; }
```