# API-driven Cloud Native Solutions · Session 03 · Cloud Native Application

*Learned 1 Aug 2026*

## Why this matters

Cloud-native work is mostly ecosystem work: choosing the right layer and knowing which tool category solves which operational problem. This session gives the map: CNCF, microservices, service mesh, serverless, DevOps, GitOps, containers, Kubernetes, and architecture case studies. By the end, you should be able to explain whether a problem is mainly about packaging, orchestration, service-to-service traffic, release automation, or runtime scaling.

## Part 1 · Ecosystem map

*The CNCF landscape is easiest to understand as a layered toolbox rather than a page of logos.*

### 1. CNCF landscape and cloud-native ecosystem

**Intuition** — The Cloud Native Computing Foundation is a vendor-neutral home for many open-source cloud-native projects, hosted under the Linux Foundation. For study, do not memorize every logo; learn the job each layer performs.

CNCF sorts its projects by maturity stage, which is the useful signal, not the exact count (it moves over time): **graduated** projects (currently 24) are considered stable enough to bet production on — Kubernetes, Helm, Envoy, and ArgoCD are graduated. **Incubating** projects (currently 37) are still maturing — gRPC, Thanos, and OpenTelemetry are examples. Graduated vs incubating is a quick way to judge how much risk a tool choice carries.

![CNCF ecosystem map](assets/S03-cncf-ecosystem-map.svg)

**Mechanism** — The ecosystem groups around recurring operational jobs:

Read the table as "which kind of problem am I trying to solve?" rather than "which tool name should I memorize?" Each row is one job a production platform must do.

| Layer | Problem it solves | Typical tools or concepts |
|---|---|---|
| Runtime | package and run application processes consistently | containers, images, registries |
| Orchestration | place containers, restart failures, scale replicas | Kubernetes |
| Service connectivity | route requests between services safely | ingress, proxies, service mesh |
| Observability | understand health and diagnose failures | Prometheus, OpenTelemetry-style metrics/traces |
| Delivery | release changes safely and repeatedly | CI/CD, GitOps |
| Operations | manage config, policy, secrets, and governance | Helm-like packaging, policy tools |

Two quick translations:

- **Orchestration** means deciding where containers run, restarting them when they fail, and scaling them up or down.
- **GitOps** means storing deployment state in Git and using automated tools to make the live system match what the repository says.

**Worked example** — A chatbot backend deployed as a cloud-native service needs a runtime image, an orchestrator to run replicas, an ingress path for user requests, monitoring for latency and errors, a delivery pipeline for new versions, and configuration management for environment-specific settings.

**Tradeoff / when NOT to use** — Do not start tool selection from the CNCF landscape poster. Start from the failure or workflow you need to improve. If the problem is slow releases, a service mesh is not the first fix; CI/CD and tests are.

---

## Part 2 · Application structure

*Microservices split systems by capability; service mesh manages the traffic between those services when the network becomes a product concern.*

### 2. Microservices vs monolith

**Intuition** — A monolith packages many capabilities into one deployable unit. Microservices split capabilities into autonomous, loosely coupled, independently deployable services around business domains.

An everyday analogy: a monolith is one large department where every approval goes through the same desk. Microservices are specialized counters: payment, delivery, menu, support. Each counter can improve its own process, but customers still need the counters to coordinate.

![Monolith versus microservices](assets/S03-monolith-microservices.svg)

**Mechanism** —

| Aspect | Monolith | Microservices |
|---|---|---|
| Deployment | whole application deploys together | each service can deploy independently |
| Scaling | scale the entire application | scale hot services only |
| Technology choice | one dominant stack | service teams may choose fit-for-purpose stacks |
| Failure boundary | one bug can affect the whole app | failures can be isolated if contracts and timeouts are designed well |
| Operational cost | simpler to run at small scale | more networking, monitoring, CI/CD, and ownership discipline |

Microservices work best when service boundaries follow business capabilities — grouped by *why* each part changes, not just what it does. If payment rules change for different reasons than delivery assignment, those are candidates for different services.

**Monolithic limitations** — the slide sequence makes the pain concrete:

- **Technology barrier** — introducing a new stack usually means rewriting the application
- **Scalability** — the only easy scale unit is the whole app
- **Size** — as the application grows, the single codebase becomes harder to manage
- **Understandability** — new team members must learn the whole system, not just one module

