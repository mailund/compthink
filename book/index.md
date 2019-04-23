# The Beginner’s Guide to Markdown and Pandoc

Markdown is a markup language. The name is a pun, but where the humour might be be atrocious the language is not. The Markdown language lets you write plain text documents with a few lightweight annotations that specifies how you want the document formatted.  Such annotations are the defining characteristics of a markup language. Markup languages separate the semantic or content part of a document from the formatting of said document. The content of a document is the text, what should be headers and what should be emphasised etc. The formatting specifies the font and fontsize, whether headers should be numbered, etc.

Markup languages have a stronger focus on semantic information than direct formatting as you would do with WYSIWYG (what you see is what you get) formatting. With markup languages, you might annotate your text with information about where chapters and sections start, but not how chapter and heading captions should be formatted. Decoupling the structure of a text from how it is visualised and makes it easier for you to produce different kinds of output. The same text can easily be transformed into HTML, PDF, or Word documents by tools that understand the markup annotations. And because writing the text and formatting it are separate steps, you can apply one or more text documents to the same transformation program to get a consistent look for related documents, or you can transform the same document into multiple output formats so the same document can put on a webpage or in a printed book, for example. Most WISIWYG editors can export to different formats but they usually do not let you output to the same document type with different formatting, e.g., output PDF files in A4, 6’’ x 9’’ and 7’’ x 10’’ with point size 11 in the first two and 12 in the last. With a Markup language, this is relatively easy.

Among markup languages, Markdown is one of, if not the, simplest. The annotations you add to a text are minimal and most likely you will already have seen most of them if you occasionally use plain text files. For example, where you would use italic or boldface in Word, you would write \*italic\* and \*\*boldface\*\* in Markdown, and mostly likely you have seen this notation before. In my misspelled youth I frequently used TeX/LaTeX and HTML/SGML/XML. I know people who cannot concentrate on the text body if it is full of markup information. With Markdown, the markup annotation is almost invisible and they have no problem working with that. With Markdown you can generate documents in other markup languages, so you do not need to know them. If you want the full power to format your documents the way you want them, then I still recommend that you learn the other languages. You can use that knowledge to create templates, see [Chapter @sec:templates], and then you only need to use e.g. LaTeX or HTML when writing the templates. You can then still keep your document in Markdown. One exception, where you still want to use LaTeX, is if you need to write maths in your document. Then you you need to write it in LaTeX, see [Chapter @sec:math].

You need a program for translating Markdown into other file formats. The tool I will use in this book is Pandoc. Pandoc supports basic Markdown and several different extensions. It also lets you define templates and stylesheets to customise the transformed files. Pandoc can do more than translate Markdown files into different output files. It can translate from and to several different formats. I will only describe how you translate from Markdown to other formats, but if you have a existing text in Word, for example, and you want to try out Markdown by editing that document, then you should be able to generate a Markdown file from the Word file, edit the Markdown format, and then translate the Markdown document back to Word.


# Why use Markdown and Pandoc


If you are used to WYSIWYG editors such as Microsoft Word, you might reasonably ask why you should use Markdown files. You can write your document and format them any way you like, and you can export your document to different file formats if you wish. For short document that you only need to format one way you do not need Markdown. I will argue that Markdown can still be a competitive choice for such documents, but it is for more advanced applications where you really want to use it.

For applications that are just as easy to handle with a WYSIWYG editor, plan text can be a better choice in situations where you need to share documents with others. A de facto file format for this is Word files but not everyone has Word. I don’t. I can import Word files into Pages, which I have, and export to Word, but I don’t know what that does to the formatting. Everyone has an editor that can work on plain files, and with a plain text file you know exactly what you are editing.[^1] If the text and the formatting are separated then someone with more artistic skills can handle the formatting while I can write the text. One argument for Word might be version control. This is an important feature but with plain text files you can put them under real version control, for example GitHub, and that is superior to version tracking.

If you need your document in different formats, for example you might need to include your document in a printed progress report and also have it on a webside, then you can export the document to as many file formats as you need. If you need different typography for the different file formats you might have to do substantial manual work. You might need to change all the document styles by hand, and in the frequent occasions where you need to make changes to your text, you need to change the styles for each file format more than once. If you separate style and text you avoid this problem altogether.

Using a markup language to annotate your text makes it easier for you to distinguish between the semantic structure of a text and how it is formatted. In the Markdown document you markup where headers and lists are, for example, but not how these should be formatted in the final output. The formatting styles are held in different files and you can easily transform your Markdown input into all the output file formats and styles you need. Furthermore, someone else can work on the style specification while you concentrate on the text. You Markdown doesn’t have to be in a single file either. You can split it into as many as you want, and then different authors can work on separate pieces of the text without worrying about how to merge files afterwards. With version control you can even work on the same file in parallel up to point.

  

## Separating semantics from formatting

Most documents have a semantic structure. Texts consist of chapters and sections, plain text and emphasised text, figures and citations, quotes and lists. When we read a document, these semantic elements are visualised by different fonts, bold and italic text, different font sizes, and we don’t directly see the semantic structure. Because we don't directly see the structure, it is easy to forget that it is there.

Most word processors separate semantics from formatting. If you take care to use the formatting section when working on a Word document, then the semantic information needed to change styles, i.e., the visual representation of all semantic units, e.g., headings, is readily available. Separating the semantics of a document from its formatting is not an exclusive property of markup languages. However, when separation of text and semantics is not enforced there is a potential for error. If you decide to change the font size of level two section headers, for example, you can easily do this, but you can equally easy highlight a single section header and reformat that, changing only that single header. That makes this particular header different from all the rest, and if you later modify the formatting of level two headers, you won’t be changing this one header. Great if this is on purpose; not great is this is not what you wanted.

With WYSIWYG editors you can separate semantics from formatting, but it is easy to break this separation. With markup languages you can also define some text elements as special, and their formatting different from related elements, but you have to do this explicitly so you cannot easily do this by mistake. Keeping the core text consisting of semantic elements and separate from formatting is important in many situations. If you want to translate your text into both paper documents and web pages, you typically want the formatting to be different in the two resulting documents. If the core text only contains the semantic structure, this is easily done, by having a different mapping from semantic elements to formatting information, typically called *templates* or *style sheets* (see [Chapter @sec:templates]). With different stylesheets for different output formats, the formatting is tied to the output text rather than the input text, see [@fig:many_to_many].

![You can translate the text in multiple documents, or multiple chapters that should be merged into a single document. You combine these with templates for formatting the documents and using Pandoc you can combine it all to produce the documents you want.](many-to-many-compilation.pdf "many_to_many")


Having the semantic elements of the text explicitly represented, rather than implicitly through how the text is formatted, is also important if you want to automatically make a table of contents or lists of figures and tables. If all sections are marked up explicitly as sections, with headers at different section levels, any tool can scan your document and identify these. If the tools had to guess at the semantic meaning of text elements, based on how the text was formatted, this would be a much harder task.

Using WYSIWYG word processors doesn’t prevent you from structuring your documents as semantic units—they usually support this—but having an explicit markup language makes it much easier to enforce.

## Preprocessing documents

If your documents are in plain text, you also get a lot of options for how to process your text before you format it into a final document. There are a large number of tools that will work well with plain text and let you preprocess your documents.

Preprocessing documents often require a few programming skills, so it might not be the first thing you want to worry about if you are only interested in writing text, but since the option is there, you can write your text without worrying about processing it initially, and add such steps later. When I write my books, I make both PDFs for printed versions and EPUBs for ebooks. In PDF documents, I want my figures to be inserted as PDF, so they are in vector graphics format and can be resized without resolution issues, but for ebooks, I need them to be bitmap graphics. I use a preprocessor to take care of this.

I write a lot about R programming, and in those books, I have a lot of code examples. Here, I use another preprocessor, one that lets me evaluate the code when processing the documents so I know that all the code examples work and so I can get the output of running code inserted into the documents automatically before I create the output formats.

Preprocessing your documents adds some complications to how you process your text, but the complications are only there when you need them. If you do not need a preprocessor then you can ignore that they exist altogether. If you *do* need preprocessing, then read [Chapter @sec:preprocessing].

## Why Markdown?

There are many different markup languages you can use. HTML (hypertext markup language) is used for web pages. TeX and LaTeX are used for many kinds of text documents but are especially powerful for typesetting mathematics. Markdown is what we do on in this book.

