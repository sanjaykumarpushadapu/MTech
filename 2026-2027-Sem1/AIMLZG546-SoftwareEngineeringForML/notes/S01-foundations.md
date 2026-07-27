# Software Engineering for Machine Learning · Session 01 · Foundations of ML Systems Engineering

*Learned ____*

## Why this matters

This is the session that separates people who can *train* a model from people who can *ship* one — the difference that defines an ML **engineer**. Its central claim, which you'll spend a career proving true: **the model is rarely the problem; everything around it is.** Data quality, latency, cost, monitoring, fairness, the handoff between data scientists and engineers — that's where ML products actually live or die. This note gives you the vocabulary (algorithm vs model, parameters vs hyperparameters), the process (SDLC, ML pipeline, MLOps), and the judgment (the risk spectrum, when the general answer is the wrong one) to reason about real systems.

Three sources, one argument: the slides give the process history, Kästner (T1) gives the failure evidence (**87% of ML projects fail**), the Tech Mahindra paper gives the local-optimisation trap. Read them as one.

**Running example throughout:** **fraud detection**, used in every section — and it's Kästner's own ch3 example too, so book and note align from page one.

## Topics

**Part 1 — The argument** *(read these two first)*
1. **Why this course exists** — Sidney's transcription start-up; excellent models, failing business; 87% / 53%
2. **ML vocabulary** — algorithm vs model, parameters vs hyperparameters, the compiler analogy

**Part 2 — Process** *(what engineering already knows)*
3. **Two lifecycles** — the SDLC and the ML pipeline, and how they nest
4. **From Waterfall to ADLC** — five stages, each fixing the last one's pain; and why AI-in-SDLC adoption keeps failing

**Part 3 — Context** *(landscape — tables, not prose)*
5. **How software and data got here** — two parallel evolutions
6. **What data science is** — the three-way overlap, and the hierarchy of needs

**Part 4 — People and judgment** *(where the marks are)*
7. **Who builds these systems** — SDLC roles, the three data roles, and the DS↔SE friction
8. **What ML changes about engineering** — three challenges, each "harder but not new"
9. **The risk spectrum** — the course's actual thesis, and the five enduring principles
10. **Foundation models and prompting** — when the general answer is the wrong one
11. **MLOps and responsible ML** — why both are cross-cutting and can't be scheduled late

---

## Part 1 · The argument

### 1. Why this course exists

*Reference: T1 Kästner, *Machine Learning in Production* ch1 (Introduction) — free online at mlip-cmu.github.io.*

**Intuition** — You can train a good model and still have no product. The gap between "the model works in my notebook" and "customers pay for this and it doesn't fall over" is the entire subject of this course, and it's an engineering gap, not an ML gap.

**The numbers** — consultants report **87% of ML projects fail**, and **53% never make it from prototype to production**.

**Worked example — T1's spine, the transcription start-up.** Sidney, a data scientist, publishes state-of-the-art domain-specific speech recognition and starts a company selling transcription to researchers and conference organisers. The models are genuinely excellent. The business struggles anyway:

| What went wrong | Which module fixes it |
|---|---|
| Customer audio far noisier than academic benchmarks | Requirements (M2), data quality (M5) |
| Customers want <15 min turnaround; live captioning needs to be instant — turned out **infeasible** without shipping specialised hardware to venues | Quality attributes (M2), architecture (M3) |
| Training and inference costs eat the margin; pricing took a lot of experimentation | Quality attributes, cost (M2–M3) |
| LLM features hit excessive API costs; self-hosting open models was brittle and consumed their few GPUs | Architecture (M3), deployment (M6) |
| Team had to build a website and payments they had no experience with or interest in; UX was an afterthought | From models to systems (M1) |
| Founders and hired front-end engineers **could not communicate effectively** | Interdisciplinary teams (M1) |
| Manual training scripts; nobody updated TensorFlow for a year out of fear; a model update caused a major outage and a long night reverting | Automation, versioning (M6) |
| Medical diagnoses mistranscribed **with high confidence**; African American vernacular barely intelligible | Fairness, responsible ML (M7) |
| No visibility into model performance unless a customer complained | Monitoring (M6), QA (M5) |

**The line to remember** — T1's own framing after that list: *most of these challenges are not surprising and most are not unique to ML.* The model was never the problem. Every failure was an engineering failure **around** a good model.

*The whole course in one picture (my own, after Sculley et al., "Hidden Technical Debt in ML Systems"):*

```mermaid
flowchart LR
    subgraph SYS["A real ML system — what you actually build and operate"]
        direction TB
        DATA["data collection ·<br/>cleaning · labeling · validation"]
        FEAT["feature<br/>engineering"]
        ML[["ML model —<br/>the part you trained"]]
        SERVE["serving ·<br/>APIs · scaling"]
        MON["monitoring ·<br/>drift detection"]
        INFRA["config · resource &<br/>process management"]
    end
    DATA --> FEAT --> ML --> SERVE --> MON
    INFRA -.-> ML
```

The famous finding: the ML code is a **tiny fraction** of a production ML system. The box you trained sits inside data pipelines, serving, monitoring and infrastructure — and *that* surrounding system is where the effort goes and where the failures happen. Every module of this course is one of the boxes around `ML model`.

**Tradeoff / when NOT to worry about this** — Not every model needs a product around it. A one-off analysis answering a board question is finished when the answer is delivered; building requirements, monitoring and deployment infrastructure for it is waste. The engineering investment is justified by *continued operation*, not by the model's existence.

