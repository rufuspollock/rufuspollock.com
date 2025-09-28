---
title: >-
  
slug: note-taking-software
date: 2017-11-28T09:43:07
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - page_id: 1395
layout: misc-special
---
# Comparison of Apps for Note-Taking, Researching and Organizing


There are a number of note-taking applications in the market, but if you are a power user, it can be hard to find exactly the "right solution". Depending on your needs, you may want to use several different applications - none of which will usually integrate together in any helpful way. And if you want to retain full access to your notes and avoid lock-in to a particular provider it gets even harder.

Because the topic is complex, this will require a series of articles. In this first one, we will look at some of the main applications available on the market and compare their features and costs.

In later articles, we look in greater depth at the various use cases for a specific application and look further at other candidates. Finally, the plan is to describe our "perfect application".

The main focus in this article is to look at:

1. **Features**: Each application has specific sets of features, and below we will see what are some of the most important ones. Features that we look into are (later in text, "full" means that all features in that category are existing in an application):

    - **Core**: Taking notes and creating checklists, organizing notes and searching them
    - **Collaboration**: Sharing and working together on a note
    - **Web clipping**: Taking screenshots, saving a page, reading later, adding documents, embedding videos
    - **Annotation**: Annotating web pages, PDFs, images and notes themselves
    - **Extras**: Various additional features that set application apart

2. **User experience (UX)**: Is the app easy and simple to use? Is its interface clean and elegant? We use: "ok", "good", "great".

2. **Supported platforms**: For application to fit our everyday needs, we need to take into account which devices and operating systems it supports. E.g. If you are spending a lot of time traveling, chances are that application without mobile version will not work for you.

3. **Cost**: Even open source applications have free and pro versions that are offering different sets of features.

4. **Pros and cons**: As I already mentioned, no application is perfect. You will probably need to compromise something - It all goes down to what you really want and what you can live without.

5. **User freedom**:

    - **Export and backup**: As the time passes by, a number of notes you collect can grow enormously. If there is no easy way to export data in a format that allows you to import it easily into other application, you are risking to get locked in the system. Also, without an export, there is no easy way to backup the data.

    - **Open-source**: When the application is open-source, there is potential for provision of the service by alternate providers which creates competition and ensures reasonable pricing on an ongoing basis. Also, if application provider goes out of business, you can self-host the data or find another provider.

    - **Option to extend the application**: One example of extending an application is linking documents in your note without opening storage application. Other ways to extend application would be using public or free API or having deep access to the content so you can build sophisticated additional features.

    - **Self-hosting**: If the application is self-hosted, you have more control over your data infrastructure, it is more secure, and you can create backup easier. You can self-host the data on your own server or use cloud services like Google Drive or Dropbox.


| Title | Features | Mobile | Web app | Desktop | Browser addon | Open source | Bulk export | Self hosting | Extensability|UX | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Evernote][evernote] | High | Android, iOS, Windows	| Y | Mac, Windows | Chrome, Firefox | N | Y (proprietary format .enex) | N | Medium (API) | Geat | **Basic** (Free), **Plus** (EUR 29.99/YR), **Premium** (EUR59.99/YR) |
| [OneNote][onenote] | High | Android, iOS | Y | Mac, Windows | Chrome, Firefox | N | Y (whole notebook to.pdf, .xps,.onepkg) | N | Medium (API) | Great | **Free** |
| [Diigo][diigo]| High | Android, iOS | Y | N | Chrome (full addon), All other browsers (simplified addon-Digolet) | N | Y (.csv, rss, IE bookmark, Firefox bookmark) | N | Medium (API) | Good | **Free**, **Basic** ($10/year), **Standard** ($5/month, $40/year), **Professional** ($6/month, $59/year), **Teacher** (All features are avaiulable but limited in use) |
| [Google Keep][google]| Medium | Android, iOS | Y | N | Chrome | N | Y (save to Google Drive, or export .html using Google Takeout) | N | Core | Great | **Free** |
| [Laverna][laverna] | Medium | Android (coming soon) | Y (self hosted) | Mac, Windows, Linux | Firefox | Y | Y (.zip with .json and .md files) | Y | High | Good | **Free** (except cost for self-hosting) |
| [Turtl][turtle] | Medium | Android, iOS (coming soon) | N | Mac, Linux, Windows | Chrome | Y | N (planned: .json and .enex) | Y | High | Good | **Free**, **Premium** (coming soon) |
| [TagSpaces][tag]| Medium | Android, iOS | N | Mac, Linux, Windows | Chrome, Firefox | Y | Y (.json) | Y | High | Great | **Free**, **Pro** (EUR 39). **Enterprise** (coming soon) |

