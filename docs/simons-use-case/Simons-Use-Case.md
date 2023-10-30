---
title: Simon's use case
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Simon Flood at Secure Linux suggested a use case as follows;
A visual representation of the valid upgrade paths available
for [Harvester](https://docs.harvesterhci.io/v1.2/upgrade/index).

```console
graph LR/TB;
    1.0.0-->1.0.1;
    1.0.1-->1.0.2;
    1.0.2-->1.0.3;
    1.0.3-->1.1.0;
    1.0.3-->1.1.1;
    1.1.0-->1.1.1;
    1.1.0-->1.1.2;
    1.1.1-->1.1.2;
    1.1.2-->1.2.0;
    1.1.2-->1.2.1;
    1.2.0-->1.2.1;
```


## LR orientation.

```mermaid
graph LR;
    1.0.0-->1.0.1;
    1.0.1-->1.0.2;
    1.0.2-->1.0.3;
    1.0.3-->1.1.0;
    1.0.3-->1.1.1;
    1.1.0-->1.1.1;
    1.1.0-->1.1.2;
    1.1.1-->1.1.2;
    1.1.2-->1.2.0;
    1.1.2-->1.2.1;
    1.2.0-->1.2.1;
```

Swapping the `1.1.0` lines to avoid path overlapping.

```mermaid
graph LR;
    1.0.0-->1.0.1;
    1.0.1-->1.0.2;
    1.0.2-->1.0.3;
    1.0.3-->1.1.0;
    1.0.3-->1.1.1;
    1.1.0-->1.1.2;
    1.1.0-->1.1.1;
    1.1.1-->1.1.2;
    1.1.2-->1.2.0;
    1.1.2-->1.2.1;
    1.2.0-->1.2.1;
```

## TB orientation.

It would be nice to swap to this if on a phone screen. Option
via tabs perhaps. But only for the diagram switch. I'm not a fan of tabs if
they hide searchable content.

<Tabs>
  <TabItem value="Horizontal LR" label="Horizontal LR" default>

```mermaid
graph LR;
    1.0.0-->1.0.1;
    1.0.1-->1.0.2;
    1.0.2-->1.0.3;
    1.0.3-->1.1.0;
    1.0.3-->1.1.1;
    1.1.0-->1.1.2;
    1.1.0-->1.1.1;
    1.1.1-->1.1.2;
    1.1.2-->1.2.0;
    1.1.2-->1.2.1;
    1.2.0-->1.2.1;
```

  </TabItem>
  <TabItem value="Vertical TB" label="Vertical TB">

```mermaid
graph TB;
1.0.0-->1.0.1;
1.0.1-->1.0.2;
1.0.2-->1.0.3;
1.0.3-->1.1.0;
1.0.3-->1.1.1;
1.1.0-->1.1.2;
1.1.0-->1.1.1;
1.1.1-->1.1.2;
1.1.2-->1.2.0;
1.1.2-->1.2.1;
1.2.0-->1.2.1;
```

  </TabItem>
</Tabs>

## Some twiddling of options

Playing with shapes, etc. Seems to need the neutral theme to avoid the link text line running through the link text.

<Tabs>
  <TabItem value="Horizontal RL" label="Horizontal RL" default>

```mermaid
%%{init: "theme": "neutral"}%%
flowchart RL;
1.0.0(1.0.0)-->1.0.1((1.0.1));
1.0.1-->1.0.2[/1.0.2/];
1.0.2-->1.0.3;
1.0.3-->1.1.0;
1.0.3-->1.1.1;
1.1.0-->|Breaking changes|1.1.2;
1.1.0-->1.1.1;
1.1.1-->1.1.2;
style 1.2.0 fill:#b96
1.1.2-->1.2.0;
1.1.2-->1.2.1;
1.2.0-->1.2.1;
```

  </TabItem>
  <TabItem value="Vertical BT" label="Vertical BT">

```mermaid
%%{init: "theme": "neutral"}%%
flowchart BT;
1.0.0(1.0.0)-->1.0.1((1.0.1));
1.0.1-->1.0.2[/1.0.2/];
1.0.2-->1.0.3;
1.0.3-->1.1.0;
1.0.3-->1.1.1;
1.1.0-->|Breaking changes|1.1.2;
1.1.0-->1.1.1;
1.1.1-->1.1.2;
style 1.2.0 fill:#b96
1.1.2-->1.2.0;
1.1.2-->1.2.1;
1.2.0-->1.2.1;
```

  </TabItem>
</Tabs>

## Observation

A good use of Mermaid in our documentation.
