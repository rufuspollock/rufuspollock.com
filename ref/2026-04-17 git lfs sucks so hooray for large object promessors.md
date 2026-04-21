First of all, why does Git LFS suck? I say this as someone who has used Git LFS a lot, even built an entire Git LFS replacement server and API called Gifless and more.

First, it's just an intuition about Git LFS: the UI is painful. You have to install something else, and even developers get confused by Git LFS.

Let's just go on to other reasons. Migration, for example from GitLab to GitHub or any other provider, is now a complete pain. It's easy to go wrong and easy to lose files. Normally, you just get cloned, get pushed, and you're done. Oh no, you have to get LFS everything, and you have to re-push it on the new server. You have to check it. Super easy to get this to go wrong.

Obviously, there's the basic cost point, like GitHub or elsewhere. You start paying GitHub money, and getting off Git LFS is really a pain; it's like quitting crack. It is painful to get off. There are weird edge cases you wouldn't believe.

For example, we had a Git repo for our flower show project for our markdown publishing platform. There were just a few files straight into Git LFS, not a lot. We just happened to have used Git LFS by default for a few asset files at the beginning that we thought might be big and maybe a video or two. There were only a few MB.

What turns out is that even if you migrate off Git LFS completely and you try to turn it off in your repo and you contact GitHub support, it turns out things like you cannot turn your site into a template repo, which is what we want to do so people could copy it. Even if you've got it all turned off, you've removed GitHub Git LFS everywhere, it turns out it now can't be turned into a template repo because template repos don't allow Git LFS. Even if you've removed it completely and copied and contacted GitHub support, they cannot remove that flag for you. Who knew?

The list can go on of kind of edge cases that you run into if you've ever run `git lfs migrate` to get off Git LFS. You'll know how painful and complex and error-prone that can be. 

---

The question is, could we get rid of GitLFS?

My policy at the moment has been to just use Git. If I have files bigger than 100 MB, I'll just check everything in. It's a pain, and it means I sometimes get to the GitHub repo size limit, but it's better than GitLFS.

Is there anything better we could do? That's where this sounds exciting: we may be getting a GitLFS replacement that's built into Git. Read about it here.

https://tylercipriani.com/blog/2025/08/15/git-lfs/ - good article

https://git-scm.com/docs/large-object-promisors - some of what is involved.