**Why the deployment-frequency gap is the real evidence** — reported deploy rates make the microservices case concretely: Amazon ~23,000 deploys/day, Google ~5,500/day, Netflix ~500/day, Twitter ~3/week. A monolith can't approach numbers like that, because every team funnels changes through one shared repository and one deployment pipeline — the textbook "monolithic hell" case is three separate teams (order, restaurant, delivery) all committing to one repo, queued behind one Jenkins pipeline with manual testing, so any team's change waits on everyone else's. Splitting into **one pipeline per service** — each team owns its own repo and its own automated pipeline — removes that queue and is what makes the high deploy rates possible.

Two more pieces of the standard microservices picture: each service usually owns its own database (**database-per-service**), reached only by calling that service — not by another service reading its tables directly — which is what actually lets services deploy and scale independently. A shared database looks simpler at first — one schema, no network hop for a read — but it quietly re-couples services that are supposed to be independent: any team can change a column and break another team's queries with nothing to catch it at build time, schema migrations need cross-team coordination, and a slow query from one service can lock rows another service needs right now. Routing every cross-service read through an API instead of a shared table turns a schema change into a normal, versioned API change rather than a silent breakage.

*Everyday picture: a shared database is like several departments in an office sharing one filing cabinet with no rules about who can rearrange the folders — one department reorganizing "their" folder can leave another department unable to find what it needs, with no warning given. Database-per-service is each department keeping its own locked cabinet and only sharing information by handing over a filled-out request slip (the API) — nobody reaches into someone else's cabinet and moves things around directly.*

And this isn't a niche pattern: the cloud microservices market was estimated at $1.33B in 2023, projected to reach $3.72B by 2028 (~23% CAGR), which is a rough proxy for how fast companies are adopting it.

**Worked example** — In a food-delivery system, restaurant search, cart, order, payment, delivery assignment, notification, and support are different capabilities. During dinner peak, search and cart may need more replicas than support. Independent services let those parts scale and release separately.

**Tradeoff / when NOT to use** — A monolith is often better for a small team or early product because local function calls, one deployment, and one database are easier to reason about. Premature microservices create distributed-system failures before the product has enough scale to justify them.

This isn't only a small-team caution — it holds at large-company scale too. Amazon Prime Video's monitoring team moved a microservices/serverless pipeline back into a single monolithic process on EC2/ECS and cut that workload's operating cost by about 90%. The coordination and per-service infrastructure overhead of microservices can outweigh the benefit even for a big-name product, if the workload doesn't actually need independent scaling.

---

### 3. Service mesh

**Intuition** — A service mesh is infrastructure for service-to-service communication. It handles cross-cutting traffic concerns such as retries, timeouts, mutual TLS, routing policy, and telemetry without forcing every service team to write the same networking code.

![Service mesh sidecar pattern](assets/S03-service-mesh.svg)

**Mechanism** — A common service-mesh pattern puts a small proxy beside each service instance. The service talks through its local proxy; proxies talk to other proxies. A control plane distributes traffic policy.

| Concern | Without service mesh | With service mesh |
|---|---|---|
| Retry and timeout | each service implements its own logic | central policy applied consistently |
| mTLS | each service team manages certificates | mesh automates service identity and encryption |
| Traffic shifting | custom deployment or gateway logic | route 5%/50%/100% to a new version |
| Telemetry | each service emits different signals | uniform request metrics and traces |

**Worked example** — Suppose `order-service` calls `payment-service`. Without a mesh, the order code must implement timeout, retry, TLS, and metrics. With a mesh, the order code calls payment normally, while the sidecar proxy enforces retry policy, records latency, and encrypts traffic to the payment proxy.

**Tradeoff / when NOT to use** — Do not add service mesh when there are only a few services and the main problem is still unclear boundaries or missing tests. A mesh improves traffic control; it does not fix bad service design, bad data ownership, or missing observability discipline.

*Everyday picture: without a service mesh, every employee in a building has to personally check IDs at the door, keep their own phone log, and learn security procedures their own way — repeated, inconsistently, by everyone. A service mesh is like giving every employee a personal assistant stationed right beside them who checks IDs, logs calls, and applies security consistently for everyone in the building, so the employee just gets on with their actual job.*

---

## Part 3 · Compute and deployment models

*Serverless, containers, and Kubernetes are three different answers to "how does code run in production?"*

### 4. Serverless computing and serverless stack

**Intuition** — Serverless means developers deploy code or configuration without managing servers directly. The provider runs the infrastructure, scales on demand, and charges mainly when code executes.

![Serverless stack](assets/S03-serverless-stack.svg)

**Mechanism** — A typical serverless application combines:

| Component | Job | AWS-style example |
|---|---|---|
| HTTP gateway | receive and route web/API requests | API Gateway |
| Function compute | execute application code on demand | Lambda |
| Database service | persist application state | DynamoDB or RDS |
| Event source | trigger work without a user request | S3 upload, stream, queue, scheduler |
| Monitoring | track executions, failures, and latency | logs and metrics |

Cold start is the key mechanism cost: if no warm function instance exists, the platform creates one before executing the request, adding latency.

Serverless is broader than just function compute — the same pay-per-use model covers data stores (Amazon Aurora Serverless, not just DynamoDB) and integration services (EventBridge, SQS, SNS, Step Functions) that connect functions together without you running any of the connecting infrastructure yourself.

**Worked example** — A document-upload API can use an HTTP gateway for `POST /documents`, a function to validate metadata, object storage for the file, a database row for status, and another event-triggered function for asynchronous processing.

**Tradeoff / when NOT to use** — Serverless is weak for long-running tasks, workloads needing deep environment control, and systems where vendor lock-in is unacceptable. Containers or VMs may be better when runtime control and predictable long execution matter more than pay-per-use scaling.

*Everyday picture: running your own servers is like buying and maintaining a home generator that sits idle most of the year just in case you need power. Serverless is like being connected to the electricity grid instead — you don't own or maintain any generating equipment, you draw exactly as much power as you need at that moment, the utility scales its output to match demand across every customer, and your bill reflects only what you actually used.*

---

### 5. Containers and Docker

**Intuition** — A container is a standardized package containing the application code, runtime, system tools, libraries, and settings needed to run consistently across environments.

The singer analogy is useful: a singer who can't rely on the venue's microphone or speakers just brings their own. A container carries its own runtime environment the same way, so the deployment venue matters less.

![Virtual machines versus containers](assets/S03-containers-vms.svg)

**Mechanism** — Docker popularized container packaging. A container image is built once and run many times. Unlike a virtual machine, a container does not include a full guest operating system per application; containers share the host OS through a container runtime.

| Packaging model | Includes | Strength | Cost |
|---|---|---|---|
| Virtual machine | app, libraries, guest OS | strong isolation, familiar server model | heavier image, slower start, more resource use |
| Container | app, libraries, runtime settings | lightweight, portable, fast start | weaker isolation than VM; needs image and runtime discipline |

**Worked example** — A FastAPI service can be packaged with Python, dependencies, model files, and startup command in one Docker image. The same image can run on a laptop, test server, or Kubernetes cluster, reducing "works on my machine" failures.

**Tradeoff / when NOT to use** — Containers do not remove the need for good configuration, secrets management, vulnerability scanning, or deployment strategy. For a one-off script run locally by one person, a virtual environment may be simpler than building and maintaining an image.

---

### 6. Kubernetes

**Intuition** — Kubernetes is a container orchestration system: it manages the deployment, scaling, and operation of containerized applications. Its core idea is desired state: declare what should be running, and Kubernetes keeps trying to make reality match. It was originally built inside Google, later donated to the CNCF, and is open source and written in Go — which is why it's the graduated CNCF project every other orchestration tool gets compared to.

![Kubernetes desired-state control loop](assets/S03-kubernetes-control-loop.svg)

**Mechanism** — Kubernetes has a control plane and worker nodes. The control plane accepts desired state through the API, schedules workloads, and runs controllers. Worker nodes run pods, which are the smallest deployable units Kubernetes manages.

Important ideas:

| Concept | Plain meaning |
|---|---|
| Pod | one or more containers deployed together |
| Deployment | desired replica count and rollout strategy for pods |
| Service | stable network identity for a set of pods |
| Control loop | compare desired state with actual state and correct drift |
| Scaling | change replica count based on demand or policy |

**Worked example** — If the desired state says "run three replicas of order-service" and one pod crashes, Kubernetes detects that actual state is two healthy replicas and starts another pod to return to three.

*Everyday picture: a home thermostat runs the same kind of control loop. You set a desired temperature, and the thermostat keeps checking the actual room temperature, switching the heater on or off to close any gap — nobody has to notice a chill and manually flip a switch. Kubernetes' control loop does this for containers: you declare "3 replicas," and it keeps checking the cluster and starting or stopping pods to correct any drift from that number, continuously and without a human watching a dashboard.*