---

### 2. Machine learning vocabulary

*Reference: T1 Kästner ch3 — the ML terminology the deck's agenda promised but stopped short of.*

#### 2.1 Algorithm vs model, training vs inference

**Intuition** — Two different things both get called "the ML", and keeping them apart is most of the clarity in this course. The **algorithm** is the procedure that *creates* the function. The **model** is the function that gets *used*. The algorithm runs once, at training. The model runs a billion times, in production.

```mermaid
flowchart LR
    TD[(Training data)] --> ALG[ML algorithm<br/>sklearn, TensorFlow]
    ALG -->|model training| MOD[Machine-learned model<br/>the learned function]
    NI[New input] --> MOD
    MOD -->|model inference| PRED[Prediction]
```

The nesting, stated flatly in T1: **AI ⊃ machine learning ⊃ deep learning**, with **foundation models** a kind of large model typically produced by deep learning. Supervised ML learns from *(data, label)* pairs, where the label is the expected output.

**Worked example** — `sklearn.tree.DecisionTreeClassifier` is the *algorithm*. `.fit(transactions, is_fraud)` is *training*. The fitted tree — a specific set of if-then-else conditions — is the *model*. `.predict(new_transaction)` is *inference*. Only the model ships to production; sklearn's training code needn't be there at all.

**Tradeoff / when the distinction bites** — Software engineers routinely conflate the two and then reason wrongly about deployment: shipping the whole training environment to production "because we need sklearn", inflating the container and the attack surface. This distinction is what makes model serving a separate architectural concern (S12).

> ***In practice*** *(beyond the deck — how "the model ships, not the algorithm" actually works):*
> - The model is **serialized** to a file and loaded by a runtime. Formats you'll meet: **pickle/joblib** (sklearn — convenient but unsafe to load from untrusted sources, and version-brittle), **ONNX** (framework-neutral, for cross-runtime serving), **safetensors** (the safe standard for deep-learning weights). "Which format" is a real deployment decision.
> - Trained models live in a **model registry** (MLflow Model Registry, SageMaker) — versioned, staged (staging → production), and rolled back like any other artifact. The registry is to models what git is to code.
> - Because **training is non-deterministic** (see below), teams log every run — data version, hyperparameters, metrics, the resulting model — with **experiment tracking** (MLflow, Weights & Biases). "Which data + code produced *this* model?" has to be answerable, and that's what S14's provenance section is about.

#### 2.2 Parameters, hyperparameters, and the compiler analogy

**Intuition** — Inside a model there are numbers the algorithm *learned* and numbers you *chose*. Learned → **parameters**. Chosen → **hyperparameters**.

| | Set by | Example | Fixed when |
|---|---|---|---|
| Model architecture | You (T1 counts it as a hyperparameter) | 3-layer net; decision tree | Before training |
| **Hyperparameters** | You | Max depth = 2; learning rate; stopping criterion | Before training |
| **Parameters** | The algorithm, from data | Threshold `amount > 500`; matrix weights | During training |

**The analogy to remember**, in T1's words: *where a compiler takes source code to generate an executable function, an ML algorithm takes data to create a function (model). Just like the compiler, the ML algorithm is no longer used at runtime. Hyperparameters correspond to compiler options.*

| Traditional software | Machine learning |
|---|---|
| Source code | Training data |
| Compiler | ML algorithm |
| Compiler options (`-O2`) | **Hyperparameters** |
| Executable | Model |
| Running the executable | Inference |
| Bytecode + JVM | Serialized ("pickled") model + runtime |

**Worked example — T1's own, and it's fraud detection.** A decision tree for credit-card fraud, trained with a hyperparameter capping nesting at two levels. The learned function is two nested if-then-else statements (the *internal structure*), with specific decision boundaries on `terminalRisk` and `amount` (the *parameters*). You chose "depth ≤ 2"; the data chose the thresholds.

**Two consequences T1 draws out:**

- **Training is often non-deterministic** — retraining on identical data can produce a slightly different model. This breaks the reproducibility assumption engineers carry over from compilers, and is why S14 devotes a section to provenance and reproducibility. *Where the randomness comes from (my clarity — T1 names the fact, not the cause): **random weight initialisation**, the **random order of mini-batches** in stochastic gradient descent, randomised techniques like **dropout**, and even **floating-point addition being non-associative on a GPU** — parallel threads sum partial results in whatever order they finish, giving bit-level-different totals. Same data, same code, slightly different model. A compiler has none of these, which is why its output is reproducible and a trained model's isn't.*
- **Models are stored serialized, not as binaries** — an intermediate format of learned parameters, loaded by a runtime. Directly analogous to Java bytecode plus the JVM. Some infrastructure compiles models to native code for speed.

**Tradeoff / where the analogy breaks** — and this is exam-worthy precisely because it's so nearly right: a compiler is deterministic and its output is *specified*. An ML algorithm is neither. Push the analogy too far and you start expecting a "correct" model the way you expect a correct binary. T1's precise position: the **model** is a pure, deterministic, side-effect-free function; the **training** that produced it is not.

#### 2.3 Terminology traps

T1 devotes a section to this, which signals it can be asked.

| Ambiguous word | Say instead |
|---|---|
| model | *machine-learned model* vs *software-architecture model* |
| performance | *prediction accuracy* vs *inference latency* |
| parameter | *model parameter* (learned) vs *hyperparameter* (chosen) |

