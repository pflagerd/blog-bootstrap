# blog-bootstrap

This contains a simple blog with collapsible blog entries.

It is meant to be either `.fork`ed  (read dot-forked) or branched.



### `fork`ing blog-bootstrap

If it is `.fork`ed, its contents are copied to another repository, along with a `.fork` file containing the version of both repositories at the time of the dot-fork.  You also add an entry in `blog-bootstrap/.forks` with the same information in a slightly different format.

You may consult this [gist](https://gist.github.com/pflagerd/22bb3e89b56e158b303d7101009112e2) for guidance on how to a) create a `.fork file, and b) how to update `blog-bootstrap/.forks`.  There are prototype `.fork` and `.forks` files described there.  Those prototypes contain instructions on how to put entries into them.



### branching blog-bootstrap

If it is branched, `blog-bootstrap` may be renamed because it will become a subdirectory of the containing project.  The `blog-bootstrap` repository should be branched with the name of the containing project.  If, for example, the containing project is called `investing`, the branch should be called `investing` also. The blog might be cloned at `investing/blog`.  Since it is a nested repository, `blog` (in this case) should be added to `investing/.gitignore`.



### inline-index-html.mjs

This program can be used to generate a standalone version of `index.html` or `mega-blog.html`.  It is run thus:

```bash
node inline-index-html.mjs input.html output.html
```

Where `input.html` is either `index.html` or `meta-blog.html`, and `output.html` is the name of the new standalone version.

Standalone versions are typically copied into another repository directly and are not dot-forked.

The names `inline-index.html` and `inline-meta-blog.html` are commonly substituted for `output.html`, so they are in `blog-bootstrap/.gitignore`.



Some branches have interesting things in them:

blog-bootstrap@cracking-the-coding-interview 
	has a script to load a file into the page. This could probably be moved to blog.js.
	has a stand-alone version valled file-viewer-hardcoded.html
	
blog-bootstrap@improve-expand-collapse
	contains some code in blog.js that might be worth understanding.

blog-bootstrap@bok-blog
	has a RUNME
	has a SETMEUP
	has a watcher in index.js
	index.js also remembers the last browser size
	
blog-bootstrap@playback
	has a RUNME
	has a SETMEUP
	
blog-bootstrap@the-intelligent-investor
	has a RUNME
	has a SETMEUP
	