**Use case — autoscaling under load.** A flash sale sends checkout traffic to 4x its normal level within minutes. A Horizontal Pod Autoscaler watches CPU or request-rate metrics and raises `checkout-service` from 3 replicas to 12 automatically; when the sale ends, it scales back down. Without this, someone has to manually add and remove pods around every predicted spike, or keep enough capacity running idle at all times to survive one.

**Tradeoff / when NOT to use** — Kubernetes has a steep operational cost. If one container on one VM is enough, Kubernetes may add more moving parts than value. It becomes worthwhile when you need repeated deployments, scaling, healing, and many services across environments.

---

## Part 4 · Delivery operating model

*DevOps and GitOps are not runtime technologies; they are ways of making change safer and faster.*

### 7. DevOps and CI/CD

**Intuition** — DevOps aligns development and operations so software can move from idea to production in small, safe, frequent changes. CI/CD is the automation spine of that movement.

**The organizational change behind it** — a traditional org splits Development, QA, and Operations into separate teams under one IT umbrella, so a change passes through three handoffs before it ships. DevOps replaces that with small, cross-functional teams that each own development, testing, and operations for their own service end to end. The automation (CI/CD) only works this well because the handoffs it's removing were mostly organizational, not technical.

**Why it's needed — the "wall of conflict"** — Development wants to ship change quickly (agility); Operations wants the running system to stay stable; each pulls in the opposite direction, and the friction between them is sometimes literally called the wall of conflict. Agile addresses the business-to-development side of that friction (faster requirements-to-build cycles); DevOps addresses the development-to-operations side (faster, safer build-to-release cycles).

**The DevOps loop** — People commonly draw DevOps as an infinity loop: **plan → code → build → test** (development side) feeding into **release → deploy → operate → monitor** (operations side), which feeds back into planning the next change. CI/CD (section above) is the automation that makes this loop fast; source control, infrastructure-as-code, and configuration management are what make each stage repeatable instead of manual.

![DevOps and CI/CD loop](assets/S03-devops-cicd.svg)

**Mechanism** —

| Practice | Meaning | Human gate |
|---|---|---|
| Continuous Integration | developers merge frequently; every change is built and tested | before merge through review/tests |
| Continuous Delivery | build artifact is always ready and may deploy after approval | manual production approval |
| Continuous Deployment | every passing change deploys automatically | no manual production approval |

The difference between delivery and deployment is the production gate. Delivery prepares the release automatically but waits for approval; deployment removes that gate.

**Worked example** — A microservice team pushes a change. The pipeline builds the container image, runs unit tests, runs integration tests, scans dependencies, deploys to staging, runs smoke tests, and either waits for approval or automatically deploys to production depending on the CD model.

**Tradeoff / when NOT to use** — Continuous deployment is risky when tests are weak, observability is poor, or rollback is slow. In regulated systems, continuous delivery with human approval may be the better tradeoff.

*Everyday picture: imagine a restaurant where the kitchen and the serving staff work in separate rooms, never talk directly, and every dish needs three separate manager sign-offs before it reaches a table — food arrives cold and orders get crossed. DevOps is like merging cooking and serving into one team that owns a dish from stove to table, with a conveyor belt of automatic quality checks (CI/CD) moving each plate through the required checks on its own, instead of waiting for a manager to walk over and approve it by hand.*

---

### 8. GitOps

**Intuition** — GitOps applies DevOps practices to infrastructure and operations. Git becomes the single source of truth for declarative desired state, and automation reconciles the running system to match it.

![GitOps reconciliation flow](assets/S03-gitops-flow.svg)

**Mechanism** — GitOps has four core moves:

| Step | What happens |
|---|---|
| Declare | desired application and infrastructure state is written as code/config |
| Review | changes go through Git review, history, and approval |
| Reconcile | an agent compares Git desired state with cluster actual state |
| Correct drift | if reality differs, automation applies or alerts |

GitOps is especially natural with Kubernetes because Kubernetes resources are already declarative.

**Why not just run `kubectl apply` by hand when something needs to change** — a manual deploy leaves no reliable record of who changed what, when, or why, so once the cluster drifts from what anyone intended, there is no trustworthy baseline to compare against — you end up debugging from memory instead of from history. Rollback becomes a manual, error-prone reconstruction instead of a single revert. GitOps fixes this by making Git the durable source of truth: every change is a reviewed, timestamped commit, and a reconciliation loop continuously checks the live cluster against that record instead of trusting that whoever ran the last command typed it correctly.

*Everyday picture: manual deployment is like several people editing a shared paper document by hand with no version history — if something looks wrong, nobody can say for sure who changed what or how to get back to the last good version. GitOps is like a document with full version history plus an assistant who automatically retypes the document to match whatever the latest saved version says — every change is recorded, reviewable, and easy to undo.*