[evernote]: https://evernote.com/
[onenote]: https://www.onenote.com/
[diigo]: https://www.diigo.com/
[google]: https://www.google.com/keep/
[laverna]: https://laverna.cc/
[turtle]: https://turtlapp.com/
[tag]: https://www.tagspaces.org/


## Evernote

https://evernote.com/

### Features

- **Core**: Full
- **Collaboration**: Full
- **Web clipping**: You can add documents, and clip web pages and images but you can't embed videos. You can clip web pages as articles to read them later easily.
- **Annotation**: You can annotate PDFs, images, and notes themselves but you can't annotate notes
- **Extras**: Searching for text inside images, adding passcode lock on mobile apps, forwarding emails into Evernote, scanning and digitizing business cards, searching for text in PDFs, searching for text in Office docs

You can check the list of features for each pricing plan on [Evernote's website](https://www.diigo.com/premium/pricing_table_details).

### Pros

Evernote is a robust application with a really good set of features in one application that will definitely help you to organize notes and uploaded files the way you want.

There is integration with Google Drive, so you can easily add links to a  document without additional steps to find it in Google Drive first.

You can easily clip content from the web in form of a full page, article, bookmark, and add it to responding notebook without opening an app.

### Cons

Evernote doesn't have Linux version, but there is open source Linux client using their API, [http://nixnote.org/](nixnote). You can use it to synchronize notes with Evernote.

There is no self-hosting option and you can't export data outside the application except in Evernote's XML format (.enex).

With the free version you can sync data only between two devices, and, if you are an advanced user, you can end up paying a high price for all the features.

## OneNote

https://www.onenote.com/

### Features
- **Core**: Full
- **Web clipping**: Full
- **Collaboration**: Full
- **Annotation**: You can annotate PDFs and notes themselves, and you can add notes when web clipping, but you can't annotate web pages
- **Extras**: Sending notes to yourself in an email, drawing, sketching, or handwriting notes, embedding Excel spreadsheets and Visio diagrams, making tables, creating quick notes and page templates, adding internal links, docked note taking while in other documents, version history.

### Pros

Compared to Evernote, OneNote has mostly the same options but it is free. It is also robust and has good web clipper extension. You can use it for organizing into sections inside notebooks. You can also annotate notes inside it with handwriting tools.

### Cons

While you can annotate notes in the app, you can't do it directly in the document or on a webpage (like Diigo).

There is no Linux version either.

While it is easy to export and share notes with others in .docx, .mht and .pdf, bulk export that can be used for import is limited to OneNote's .onepkg and .xps.

## Diigo

https://www.diigo.com/

### Features

- **Core**: Full
- **Collaboration**: Full
- **Web clipping**: You can add documents and clip web pages and images and annotate them right away, but you canćt embed videos.
- **Annotation**: Full
- **Extras**: Multi colors highlighting, quick bookmarking, using groups, using lists, search meta tags (title, highlights, tags, description), searching cached pages, creating outlines out of highlighted information, or while reading note.

Pricing table is available on [Diigo's website](https://www.diigo.com/premium/pricing_table_details).

### Pros

It is a great application for researchers and has a feature-rich extension that allows annotating the data directly on web pages. You can annotate the article/page/pdf directly without opening the app and create an outline for later.

### Cons

Free plan has too limited features.

Organization of notes is also bad, with time it would become too messy to find your notes.

You can't self-host it, but compared with Evernote, you are not locked-in, there is an option to export your data and change the system.


## Google Keep

https://www.google.com/keep/

### Features

- **Core**: Full
- **Collaboration**: Full
- **Web clipping**: You can clip web pages, but you can't create a screenshot, read later, embed video or add a document.
- **Annotation**: You can only add a note when you are clipping the web page
- **Extras**: Grab image text, using labels to organize notes

### Pros

Google Keep is a simple and fast application. It is great for creating checklist, quick idea capturing or clipping interesting stuff for further reference.

You are not locked in, and you can easily export your data.

### Cons

It has limited features when compared to Evernote or OneNote, and it is not self-hosted. If you are a heavy researcher, with time it might become hard to organize your notes.


## Laverna

https://laverna.cc/
https://github.com/Laverna/laverna

### Features

- **Core**: You can create notes in a Markdown, organize and search them
- **Collaboration**: No
- **Web clipping**: No
- **Annotation**: No
- **Extras**: Markdown editor based on Pagedown, secure client-side encryption, synchronization with cloud storage services (currently only with Dropbox and RemoteStorage), three editing modes (distraction free, preview, and normal mode), WYSIWYG control buttons, MathJax support, syntax highlighting, no registration required, web based, keybindings

### Pros

Laverna's web app is open source Evernote alternative, it is self-hosted and you have control over data. Data is encrypted (therefore is private and secure).

Unlike Evernote, Laverna has Linux desktop application.

Laverna uses Markdown and allows opening Markdown files in Laverna from the file system.

### Cons

There us no mobile app, although there is a pre-release on their [Github page](https://github.com/Laverna/laverna/releases).

For now, you are limited to web and desktop apps. Also, there is no web-clipper so it is not easy to capture information quickly as it is with other applications.

## Turtl

https://turtlapp.com/

### Features

- **Core**: Full
- **Collaboration**: Full
- **Web clipping**: You can take a screenshot, save a page and upload a document, but you can't embed videos.
- **Annotation**: Annotating web pages, PDFs, images and notes themselves
- **Extras**: Self-hosted and highly secure so beside notes, you can keep research, passwords, bookmarks, dream logs, photos, documents and anything else you want to be kept safe.

### Pros

It is self-hosted and you can run your own [Turtl server](https://turtlapp.com/docs/server/).
Because there is not a web app, it eliminates the risk of hijacked servers and losing the data.

### Cons

There is no data export. On [their blog](http://turtlapp.tumblr.com/post/145921919089/turtl-v064-is-out), there is information that export option is  planned for the future:

>Turtl-specific plain text format (JSON), and importing/exporting Evernote's data format).

Having no web app can also be a bad thing if using web app is what you prefer.

## TagSpaces

https://www.tagspaces.org/
https://github.com/tagspaces/tagspaces

### Features

- **Core**: Taking notes and creating checklists, organizing notes and searching them
- **Collaboration**: No
- **Web clipping**: You can take screenshots, save a page, add documents, but you can't embed video or save simplified version for later reading
- **Annotation**: No
- **Extras**: Organizing photos, ebooks, music, recipes or invoices, managing projects using the GTD methodology, tag-based file manager, creating notes in Markdown and HTML, browsing and navigating local file system

### Pros

With TagSpaces you can easily export data in JSON. The application persists the tags in the file names. The tagging information is not vendor locked and it can be used even without the TagSpaces application.

You can self-host it on a WebDAV server (such as Nextcloud or ownCloud), or sync across different devices with services like Dropbox.

### Cons

It doesn't have a web version and browser addons, which means it can't be used to easily capture information or annotate data.

## Other applications - not evaluated in depth

These applications were looked into but not included in the table.

### Simplenote

https://simplenote.com/

Simplenote is light, clean, and free note taking application available for iOS, Android, Mac, Windows, Linux, and the web. iOS, Android, and MacOS applications are open source and under GPLv2 license.

### Paperwork

http://paperwork.rocks/

Currently, Paperwork has just a demo version. It lets you organize your notes in notebooks and tag those notes so you can easily find them and you can also attach files like images or PDFs to your notes. It embeds the images into the bodies of your notes, and it treats other documents (such as PDFs) like email attachments.

### Permanote

http://permanote.tumblr.com/

According to their blog, they are currently changing their business model but the old application is still available. Permanote is simple, it doesn't let you collect your notes in notebooks, but it has a very good search engine. You can use tags to organize and filter your notes and format your notes using Markdown.


## Conclusion

As you can see, it is hard to choose which application is the best. Every application has its advantages, and it all depends on your specific needs. If you like security and freedom and prefer open-source, Laverna or Turtl might be the right solution for you. TagSpace is great for organizing and tagging your own data on different devices and accessing them from one application. Evernote and OneNote are great feature-rich solutions if you don't need Linux version and you are not worrying about getting locked-in. If you are a researcher, teacher or a student, easy annotation and outline of web data in Diigo or OneNote's ease of organizing information on a page, and broad possibilities to annotate notes might be exactly what you want.
