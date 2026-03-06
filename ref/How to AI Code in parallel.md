
Great (as usual) post from Simon Willison https://simonwillison.net/2025/Oct/5/parallel-coding-agents/

References couple of other good posts:

> Jesse Vincent wrote [How I’m using coding agents in September, 2025](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/) which describes his workflow for parallel agents in detail, including having an architect agent iterate on a plan which is then reviewed and implemented by fresh instances of Claude Code.
> 
> In [The 7 Prompting Habits of Highly Effective Engineers](https://sketch.dev/blog/seven-prompting-habits) Josh Bleecher Snyder describes several patterns for this kind of work. I particularly like this one:
> 
> **Send out a scout**. Hand the AI agent a task just to find out where the sticky bits are, so you don’t have to make those mistakes.
> 
> I’ve tried this a few times with good results: give the agent a genuinely difficult task against a large codebase, with no intention of actually landing its code, just to get ideas from which files it modifies and how it approaches the problem.
> 
> Peter Steinberger’s [Just Talk To It—the no-bs Way of Agentic Engineering](https://steipete.me/posts/just-talk-to-it) provides a very detailed description of his current process built around Codex CLI.

Extras

- https://github.com/obra/superpowers

> It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it _doesn't_ just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do.
>
> Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest.