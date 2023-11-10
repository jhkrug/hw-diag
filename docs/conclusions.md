---
sidebar_label: Conclusions
sidebar_position: 400
title: Conclusions
---

## Markup tools

### Mermaid

Great for less complicated layouts, but can be used with patience for more complex stuff.
Not necessarily a downside, doing complex stuff in an interactive editor is also complicated, but perhaps differently.
Simon's use case, for example, is a simple application for which Mermaid does a perfect job.
You can do more complex layouts as in the Kubewarden and Epinio diagrams,
but small changes in markup can result in big changes in output appearance as the
automated layout algorithm reworks paths from scratch again.
Lots of grouping using `subgraph` is useful here.
Mermaid's big advantage is that it's well integrated with Docusaurus.
Also, easy to use with VScode extensions.
Mermaid has an active community.
GitHub renders Mermaid diagrams in Markdown, which is convenient.

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
For graphics from the ground up with full control over many features.

## Generally, ...

Tools like Excalidraw are simpler and better orientated towards a particular domain, Mermaid even more so, and classes of diagramming encapsulated within Mermaid, more so again.
So, Mermaid is good for generally drawing objects and connections, the C4 language within is much more domain restricted.
Less flexibility, but more suited for a particular style of architecture diagramming use cases. Whether that style is suitable for either of Epinio or Kubewarden needs further consideration

## TL;DR

- Use Mermaid as a first choice.
- If interactivity is wanted or needed:
  - Use Excalidraw for simplicity
  - Use draw.io, Inkscape, or Lucid for features and power.
