---
sidebar_position: 20
title: Epinio push process diagram
---

This diagram is part of the description of the [Epinio push process](https://docs.epinio.io/explanations/detailed-push-process).

<figure>

![Epinio detailed push diagram](/img/epinio-push-detailed.svg)

<figcaption>Epinio push diagram</figcaption>
</figure>

## Epinio with Excalidraw

Nice enough graphical editor to use.
Certainly, it felt easier to get going with than Inkscape.
A much simpler interface.
It won't have the graphical power and features of Inkscape, but that's not necessary for the architectural diagrams use case we're considering.

Excalidraw saves files in its own format, which is JSON based, so amenable to version control management.

It was easy to re-create the Epinio diagram in Excalidraw, it took a couple of hours with no prior experience of the tool.
The exported result in SVG and PNG and displayed below.
The PNG looks more like the editor version than the SVG.
Notice the use of icons imported from Kubernetes and other libraries.
There is also a variant in Excalidraw's handwritten/drawn style.
Which I sort of like, but am not sure about its use in technical documentation.

<figure>

![Excalidraw SVG](/img/epinio-excalidraw.svg)

<figcaption>The Excalidraw SVG</figcaption>
</figure>

<figure>

![Excalidraw PNG](/img/epinio-excalidraw.png)

<figcaption>The Excalidraw PNG</figcaption>
</figure>

<figure>

![Excalidraw hand PNG](/img/epinio-excalidraw-hand.png)

<figcaption>The Excalidraw hand drawn PNG</figcaption>
</figure>

<figure>

```mermaid
graph LR
    app_user((App user))
    subgraph epu[" "]
        epinio_user((Epinio user))
        epinio_push[Epinio push]
    end
    subgraph epinio_system[Epinio System]
        epinio_api_server[api/v1]
        subgraph epinio_api[Epinio API]
            direction LR
            upload
            stage
            deploy
        end
        subgraph app_runtime_resources[App runtime resources]
            direction LR
            k8s_dep[K8s Deployment]
            k8s_service[K8s Service]
            k8s_ingress[K8s Ingress]
            stage
            deploy
        end
        subgraph staging_job[Staging Job]
            direction LR
            download
            unpack
            build
        end
        subgraph reg[Registry]
            direction LR
            app1_r1[App 1]
            app2_r2[App 2]
            appn_rn[App n]
        end
        subgraph s3_minio["S3 (Minio)"]
            direction LR
            app1_s3m[App 1]
            app2_s3m[App 2]
            appn_s3m[App n]
        end
    end
    epu -->|1a| epinio_api_server
    epu -->|3a| epinio_api_server
    epu -->|8a| epinio_api_server
    epinio_api_server -->|1b| upload
    epinio_api_server -->|3b| stage
    epinio_api_server -->|8b| deploy
    upload -->|2| s3_minio
    stage -->|4| unpack
    deploy -->|8| app_runtime_resources
    s3_minio -->|5| download
    build -->|7| reg
    k8s_dep -->|9| reg
    k8s_service --> app_user
    k8s_ingress --> app_user
```

<figcaption>The Epinio push process - Mermaid C4 - `dagre` layout</figcaption>
</figure>

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
graph LR
    app_user((App user))
    subgraph epu[" "]
        epinio_user((Epinio user))
        epinio_push[Epinio push]
    end
    subgraph epinio_system[Epinio System]
        epinio_api_server[api/v1]
        subgraph epinio_api[Epinio API]
            direction LR
            upload
            stage
            deploy
        end
        subgraph app_runtime_resources[App runtime resources]
            direction LR
            k8s_dep[K8s Deployment]
            k8s_service[K8s Service]
            k8s_ingress[K8s Ingress]
            stage
            deploy
        end
        subgraph staging_job[Staging Job]
            direction LR
            download
            unpack
            build
        end
        subgraph reg[Registry]
            direction LR
            app1_r1[App 1]
            app2_r2[App 2]
            appn_rn[App n]
        end
        subgraph s3_minio["S3 (Minio)"]
            direction LR
            app1_s3m[App 1]
            app2_s3m[App 2]
            appn_s3m[App n]
        end
    end
    epu -->|1a| epinio_api_server
    epu -->|3a| epinio_api_server
    epu -->|8a| epinio_api_server
    epinio_api_server -->|1b| upload
    epinio_api_server -->|3b| stage
    epinio_api_server -->|8b| deploy
    upload -->|2| s3_minio
    stage -->|4| unpack
    deploy -->|8| app_runtime_resources
    s3_minio -->|5| download
    build -->|7| reg
    k8s_dep -->|9| reg
    k8s_service --> app_user
    k8s_ingress --> app_user
```

<figcaption>The Epinio push process - Mermaid C4 - `elk` layout</figcaption>
</figure>

## Lucid Chart

<figure>

![](/img/Epinio-Lucid-Test.svg)

<figcaption>Epinio push process in Lucid exported as SVG</figcaption>
</figure>