What makes Markdown particularly pleasant to work with is its simplicity. In HTML, for example, you need to structure your text using tags that enclose every paragraph, every header, every list, etc. When you edit an HTML document, it is hard to separate the annotations from just the text you want to write. LaTeX has the same problem. The annotation of the text can be hard to ignore when you want to focus on writing.

Worse, if write your documents in HTML or LaTeX much of the text is markup codes that specify the formatting. How much, of course, depend on your document, but any markup instructions you make can make the text difficult to read.

Consider this Markdown document:

```
# This is a level one header

This is a paragraph

## This is a level two header

Here is a paragraph that is followed by

 * an unnumbered
 * list


1. and a numbered
2. list that is
3. three items long
```

I hope you will agree that the markups here are minimal and that they do not get in the way of reading or writing the text.

For comparison, the HTML version of the same text looks like this:

```html
<head></head>
<body>
  <h1>This is a level one header</h1>
  <p>This is a paragraph</p>
  <h2>This is a level two header</h2>
  <p>Here is a paragraph that is followed by</p>
  <ul>
    <li>an unnumbered</li>
    <li>list</li>
  </ul>
  <ol type="1">
  <li>and a numbered</li>
  <li>list that is</li>
  <li>three items long</li>
</ol>
</body>
```

It is not terribly complicated and after look at it a bit you can certainly follow the structure of document. It is far from as clean as the Markdown file.

The LaTeX version is slightly easier to read than the HTML file, but there are still several formatting instructions that get in the way of just writing.

```latex
\section{This is a level one header}
This is a paragraph

\subsection{This is a level two header}
Here is a paragraph that is followed by

\begin{itemize}
\item an unnumbered
\item list
\end{itemize}

\begin{enumerate}
\item and a numbered
\item list that is
\item three items long
\end{enumerate}
```

Markdown is designed so you can annotate your text with semantic information with little annotation clutter. It is designed such that reading the input text is almost as easy as reading the formatted text. With Markdown you don’t have quite the same power to control your formatting as you do in a language like LaTeX, but the simplicity of Markdown more than makes up for it.

## Why Pandoc?

Since Markdown is just a language for adding structure to a text, it is not tied to any particular tool. You can use any Markdown aware software when you want to process your documents. Many blogging platforms will let you write your text in Markdown and automatically format it for you. Translating Markdown into HTML was, after all, one of the primary motivations for the language. Now, many text editors also support Markdown and will  support formatting in Markdown and exporting to various file formats, usually with various formatting and style choices  determining what your output files will look like.

If your editor can export to different file formats and in different styles, then that is obviously the easiest way for you to export your Markdown text. With Pandoc, however, you have a lot of power over how your documents should be processed. Pandoc is vastly more versatile than any Markdown-aware text editor that I am aware of.

If you want to create a simple document with no fluff, it is easy to do so with Pandoc, but easier to do from inside your editor. Try using Pandoc for simple cases though, so you get familiar with the tool. When you get into serious writing, and you want full control of how your final documents will look, then you need the power of Pandoc. The learning curve can be steep, but if you are familiar with using Pandoc for simple documents, then you have a foundation to build on when you explore advanced features.





# Writing Markdown

If you have used plain text to write and share documents in the past, then you are likely to be familiar with most Markdown markup annotations already. Much of the syntax for Markdown is based on how people have written plain text documents for years. This chapter covers the basic Markdown annotations, which make up 99% of the annotations you will use regularly.

## Sections

At the highest level, a text document is composed of its sections. Sections come at different levels. In a book the top level might be chapters, the second level are sections within the chapters, and the third level are subsections within the sections.

To make a new section, you give it a header. The headers start with a hashtag. Using one hashtag gives you a level one header, which will be a chapter in a book or a section in a smaller document. Two hashtags give you a level two section, a section if the first level is chapters or a subsection if the first level is section. The next level sections have three hashtags, and so on.

    # Header level 1
    ## Header level 2
    ### Header level 3

For the first two levels, you can alternatively underline the section titles with `=` and `-`, respectively:

    Level one header
    ================
    Level two header
    ----------------

Any text you write following a header becomes the body of the section.

By default the headers are numbered. You can change this using a template (see [Chapter @sec:templates]) or you can disable numbering on selected headers by putting “{-}” or “{.unnumbered}” after the header title:

    # Unnumbered header {-}
    ## Another unnumbered header { .unnumbered }
## Emphasis

We emphasise part of a text for example by putting it in italic or boldface. In Markdown we use asterisks, \*, to do this. To put a word in italic, we use *one* asterisk and to put it in boldface we use **two**.

The section above, in Markdown, looks like this:

    We emphasise part of a text by putting
    it in italic or boldface. In Markdown
    we use asterisks, \*, to do this.
    To put a word in italic, we use *one* 
    asterisk and to put it in boldface we 
    use **two**.

You will also notice, that the first asterisk is escaped using a backslash. That backslash prevents Markdown from interpreting the asterisks as the beginning of italic text.


## Lists

You have two kinds of lists: numbered and unnumbered. To create a numbered list, you put a number, followed by a period, at the start of a line and write the list item after it. For the next list item you go to the next line, add another number, followed by a dot, and write the next item text. An example could look like this:

    1. This is a numbered list.
    2. Where this is list item two.
    3. And this is list item three.

The result will look like this:

1. This is a numbered list.
2. Where this is list item two.
3. And this is list item three.

The actual numbers are ignored, so you can get the same result if you wrote:

    10. This is a numbered list.
    51. Where this is list item two.
    42. And this is list item three.

If you want your list items to span multiple lines, you need to indent the lines following the number, like this:

    1. This is a multi-line list item.
       This is also part of the list item.
       And so is this
    2. Here is another one.
       Where this is also part of the list item.

Doing that will give you this list:

1. This is a multi-line list item.
    This is also part of the list item.
    And so is this.
2. Here is another one.
    Where this is also part of the list item.

For unnumbered lists, you use an asterisk or a dash instead of numbers; so you can write an unnumbered list like this:

    * This is a numbered list
    - Where this is list item two
    * And this is list item three

* This is a numbered list
 - Where this is list item two
* And this is list item three

As you can see, you can mix asterisks and dashes, or stick to any of the two you prefer. How the list is formatted when you create a document is determined by the stylesheet and not which symbol you use to create the list.

If you want to have sublists under a list item, you can do this by indenting the lines for the sublists. So you can write a list with a sub-list like this:

```
    * This is a top-level list item
        * Here is a sublist item
        * Here is another
    * Now we are at the top level again.
```

The result will look like this:

* This is a top-level list item
	* Here is a sublist item
	* Here is another
* Now we are at the top level again.

When you indent, you need at least four spaces or a tab per level.

## Tables

To add tables to a document, you can mark up the columns using dashes. You can write a table like this:

       Right     Left     Center     Default
     -------     ------ ----------   -------
          12     12        12            12
         123     123       123          123
           1     1          1             1

The result will the look like this:

  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1

How you align the elements in the columns determine how you align the headers above the dashes. If the text is to the right, the column will be right aligned. The same for left and centre alignment, if the text is on the left or in the middel the table column will be left aligned or centered. If you start the header at the same position as the dashes, you get the default alignment, which is left alignment.

You can leave out the headers, but then you need to repeat the dashes at the end of the table as well.

     -------     ------ ----------   -------
          12     12        12            12
         123     123       123          123
           1     1          1             1
     -------     ------ ----------   -------

-------     ------ ----------   ------- 
     12     12        12            12
    123     123       123          123
      1     1          1             1
-------     ------ ----------   -------

If you do not provide a header, the alignment is determined by the first line in the table. In the example above, in the last column, the reason it isn’t right aligned is that there is a space after the first number in the column before the end of the dashes that specify the column. Move the first number one position to the right, and that column would also be right-aligned.

## Block quotes

Should you need to add a quote to your text, you put a “\>” before the quoted text. 

So you can write:

    > This is a blockquote. The blockquote
    > can span multiple lines. If you don't
    > put any new lines in it, you only
    > need to put the ">" at the beginning
    > of the line.
    > If you want multiple lines where you 
    > include new lines, you should add
    > the ">" to each line.

The result will look like this:

> This is a blockquote. The blockquote can span multiple lines. If you don't put any new lines in it, you only need to put the "\>" at the beginning of the line.
> If you want multiple lines where you include new lines, you should add the "\>" to each line.
## Verbatim text

Sometimes, you don’t want any formatting at all of a text; you want to leave it verbatim as it is. When you want this, you can indent it with a tab (or four spaces). You can write this:

        This will be shown
        absolutely verbatim

