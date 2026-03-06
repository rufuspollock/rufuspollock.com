Facing a dilemma about issue tracking. I found beads really annoying now, though I really like the fact I just had command line creation. I think I want something that just works with markdown files because it's more flexible.

I'm a bit more specific. I tried beads, which is kind of cool! I like the command line. I like the integration with AI for me, but I actually was looking for something that I wanted to use quite manually, and I'm not using it so much on a coding project. I wanted to actually use it for my personal issue tracking planning.

At the same time, as i've mentioend before (have i posted?), I really am over github issue tracking and issue trackers, at least in terms of their UI etc. I want something fast and local.

I'm thinking I want something that integrates more with existing kind of Obsidian and Markdown. It should also sort of automated and give me a nice command line interface for other things. I'm wondering about going back to [[projects/TaskGraph]] and rolling my own, or looking for other things that are on there. I guess I should first do some research; that would be a good thing to write up. 

Yes, best practise is to create a product vision first, see what's out there, and get comments (post it on Reddit or whatever).

### The problem with beads

So, beads was kind of cool, but there were several issues with it:

- It does a lot of stuff that I don't need. e.g. it runs a daemon, has many, many commands.
- Also quite invasive: it adds AGENTS.md it add git commit hooks etc.
- But the real issue was: got broken in version 50, which was released a couple of weeks ago.
    - One day it was working. next day it encourages me to do an upgrade. do an upgrade, and it's broken..
    - Switched to encforcing use of dolt which is a massive thing i didn't want. and worse that was completely broken
    - And what was worse, t was really hard to go back.
- And that meant that every git commit doesn't work because of the agents.md file and the git hooks. 🤦‍♂️
- Yeah, it was a bit of a nightmare!

Fortunately found a fork of it in Rust that is kind of compatible with it and which at least still reads the file. I've been using that, but I'm not sure it's the long-term solution. I think that this was a little bit of a prompt, to see that, at least my personal stuff, I should get off beads -- it's a bit of an overkill for what I'm wanting to do, and even in general I think.