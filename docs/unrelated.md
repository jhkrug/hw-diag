---
sidebar_label: Unrelated
sidebar_position: 500
title: Unlrelated discovery
---

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

![](/img/suse.png)

<figcaption>A figure caption</figcaption>
</figure>

You can link to the image like the next inline link anchor, if using `id` in the `<figure>` tag.
A [figure](#fig-capt) to demo.
It's pretty good but needs some more effort on the CSS styling.