The result will then look like this:

    This will be shown
    absolutely verbatim

Sometimes, you also want to add verbatim text inline in a paragraph. To achieve this, simply put the verbatim text in back-ticks. So you can write `` `this` `` to achieve `this`.

## Links

Markdown was initially written for the purpose of making it easier to write text for web pages. Consequently, it has a built-in syntax for inserting hypertext links. These will work both with links to web pages and for cross-references within your text.

You have two options for specifying a link: you can put the destination URL where you insert the link, or you can create a label and map it to the URL so you can refer to the label when you insert a link. To put the URL where you insert the link, you put the text you want to be the link in square brackets and the destination URL for the link in round parentheses right after. You would write text like this:

    This is a link to [my blog](http://www.mailund.dk).

This is fine for most cases, but if you have many links in a paragraph, then the link annotations start interfering with how easy it is to read the text. Instead, you can give the destinations a shorter name and put the destination later in the text. To do this, you replace the round parentheses with square brackets, like this:

    This is a link to [my blog][blog].

Then, later in the text, you define what the link should point to like this:

    [blog]: http://www.mailund.dk

You use the same syntax to make hypertext links within your document. The simplest way to create a link to a section is to leave out the destination but put the name of the section in square brackets. A link to this chapter would then be written like this:

    This is a link to the [Writing Markdown] chapter.

This, of course, will not work if you want the link to contain a different text than the section name, or if you have several sections with the same name. You can work around this by giving the section headers explicit labels. These, you put in curly brackets after the section header. You can assign a label to a header like this:

    # My header {#header}

The hashtag is needed here and is also necessary when linking to the section. The hashtags are used in HTML to refer to sections of a web page, and it is from there that Markdown gets its syntax. To link to the section we have labelled this way, we would write the link like this:

    This is a link to [the section](#header).

Links are only really useful for hypertext documents, and in standard Markdown, you cannot make cross-references to figures or tables or any non-section elements. In Pandoc you can, using an extension, but we cover that in the [Cross-referencing](#crossref) chapter.

## Images

To insert figures in your document, you use a syntax similar to inserting links. The difference is that you need to put a bang, “!”, before the link.

    ![Title of the figure](URL-to-figure)

Typically, you will have the figures as local files and there you use the path to the figure file, either relative to where you build your document or as an absolute path.

    ![Title of the figure](path-to/my-figure)
## Footnotes

You can insert footnotes in your text using a syntax resembling links and images. For footnotes, you need to add a caret, (^). To put the footnote inside the text paragraph you are writing, you add a caret and then the footnote text in square brackets.

    This is text with a footnote.^[This is the footnote.]

Since footnotes tend to interfere with the main text, you can give them a label and add the text elsewhere. When you do this, you name the footnote and put the name in main text.

    This is a text with a footnote.[^footnotelabel]

When you add a footnote this way, the caret has to go inside the brackets. If it goes before the brackets you are adding the footnote inside the text.

Here I put the footnote inside the paragraph that will refer to it^[footnote].

Here I refer to a footnote named `footnote` that must be defined elsewhere[^footnote].

Somewhere the text you must define what a footnote label refers to. The syntax is the same as the one for defining links you can refer to inside the text, except that for defining footnotes the name must start with a caret.

    [^footnotelabel]: This is the footnote text.
    
        If you want it to cover multiple lines, you
        have to indent the following footnote lines.

# Pandoc Markdown extensions

Markdown is, unfortunately, not standardised. Different tools will support different markup syntax and process it differently. The Markdown described in the previous chapter will work in most, if not all, tools. The table syntax is usually less well supported, but the rest of the markup will ordinarily work.

Pandoc provides several extensions to the Markdown language described in the previous chapter. In this chapter, we will see some useful extensions for lists and tables. To get a complete list of Pandoc extensions to Markdown, you should consult the Pandoc documentation (http://pandoc.org/MANUAL.html#pandocs-markdown).

## Lists

Generally, the numbers you use when you write a numbered list are ignored. They are used to indicate list items, but the actual numbering is does not matter. This makes it easier to insert a new item in the middle of a list, which is a good thing, but sometimes you want to start a list at a different number than one, and in that case, basic Markdown can’t help you. With Pandoc, though, lists start with the number you give the first item in a list. So you can start a list at number three like this:

    3. This lists start at number three.
    5. Although we used “5.” to start this
       item, it still gets the number 4.

The numbers in the following list items are still ignored. The result will look like this:

3. This lists start at number three.
5. Although we used “5.” to start this item, it still gets the number 4.

This is a good way to continue lists, but you will have to update the initial number when you have added or removed items in the previous list.

To automatically make a list continue at the next number, even when you changed a previous list, you can use the special symbol “@“. This works just as a number when you use it in a list, and it always counts from where you left off. So you can write something like this:

    (@) Starting a list
    (@) Continuing the list
    
    Here is some text that doesn't
    belong to the list.
    
    (@) This continues the list,
        numbered from where we 
        left off the list.
    
    (@label) This item is labelled
        so that we can refer back
        to it. Like this: see item
        (@label).

The result will look like this:

(@) Starting a list
(@) Continuing the list

Here is some text that doesn't belong to the list.

(@) This continues the list, numbered from where we left off the list.

(@label) This item is labelled so that we can refer back to it. Like this: see item (@label).

This can be very useful for lists of examples or such, but the “@“ counter is global, so you cannot restart the counter. Unfortunately, there is currently no support for both automatically number items *and* restarting counters.

If you make lists using a number and a period, you get the standard numbered lists, but you can also use letters or Roman numerals just by starting the list with such. If you want to use parenthesis instead of periods, you can also do this. You can, for example, create a list like this:

a. This list uses letters instead of numbers.
b. We can make a sublist with roman numerals:
i) This sublist also uses parenthesis
ii) Cool, isn't it?

The source markup for that list looks like this:

    a. This list uses letters instead of numbers.
    b. We can make a sublist with a roman numerals:
        i) This sublist also uses parenthesis
        ii) Cool, isn't it?


Lists are often used to define terms or concepts, and in Pandoc you can create definition lists by following a term with a colon and indenting the start of the definition with a tab or at least four spaces. So you can create definition lists like this:

Something we want to define.
:    Definition of the thing

As long as we indent the following lines, they become part of the definition.

Here starts the next thing we define.
:    Here we write the definition.

   More of the definition

The syntax for creating this list is this:

    Something we want to define.
    :    Definition of the thing
    
            As long as we indent the following lines, they
            become part of the definition.
    
    Here starts the next thing we define.
    :    Here we write the definition.
    
        More of the definition

An alternative syntax uses tildes, “~”, instead of colons:

    Term 1
      ~ Definition 1
    
    Term 2
      ~ Definition 2a
      ~ Definition 2b

Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b

Either syntax will do.

## Tables

Tables are the Markdown markups with the least consistent support in different tools. The table syntax described in the previous chapter frequently works, but even in the two editors I usually write in, they are not supported. In all the Markdown viewers I am familiar with, though, they display correctly.

In Pandoc, there is good support for tables, and Pandoc provides some extensions to table markup beyond that.


For figures, you can add captions using the link syntax. For tables, you have no similar syntax. You can, however, add a caption to a table using “Table: Caption” following the table. So you can create a table with a caption like this:

```
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1
-------     ------ ----------   -------
   
Table: This is a caption
```

The result looks like this:

-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1
-------     ------ ----------   -------

Table: This is a caption

You can leave out the “Table” part if you want; just having the colon will give you a caption.

If you want table cells to span multiple lines, you can do this as well. For multi-line tables, you must put a row of dashes before the header (unless you don’t have a header), you must end the table with a row of dashes and then a blank line, and you must separate rows by a blank line.

This example, from the Pandoc manual, shows how this work:

	-----------------------------------------------------
	 Centred    Default      Right Left
	  Header    Aligned    Aligned Aligned
	----------- ------- ---------- ----------------------
	   First    row           12.0 Example of a row that
	                               spans multiple lines.
	
	  Second    row            5.0 Here's another one.
	                               Note the blank line
	                               between rows.
	----------- ------- ---------- ----------------------

The result will look like this:

-----------------------------------------------------
 Centred    Default      Right Left
  Header    Aligned    Aligned Aligned
----------- ------- ---------- ----------------------
   First    row           12.0 Example of a row that
                               spans multiple lines.

  Second    row            5.0 Here's another one.
                               Note the blank line
                               between rows.
----------- ------- ---------- ----------------------

