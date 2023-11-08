---
sidebar_position: 30
title: Kubewarden architecture diagram
---

This diagram is part of the [Kubewarden architecture](https://docs.kubewarden.io/architecture) description.

This is the original diagram from that documentation.

<figure>

![Kubewarden architecture diagram](/img/kw-architecture.png)

<figcaption>Original Kubewarden architecture diagram</figcaption>
</figure>

## Inkscape

This is the result of my first hour with Inkscape.
It appears Inkscape is a comprehensive graphical drawing tool.
So, you need to be familiar with the concepts of layers and transparency and all the other concepts related to this type of tool.
I dived in and tried to do an architecture block diagram.
It was difficult going.
I did start making progress, managing to get text and rectangles on the screen and group them together into objects.
I had particular difficulties in having text appear on the screen.
There is a long, comprehensive list of fonts but only those installed on your system are displayable.
Which was disconcerting, 'why is the text I typed in invisible?'.
Why not display only those that are going to be useable.

<figure>

![Kubewarden architecture diagram](/img/inkscape-kw-diag.svg)

<figcaption>Kubewarden architecture</figcaption>
</figure>

To continue there needs to be a period of time spent learning Inkscape and its working methodology.

## With Mermaid, `dagre` layout

<figure>

```mermaid
%%{init: {"flowchart": {"htmlLabels": false}} }%%
graph TB
    kubewarden_controller[Kubewarden Controller]
    subgraph k8s[Kubernetes]
      subgraph kubernetes_api_server[Kubernetes API Server]
          policy_server_in[PolicyServer]
          cluster_admission_policy_in[ClusterAdmissionPolicy]
          webhook_configuration[webhook Configuration]
      end
      subgraph planes[K8S Planes]
      k8s_control_plane[Control]
      k8s_data_plane[Data]
      end
    end
    policy_server_out[PolicyServer]
    cluster_admission_policy_out["`**ClusterAdmissionPolicy**<br/>(1....n)`"]
    cluster_admission_policy_in[ClusterAdmissionPolicy]
    kubewarden_policy_server_1[Kubewarden Policy Server]
    kubewarden_policy_server_2[Kubewarden Policy Server]
    oci_registry[(OCI Registry)]
    policy_server_out --> policy_server_in
    cluster_admission_policy_out --> cluster_admission_policy_in
    policy_server_in --> kubewarden_controller
    cluster_admission_policy_in --> kubewarden_controller
    kubewarden_controller --> webhook_configuration
    kubewarden_controller --> kubewarden_policy_server_1
    kubewarden_controller --> kubewarden_policy_server_2
    subgraph kwps [Kubewarden Policy Servers]
      subgraph kubewarden_policy_server_1[Kubewarden Policy Server]
          direction LR
          policy_1[Policy]
          policy_2[Policy]
      end
      subgraph kubewarden_policy_server_2[Kubewarden Policy Server]
          direction LR
          policy_3[Policy]
          policy_4[Policy]
          policy_5[Policy]
          policy_6[Policy]
      end
    end
    policy_1 --- oci_registry
    policy_2 --- oci_registry
    policy_3 --- oci_registry
    policy_4 --- oci_registry
    policy_5 --- oci_registry
    policy_6 --- oci_registry
    kubewarden_policy_server_1 --> kubernetes_api_server
    kubewarden_policy_server_2 --> kubernetes_api_server
```

<figcaption>Mermaid, `dagre` layout</figcaption>
</figure>

## With Mermaid, `elk` layout

<figure>

```mermaid
%%{
  init: {
    "flowchart": {
      "htmlLabels": false,
      "defaultRenderer": "elk"
    }
  }
}%%
graph TB
    kubewarden_controller[Kubewarden Controller]
    subgraph k8s[Kubernetes]
      subgraph kubernetes_api_server[Kubernetes API Server]
          policy_server_in[PolicyServer]
          cluster_admission_policy_in[ClusterAdmissionPolicy]
          webhook_configuration[webhook Configuration]
      end
      subgraph planes[K8S Planes]
      k8s_control_plane[Control]
      k8s_data_plane[Data]
      end
    end
    policy_server_out["`**PolicyServer** (1...n)`"]
    policy_server_in["`**PolicyServer** (1...n)`"]
    cluster_admission_policy_out["`**ClusterAdmissionPolicy** (1...n)`"]
    cluster_admission_policy_in["`**ClusterAdmissionPolicy** (1...n)`"]
    kubewarden_policy_server_1[Kubewarden Policy Server]
    kubewarden_policy_server_2[Kubewarden Policy Server]
    oci_registry[(OCI Registry)]
    policy_server_out --> policy_server_in
    cluster_admission_policy_out --> cluster_admission_policy_in
    policy_server_in --> kubewarden_controller
    cluster_admission_policy_in --> kubewarden_controller
    kubewarden_controller --> webhook_configuration
    kubewarden_controller --> kubewarden_policy_server_1
    kubewarden_controller --> kubewarden_policy_server_2
    subgraph kwps [Kubewarden Policy Servers]
      subgraph kubewarden_policy_server_1[Kubewarden Policy Server]
          direction LR
          policy_1[Policy]
          policy_2[Policy]
          policy_3[Policy]
      end
      subgraph kubewarden_policy_server_2[Kubewarden Policy Server]
          direction LR
          policy_4[Policy]
          policy_5[Policy]
          policy_6[Policy]
          policy_7[Policy]
      end
    end
    policy_1 --- oci_registry
    policy_2 --- oci_registry
    policy_3 --- oci_registry
    policy_4 --- oci_registry
    policy_5 --- oci_registry
    policy_6 ---|some text| oci_registry
    kubewarden_policy_server_1 --> kubernetes_api_server
    kubewarden_policy_server_2 --> kubernetes_api_server
```

<figcaption>Mermaid, `elk` layout</figcaption>
</figure>

## Excalidraw import of Mermaid markup

You can import Mermaid markup into Excalidraw.
But, impossible to export from Excalidraw to Mermaid markup.
Which is understandable but means the facility has limited use.
You would want to change permanently from a Mermaid markup diagram to Excalidraw.

Saved from Excalidraw in exported SVG and PNG.

<figure>

![](/img/excalidraw-import-of-kw-mermaid.svg)

<figcaption>Excalidraw rendering of an imported Mermaid KW diagram</figcaption>
</figure>

The same but exported as a PNG.
It's a better preservation of Excalidraw's default hand drawn and written style.

<figure>

![](/img/excalidraw-import-of-kw-mermaid.png)

<figcaption>Excalidraw rendering of an imported Mermaid KW diagram, but exported as a PNG</figcaption>
</figure>

## Excalidraw drawings

I replicated the Kubewarden architecture diagram in Excalidraw, saved in Excalidraw/JSON format.
There are two versions, one appearing somewhat hand drawn the other more traditional.
They are versioned in git. [This](kubewarden-arch-hand.excalidraw.json) is the hand drawn version Excalidraw/JSON format file with a file extension of json, it should be viewable in your browser.

The next two figures are the exported PNG versions.

<figure>

![](/img/kubewarden-arch-hand.png)

<figcaption>Excalidraw hand drawn PNG of Kubewarden architecture</figcaption>
</figure>

<figure>

![](/img/kubewarden-arch.png)

<figcaption>Excalidraw traditional PNG of Kubewarden architecture</figcaption>
</figure>