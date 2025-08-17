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

```bash
git diffs origin/main
```