You can leave out the header, but then you must repeat the dashes that define the columns after the table, followed by a blank line.

	----------- ------- ---------- ----------------------
	   First    row           12.0 Example of a row that
	                               spans multiple lines.
	
	  Second    row            5.0 Here's another one.
	                               Note the blank line
	                               between rows.
	----------- ------- ---------- ----------------------

Result:

----------- ------- ---------- ----------------------
   First    row           12.0 Example of a row that
                               spans multiple lines.

  Second    row            5.0 Here's another one.
                               Note the blank line
                               between rows.
----------- ------- ---------- ----------------------

An alternative syntax for tables uses plain text grids to separate columns. An example, with a header, looks like this:

    +---------------+---------------+--------------------+
    | Right         | Left          | Centered           |
    +==============:+:==============+:==================:+
    | Right         | Left          | Centered           |
    +---------------+---------------+--------------------+

Result:

+---------------+---------------+--------------------+
| Right         | Left          | Centered           |
+==============:+:==============+:==================:+
| Right         | Left          | Centered           |
+---------------+---------------+--------------------+

Without headers, it looks like this:

    +--------------:+:--------------+:------------------:+
    | Right         | Left          | Centered           |
    +---------------+---------------+--------------------+

Result:

+--------------:+:--------------+:------------------:+
| Right         | Left          | Centered           |
+---------------+---------------+--------------------+

For this type of headers, the colons determine the alignment. Put a colon at the end of the “=“ or “-“ the cell-board to get right-aligned columns, at the left to get left-aligned columns, at both ends to get centred columns, and leave them out for the default alignment.

You can also use pipes, “|”, to specify the columns. Then, the syntax will look like this:

    | Right | Left | Default | Center |
    |------:|:-----|---------|:------:|
    |   12  |  12  |    12   |    12  |
    |  123  |  123 |   123   |   123  |
    |    1  |    1 |     1   |     1  |

Result:

| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|   12  |  12  |    12   |    12  |
|  123  |  123 |   123   |   123  |
|    1  |    1 |     1   |     1  |
## Smart punctuation

Proper text typography uses different types of dashes—hyphens in words, en-dashes for numeric intervals, and em-dashes for parenthetical sentences and emphasis. Quotes are usually different at the beginning and end of a text in quotation marks. Three dots are different from ellipses. Many word editors will automatically substitute some dashes and translate straight quotes into the correct form, but not all. Since you are writing Markdown in plain text, and since most keyboards do not give you access to all typographic symbols, Pandoc can help you out with getting these symbols. To enable this, you need to call Pandoc with the option `--smart` (we see how to invoke Pandoc in [Chapter @sec:translating]).

If you turn on smart punctuation, quotes will be handled correctly, three dots will be translated into ellipses, a single “-“ will be a hyphen, two dashes will give you an en-dash, and three dashes will give you an em-dash.

# Translating documents {#sec:translating}

Once we have a document written in Markdown we want to translate it into other file formats using Pandoc. First, though, we have to download Pandoc. Go to http://pandoc.org/installing.html and follow the instructions relevant for your platform.

## Formatting a Markdown document with Pandoc

For our first example, we can take the small Markdown document shown below:

    # This is a test document
    
    Here is some text in the document.
    
    * This is a list
    * With two items


If we save this Markdown document in a file called `input.md`, we can translate it into an HTML file, `output.html` using the command:

    pandoc -o output.html input.md

The `-o` option specifies the output file. The `input.md` file is specified without any options. You do not need any options for input files, and you can provide more than one. If you provide more than one input file, they are in effect concatenated before Pandoc process them, so if you want to construct a book from several chapters you have written in separate files, you can provide them on the command line in the order you want the chapters to appear in the book.

Pandoc figures out the input and output format from the file extensions, so if you use the command above, it will know that the input is Markdown (filename suffix `.md`) and that the output should be HTML (filename suffix `.html`). You can make the format of input and output formats explicit. You can use the option `--from` to specify the input format and `--to` to specify the output format. In most cases, you will not need to specify the formats—the filenames contain all the information you need—but sometimes different formats share the same filename suffixes, such as the EPUB and EPUB3 formats that both use filename suffix `.epub`. In those cases, you need the options. 

If you specify the input and output document format then you can also treat `pandoc` as a program you can pipe input into and get the formatted document out from. You could, for example, write

	cat input.md | pandoc --from markdown --to html > output.html

In itself there is little use for this, but combined with preprocessing ([Chapter @sec:preprocessing]) and filters ([Chapter @sec:filters]) it is very handy.

Back to the output of  `pandoc`. If you run the command 

    pandoc -o output.html input.md

above in your terminal, then the `output.html` file should now contain the following HTML:

 <h1 id="this-is-a-test-document.">
	    This is a test document
	  </h1>
    <p>Here is some text in the document.</p>
    <ul>
    <li>This is a list</li>
    <li>With two items</li>
    </ul>
   
If you are not familiar with HTML, this might not be readable, but I hope that you can at least recognise the elements from the input Markdown, at least.

This HTML is not a complete HTML file. It is a fragment of an HTML file that corresponds to the Markdown document, but it is missing header and footer markup that is needed for a complete HTML page. Per default, Pandoc creates HTML markup that can be added to a web page, but not stand-alone documents. To get the header and footer added as well, you can use the option `--standalone`.

    pandoc --standalone -o output.html input.md