---

## Part 2 · Process — what engineering already knows

### 3. Two lifecycles: the SDLC and the ML pipeline

*Reference: T1 Kästner ch1 (why the SDLC assumption breaks) & ch3 (the ML pipeline); for the SDLC itself, any SE text (Sommerville, *Software Engineering*).*

#### 3.1 The Software Development Life Cycle

**Intuition** — A structured, repeating process for building software: plan it, understand it, design it, build it, check it, ship it, keep it alive. A cycle, not a line — maintenance feeds back into planning.

```mermaid
flowchart LR
    P[Planning] --> A[Analysis]
    A --> D[Design]
    D --> Dev[Development]
    Dev --> T[Testing]
    T --> Dep[Deployment]
    Dep --> M[Maintenance]
    M --> P
```

**Shift-left testing** — move testing earlier ("left" on the timeline) rather than treating it as a final gate. Defects found in design cost a fraction of defects found in production. Called out explicitly on the roles slide, which usually signals exam-worthy.

**Worked example** — Fraud detection. *Planning* — is fraud loss worth a project? *Analysis* — what counts as fraud, what data exists. *Design* — where the scorer sits in the payment flow. *Development* — build it. *Testing* — catches known fraud without blocking good customers. *Deployment* — shadow mode, then live. *Maintenance* — fraud patterns shift, retrain.

**Tradeoff / when the SDLC assumption fails** — The phases are always present; running them **once, in strict order** (Waterfall) only works when requirements are fixed and knowable up front. ML violates that by construction — you cannot specify the accuracy target before seeing whether the data supports it. That is the *lack of specifications* problem, developed in section 8.1.

#### 3.2 The machine-learning pipeline

**Intuition** — Training is one step of many. Everything before it is making data fit to learn from; everything after is deciding whether it's good enough and keeping it alive.

```mermaid
flowchart LR
    R[Model requirements] --> DC[Data collection]
    DC --> DL[Data labeling]
    DL --> CL[Data cleaning &<br/>feature engineering]
    CL --> TR[Model training]
    TR --> EV[Model evaluation]
    EV --> DEP[Deployment]
    DEP --> MON[Monitoring]
    EV -.->|not good enough| CL
    EV -.->|different algorithm<br/>or hyperparameters| TR
    EV -.->|need more data| DC
    MON -.-> R
```

Two engineering-relevant properties, both from T1:

1. **It is highly iterative.** A bad evaluation sends you back to a different algorithm, different hyperparameters, more data, or different preparation. The dashed arrows are the normal path, not the exception.
2. **Most steps have surprisingly little code.** Preparation is programmed transformations (drop outlier rows, normalise a column). Training is "very few lines calling the library." **Deployment and monitoring are where the substantial infrastructure lives** — which is exactly why this is a software-engineering course.

**Worked example** — Fraud detection. *Requirements* — catch fraud above ₹5,000 within 200ms. *Collection* — 18 months of transactions. *Labeling* — confirmed chargebacks, which arrive 30–90 days late (a real problem, not a footnote). *Cleaning/features* — merchant risk score, velocity in last hour. *Training* — six lines. *Evaluation* — recall at a fixed false-positive rate. *Deployment* — behind the payment API. *Monitoring* — recall against chargebacks as they arrive.

#### 3.3 How the two relate

Worth being able to state, because the exam can ask it either way round:

| | SDLC | ML pipeline |
|---|---|---|
| Scope | The whole system | One component of it |
| Driven by | Requirements | Requirements **and data** |
| Iterates because | Requirements change | Evaluation fails — routinely, by design |
| "Done" means | Meets the specification | Good enough on average; no specification exists |
| Output | Deployable system | A model that becomes *one part* of that system |

The ML pipeline sits **inside** the SDLC, roughly spanning its Design–Development–Testing phases, and adds a monitoring loop the SDLC's Maintenance phase never had to run continuously.

**Tradeoff / when NOT to automate the pipeline** — Full pipeline automation is the goal (S13), but automating *early*, before you know which steps you'll keep changing, builds infrastructure around a design you're about to throw away. Data scientists work notebook-cell-by-cell during exploration for good reason. The engineering judgment is knowing when exploration has stabilised enough to be worth automating.

Cross-link: → `_shared/ml-lifecycle.md` · **549 S4–S7** · **546 S13**

---

### 4. From Waterfall to ADLC

*Reference: R1 Tech Mahindra ADLC white paper (held in `/_library/`).*

**Intuition** — Process models climbing a ladder: Waterfall → Iterative → Agile → Scaled Agile → *Scaled Agile with AI infusion*, which the report calls **ADLC** (AI-Driven Development Life Cycle) and names as the desired state. Each rung fixed the previous rung's worst pain and introduced a new one.

