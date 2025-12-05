
https://upperhorizon.com/tailwind-to-wordpress-blocks-converter

What's my need? Well, I think it's clear that the best way to often design now is going to be with AI. And what you'd really like is you'd like to be able to outline something in AI and then tweak things and then iterate again with the AI based on what you've tweaked and keep going in that way. And then finally that you can want to output the result in a form that you can then put in your website and then people, content editors or designers can obviously change text, tweak things, change links, change featured images, even tweak the design a little bit.

And what would be really cool is you'd then want to be able to go back from that if you wanted to make a later design, just pull that out. [and iterate with AI again]

And the issue I have at the moment is let's say I design locally with AI. The output is likely html + tailwind. But my site say is running on WordPress. So I then have to somehow get my design into WordPress, which means I seem to, at the moment, it seems to me I have to hire some WordPress developers to hack it into WordPress. And once it is Wordpress then I can't get it out of WordPress again if I ever want to tweak that design more.

So I've got this huge impedance which I have to pay WordPress developers (and wait for them) to convert my thing into WordPress when I already have it in like Tailwind and HTML. It's just kind of weird.

So why am I using Wordpress? Well the issue is if I'm in Tailwind and HTML, there's no, there's no visual editor. So the rest of the team who aren't happy in raw html and tailwind, who want a wysiwyg visual editor, they want something like wordpress.

And I don't know of *any* visual editor even vaguely close to something like Framer or Wix where you can really move things around or even where you can easily correct the text on a button.

So, I'm looking for several things:

- One would be a world in which I could stay in Tailwind and HTML, which seems to be the best world for at least AI development and coders. But then I need a WYSIWYG editor for that Tailwind and HTML.
- Or I have to get it into WordPress, but that's something I already have a problem about.
- And then I have to have a way to get it out, which is also problematic.

### Random stuff i found

- https://upperhorizon.com/tailwind-to-wordpress-blocks-converter - convert tailwind to gutenberg *content* blocks. closest to what i want on the tailwind => wordpress direction. however, seems to be quite basic and not so active.
- https://www.reddit.com/r/tailwindcss/comments/ykabxu/visual_editors_for_tailwind_what_are_you_using/ - basically no good ones. best was https://getpiny.com/ tried it in vscode quickly and didn't really work so great for my case (flowershow stuff)

Not relevant but interesting

- https://html-to-gutenberg.com/ -- create new gutenberg blocks from html and tailwind
- https://www.subframe.com/ - v nicely designed app i didn't have time to try out

### Part 2

And that leads to a general point about AI-assisted development and design pros. I think the way we're going to go is that I want to be using it continuously. You see this in code editors now, in VS Code or even in Z that I've been using. I can basically write some stuff or dictate some stuff. Then I can have a side pane where I make some modifications, and it updates my editor. I can even highlight things I want to change and prompt. I particularly noticed this in Atlas. The way it integrates the browser, I can highlight things. I'm even using it to correct GitHub issues. That kind of integration and iterative ability is really, really valuable. And that kind of flow would be amazing. At the moment, it's a little bit painful to do, really. So I haven't really figured out how to do it in Obsidian without paying for something. And even then, I don't know how it works. When I'm fully in an AI system, where I'm in ChatGPT or Gemini, I can use the Canvas tool. But the Canvas tool is nothing like either Obsidian or Google Docs or anything, a good word editor. So it's sort of okay. And also, often it loses—when I do personal edits and then I want to iterate more with my prompting, it doesn't always seem to recognize the edits I've made. So just the experience there of the seamlessness doesn't work. But when I'm in a pure text editor or something like that, my experience of Google Docs and Gemini's integration is just horrific. It doesn't seem to do what I want almost at all. Even basic things like take this section that I just dictated and turn it into bullet points, go wrong. So there's this aspect, which is you really want to somehow merge these tools—the text editor and the AI. And this is similar. The close I've seen is more in code editors. I think this is a point that's, well, anyway, one point about it is you definitely want things—you're now going to value text editors. Actually, it's why Markdown again comes into it, but you're going to value editors that sort of preserve relatively good syntax structure. Because that's something that the AI is basically generating; it's generating the underlying tokens, not the design. So things that have relatively transparent or clean mapping between the output and the underlying syntax are attractive. So, for example, that's why Tailwind and HTML are so good for AI, because there's a pretty clean underlying structure mapping. Similarly, Markdown is going to be really good because it's got this pretty straightforward syntax, but which is still human editable a little bit. So that's the second point: I think there's a real thirst for those kinds of editors that integrate well those two, that really integrate the AI well and the editor experience well in a whole bunch of days—programming and writing being the most obvious. Also visual design would be the next one.