A GitOps toolchain is usually assembled from one tool per category, not one product:

| Category | Example tools |
|---|---|
| Git hosting | GitHub, GitLab, Bitbucket |
| CI (build/test) | Jenkins, CircleCI, GitHub Actions |
| CD / reconciliation | ArgoCD, FluxCD, Spinnaker |
| Container registry | Docker Hub, AWS ECR, GHCR |
| Infrastructure-as-code | Terraform, AWS CloudFormation, Pulumi |
| Config management | Ansible, Chef, Helm charts |

**Worked example** — To change `order-service` from version `1.4` to `1.5`, a developer changes the image tag in Git. After review and merge, the GitOps controller detects the change and applies it to the cluster. If someone manually changes the cluster later, the controller notices drift and restores the Git-declared state or alerts.

**Tradeoff / when NOT to use** — GitOps is less useful when infrastructure is small, mostly manual, or not declarative. It also requires discipline: emergency manual fixes must be reconciled back to Git or they will be overwritten or become invisible.

---

## Part 5 · Case-study thinking

*A cloud-native case study is an architecture diagnosis exercise: what failed, why it spread, and which cloud-native capability would contain it.*

### 9. Analysis of a cloud-native application architecture

**Intuition** — A sale-day or streaming-scale case study is not mainly about the brand name. It is about diagnosing bottlenecks, coupling, state consistency, scaling boundaries, and observability.

Named examples from the lecture point in the same direction:

- **Flipkart Big Billion Day** (launched 6 Oct 2014, 70+ discounted categories) shows what happens when traffic spikes faster than the system can isolate failure — the sale drew roughly 3 lakh (300,000) orders in six hours, and the site crashed under the load.
- **Hotstar** shows the same scaling problem at much larger concurrency — its architects had to design for **25.3 million concurrent users** during peak live-sports traffic.
- **Monolith** is the counterexample: one big deployable unit makes the whole system move together.

![Cloud-native architecture case-study checklist](assets/S03-architecture-case-study.svg)

**Mechanism** — Use this checklist:

| Question | What to look for |
|---|---|
| Traffic pattern | sudden spike, steady growth, or regional concentration |
| Hot capability | login, search, cart, payment, video, recommendation |
| Coupling | whether one overloaded service blocks unrelated flows |
| State risk | cart loss, duplicate payment, inconsistent order status |
| Scaling boundary | whether the hot capability can scale independently |
| Resilience | queues, retries, timeouts, **circuit breakers** (stop calling a dependency that's already failing, instead of retrying into a failure and making it worse — the caller "trips the breaker" and fails fast until the dependency recovers), graceful degradation |
| Observability | metrics and traces that reveal where latency or errors begin |

*Everyday picture: this is the same idea as the circuit breaker in a home's electrical panel. When a circuit draws too much current, the breaker trips and cuts power immediately, instead of letting the wiring keep overheating toward a fire; someone resets it only once the fault is cleared. A software circuit breaker does the same job for a failing dependency — it stops sending requests the moment failures cross a threshold, waits, then cautiously tests whether the dependency has recovered before letting traffic flow again.*

**Worked example** — On a sale day, users report that selected products vanish from carts and money is deducted without orders. That points to state inconsistency between cart/order/payment, missing idempotency, overloaded synchronous calls, and no compensating step for partial failures. A cloud-native redesign would isolate cart, order, inventory, and payment; add idempotency keys; queue bursty order creation; and monitor each step.

**Tradeoff / when NOT to use** — Do not answer every case study with "use microservices." Sometimes the best fix is caching, database indexing, queueing, rate limiting, or a rollback strategy. Microservices help only when the failure follows service boundaries that can be separated and operated independently.

---

## Self-study / Lab / build

Draw a one-page architecture diagnosis for an ecommerce flash sale:

1. Mark the hot path: browse -> cart -> order -> payment -> confirmation.
2. Circle the two places where data consistency matters most.
3. Decide which part should be synchronous and which part can be queued.
4. Add one monitoring metric for each service.
5. Name the simplest non-cloud-native solution that might still work for a small sale.

The goal is not a perfect architecture diagram. The goal is to explain why each cloud-native tool belongs to a specific operational problem.

---

*Exam: this session is in scope for the **closed-book mid-sem** (S1-S8). Full evaluation, weights, dates and course logistics live once in [`549-master.md`](../549-master.md) — not repeated per session.*