| Stage | Features | Challenges | Impact |
|---|---|---|---|
| **Waterfall** | Predictability, simplicity; works with well-defined requirements | Static docs in monolithic blocks; heavy up-front documentation error-prone; **late defect discovery** | Higher time to market; increased cost; customer dissatisfaction |
| **Iterative** | Evolving documentation; continuous testing for early detection | Document synchronisation; keeping test cases consistent across iterations | Higher operational overhead; inconsistent quality; unpredictable timelines |
| **Agile** | Just-enough documentation; continuous integration, testing, deployment | Balancing detail with agility; robust automation suite is hard; needs experienced team | Depends on human skill; higher initial investment; efficiency/quality tradeoffs |
| **Scaled Agile** | Consistent documentation; systematic integrated approach with continuous delivery pipeline | Consistent artifacts across many teams; cross-team test coordination cumbersome | Impact on time-to-market; high human dependence; reduced cross-team efficiency |
| **ADLC** (desired) | AI-assisted automation of **all** SDLC activities — documents, design, code, test cases, test data, automation scripts, deployment scripts | *(the report lists none — that is itself the finding)* | Faster time-to-market; reduced dependence on human expertise; consistent quality |

**Worked example** — Fraud detector under Waterfall: a 60-page spec, then discovering in UAT that the label definition was wrong, then a six-month delay. Under ADLC: AI drafts the spec, generates test data covering fraud edge cases, writes the deployment scripts — so "the label definition is wrong" → corrected and redeployed takes days.

#### What the report is actually about

*The slide shows only the evolution table. The paper's real subject is different, and more useful for this course.*

Its opening claim: **"the adoption levels are still far below expectations. Many organizations struggle to realize value by adopting AI in SDLC."** Not because the tools are bad — *"Does this mean these tools lack value? Absolutely not."* — but because **tool adoption is only one step**, and organizations ignore the rest of the ecosystem.

**The example that makes the whole argument, and the one to memorise:**

> A team adopts an **AI Pair Programming** tool. It *will* accelerate the coding phase. But it will **not** reduce overall time-to-market or TCO, **because the overall cycle remains unchanged.**

Concretely: an Agile team on a 4-week iteration adds an AI pair programmer. Developer productivity rises. Nothing else improves — **unless the subsequent testing and deployment activities are also advanced**, shortening the release cycle at the same bandwidth. Only then does cost saving appear.

*This is a local-optimisation trap, and it's the same shape as 546's central theme: improving one component doesn't improve the system. Compare section 1 — Sidney's models were excellent and the business still failed.*

#### The five GenAI capabilities, and where they pay

| Capability | What it does |
|---|---|
| **Generate** | Code, documentation, code explanation, requirements and design documents, test cases, test data |
| **Recommend** | Analyse context and available options, **with reasoning** |
| **Review** | Review human-generated artifacts and code |
| **Summarize** | Consume large documents and code, produce concise artifacts |
| **Knowledge Search** | Contextual search for high-quality matches |

Claimed productivity improvement, by SDLC phase:

| Phase | Up to | Example applications |
|---|---|---|
| **Requirement Analysis** | **20%** | Generate overview/glossary from BRDs; review requirement completeness; find information across documents |
| **Design** | **15%** | Generate design options from BRDs; find similar designs for reuse; generate architecture/class/sequence diagrams |
| **Build** | **30%** | Write code from natural-language instructions; AI-generated comments; faster, more accurate code reviews |
| **Test** | **30%** | Generate test cases (document and code); review coverage against requirements; **generate synthetic test data** |

*Note the shape: **Build and Test gain most (30%), Design least (15%)**. Design is judgment-heavy and hardest to automate — which is precisely why modules 2–3 of this course are about design and not about coding.*

#### Why adoption fails — four categories

| Category | Representative failure |
|---|---|
| **Planning & Execution** | Narrow focus on tool adoption without holistic replanning; no training environment; poor infosec architecture; weak implementation partners |
| **Technology** | Insufficient infrastructure investment; **uncontrolled LLM-on-cloud usage driving subscription costs that erode ROI**; leaders lacking technical depth to evaluate tools |
| **Commercial** | Poor commercial structuring neutralising ROI |
| **Stakeholder Management** | IT leaders fear **next year's budget cuts** because of this year's savings; inter-departmental barriers; **junior employees fear job loss** |

That last row is worth pausing on. It's an *organisational* failure mode, not a technical one — the efficiency gain is real and gets resisted because of what it implies for budgets and jobs. The report's remedy is to **incentivise leaders for efficiency gains** rather than punish them with reduced budgets.

#### The four-stage adoption journey

```mermaid
flowchart LR
    E["1 · EXPERIMENT<br/>find what fits<br/>POCs · security & legal vetting<br/>usage guidelines"]
    O["2 · ONBOARD & PILOT<br/>license management<br/>training, hackathons<br/>establish KPIs, ROI, baseline"]
    S["3 · SCALE & SOAR<br/>org-level rollout<br/>train champions<br/>publish success stories"]
    Su["4 · SUSTAIN<br/>maintain >80% usage<br/>remove roadblocks<br/>continuous improvement"]
    E --> O --> S --> Su
    Su -.->|feedback| E
```

Two specifics worth carrying: **KPIs and a baseline must be established at the pilot stage** — you cannot demonstrate ROI without a before-measurement — and the sustain target is **at least 80% active utilisation**, monitored, with roadblocks actively removed.

**Tradeoff / when NOT to use** — Read the Impact column downward: every stage reduces *human* dependence and increases *tooling* dependence. ADLC's stated benefit — "reduced dependence on human expertise" — is also its risk. Generated code, tests and specs need a human who can tell correct from plausible, and that judgment is exactly what atrophies when generation is automated. The report lists no ADLC challenges in its table; read that as *unproven*, not *solved* — and note that the rest of the paper is, in effect, thirteen pages of the challenges the table omits.

