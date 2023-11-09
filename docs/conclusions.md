---
sidebar_label: Conclusions
sidebar_position: 400
title: Conclusions
---

## Markup tools

### Mermaid

Great for less complicated layouts, but can be used with patience for more complex stuff.
Not necessarily a downside, doing complex stuff in an interactive editor is also complicated, perhaps a bit differently.
Simon's use case for example, is a simple application for which Mermaid does a perfect job.
You can do more complex layouts as in the Kubewarden diagrams,
but small changes in markup can result in big changes in output appearance as the
automated layout algorithm reworks paths from scratch again.
Mermaid's big advantage is that it's well integrated with Docusaurus.
Also, easy to use with VScode extensions.
Mermaid has an active community.
GitHub renders Mermaid diagrams in Markdown, which is very convenient.

## Interactive tools

### Excalidraw

Seemed to be very intuitive and easy to use.
Less features than Inkscape but more than enough for doing architecture diagrams.
Easy grouping, ungrouping and object moving.
Saves in Excalidraw/Json format, but can export SVG.
Also, exports PNG for display.
The SVG is rendered by browsers but doesn't look as good as exporting PNG, for display, from Excalidraw.
If being used for production I'd recommend saving in Excalidraw/JSON and exporting PNG for display.

### Inkscape

Obviously, a comprehensive tool for graphic designers.
There is plenty to learn before becoming proficient.
For graphics from the ground up.

## Generally, ...

Tools like Excalidraw are simpler and better orientated towards a particular domain, Mermaid even more so, and classes of diagramming encapsulated within Mermaid, more so again.
So, Mermaid is good for generally drawing objects and connections, the C4 language within is much more domain restricted.
Less flexibility, but more suited for architecture diagramming use cases.

## Other, unrelated.

I found (using the InterWEbs) a way of having figure captions included, more or less, automatically.
Figures are numbered sequentially in a page.
Unfortunately, there is no mechanism within Docusaurus to use cross-references and anchors for these.
So, if you reference them within the page. i.e. See Figure 2., you still need to manually check the cross-references are still valid when creating or editing a document.

There is this CSS added to `src/css/custom.css`:

```css
body {counter-reset: figures;}
figure {
  border: 1px solid darkgreen;
  padding: 2px;
}

figcaption {
  counter-increment: figures;
  font-style: italic;
}

figcaption::before {
  content:'Figure ' counter(figures) ': ';
}
```

So, now you can use `<figure>` and `<figcaption>` in your markdown file as normal:

```html
<figure id="fig-capt">

![](/img/favicon.ico)

<figcaption>A figure caption</figcaption>
</figure>
```

And it renders like other images seen in this document.

<figure id="fig-capt">

![](/img/favicon.ico)

<figcaption>A figure caption</figcaption>
</figure>

You can link to the image like the next inline link anchor, if using `id` in the `<figure>` tag.
A [figure](#fig-capt) to demo.
It's pretty good but needs some more effort on the CSS styling.