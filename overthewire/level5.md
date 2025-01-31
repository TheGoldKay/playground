#### Display all file contents:

*find* all files in currenct dir, check for *file_type*, *grab* only text files, *cut* out by colon (':') and get first column, and finally *display* file content

```bash
find ./ -type f | xargs file | grep "ASCII text" | cut -d':' -f1 | xargs cat
```

**Password:**
```bash
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
```
