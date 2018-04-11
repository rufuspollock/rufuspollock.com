Rufus Pollock's website: http://rufuspollock.com/

Central git repo is on gitlab:

http://gitlab.com/rufuspollock/rufuspollock.com


## Planning etc

Main hackmd: https://hackmd.io/CYZgbADAHFEKwFoCcAzKBjBAWJILLCSwQENgUkBGcCEuAUwiA===


## Technical Stuff

* The source is managed in git.
* The website is statically built using hugo.

To work on the website:

* Install hugo
* Install git lfs and pull git large files
* Run hugo:

  `hugo serve`

### Deployment

We deploy it using gitlab pipelines -- see .gitlab-ci.yml

## Publishing

In this section we explain how new articles should be added to the site.

### Table of contents

#### How to define a table of content in a page

Simply add `{{< toc >}}` in a desired position within a page and a table of contents will be rendered there. E.g., the following document would have table of content in the beginning:

```
{{< toc >}}

# My h1 heading

Some intro text

## My h2 heading

Some paragraph
```

#### Organizing headings

It is strongly recommended to have consistent headings in an article:

* all h2 headings should belong to a h1 heading;
* all h3 headings should belong to h2 heading;
* and so on.

If headings are not defined in this way, a table of content would look like following. Here, only h3 headings defined without h2 and h1 headings:

<iframe src="https://drive.google.com/file/d/0B4NG_fY_aUNbemFoT2R0ZVp0alk/preview" width="640" height="480"></iframe>
If the image is not visible preview it here - https://drive.google.com/file/d/0B4NG_fY_aUNbemFoT2R0ZVp0alk/view?usp=sharing

### MathJax

#### Inline MathJax

When writing inline MathJax, please wrap formulas in single `$`, e.g.:

```
This is my inline math formula: $ \\Omega\_{G} = [0,1]^{N}, N=|G| $
```

#### Block MathJax

For block MathJax wrap formulas in double `$$`, e.g.:

```
The formula below is not inlined:
$$ \\Omega\_{G} = [0,1]^{N}, N=|G| $$
```

### Embeddable PDFs

To embed a PDF file into a page, you need to use our custom shortcode when writing a content document in markdown. Just have following code snippet where you want to embed a PDF:

```
{{< pdf src="URL or path to pdf file" >}}
```

See an example of how it works:

Source file: https://gitlab.com/rufuspollock/rufuspollock.com/blob/master/content/post/2016-05-20-my-evening-seminar-in-may-2016-at-the-faculty-of-law-as-a-guest-of-cipil.md
How it is rendered: https://rufuspollock.com/2016/05/20/my-evening-seminar-in-may-2016-at-the-faculty-of-law-as-a-guest-of-cipil/