**The deeper tradeoff, and the one an exam would reward:** the report's own evidence is that **AI in one SDLC phase yields nothing unless the whole cycle is replanned**. So ADLC isn't a tool decision, it's a process-redesign decision. Adopting the tool is cheap; replanning the cycle, retraining staff, restructuring incentives and controlling LLM spend is where the cost and the failure risk actually sit.

Cross-link: → **546 S15** (ADLC phases in detail)

---

## Part 3 · Context

### 5. How software and data got here

*Reference: deck only for the framing; cloud-native evolution is developed in 549 S2–S3 and `_shared/docker-k8s.md`.*

#### 5.1 Evolution of software development

**Intuition** — Four things evolved *together*, not separately: how you develop, how the app is structured, how you ship it, what it runs on. Each era's four choices reinforce each other.

| Era | Development process | Architecture | Deployment & packaging | Infrastructure |
|---|---|---|---|---|
| ~1980–1990 | Waterfall | Monolithic | Physical server | Datacenter |
| ~2000 | Agile | N-tier | Virtual servers | Hosted |
| ~2010 | **DevOps** | **Microservices** | **Containers** | **Cloud** |

```
Cloud Native App = Agile + DevOps + Microservices + Containers + Cloud
```

**Tradeoff / when NOT to go cloud-native** — Microservices and containers buy independent deployment and scaling, and cost you distributed-system problems you didn't previously have: network failures between services, distributed tracing, eventual consistency, far more operational surface. A monolith on one server is genuinely right for a small team with modest load. "Cloud native" is not a maturity score.

#### 5.2 Evolution of data

**Intuition** — Sixty years of one pressure: more data than the previous generation's tools could hold, forcing a new layer each time.

```mermaid
timeline
    title Evolution of Data
    1960s : Files and spreadsheets : Manual, paper-based, limited sharing
    1970 : Codd's relational model : Foundation for modern RDBMS
    1989 : KDD and data mining : Classification, regression, clustering
    Early 2000s : Transactional to analytical : Data warehousing, ETL, BI dashboards
    Mid 2000s : Social media : User-generated data, supervised ML advances
    2006-2008 : Cloud computing : AWS and Azure, scalable compute and storage
    2010-2015 : Big data deluge : Mobile and IoT, deep learning in NLP and CV
    2018 : Transformers : Attention Is All You Need, NLP and AI at scale
```

**The through-line** — storage → compute → algorithms → data volume, each unlock enabling the next. Transformers didn't arrive because someone had a clever idea in 2018; they arrived because the 2010–2015 data deluge and cloud compute made them trainable.

Cross-link: → `_shared/docker-k8s.md` · **549 S2–S3** · **536 S1–S2**

---

### 6. What data science is

*Reference: deck; the DS Venn and the "hierarchy of needs" are standard framings (Monica Rogati, "The AI Hierarchy of Needs").*

**Intuition** — The study of data: turning it into a *story* that produces insight, and insight that produces a decision. If no decision changes, it wasn't data science — it was reporting. Scope runs collection → preprocessing → analysis → prediction → visualisation (storytelling) → insight.

**The convergence** — three fields, and each pairwise overlap has its own name:

| Overlap | Produces |
|---|---|
| Math/Statistics ∩ Domain knowledge | **Research** |
| Math/Statistics ∩ CS/IT | **Software development** |
| Domain knowledge ∩ CS/IT | **Machine learning** |
| **All three** | **Data science** |

That third row is a favourite exam question because it's counter-intuitive: ML sits in the *domain + CS* overlap, meaning ML without statistical grounding is still ML — just fragile.

**The hierarchy of needs** — you cannot do the fun layer until the boring layers underneath work. AI sits at the apex of a pyramid whose base is instrumentation and logging.

```mermaid
flowchart BT
    C["COLLECT<br/>instrumentation, logging, sensors,<br/>external data, user-generated content"]
    M["MOVE / STORE<br/>reliable data flow, infrastructure,<br/>pipelines, ETL, structured + unstructured storage"]
    E["EXPLORE / TRANSFORM<br/>cleaning, anomaly detection, prep"]
    A["AGGREGATE / LABEL<br/>analytics, metrics, segments,<br/>aggregates, features, training data"]
    L["LEARN / OPTIMIZE<br/>A/B testing, experimentation,<br/>simple ML algorithms"]
    AI["AI, DEEP LEARNING"]
    C --> M --> E --> A --> L --> AI

    C -.- r1["Data Infrastructure Engineer"]
    M -.- r2["Data Engineer"]
    A -.- r3["Data Scientist / Data Analyst"]
    AI -.- r4["ML Engineer"]
```

**Worked example** — A team wants an LLM assistant over company documents. Apex layer. But if documents aren't collected in one place (COLLECT), or the sync pipeline is unreliable (MOVE/STORE), or they're full of duplicates and dead links (EXPLORE/TRANSFORM), the assistant produces confident nonsense. It looks like a model problem; it's a base-of-pyramid problem.

**Tradeoff / how NOT to read the pyramid** — It's a *dependency* claim, not a *sequencing mandate*. Read literally it says "spend two years on data infrastructure before touching ML," which kills projects. Honest reading: cut a thin vertical slice through all six layers for one use case, then widen. Note also that simple ML sits *below* deep learning — A/B tests and logistic regression solve a large share of problems pitched as AI.

---

## Part 4 · People and judgment

### 7. Who builds these systems

