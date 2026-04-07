# Issues / Tasks

An issue is a way to log ideas/tasks. They can be edited to be open or closed, with the ability to organise them with tags, assign them to people in the group and apply due dates.

Create issues for most tasks you are working on. The following provides the pattern for creating and managing issues. I recommend following this pattern for two reasons:

1. It helps *you* think through the task (much effort has been saved by good job stories even on the most mundane of tasks).
2. A good, consistent structure helps *others* understand and facilitates communication in a distributed, multi-cultural team.

Both these points apply not only to issue creating but also updating and closing: will you remember in 3 months why you closed that issue and how? If you take over a task from an unavailable team mate can you quickly understand what they completed and where that work is?

https://youtu.be/F-FOb7eZIkE

## Creating Issues

The issue can be written in Markdown, and is a good way of tracking your 'to-do list' in a project. To make one, go onto your sidebar, find the tab that says 'Issues', and click the green and white button that says 'New Issue'. Fill it out, create the issue, and then it will be available to see for you and/or your group, depending on which repo you created it in.

This key information SHOULD be present:

- Short description: what is involved. A user story/job story if possible.
- Acceptance criteria: what would it mean for this to be done.
- Tasks Checklist: a list of tasks involved to accomplish this task. If you are not sure yet a first task should be "Analyze this and get set of tasks".

### Issue Layout

You should create an issue for any assignment, or project, that has more than one actionable step, and you should lay your issue out as follows:

```md
## Job Story
## Acceptance
## Tasks
## Analysis
```

E.g.

```md
## Job Story
I want to create an FAQ for new recruits, accessible from the Onboarding guide, so they have access to useful information that will make the joining process as smooth as possible.

## Acceptance:
* [ ] An FAQ section at the end of the Onboarding Guide with answers to the questions below.

## Tasks:
* [ ] Write answers to the following questions:
   1. How do I write an issue?
   2. How do I set/plan my work?
   3. How should I report on my work / progress?
   4. Who's my 'boss'? Who am I accountable to?
   5. Outside of my work responsibilities, do I have other commitments / things to attend?
   6. What's my work responsibilities?
   7. What's your culture? What makes you unique?
   8. How do you get stuff done?
   9. How do your projects get initiated?
   10.How does your budget get set?

## Analysis

None for this issue. Here you might include your questions and hypotheses, or other contextual information relevant to your issue.
```

Once you've set out your issue like this, you should keep it up to date so that your team members can follow along.

**Tip:** On Github you can create an issue template so this structure is always present.

### Issue Naming

Issue creators MAY use the following naming patterns:

- `[epic]` prefix in title for epic issues
- (Optional) Grouping ... e.g. `[ux]` for UX issues

### Relationships between Issues

Make sure you record relationships between issues, e.g.:

- Individual issues and their epics.
- Support requests and their fixes.

**Tip:** Use keywords such as 'parent of #...', 'child of #...', 'depends on #...' in the issue description to automatically create these relationships.

## Updating the Issue

- First, ensure that it is labelled correctly. You can label issues so that issues with the same label appear together. This makes reviewing outstanding issues easier. See more information on Labels below.
- Make comments next to each task, **in bold**, to indicate how you're progressing with each task. This should be done so that somebody else can see, at a glance, how you're getting on. See completing tasks below.
- If you need someone else to assist you, you can @ them in the Comments section with a message to indicate what you'd like their help with. However, ensure you've generated a hypothesis first, and that you include it in your message. This way, you might find you can solve it yourself, and if you can't, it helps your team follow your thought process.

### Status

We use a Kanban board to track the status and workflow of issues. An issue might have one of the following statuses:

- 'Backlog' - 'Backlog' should contain all issues that have been created, but not yet processed. Issues would normally move from 'Backlog' into 'Prioritized' or 'Someday/Maybe'.
- 'Prioritized' - issues not currently being worked on but which have been identified from the backlog as prioritized for work next.
- 'Next' - We only use this status if 'Prioritized' is overflowing with issues, essentially to identify the top priorities of the 'Prioritized'. 'Next' should contain no more than a few issues which are to be worked on immediately next.
- 'In Progress' - issues that are currently being worked on.
- 'Done' - issues that have been completed.
- 'Blocked/Waiting For' - if there is a blocker external to our organization.
- 'Someday/Maybe' - issues that we don't intend to work on for now but would like to reconsider in the future.

### Estimating Time

Estimation is the process of estimating time to complete tasks. There are many approaches to estimation.

Estimation is central to workability and low-stress because it allows us to make promises grounded in reality. It is up to the delivery team or the individual responsible for delivery to come up with time estimates. Equally important as estimating, is **assessing** performance against estimates so as to improve our skill at estimating -- without assessment estimates don't get better, without assessment you don't know your velocity (how much you can actually get done).

In general tasks that are over 5d should be broken down into smaller tasks. This will both improve estimation (errors greatly increase as tasks get larger) and make tasks better suited to planning (as tasks can fit inside one sprint).

### Completing Tasks

When completing a task (i.e. a checklist item) you SHOULD:

- Check the item.
- Edit the item to add some information about what happened and make this obvious (e.g. use bolding) so that people can see at a glance the status of the issue (and don't have to wade through all the comments).
- Leave a comment on the issue task so that people get notified.

The difference between writing updates in the description and in the Comments section is that the Comments section represents the _flow_ of your work, whereas the Description represents the most up-to-date _state_ of your work. You should ensure you use both.

Why do both description updates and commenting? Because we want both *flow* and *state* information readily available. For example, a product owner may just want to see quickly the overall state of the work by looking at the issue description without having to wade through a complex comment thread.

For example, suppose the task was:

```markdown
* [ ] Create the mockup of front page
```

The updated item would be:

```markdown
* [x] Create the mockup of front page **Done -- mockup here {LINK}. Few minor items to finalize once we have answers from client**
```

And the comment here would be almost identical (often comments can be terser):

```markdown
Mockup complete:{LINK}. Few minor items to finalize once we have answers from client.
```
