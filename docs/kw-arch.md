---
sidebar_position: 30
title: Kubewarden architecture diagram
---

This diagram is part of the [Kubewarden architecture](https://docs.kubewarden.io/architecture) description.

![Kubewarden architecture diagram](/img/kw-architecture.png)

## With Mermaid

```mermaid
graph TB
    kubewarden_controller[Kubewarden Controller]
    subgraph k8s[Kubernetes]
        k8s_control_plane[Control Plane]
        k8s_data_plane[Data Plane]
    end
    policy_server_out[PolicyServer]
    cluster_admission_policy_out[ClusterAdmissionPolicy]
    cluster_admission_policy_in[ClusterAdmissionPolicy]
    subgraph kubernetes_api_server[Kubernetes API Server]
        policy_server_in[PolicyServer]
        cluster_admission_policy_in[ClusterAdmissionPolicy]
        webhook_configuration[webhook Configuration]
    end
    kubewarden_policy_server_1[Kubewarden Policy Server]
    kubewarden_policy_server_2[Kubewarden Policy Server]
    oci_registry[OCI Registry]
    policy_server_out --> policy_server_in
    cluster_admission_policy_out --> cluster_admission_policy_in
    policy_server_in --> kubewarden_controller
    cluster_admission_policy_in --> kubewarden_controller
    kubewarden_controller --> webhook_configuration
    kubewarden_controller --> kubewarden_policy_server_1
    kubewarden_controller --> kubewarden_policy_server_2
    subgraph kubewarden_policy_server_1["&nbspKubewarden Policy Server&nbsp;"]
        direction LR
        policy_1[Policy]
        policy_2[Policy]
    end
    subgraph kubewarden_policy_server_2["&nbspKubewarden Policy Server&nbsp;"]
        direction LR
        policy_3[Policy]
        policy_4[Policy]
    end
    kubewarden_policy_server_1 --> oci_registry
    kubewarden_policy_server_2 --> oci_registry
```