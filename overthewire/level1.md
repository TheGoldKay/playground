Display the whole file:
```bash
cat readme 
```

Show only the line with the password:
```bash
grep 'password' readme
```

Return just the password:
```bash
rep -o ': .*' readme | sed 's/: //'
```


**Connect via SSH:**
```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
```
**Password:** 
```bash
ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
```