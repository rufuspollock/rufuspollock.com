---
title: >-
  Thinking about Annotation
slug: thinking-about-annotation
date: 2007-01-17T18:36:12
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 154
---

Annotation means the adding of comments/notes/etc to an underlying resource. For the present I'll focus on the situation where the underlying resource is textual (as opposed to being an image, or a piece of film or some data). Various things to consider when implementing an annotation/comment system:

1. Addressing and atomisation: Are annotations specific to particular parts of the resource. If so how do we store this address (relatedly: how is the resource 'atomised' and how to we address these atoms, or range of atoms). For example, do we address by word, by character, by paragraph or by section? Do we wish to store ranges rather than a single address? Do we wish to allow a given annotation to be associated with multiple ranges/atoms?

2. Permissions: Are there restrictions on the creation (deletion/updating etc) of annotations.

3. Will the underlying resource change and if so are annotations intended to be robust to those changes.

Let's concentrate on the first issue for the time being as it is the most immediately important. Furthermore, defining the 'atoms' of the resource sharply narrows the implementation options.

### The Simple Case: Mod a Blog

If one is happy to have fairly large atoms (pages, or even sections of some piece of text) then implementing an annotation system can be reduced to grabbing your favourite CMS or blogging software and feeding the text in in appropriate chunks. This is often satisfactory and is a simple, low tech solution that will pretty much work out of the box. A classic example of this approach is <http://www.pepysdiary.com/> which works so well because the subject matter (Samuel Pepy's diary) has a very obvious atomisation (namely the daily diary entries) suited perfectly suited to blog software (in this case movable type).

You can even start doing a bit of modding, for example to present recent annotations (<http://www.pepysdiary.com/recent/>) or to present the text plus annotations all in one piece. (Given that [commentonpower][] seems to fall neatly into this category with most commentable atoms of the right size for 'blog' entries I wonder why they didn't just implement it as a plugin for wordpress -- perhaps it was such a simple app that it easier to 'roll their own').

[commentonpower]: http://www.commentonpower.org/

### Getting More Atomic

Once you want to have atoms below a size comfortable for individual html pages/blog entries, wish to allow people to comment on chunks too large for an individual page, or to comment on ranges one starts to have problems with this approach. The main challenge at this point is to find some way to extract the addressing information from the client doing the annotation. Confining ourselves to the web the challenge becomes way to structure the interface and the text so that one can determine range start and end points. This is a non-trivial matter. Possible options include:

  * Javascript: in theory the selection/range objects should help us out here unfortunately cross-browser support is patch (firefox as usual is excellent and IE pretty bad). If one does not want to be as precise as to get ranges javascript could also be used to extract e.g. element ids.
  * Copy and paste of the quote to annotate with some backend algorithm to determine the actual range. Nice and simple but not clear that one can 'invert' (i.e. find a unique range from a given selection) unless the selection is large.
  * If addressing fairly large atoms (e.g. a paragraph or large) one could just insert a unique piece of user interface equipment (e.g. a button or link) with each atom. Note however that this prevents support for ranges.

### Separating Data and Presentation

Whatever one chooses to do it does seem sensible to clearly separate data and presentation. This is particularly important when there is so much uncertainty over the user interface. In particular, it would be good to clearly specify the annotation format and implement a programmatic interface to it independent of the standard (human) user interface. That way is easy to switch interfaces (or have multiple ones). Given that annotations are essentially just a comment it would seem sensible to try and reuse an existing format such as Atom (or RSS) for the machine interface to the comment store. [marginalia] already had such a format based on atom. I've recently reimplemented a stripped down version of this format for the annotation store backend in python in preparation for adding annotation support to openshakespeare web interface, see:

  <http://project.knowledgeforge.net/shakespeare/svn/annotater/trunk/>

[marginalia]: http://www.geof.net/code/annotation
[openshakespeare]: http://demo.openshakespeare.org/

Of course as discussed above this isn't quite as simple as it looks as your user interface can constrain what you can and can't store (using a blog approach you can't store ranges and from what I have read getting reliable character offsets is problematic). Nevertheless it seems the best place to start.



