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
  <TabItem value="Horizontal" label="Horizontal" default>

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
  <TabItem value="Vertical" label="Vertical">

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

## Observation

A perfect use of Mermaid in our documentation.