*Reference: T1 Kästner ch1 (data scientists vs software engineers; T-shaped people; unicorns).*

**Intuition** — Roles exist because different failures need different specialists watching for them. In ML systems the roles come from two different traditions that were trained differently and mean different things by "done" — which is where the friction lives.

#### 7.1 Roles in the SDLC

| Role | Responsibility |
|---|---|
| Business Analyst | Translates business needs into technical requirements |
| Project Manager | Plans, coordinates, tracks execution against deadlines |
| Product Owner | Defines vision, prioritises features for value |
| Team Lead | Guides technically, keeps tasks moving |
| Software Architect | Designs system structure and technical strategy |
| Developers | Build and implement functionality |
| QA Team | Validates quality systematically (shift-left testing) |
| Testers | Find defects, verify requirements met |
| Scrum Master | Facilitates Agile, removes impediments |
| UX/UI Designers | Design intuitive interfaces |

#### 7.2 The three data roles

Distinguished by **what they hand over**, and the handovers get progressively harder to engineer.

**Data engineer** — moves and stores data reliably.

```mermaid
flowchart LR
    S[Data source] -->|Extract| ST[Staging area]
    ST -->|Transform| DW[(Data warehouse)]
    DW -->|Load| BI[Business intelligence]
```

**Data scientist** — produces a model and an answer, typically once.

```mermaid
flowchart LR
    D[(Data)] --> M[ML model]
    M --> F[One-time forecast]
```

**ML engineer** — runs a model continuously in production, with feedback.

```mermaid
flowchart LR
    CD[(Client data)] --> M[ML model]
    AD[(Additional data)] --> M
    M --> PD[(Prediction data)]
    GT[(Ground truth data)] --> MON[Monitoring and analysis]
    PD --> MON
    MON -.->|drift detected, retrain| M
    CD --> GT
```

**Worked example** — Fraud detection. The *data engineer* guarantees last night's transactions land in the warehouse by 6am. The *data scientist* shows a model catches 82% of fraud on last year's data. The *ML engineer* runs it on live traffic, compares predictions against confirmed-fraud ground truth as it arrives, notices recall sliding from 82% to 61% as tactics change, and retrains.

**Tradeoff / when the one-time forecast is correct** — The data scientist's diagram genuinely is the right shape for a pricing study, a feasibility check, a board question. Building the full ML-engineer loop for a question asked once is waste. The failure this course targets is the opposite: a one-time-forecast notebook promoted into a production dependency without the ground-truth loop, degrading silently.

#### 7.3 Data scientists vs software engineers — the actual friction

T1 states its own central theme outright: *how to get data scientists and software engineers to each contribute their distinct expertise while effectively working together.* The friction isn't skill, it's different notions of what "done" means.

| | Data scientists | Software engineers |
|---|---|---|
| Background | Statistics, ML algorithms (often PhD) | Requirements, design, QA, distributed systems, security |
| Prefer | Feature engineering, architecture, hyperparameter tuning; also much data gathering/cleaning | Delivering products meeting user needs, within budget and time |
| Workflow | Science-like, **exploratory**, computational notebooks | Design → implement → test → deploy → maintain |
| Evaluate by | **Accuracy on held-out test data**; maybe fairness, robustness | **Trade-offs** across usability, scalability, maintainability, security, cost, time |
| Rarely focus on | Inference latency, training cost | Feature engineering, testing for generalisation |

**Two terms that get asked:**

- **"Unicorns"** — people deeply skilled in both. Rare, "even considered mythical." Most people specialise. Don't staff a plan on unicorns.
- **T-shaped team members** — deep expertise in one area (the vertical) plus broad understanding of others (the horizontal). T1's stated goal is not to turn data scientists into engineers, but to give each enough breadth to *understand and appreciate* the other. T-shaped people are what make interdisciplinary teams work.

T1's evidence on the reverse direction is worth sitting with, since it describes most of this cohort: software engineers who pick up ML without formal training "approach machine learning rather naively with little focus on feature engineering, they rarely test models for generalization, and they think of more data and deep learning as the only next steps when stuck."

**Tradeoff / how NOT to use this contrast** — T1 calls it "oversimplified and overgeneralized" itself. As a lens on why a handover failed, useful. As a hiring stereotype, wrong — the point is complementarity, not superiority. And in a small team one person wears four hats, where the risk flips from coordination overhead to blind spots: whoever wrote the code also decides whether it's tested enough.

Cross-link: → `_shared/ml-lifecycle.md` · **546 M1 Interdisciplinary Teams** · **549 S4**

---

### 8. What ML changes about engineering

*Reference: T1 Kästner ch1 (the three challenges, each "harder but not new").*

**Intuition** — There's an open debate about whether ML fundamentally changes engineering or just demands that we finally apply existing practice rigorously. T1 gives three challenges, and for each argues the challenge is *harder* but *not new*. That two-part shape — challenge, then "but we've seen this before" — is what makes it exam-friendly, and you should reproduce both halves.

#### 8.1 Lack of specifications

Traditional engineering relies on decomposition: specify each component, build and test separately, compose. T1's contrast:

```python
def compute_deductions(agi, expenses):
    """Compute deductions based on provided adjusted gross income
    and expenses in customer data. See tax code 26 U.S. Code A.1.B, PART VI.
    Adjusted gross income must be a positive value.
    Returns computed deduction value."""
```

```python
def transcribe(audio_file):
    """Return the text spoken within the audio file.
    ????"""
```

