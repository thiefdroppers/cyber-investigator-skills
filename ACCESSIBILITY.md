# Accessibility

## Commitment

This project is written content first: curriculum pages, worksheets, and
skill files, published as Markdown and as a static site. We try to keep
that content readable by anyone, including people using a screen reader
or other assistive technology, and we'll fix a reported barrier rather
than argue about it.

## Supported environments

- **GitHub's own rendering** of every Markdown file, which inherits
  GitHub's accessibility work. This is the one guaranteed-accessible way
  to read the content, since it doesn't depend on our theme or build.
- **The MkDocs Material site**, once published, which uses Material for
  MkDocs' built-in accessibility features (keyboard navigation, semantic
  headings, skip links). We haven't run a dedicated audit against this
  theme ourselves; its own accessibility posture is documented upstream.

## Known limitations

- **Mermaid diagrams.** Most days include a Mermaid flowchart or sequence
  diagram alongside the written explanation. The diagram is a visual aid,
  not the only copy of that information, but the diagrams themselves
  don't currently carry text alternatives a screen reader can describe in
  detail. The surrounding prose is written to stand on its own without
  the diagram, but we know the diagram's content isn't equally available.
- **Code blocks and terminal output.** Long command examples and
  illustrative output are presented as code blocks, which read fine
  linearly but don't have a shorter summary for anyone who wants one.
- **Images.** The README's logo and hero image carry descriptive alt
  text. Screenshots are avoided in the curriculum itself for other
  reasons (see `CONTRIBUTING.md`), which also means there's little
  image content to need alt text in the first place.

## Reporting a barrier

Open an issue using the "Content correction" template, or a blank issue
if that doesn't fit, and describe what didn't work and what you were
using to read it (screen reader, browser, zoom level, and so on). Treat
it the same as any other content bug: see [CONTRIBUTING.md](CONTRIBUTING.md).
