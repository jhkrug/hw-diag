---
slug: /
sidebar_label: Introduction
sidebar_position: 1
title: SUSE HackWeek Nov 2023 - Diagramming for Docs
---

## Introduction

My (John Krug, john.krug@suse.com) proposal for hack week is to dive into
diagramming for the doc(s) team(s).
I've struggled to give it the decent block of time it needs.
There are two docs teams, that which came from SUSE and that which originated within Rancher.

This hack week project is driven by the need to update the architecture and process diagrams that exist for my current projects [Epinio](https://epinio.io) and [Kubewarden](https://kubewarden.io).

It's worth noting that I'll not just be trying to reproduce them, I'd like to understand better whether there are better ways of diagrammatically conveying their meaning.

I'm approaching this without the benefit of much background in the area and no experience in any of these particular tools.
I have almost certainly missed some tools that would be useful. Point them out to me. Thanks!
My experience is as a system administrator and developer and my leaning is going to be towards formats that integrate well with a docs-as-code approach.

Thoughts, pointers, links and contributions welcome.

There are a few iterative parts:

- Refine and expand the requirements
- Select a few tools, one or two diagrams-as-code tools, one or two more interactive tools
- Do work with (some of) them, produce the two current requirement diagrams, consider the trials and tribulations.
- Make the recommendations for moving forwards, a report, as a small [Docusaurus](https://main--chipper-kheer-a572a0.netlify.app/) site.

The requirements:

- Text based format for diagram files.
At a minimum SVG or XML.
This requirement enables source code management and versioning.
- Usable on Linux, Mac, Windows, or via the web
- Open Source project compatible.
- Standards, not much out there, maybe C4 architecture diagramming, or UML
- Simplicity is best, we don't have many diagrams. But extensibility is a consideration.
A short learning curve as opposed to features
- Consider merits of Diagram-as-Code vs Interactive editors (for current, and perhaps future use cases)
- The Rancher docs team use [Docusaurus](https://docusaurus.io)
and [VSCode](https://code.visualstudio.com) for editing.
So, tools that play well with both of those have advantages.