The `--standalone` option is needed for HTML output if you want a complete document. If you choose an output format that is typically not meaningful as a fragment, such as PDF documents (suffix `.pdf`), EPUB documents (suffix `.epub` or `.epub3`, or Word files (suffix `.docx`), Pandoc will automatically create complete documents and the `--standalone` option is not needed.

If you run 
    pandoc --standalone -o output.pdf input.md

you will get a warning

```
[WARNING] This document format requires a nonempty 
  <title> element.
  Please specify either 'title' or 'pagetitle' in
  the metadata,
  e.g. by using --metadata pagetitle="..." on the
  command line.
  Falling back to 'input'
```

but despite the warning you will get an HTML document that contains all the elements such a document needs:

```
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>input</title>
  <style>
      code{white-space: pre-wrap;}
      span.smallcaps{font-variant: small-caps;}
      span.underline{text-decoration: underline;}
      div.column{display: inline-block; vertical-align: top; width: 50%;}
  </style>
  <!--[if lt IE 9]>
    <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
  <![endif]-->
</head>
<body>
<h1 id="this-is-a-test-document">This is a test document</h1>
<p>Here is some text in the document.</p>
<ul>
<li>This is a list</li>
<li>With two items</li>
</ul>
</body>
</html>
```

There is more generic HTML here than there is of our text but luckily we do not need to worry about it; we can focus on the Markdown and let Pandoc worry about the rest.

The warning we got has to do with the title we get in the line

```
  <title>input</title>
```

Pandoc just took the name of the input file but was hoping to get the title explicitly provided. You can do this using meta data, see [Chapter @sec:metadata]. Ignore it for now.

You can try making different output formats with the commands

    pandoc -o output.pdf input.md
    pandoc -o output.epub input.md
    pandoc -o output.epub input.md
    pandoc --to=epub3 -o output.epub input.md

In the last example, we explicitly specify that the EPUB format to use in the output is EPUB3.

Another case is where we might want to specify the to-format is for PDFs. By default, Pandoc will create PDF files using LaTeX, but you can specify that it should use ConTeXt instead with the command:

    pandoc --to=context -o output.pdf input.md

To get a complete list of supported input and output formats, run the commands

    pandoc --list-input-formats

and

    pandoc --list-output-formats

respectively.

Pandoc can translate between many different input and output formats, but in this book, we will only consider Markdown input and how to translate Markdown to other formats.

## Frequently useful options

There are many options you can use to influence how Pandoc transform a document. I refer you to the online manual (http://pandoc.org/MANUAL.html) for a full list. Here, I will list a few that I find particularly useful in my own writing.

### Sections and chapters

First, we consider options that relate to how sections are interpreted. In Markdown we specify the different levels of section headers by the number of hashtags, but when we produce a document, we sometimes have to worry about whether the top-level sections are parts, chapters, or sections. If we are writing a short report or paper, we want the level one headers to start sections, but if we are writing a book, we want them to start chapters. The default depends on the output we produce, and Pandoc does some guessing for us, but you can choose explicitly what the top level should be using the `--top-level-division` option. For my books, where I want the level one headers to be chapter headers, I use `--top-level-division=chapter`.

### Table of content

To add a table of content to your output document, you can use the option `--toc` or the option `--table-of-content`; the first is just a shorter version of the second. You can specify the level of sections you want in the table of content using the `--toc-depth` option. When I produce ebooks, I typically only want the table of content to be specified at the chapter level, so I use `--toc-depth=1`. When I produce PDF, I am happy with the default. You can play around with the option to see what you prefer.

### Image extensions

If you want to produce both PDFs and ebooks from your Markdown input, you might want to use PDF vector graphics for figures for the PDF output but bitmap PNG for the ebook version. Using bitmap graphics for the PDF output means you have to worry about the resolution, but using PDF graphics for ebooks doesn’t always work. When you insert images into your document using the 

	![Figure caption](graphics-file)

syntax, you need to specify the input file name, but if you want to produce both ebooks and PDFs you don’t want to have to change all the file names depending on which output format you are producing.

You can leave out the filename suffix for graphics files and specify the desired suffix using the

	--default-image-extension

 option instead. Then, for any graphics file where you haven’t explicitly written the filename suffix, Pandoc will use the default. I always use
 
	 --default-image-extension=pdf
 
 when producing PDF documents and
 
	 --default-image-extension=png
 
 when producing ebooks.

### Ebook covers

Ebooks contain cover images together with their text. If you produce ebooks, you want to specify the cover image as well. You can do this using the `--epub-cover-image` option. If your cover image is in the file `cover.png` you write

	--epub-cover-image=cover.png


## Using Makefiles

For this book, I have all my text in a single `book.md` document. This is fine for a short books like this one, but usually, I keep each chapter in a separate file. The command line for compiling my books can get rather long, and I usually have various options for different output formats that I need to remember, so if I had to use the command line each time I wanted to build a new version of a book, it would quickly become tedious and extremely error-prone. So I use Make (https://en.wikipedia.org/wiki/Make_(software)) for compiling my books.

If you are not familiar with Make, I will give you sufficient detail for to read the Makefile I give as an example, and maybe a starting point for your own Pandoc Makefile, but introducing Make in full detail is beyond the scope of this book. There are many programs that solves the same problem that Make does, see e.g. https://en.wikipedia.org/wiki/List\_of\_build\_automation\_software, so there are alternatives to choose from if you do not like Make.

The Makefile I use is not sophisticated and it suffices to know this:

1. You define a variable by writing `VARIABLE_NAME := VALUES`.
2. You refer to the value that a variable holds using `$(VARIABLE_NAME)`.
3. When you write `target: dependencies` you say that of you want to have `target` then, if any of the dependencies have changed since lasts time you constructed `target` then you need to construct it again. If dependencies of dependencies have changed then you need to build the dependencies and then the. target. And so on.
4. The lines after `target: dependencies` that are indented by a tab are the instructions your computer needs to do to to make `target`.
5. The first `target: dependencies` line in the Makefile is the target it will make if you do not provide another target on the command-line.

The Makefile I use for this book looks roughly like this (although I have left out options that I have not explained yet but in later chapters). I will walk you through it below.

```
CHAPTERS := header.yml book.md 
PANDOC := pandoc
    
OPTS_ALL :=  --toc --smart \
             --top-level-division=chapter
    
PDF_OPTS := $(OPTS_ALL) \
            --default-image-extension=pdf
    
EPUB_OPTS := $(OPTS_ALL) \
             --default-image-extension=png \
             -t epub3 --toc-depth=1 \
             --epub-cover-image=cover.png
    
all: book.pdf book.epub book.docx
    
book.pdf: $(CHAPTERS) Makefile
    $(PANDOC) $(PDF_OPTS) -o $@ $(CHAPTERS)
    
book.epub: $(CHAPTERS) Makefile
    $(PANDOC) $(EPUB_OPTS) -o $@ $(CHAPTERS)
    
book.docx: $(CHAPTERS) Makefile
    $(PANDOC) $(PDF_OPTS) -o $@ $(CHAPTERS)
    
clean:
    rm book.pdf book.epub book.docx
```

I use a variable to hold the input files. Just the header and the single Markdown file in this case. You can specify meta data (see [Chapter @sec:metadata]) on the Pandoc command line or in a YML file. You can put the meta data in your Markdown text but then it has to be the first and you cannot translate a single chapter without including first one. I prefer to put my meta data in a separate file, which in this case is `header.yml`.

I only have one Markdown file for this book. I am writing this in the Ulysses editor where I can split the book into different sections but export it as one combined file. Since the partition in chapters and sections is kept in Ulysses and not reflected in exported Markdown files, I can work with a single file. At the end of the chapter I will show you an example with more than one file and where each file is preprocessed independently.

I put the input files in a variable, `CHAPTERS`, I keep the Pandoc command tool in a variable as well. I have more than one version installed, and I can switch between them by updating the variable. After that, I put the commands that all Pandoc runs share in `OPTS_ALL` and PDF and EPUB specific options in `PDF_OPTS` and `EPUB_OPTS`. I make a Word document but I can use the PDF arguments for this; Pandoc will know how to make a Word document with the same options as used for the PDF. Next is all the target, dependencies and commands for making the targets. The targets `all` and `clean` are special. The first doesn’t build anything, it just triggers a build of its dependencies, which are the three book formats the Makefile knows how to make. The `clean` target doesn’t have any dependencies but it will delete the books we generate with the middle three commands.

I then define some options I want to use for all output formats and then options that I only want to use for PDF and others I only want to use for ebooks. The metadata I set for PDF output I could also have put in the header—they wouldn’t interfere with the EPUB output if I did—but I have chosen to set them here.

I build an EPUB book in the Makefile but if you are planning to publish on iBooks I do not recommend using this file. I find it much easier to format and submit a book using Pages. Pages can read the Word document and that is how I usually submit a book to iBooks: I make a Word document, open it in Pages, and then submit it. You might think that building a book in the right format and then use iTunes Connect to submit it would be easier. You would be wrong. If you want publish on Amazon (on Kindle Direct Publishing) you are also better of using their tool Kindle Create. Kindle Create can read the Word file and you can submit from there. There is a command line tool that can translate from EPUB to the MOBI file format used on Kindle but Kindle Create is easier to use.

# Meta data {#sec:metadata}

If you go back and look at the standalone HTML document we generated earlier, you will find an empty title between title-tags:

  \<title\>\</title\>

Pandoc inserted a title to your document, but it is empty because we didn’t specify it. Try running this command instead:

    pandoc --metadata title="My Title" \
	    --standalone -o output.html input.md

If you now read the `output.html` file, you will see that Pandoc has inserted “My Title” between the title tags and inserted a level one header that says “My Title”.

When Pandoc generates a standalone document, it uses metadata such as title and author(s) to fill in some information. This data is usually not specified in the Markdown input—there aren’t any Markdown annotations for defining such metadata—but you can set it using the `--metadata` option.  Strictly speaking, there are two types of variables that are used when producing the output: metadata, specified with `--metadata` and variables, specified with `--variable`. The difference between them is that metadata can be seen and processed by Pandoc and Pandoc filters—scripts that process your input before it is formatted for the output—while variables are used in templates. If you set a variable using the `--metadata` tag, or in a metadata header, the variable will also be available to templates, so you can usually stick to metadata. The output isn’t *exactly* the same, since filters might do something with metadata that they won’t do with variables, but it is easier to stick with one kind of options. So unless you have good reasons not to, use metadata. Which variables are interpreted by Pandoc depends on the output format and the template (see [Chapter @ sec:templates ]). Check the Pandoc manual at http://pandoc.org/MANUAL.html#templates for details.


## YAML for metadata

There are potentially many values you want to specify as metadata, so you don’t want to rely on command line options for all of those. Luckily, Pandoc can read metadata from a header in your input, specified in another markup language called  YAML (Yet Another Markup Language). YAML is a different kind of markup language than Markdown. It is not intended for marking up text but for providing structured data to tools.

You can put a YAML header with metadata at the top of your input text to provide Pandoc with the information you want to give it. I usually put my metadata in a separate file instead and give that as the first input file when I run Pandoc. Since Pandoc concatenates the input files you give it, this is equivalent putting the metadata at the top of the document, but it does give me the option of using different headers when I produce output in different formats.

A YAML header starts with three hyphens `---` on a line of their own and is terminated with another three hyphens. Inside the header, you can put key-value information. The keys are followed by a colon, and the values follow the colon. The header I use for this book looks like this:

```
---
title:
  "The Beginner's Guide to Markdown and Pandoc"
author:
  - Thomas Mailund
---
```

It sets two values, the title and the author, which is all I need for this book. I didn’t need to put the title in quotes. I could write it as it is, the same way I write my name in the author’s field. However, if a title, or any value in general, contain a colon, you do need to put the value in quotes. Here, I use the quotes to show that as an example.

You will notice that for the `author:` field I have a dash before my name. I didn’t have to put that there either, but I did to tell you about lists. When you want a key to refer to a sequence of values, for example, if you have more than one author on a document, you use dashes before each element in the list. Here, I make `author` refer to a list of length one. The result is the same as if I hadn’t put my name in a list, but if I had a co-author, we would need the list syntax.

I have this header in a file called `header.yml`, and I can compile the book into a PDF file with the command:

```
    pandoc -o book.pdf header.yml book.md
```

## A quick guide to  the YAML language

# Writing code blocks

Markdown is frequently used by programmers to write about programs, so not surprisingly it has support for displaying code examples, typically with formatting to syntax highlight the examples. This support varies between different tools, but Pandoc provides excellent support for many programming languages. 

The syntax for writing a block of code uses either tilde, “~” or backticks, “\`”.  Of these, backticks are more likely to be supported by other tools; so, I will use these here. Every example I give below will also work if you use tildes instead of backticks.

You start a block with three backticks, then write your code, and then end the block with another three back-ticks.

````   
```
for (int i = 0; i < n; i++) {
   printf("%d\n", i);
}
```
````

You can also use tiles instead of backticks, but I will use backticks in this chapter.

````   
~~~
for (int i = 0; i < n; i++) {
   printf("%d\n", i);
}
~~~
````

If you use back-ticks, you get a verbatim text block, just as if you had indented the text. To get syntax highlighting, you must also inform Pandoc of which programming language you are using. You can do this by writing the language after the first line of backticks. To syntax highlight the code above, which is written in the C programming language, you would write:

````
```c
for (int i = 0; i < n; i++) {
    printf("%d\n", i);
}
```
````

The result will look like this:

```c
for (int i = 0; i < n; i++) {
    printf("%d\n", i);
}

```

A block of Python code would look like this:

````
```python
for i in range(n):
    print(i)
```
````

The result would look like this:

```python
for i in range(n):
    print(i)
```


To get a complete list of supported programming languages, you can run the command:

    pandoc --list-highlight-languages
## Code block options

This syntax for displaying code is supported by many websites where it is usual to write code in text, such as on GitHub. You can give more advanced instructions for how code should be displayed, but then you need to use a slightly different syntax that is more Pandoc specific. There, you put instructions in curly brackets after the first three backticks. You must specify the programming language, but prepend a dot to the name, e.g. write `.python` for Python. You can then number the code lines with the instruction `.numberLines`:

````
```{.python .numberLines}
for i in range(n):
    print(i)
```
````

   The result will look like this:

```{.python .numberLines}
for i in range(n):
    print(i)
```
   
You can specify which line number to start from with the option `startFrom`. To start from line 100, we can write:

````
```{.python .numberLines startFrom=100}
for i in range(n):
    print(i)
```
````
   
The result will look like this:

```{.python .numberLines startFrom=100}
for i in range(n):
    print(i)
```
## Syntax highlighting styles

The syntax highlighting scheme is controlled by a form of stylesheet: Cascading stylesheets for HTML output and a set of `\newcommand` options for LaTeX (and thus PDF) output. These highlighting instructions are put directly in the output file (when you make a standalone document) and are thus not easy to override. You can, however, choose from a list of predefined highlighting styles. You can see the complete list by running the command:

```
    pandoc --list-highlight-styles
```

You select a style using the `--highlight-style` option. When I build print versions of my books, I aim for black-and-white output, so I use the option:

```
    pandoc --highlight-style=monochrome
```

This gives me a black and white highlighting using italic and boldface to display different language components. You can also completely disable syntax highlighting, while still using code blocks, using the option `--no-highlight`.




# Writing maths {#sec:maths}

Pandoc has some excellent support for writing math as long as your output file format supports it. Word files have built in support for math and Pandoc will use this if the output file is a Word document. With PDF, Pandoc uses LaTeX as an intermediate format and LaTeX is notoriously perfect for math. With HTML and EPUB you have some math support depending on the version and libraries you use to display the math.

For HTML and EPUB, you have different options for how the output should handle math. I usually use either MathML(https://www.w3.org/Math/) or MathJax(https://www.mathjax.org) when I have math in HTML or EPUB documents.
For MathML you can use the option `--mathml`:

```
    pandoc --mathml -o document.epub document.md
```

For MathJax, you need to produce EPUB3 documents to get it to work, so you must specify the output format as well:

```
    pandoc --to=pub3 --mathjax \
           -o document.epub document.md
```

With either option, you get an EPUB document that displays the math well. Not as beautifully as in PDF documents, where LaTeX handles the math, but reasonably well.

The way you write math in your document is by inlining TeX syntax. The math in output documents will only be TeX if you output a LaTeX file or go though LaTeX when building a PDF file, but the de facto standard for how to write math in plain text is TeX so that is what Pandoc uses.

You start and end math using dollar-signs. If you use one, you get inline math, if you use two you get “display” math, which means you get math on a single line and centred. This is inline math: `$\int_a^b x\,\mathrm{d}x` looks like $\int_a^b x\,\mathrm{d}x$. You write display modemath between double dollar signs, so this

    $$\sum_{j=1}^N \frac{1}{j^2}$$

will result in this:

$$\sum_{j=1}^N \frac{1}{j^2}$$

# Cross-referencing {#sec:crossref}

Cross-referencing is not supported by standard Markdown. Markdown was written mainly to write hypertext documents for web pages, so referencing section numbers, figures, or tables, is just not part of it. We can use the link syntax to make hypertext references to sections, but that is about it.

Pandoc itself doesn't support extensions for other kinds of cross-referencing, but there is a so-called "filter", `pandoc-crossref`, that adds this support. Filters are scripts that are run to modify a document after it has been parsed by Pandoc and before the output format is generated. Filters are beyond the scope of this book, but we will use two in this and the next chapter.

The `pandoc-crossref` filter is not necessarily automatically installed when you install Pandoc, so you need to install it explicitly. How you do this will depend on your platform. I work on MacOS and use the Homebrew (http://brew.sh) package manager, so I installed using

```
    brew install pandoc-crossref
```

The filter is a Haskell package, so you can also install it using the `cabal` package manager if you have the Haskell system installed. 

```
    cabal update
    cabal install pandoc-crossref
```

If you installed Pandoc using any of the packages from the Pandoc releases webpage (https://github.com/jgm/pandoc/releases/), the filter should automatically be included. If all else fails, you can download the source code and compile it at the pandoc-crossref homepage (https://hackage.haskell.org/package/pandoc-crossref).

To invoke the filter when processing a document with Pandoc, you use the option `--filter`. To enable the `pandoc-crossref` filter, run Pandoc as:

```
    pandoc --filter pandoc-crossref
```

Cross-referencing using `pandoc-crossref` uses a syntax similar to hypertext links, but with a twist. You specify labels with curly brackets and insert references to them using square brackets. You need to include cross-referencing type as part of the labels, though. To insert a label, you use the syntax `{#type:label}` and to refer to it you use the syntax `[@type:label]`. The type, here, specifies whether you are referring to sections, tables, figures, or equations.

## Referencing sections

Using cross-referencing via links works well for HTML or EPUB documents, where you have hypertext, but less well for printed media, where you don’t. There, you would make references to chapters and sections using their numbers instead, but that isn’t supported in standard Markdown.

Using `pandoc-crossref`, we can refer to sections via section numbers. We need to define labels for the headers we want to refer to, and these labels must start with the prefix `sec:` (in addition to the hashtag that all header labels must have). We can then insert cross-references to section numbers using `[@sec:label]` markup. An example could look like this:

    # This is a chapter {#sec:chapter}

    ## This is a section {#sec:section}

    See [@sec:chapter] and [@sec:section].

Pandoc doesn’t number sections by default, and while it will number sections in some formats when we use `pandoc-crossref`, we should use the option `--number-sections` to make sure. If for example, you generate PDF output, sections will not be numbered if you leave out this option, and consequently, it makes no sense to refer to sections by their numbers.

```
    pandoc --number-sections \
        --filter pandoc-crossref \
        -o output.pdf \
        input.md
```

This approach will use the LaTeX section numbering system for PDF output but will also work for other output formats such as HTML.

You can set the section numbering depth with the metavariable `secnumdepth`. For example, to number chapters and sections (or sections and subsections, depending on the top level section type), you can add the following line to your metadata header:

```
    secnumdepth: 2
```

This will only affect LaTeX and PDF output, though, and not other output formats.

Alternatively, you can leave the section numbering entirely up to the filter by setting metadata variable `numberSections` to `true` and set the section depth you want to be numbered with the metadata variable `sectionsDepth`. For example in your header, you can add the following lines to get chapters and sections, but not subsections, numbered (assuming the top level headers are chapters; otherwise you get sections and subsection headers numbered):

```
    numberSections: true
    sectionsDepth: 2
```

This will insert chapter and section numbers to the desired depth and let you cross-reference sections in HTML and EPUB format, but unfortunately the cross-referencing does not work in LaTeX and PDF. Here, you only get the section numbers but not the cross-references inserted.

Neither of the two choices for section numbering is ideal for both PDF and EPUB output. Using `--number-sections` will insert section numbers in both output formats, but you can only control the numbering depth in PDF output. Using `numberSections` will insert section numbers to the desired depth in both output formats, but you can’t insert references to them in PDF output. You can’t use *both* `--number-sections` and `numberSections` either since then both the Pandoc filter *and* LaTeX will insert section numbers, and you end up with two of them in each header.

The only solution I’ve found for this is to call Pandoc with different options when generating EPUB and PDF. For EPUB output, I use:

```
    pandoc --metadata numberSections=true \
           --filter pandoc-crossref ...
```

For PDF output, I use:

```
    pandoc --number-sections --filter pandoc-crossref ...
```

I set the numbering depth in my YAML header, using both options for controlling that:

```
    sectionsDepth: 2
    secnumdepth: 2
```
   

## Reference prefixes 

When you need to refer to a section, you use the syntax `[@sec:label]`. When you reference a section this way, the filter will insert both the section number and a default prefix, which is “sec.” for a single section and “secs.” for multiple sections. You can refer to more than one section but separating the labels by semicolons inside the square brackets:

```
	[@sec:label1; @sec:label2]
```


For documents where you have both chapters and sections, this might not be what you want. There you probably want to use the prefix “Chapter” for chapters and “Section” for sections. Unfortunately, you cannot make prefixes that depend on the header depth, but you can disable the prefixes by overriding them.

You can either change the reference prefix on a per-reference basis or globally through metadata. For referring to chapters as “Chapter” rather than “sec.”—as in this example—the best solution is probably to set the prefix explicitly when referring to a chapter, but we can see how both approaches work.

To use a per-reference specific prefix, you need to insert the prefix you want between the start square bracket and the label. So, to make the prefix for the reference to a chapter be “Chapter”, we would write ` [Chapter @Sec:chapter]`.

To change the prefixes globally, we need to set a metadata variable. The metadata variable that controls the section references prefix is `secPrefix`. If we set it to the empty string, we get rid of the prefixes.

```
    secPrefix: ""
```

You can then manually insert the prefixes you want in the Markdown text:

```
    See Chapter[@sec:chapter]
    and Section[@sec:section].
```

Notice the lack of spaces between prefix and references here. This is needed for PDF output; the LaTeX document that Pandoc generates for the references contain a hard space, so if we put a space between the prefix and reference the PDF document will have too much space in the generated text. For HMTL and EPUB, it doesn’t matter.

Completely disabling a prefix can be done on a per-reference basis as well. Just add a “-“ between the start bracket and the label. If you write `[-@sec:chapter]`, you only get the chapter number and not the prefix. You rarely need to set the default prefix to the empty string explicitly. But using that as an example gave me an excuse to introduce the variable.

In general, you can set the `secPrefix` metadata to a list. The first element is used for single references and the second for plural. So, to use “Sect.” as the prefix for a reference to a single section, and “Sects.” as the prefix for multiple sections, we could specify this metadata:

```
    secPrefix: ["Sect.", "Sects."]
```

Strictly speaking, the prefix list can have any length, and the number of references is used to select a prefix. So, if you want a special prefix when you refer to three sections, you can add a third element to the list. When you have more references than prefixes, you get the last element in the list. Thus, if you specify two elements, the first is used for singular references and the second for multiple references.

You might want to use lowercase “sect.” when you refer to a section in the middle of a sentence but “Sect.” at the beginning of sentences. With `pandoc-crossref` it is simple to switch between upper case and lower case label prefixes. If you insert a label that starts with an uppercase, your prefix will be in uppercase as well. Thus, if you write `[@Sec:label]`, the default prefix will be “Sec.”; if you write `[@sec:label]`, the default prefix will be “sec.”. The same goes for references to figures, tables, equations, etc.


## Referencing figures, tables, and equations

To reference figures, you use pretty much the same syntax as for sections, except for where you define figure labels. To define a label for a figure you must  give it the prefix `#fig:` and place the label right after the markup for inserting the figure, so using the syntax:

```
    [Caption](link-to-figure){#fig:label}
```

Notice, you cannot put a space between the figure insertion and the label definition. You refer to figure labels as you would with references to sections.

For tables, your labels must start with `#tbl:` and placed after the table caption:

```
a   b   c
--- --- ---
1   2   3
4   5   6
    
: Caption {#tbl:label}
```

For tables you *must* have a space between the caption and the label.

For display-style math, that is math that stands on a line of its own and is written with two dollar signs, you can add labels if they begin with `#eq:` and are put on the same line as the math with a space between the label and the terminating double dollar signs:

```
   $$ f(x) = x^2 + a x $$ {#eq:label}
```
 
You can change the default prefix for figures, tables, and equations—as you can for sections—with the metadata `figPrefix`, `tblPrefix`, and `eqnPrefix`, respectively. 


For more details on how to use the cross reference filter, I will refer to its online manual (https://hackage.haskell.org/package/pandoc-crossref).



## Bibliographies

If your text requires citations and a bibliography, you can enable the filter `pandoc-citeproc` by either running Pandoc with the 

	--bibliography

option or using 

	--filter pandoc-citeproc

If you use both filters, you must always use `pandoc-crossref` first

    pandoc --filter pandoc-crossref --filter pandoc-citeproc ...

The two filters use similar kinds of citation syntax, and this means that the order in which you run the filters matter. The `citeproc` filter gets confused if it sees cross reference labels. The same does not happen if you run the cross reference filter first; it will leave the citation codes alone so they can be handled by the citation filter.

With the `--bibliography` option you need to specify the file that contains your bibliography. Using `--filter pandoc-citeproc` you can specify the bibliography file as metadata in your YAML header instead, e.g.:

```
---
    bibliography: citations.bib
---
```


The `pandoc-citeproc` filter can read bibliographies in various file formats and will pick the format based on the file suffix. With `.bib` files it will use BibTeX. For EndNote you would use `.enl` and for ISI `.wos`. Check the online documentation (https://github.com/jgm/pandoc-citeproc/blob/master/man/pandoc-citeproc.1.md) for a complete list.

To control the format used for citations and the bibliography, you can specify a CSL (http://citationstyles.org) file with the metadata variable `csl` or the Pandoc option `--csl`. CSL files for most journal styles can be downloaded from GitHub (https://github.com/citation-style-language/styles).

For example, if "smith12" is a key in your bibliography, you can insert a citation using `[@smith12]`. You need to include the `@` even though it isn’t part of the reference key; the filter uses this to recognise citations. You can cite more than one paper by separating the references with semicolons: `[@smith12; @smith14]`.

Depending on the citation style, the inserted reference might contain author names. This doesn’t read well if you have already mentioned authors in the text, and you can disable it with a minus before the reference: `[-@smith12]`. The same effect is achieved by leaving out the square brackets and write `@smith12`.

More general, you can insert text in the citations to add e.g. page information or other comments, such as `[see @smith12, chap1; also @smith14, chap 12]`. If you leave out the square brackets to get an in-text citation, you can add comments to appear inside parenthesis (again, depending on your citation style) by writing the comments in square brackets after the reference: `see @smith12 [chapter 11]`.

The bibliography will be put at the end of your document. If you want to give the bibliography a section header, you should end your Markdown document with the header for the bibliography.



# Using templates {#sec:templates}

When Pandoc creates a standalone document, it uses a template for the output. A template is essentially a document with some placeholder variables, where metadata and your processed Markdown text will be inserted. Which metadata will be used in a template depends on the output format; you can get a full list of variables for your output in the Pandoc manual (http://pandoc.org/MANUAL.html#templates). Pandoc automatically specifies some metadata, as described in the manual, but you can specify other metadata in the header.

Unless you specify another template explicitly, Pandoc will use a default for the output format. You can get Pandoc to show you the template it uses for a specific output by running the `pandoc -D <format>` command, e.g. to see what it will use if you generate a PDF file—which it does by generating a LaTeX document and then compiling it—you can write:

```
    pandoc -D latex
```


You can also get a full list of default templates and what they look like at https://github.com/jgm/pandoc-templates.

If you don’t know LaTeX, the template you get by running `pandoc -D latex` might not make a much sense, so let us look at `pandoc -D html` instead. The output is rather long, and I won’t replicate it all here but highlight a few parts of it.

Remember the title we discussed in [Chapter @ sec:metadata]. It was empty before we provided metadata for the title. Let us see what it looks like in the template. There you will find a line that looks like this:

```
    <title>
      $if(title-prefix)$
        $title-prefix$ --
      $endif$
      $pagetitle$
    </title>
```

The stuff in dollar-signs specify placeholders and code for how the template should be processed. Inside the title tags in the HTML template, you have two metadata variables that can be inserted, `title-prefix` and `pagetitle`. The title prefix will only be inserted if it exists, that is what the `$if(title-prefix)$` code checks. Strictly speaking, `pagetitle` will only be inserted if it exists. Otherwise, we get an empty string, but because the title prefix should be followed by a dash, there is an explicit test to see if anything should be inserted.

We never provided metadata for `title-prefix` and `pagetitle`, so it is hard to see how they relate to the `title` metadata we provided. We *could* have provided those two explicitly, but Pandoc creates them based on our title. It directly use `title` variable elsewhere in the template, where the template contains:[^2]

```
    <h1 class="title">$title$</h1>
```

Pandoc and filters can access metadata and create new metadata, which is what it does for the `title-prefix` and `pagetitle`. The `title` placeholder is just inserted directly as the text you specified in the metadata.

I am not aware of any documentation for exactly what metadata manipulations you can expect for each output format, and I am not sure you should rely on any as it might not be stable across different versions of Pandoc and filters. If you don’t work with derived metadata and stick to explicitly defined metadata, however, how the data is used is relatively straightforward. If you have a simple placeholder like `$title$`, then the string you specified in the metadata will just be inserted there in the output file.[^3]

As we saw for `title-prefix`, metadata can also be inserted conditional on it being defined. To insert `some text` only if a metavariable `variable` is defined, a template can contain this construction:

```
    $if(variable)$ some text $endif$
```

There is also an if-else construction that looks like this:

```
    $if(variable)$
    some text
    $else$
    some other text
    $endif$
```

Finally, there is a loop-construction. In the HTML template, you can find this piece of text:

```
    $for(author)$
    <h2 class="author">$author$</h2>
    $endfor$
```

This runs through the authors specified in the metadata and inserts each of them. If `author` is not a list, it will still work, it will just be considered a list of length one, but if we did have a list of authors, we will get a level two header for each of them.

Metadata can be structured with values containing lists of key-value bindings. Take this example from the Pandoc manual for structured author information:

```
    author:
    - name: Author One
      affiliation: University of Somewhere
    - name: Author Two
      affiliation: University of Nowhere
```

Here, authors are not simple strings, but structures with a name and an affiliation. Inside a template, these fields can be accessed using “dot-notation”, so a template might contain code like this:

```
    $for(author)$
     $if(author.name)$
       $author.name$
       $if(author.affiliation)$
         ($author.affiliation$)
       $endif$
     $else$
       $author$
     $endif$
    $endfor$
```

This code iterates through the authors list and inserts authors that are named, and if they have an affiliation, the affiliation is inserted after the name. If the list of authors contains items that are not structured with a name and an affiliation, the template inserts the list item (see the `$else$` part of the `$if(author.name)$` test).

The most important part of the output, of course, is the processed input text. In the template, this is shown as the hardly noticeable `$body$` placeholder. It doesn’t look like much, but this is where all your Markdown will be inserted once it is processed to the output format.


## Writing your own templates

Templates are another of those features that are nice to have when you need them, but you don’t have to worry about when you don’t. You can use Pandoc without every having to worry about templates, but if you have to format your documents in a specific way, you don’t have to abandon Pandoc to write your text; you can create a template to take care of the formatting. For example, if you are an academic like me, and have to use different templates for submissions to different journals, you can make templates to match the journals. Journals often provide LaTeX templates for papers, and you can take one of those templates and put in Pandoc placeholders, and presto you have a Pandoc template and you can write the paper in Markdown and still have it formatted according to the journal standard.

You can get inspiration for writing your own templates from Pandoc’s user contributed templates (https://github.com/jgm/pandoc/wiki/User-contributed-templates). I find that the easiest way to create a new template is to take one of Pandoc’s existing templates and modify it, or by taking an existing HTML or LaTeX file and put in metadata and `$body$` placeholders.




I admit that there is a little more work involved with creating templates if you want to write your articles in Markdown instead of LaTeX, but the ease of use of Markdown does make up for it, in my opinion. Plus, you only need to modify a template once, after all, and then you can reuse it for future articles, books, reports etc.

## Using stylesheets

For HTML output, including EPUB that is just a bundled HTML document, much of the typography is defined using cascading style sheets (CSS) (https://en.wikipedia.org/wiki/Cascading_Style_Sheets). This is a language for specifying the layout of HTML pages, and how it works is beyond the scope of this book. I will just mention that to control the output for HTML formatting you should use the `--css` option to specify the stylesheet, and for the EPUB format you should use the `--epub-stylesheet` option.

# Preprocessing {#sec:preprocessing}

# Filters {#sec:filters}

Filters let you manipulate your documents similarly to preprocessors. Unlike preprocessors, they do not modify the text before Pandoc gets hold of it, but rather they are plugged into the text transformation that Pandoc does. Think of them as post processors; it is not far from the truth.

Both preprocessors and filters have strength and weaknesses. They can do the same things to your files but some things are easier to program in a preprocessor and some things are easier to program in a filter.



# fixme below

Installing Pandoc modules (assuming Haskell compiler GHC and cabal is installed—https://www.haskell.org/cabal/download.html).

```bash
$ cabal install pandoc
```

## Haskell filters

**fixme now to write plugins — I don’t actually know how to do it.**

foo http://pandoc.org/filters.html a

```haskell
import Text.Pandoc.JSON

main:: IO()
main = toJSONFilter extractFigLabel
    where
    extractFigLabel (Image (id, classes, keyValPairs)
                     caption (url, title)) =
        Image (title, classes, keyValPairs) caption (url,[])
    extractFigLabel x = x

```

## Python filters

```bash
$ pip install pandocfilters
```

other languages https://github.com/jgm/pandoc/wiki/Pandoc-Filters  oo

```bash
$ pip install panflute
```

```python
import sys
from pandocfilters import toJSONFilter, Image

def separator(key, value, format, meta):
    if key == "Image":
        attr, caption, target = value
        _, classes, pairs = attr
        url, name = target

        return Image((name, classes, pairs),
                     caption, (url,""))

    else:
        # do not change anything.
        return None

if __name__ == '__main__':
    toJSONFilter(separator)
```

```python
from panflute import *

def add_fig_label(elem, doc):
    if type(elem) == Image:
        elem.identifier = elem.title

def main():
    return run_filter(add_fig_label, doc=None)

if __name__ == "__main__":
    main()
```
# Conclusions

By now, you have seen most of the features of Markdown and Pandoc. As this is a beginner’s guide, I have not covered all features, but you should have a good idea of what you can do with these tools and be able to learn more from online manuals.

With Markdown you do not have quite as much control over typesetting and document structure as you would have in for example LaTeX, but the much simpler syntax for many markup instructions makes it much easier to work with. Especially for tables, lists, and figures, where LaTeX’s syntax can overshadow the actual content of your document.

**FIXME: more here**


[^1]:	Editing plain text files is WYGIWYG, What you get is what you get.

[^2]:	This is an example of where there is a difference between `--variable` and `--metadata`. If we had specified the title using `--variable` instead of using metadata in the header, Pandoc wouldn’t have created `pagetitle` for us, but the template would still see our `title` variable. Variables go directly to the template; metadata can be processed before Pandoc generates output.

[^3]:	Strictly speaking, it is the variables that are directly inserted, but since metadata is also considered variables, the distinction is academic.