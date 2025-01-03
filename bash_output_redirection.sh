```markdown
## Bash Output Redirection

tags: bash, shell, output, redirection, stdout, stderr

### Code:
```bash
# Save the normal outputs for recovery
exec 3>&1 4>&2
# Restore the normal outputs on script exit or interrupt
trap 'exec 2>&4 1>&3' 0 1 2 3
# Redirect stdout and stderr to a file
exec >output.log 2>&1
```

### Breakdown:

#### `exec 3>&1 4>&2`
- **Purpose**: Creates duplicates of the standard output and standard error file descriptors.
  - `3>&1`: Duplicates the current standard output (stdout, file descriptor 1) to file descriptor 3.
  - `4>&2`: Duplicates the current standard error (stderr, file descriptor 2) to file descriptor 4.
- **Effect**: The original stdout and stderr are saved in file descriptors 3 and 4, so they can be restored later if needed.

#### `trap 'exec 2>&4 1>&3' 0 1 2 3`
- **Purpose**: Sets up a trap to restore the original stdout and stderr when certain events occur.
  - `exec 2>&4`: Redirects stderr (file descriptor 2) back to the original stderr saved in file descriptor 4.
  - `exec 1>&3`: Redirects stdout (file descriptor 1) back to the original stdout saved in file descriptor 3.
- **Signals and Exit Code**:
  - `0`: Script exits (normal termination).
  - `1`: SIGHUP (hangup signal).
  - `2`: SIGINT (interrupt signal, e.g., from pressing `Ctrl+C`).
  - `3`: SIGQUIT (quit signal, e.g., from pressing `Ctrl+\`).

#### **Purpose of the Entire Script**
- **Preserve Original Outputs**: Ensures that the original stdout and stderr are saved before any redirection occurs.
- **Automatic Restoration**: Guarantees that stdout and stderr are restored to their original destinations when the script exits or encounters an interrupt signal.

#### Example Use Case
This script can be useful when:
1. Redirecting stdout or stderr to a file or another process during execution.
2. Ensuring that the original stdout and stderr are restored even if the script crashes or is interrupted.

#### Full Example:
```bash
#!/bin/bash
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3

# Redirect stdout and stderr to a file
exec >output.log 2>&1

echo "This message goes to output.log"
ls non_existent_file

# Simulate a crash
kill -SIGINT $$

echo "This message won't be printed due to the crash"
```

- Output:
  - `output.log` will contain the redirected output.
  - If the script crashes, stdout and stderr will be restored, and subsequent messages (if any) will appear in the terminal.
```