The first can be implemented by one developer and relied on by another without either seeing the other's code. The second cannot be specified — *we use ML precisely because we don't know how to specify the function.*

The deep shift: **deductive reasoning** (logic-based, applying rules) → **inductive reasoning** (generalising from observation). We can no longer ask whether a component is *correct*, only whether it works *well enough on average* on test data or in the system. And since some answers will be wrong, **the rest of the system must tolerate mistakes** — a design constraint, not an afterthought. This is the concrete reason the SDLC's "run the phases once in order" assumption (section 3.1) fails.

*But not new:* software engineering has a long history of building safe systems from unreliable components, and comprehensive formal specifications were always rare. Engineers already cope with vague specs via agile methods, cross-team communication, and lots of testing.

#### 8.2 Interacting with the real world

Models trained on observations of the world, then acting on that world:

- **Bias in, bias out** — skewed observation produces fairness failures (dialects; diseases affecting only women).
- **Feedback loops** — YouTube recommended conspiracy videos heavily because viewers of those videos watch a lot; recommending them more kept people on the platform, which strengthened the signal. **Fixed not with better ML but by hard-coding rules around the model.**
- **Adaptation and gaming** — speakers changing pronunciation to dodge mistranscription; adversarial attacks such as custom glasses defeating face recognition.
- **Drift** — user behaviour shifts, intentionally or naturally.

*But not new:* software has harmed people without ML — radiation overdoses, crashed planes and spacecraft. The established response is requirements engineering, hazard analysis, threat modelling. ML makes it *harder* because more components are poorly understood and the data isn't neutral — so requirements engineering matters *more*, not less.

#### 8.3 Data-focused and scalable

Data that doesn't fit one machine; distributed training and serving; **the ML flywheel** — more users → more data → better models → more users. Large foundation models need expensive hardware even for inference, forcing dedicated machines accessed remotely.

*But not new:* cloud operation and large-scale data management (warehouses, batch, streaming) predate ML by a decade. The demands are simply higher.

---

### 9. The risk spectrum

*Reference: T1 Kästner ch1 (the risk/rigour argument and the enduring principles).*

**Intuition** — T1's actual thesis, and the sentence most likely to be quoted at you: it isn't that ML *is* riskier, it's that we *attempt riskier things* with ML.

| Risk | Example | Practice level |
|---|---|---|
| Low | Restaurant website, podcast hosting | Light |
| Medium | Medical records, payment software | Step up: requirements, risk analysis, QA, security |
| High | Aircraft control, nuclear plant control | Heavy, slow, expensive — and we know how |

> **The conjecture:** software products with ML components tend to fall toward the more complex and more risky end of the spectrum, compared to traditional products — calling for more investment in rigorous engineering practices.

**Worked example** — Fraud detection is not a restaurant website. False negatives cost money; false positives block legitimate customers and can be discriminatory; the system runs on live payment traffic at scale. Mid-to-high on the spectrum, and the practices should match — which is what modules 2–7 supply.

**Tradeoff / the symmetric error** — T1 is careful and so should you be: "It is not that machine learning automatically makes projects riskier — and there certainly are also many low-risk systems with machine-learning components." Applying nuclear-grade rigour to a low-stakes recommender is its own failure. The judgment is *locating your system on the spectrum first*, then matching practice to position. That judgment is what 546 teaches.

**The enduring principles** T1 says survive every technology shift — a ready-made exam answer:

1. Understanding customer priorities and tolerance for mistakes
2. Designing safe systems with unreliable components
3. Navigating conflicting qualities — accuracy, operating cost, latency, time to release
4. Planning a responsible testing strategy
5. Designing systems that can be updated rapidly and monitored in production

---

### 10. Foundation models and prompting

*Reference: T1 Kästner ch3 (foundation models & prompting); the RAG stack is built hands-on in 546 S6.*

**Intuition** — Instead of training a model per task, a few organisations train one enormous general-purpose model and everyone else *instructs* it with a prompt. Customisation moves from training data to prompt text.

**Mechanism** — T1's toxicity example: rather than training a toxicity classifier on labelled examples, send `Answer only yes or no. Is the following sentence toxic: [input]`.

Two ways to customise:

| Strategy | What it is | Cost |
|---|---|---|
| **Fine-tuning** | Train a copy on custom data (internal email, forum messages) | Expensive; produces a model you must host and version |
| **In-context learning** | Put information or examples in the prompt itself | Cheap; costs context window and per-call tokens |

**Few-shot prompting** is in-context learning with examples:

```
Classify the sentence into toxic or non-toxic.
Text: We need to kill this process.
A: non-toxic
Text: RTFM
A: toxic
[more examples]
Text: [sentence to analyze]
A:
```

Providing *internal data* in the prompt is the case T1 flags forward to **retrieval-augmented generation** — which is 546 S6, and the same RAG you build in 521 and 536. The course's own tool list (LangChain, ChromaDB, OpenAI embeddings and LLM) confirms S6 is hands-on, not conceptual.

