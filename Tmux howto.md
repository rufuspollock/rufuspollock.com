# tmux Cheat Sheet

## Sessions

```bash
tmux new -s <name>      # Create session
tmux ls                 # List sessions
tmux a -t <name>        # Attach to session
```

| Action | Shortcut |
|--------|----------|
| Detach | `Ctrl-b d` |
| Switch session | `Ctrl-b s` |

## Windows

| Action | Shortcut |
|--------|----------|
| New window | `Ctrl-b c` |
| Next | `Ctrl-b n` |
| Previous | `Ctrl-b p` |
| Jump to window | `Ctrl-b 0-9` |
| List windows | `Ctrl-b w` |
| Rename | `Ctrl-b ,` |
| Close | `Ctrl-b &` |

## Panes

| Action | Shortcut |
|--------|----------|
| Split vertical | `Ctrl-b %` |
| Split horizontal | `Ctrl-b "` |
| Move between panes | `Ctrl-b` + `←↑→↓` |
| Cycle panes | `Ctrl-b o` |
| Close pane | `exit` or `Ctrl-d` |
| Toggle zoom | `Ctrl-b z` |
