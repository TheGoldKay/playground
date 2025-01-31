Find Password:
```bash
find ./ \             # search all dir in current path
    -type f \         # regular files only
    -size 1033c \     # exactly 1033 bytes
    ! -executable \   # not executable
    -exec cat {} \;   # display contents
```

One liner:
```bash
find ./ -type f -size 1033c ! -executable | xargs cat | xargs # run xargs alone to remove spaces
```

**Password:**
```bash
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```