*The full customisation ladder (my own — the deck names two rungs; here's the spectrum you actually pick from, cheapest first):*

```mermaid
flowchart LR
    A["1 · Prompt<br/>zero-shot"] --> B["2 · Few-shot<br/>examples in prompt"]
    B --> C["3 · RAG<br/>retrieve your data<br/>into the prompt"]
    C --> D["4 · Fine-tune<br/>train a copy"]
    D --> E["5 · Pre-train<br/>your own model"]
```

Cost, effort and *how much of the model you change* all rise left → right, and the engineering rule is: **reach for the leftmost rung that works.** Prompt and few-shot change nothing but the text; RAG adds a retrieval system but no training; fine-tuning produces a model you own, host and version; pre-training is for the few orgs building foundation models. The classic mistake is fine-tuning something a better prompt or RAG would have fixed — the expensive rung reached for too early. (RAG's mechanics → S6.)

**Worked example** — Fraud detection with a foundation model: `"Given this transaction and the customer's last 10 transactions, is this likely fraudulent? Answer yes/no with one reason."` No training data needed, works immediately — and costs an API call per transaction, with latency you don't control, for a task a decision tree does in microseconds.

**Tradeoff / when NOT to use** — T1 is direct: foundation models "do not have access to proprietary or recent information that was not part of the training data," and "model size and inference costs can become a challenge." Use them where the task is language-shaped, varied, and hard to specify. Don't use them for a high-volume, low-latency, narrow, well-specified task with plenty of labelled data — fraud scoring at 10,000 transactions/second being exactly that. **A foundation model is the expensive general answer to a question you might be able to specify cheaply.**

Cross-link: → `_shared/rag.md` · **546 S6** · **536 S10, S12** · **521 S7–8**

---

### 11. MLOps and responsible ML

*Reference: T1 Kästner ch1 (MLOps & responsible ML as cross-cutting concerns).*

**Intuition** — T1 treats both as *cross-cutting concerns*, not as chapters. That framing is itself examinable, because it's the argument against believing a tool can solve either.

**MLOps** — automating ML pipelines so models can be deployed, updated, monitored and operated reliably. Usually discussed as a tool market: Kubeflow (scalable workflows), Great Expectations (data quality testing), MLflow (experiment tracking), Evidently AI (model monitoring), Amazon SageMaker (end-to-end platform). T1 covers the *fundamentals* across the whole book, with the closest dedicated treatment in **Planning for Operations** (tooling landscape) and **Interdisciplinary Teams** (the collaboration culture — joint goals, joint vocabulary, joint tools).

That tool list matches your 546 lab stack almost exactly: MLflow, Evidently AI, SageMaker, plus DVC, Prefect, Docker/K8s, FastAPI, PyTest.

**Responsible ML** — T1's position is blunt: *there are no magic tools that can make a model secure or ensure fairness.* Responsible engineering requires a holistic view of the system, how the model interacts with other components, and how the system interacts with its environment. Attempted without that grounding, "attempts to tackle safety, security, or fairness are often narrow, naive, and ineffective."

**Tradeoff** — the practical implication of "cross-cutting" is that you cannot schedule either as a phase. A team that plans to "do the fairness work in sprint 12" has already lost, because the decisions that determine fairness — what data, what labels, what the system does with a low-confidence prediction — were made in sprints 1 through 11.

> ***In practice*** *(beyond the deck — what MLOps actually looks like as a job):*
> MLOps is **CI/CD extended to data and models**. On top of the usual code pipeline (git, tests, containers), an ML pipeline adds three things software CI/CD never had:
> - **Data & model versioning** — DVC or LakeFS version datasets; the model registry versions models. You can reproduce "the model from March" only if both are versioned alongside the code.
> - **Continuous training & evaluation** — a pipeline (Prefect, Airflow, Kubeflow) retrains on new data, evaluates against a held-out set *and* against the current production model, and only promotes if it wins.
> - **Monitoring for drift** — the loop the S07 diagram shows: compare live predictions against ground truth as it arrives (Evidently AI), alert when recall slides, trigger retraining. This is the part that has no equivalent in traditional software, and it's where "ML engineer" and "MLOps engineer" spend most of their time. Your 546 lab stack (MLflow, DVC, Prefect, Evidently, Docker/K8s, FastAPI) is this pipeline in miniature.

> ***Going deeper*** *(my own knowledge, beyond the deck — the three ways a model actually serves predictions; picking the wrong one is a classic mistake):*
>
> | Pattern | How | When |
> |---|---|---|
> | **Batch / offline** | Score a whole dataset on a schedule, write results to a table | Predictions can be precomputed — churn scores overnight, recommendations refreshed hourly |
> | **Online / real-time** | A service (FastAPI behind a load balancer) scores one request at a time, low latency | The answer is needed *now* — fraud check at checkout, search ranking |
> | **Streaming** | Score events as they flow through a queue (Kafka) | Continuous event data — clickstreams, IoT, live anomaly detection |
>
> The running example makes the choice concrete: **fraud detection is online** (the score gates a live payment, ~200 ms budget); a monthly churn report is **batch**. Building a heavy real-time service for something a nightly batch job would do — or vice-versa — is the same "match the machinery to the need" judgment as the risk spectrum in section 9.

---

## Lab / build

No lab this session. **546 Lab 1 is at session 3** — end-to-end ML system blueprint, fraud detection.

**Locked in:** fraud detection is the running example for all sixteen sessions. T1 ch3 uses a credit-card fraud decision tree as its own worked example (section 2.2), so the textbook and the running example line up from page one.

---

*Exam: this session is in scope for the **closed-book mid-sem** (sessions 1–8). Full evaluation, weights, dates and course logistics live once in [`546-master.md`](../546-master.md) — not repeated per session.*
