/**
 * High-Impact Software Engineering Projects Dataset
 * Covering Frontend, Backend, and Full-Stack Engineering domains.
 */
const PROJECTS_DATA = [
  {
    id: "nexus-cloud-ai",
    title: "NexusCloud AI - Distributed ML Pipeline & Orchestrator",
    badge: "Featured Full-Stack",
    category: "fullstack",
    categoryLabel: "Full Stack",
    tagline: "End-to-end deep learning workflow orchestrator with real-time distributed GPU cluster monitoring, automated experiment lineage, and zero-downtime canary rollouts.",
    coverImage: "assets/projects/nexus-cloud.jpg",
    screenshots: [
      {
        url: "assets/projects/nexus-cloud.jpg",
        caption: "Main Telemetry Dashboard - Real-time GPU cluster utilization, training loss curves, and active DAG pipeline nodes."
      },
      {
        url: "assets/projects/pulse-stream.jpg",
        caption: "Distributed Node Telemetry - Multi-worker stream telemetry and latency monitoring across GPU clusters."
      },
      {
        url: "assets/projects/dev-canvas.jpg",
        caption: "Interactive Visual Pipeline Designer - Visual DAG configuration with live node execution status."
      }
    ],
    tags: ["React 18", "TypeScript", "FastAPI", "PyTorch", "Kubernetes", "Redis", "gRPC", "TimescaleDB"],
    problemStatement: "Machine learning research teams suffered from fragmented model training scripts, unmonitored GPU resource waste (averaging 35% idle cycles), and high-risk manual model rollouts resulting in service downtime during production traffic shifts.",
    solution: "Architected a unified full-stack platform featuring a real-time reactive DAG canvas, live telemetry streaming via gRPC & WebSockets, automated model checkpointing, and progressive canary rollouts managed on Kubernetes with automatic regression rollback.",
    keyMetrics: [
      { value: "-40%", label: "GPU Idle Time Waste" },
      { value: "99.98%", label: "Model Serving Uptime" },
      { value: "3.2x", label: "Faster Deployment Cycles" },
      { value: "120+", label: "Concurrent ML Pipelines" }
    ],
    keyFeatures: [
      "Interactive drag-and-drop DAG workflow canvas for multi-step data ingestion, tokenization, training, and evaluation.",
      "Live GPU/VRAM cluster telemetry with automatic node failover and anomaly detection.",
      "Automated canary deployments with real-time p99 latency and inference accuracy regression checks.",
      "Integrated model artifact registry with Git-style versioning and SHA256 integrity validation."
    ],
    architecture: {
      overview: "Clients interact via React 18 frontend communicating over WebSockets and REST. FastAPI gateway handles authentication and dispatches jobs to Redis/Celery queue. GPU worker nodes execute PyTorch jobs while Prometheus and TimescaleDB store time-series telemetry.",
      diagramStages: [
        { step: "01", title: "Client Layer", tech: "React 18 / Vite / WebSockets", desc: "Interactive DAG Canvas, dynamic charts, live telemetry streams." },
        { step: "02", title: "API Gateway", tech: "FastAPI / gRPC / JWT Auth", desc: "Request validation, rate-limiting, gRPC dispatching." },
        { step: "03", title: "Queue & State", tech: "Redis Cluster / Celery", desc: "Distributed job queuing, distributed locks, worker coordination." },
        { step: "04", title: "Worker Cluster", tech: "PyTorch / CUDA / K8s", desc: "Autonomous ML model training and evaluation pods." },
        { step: "05", title: "Data & Storage", tech: "TimescaleDB / S3 / Postgres", desc: "Time-series telemetry, model checkpoints, metadata logs." }
      ]
    },
    techStackBreakdown: {
      "Frontend Architecture": [
        { name: "React 18 & TypeScript", purpose: "Component state, type safety, and fast reactive re-rendering." },
        { name: "React Flow / Canvas", purpose: "Interactive DAG visualization and live pipeline connection routing." },
        { name: "Chart.js & WebGL", purpose: "60 FPS rendering of loss curves and multi-GPU VRAM telemetry." }
      ],
      "Backend & Distributed Services": [
        { name: "Python FastAPI", purpose: "High-performance async REST & WebSocket endpoints." },
        { name: "gRPC & Protocol Buffers", purpose: "Microsecond inter-service communication between gateway and workers." },
        { name: "Celery & Redis", purpose: "Asynchronous task queue with automated priority retry logic." }
      ],
      "Data & Storage Layer": [
        { name: "PostgreSQL", purpose: "Relational persistence for user accounts, experiments, and model metadata." },
        { name: "TimescaleDB", purpose: "Specialized hypertable engine for millions of telemetry time-series metrics." },
        { name: "Redis Cache", purpose: "Session state and real-time pub/sub pipeline notification dispatch." }
      ],
      "Cloud & DevOps Infrastructure": [
        { name: "Kubernetes (EKS)", purpose: "Cluster orchestration and autoscaling worker pods with GPU slicing." },
        { name: "Prometheus & Grafana", purpose: "Cluster health monitoring, alerting, and metric scraping." },
        { name: "Docker & AWS S3", purpose: "Containerized reproducible execution and S3 model artifact store." }
      ]
    },
    links: {
      demo: "https://nexus-cloud.example.com",
      github: "https://github.com/developer/nexus-cloud-ai",
      docs: "https://docs.nexus-cloud.example.com"
    }
  },

  {
    id: "pulse-stream",
    title: "PulseStream - Real-Time High-Throughput Event Streaming Engine",
    badge: "Core Backend",
    category: "backend",
    categoryLabel: "Backend & Systems",
    tagline: "Ultra-low latency event ingestion and routing backbone processing 250,000+ operations/sec with automated backpressure and zero-loss failover.",
    coverImage: "assets/projects/pulse-stream.jpg",
    screenshots: [
      {
        url: "assets/projects/pulse-stream.jpg",
        caption: "Cluster Topology & Latency Monitor - Live broker health, partition consumer lag, and sub-4ms p99 latency curve."
      },
      {
        url: "assets/projects/nexus-cloud.jpg",
        caption: "Distributed Metrics View - Ingestion rate curves and active worker consumer group status."
      },
      {
        url: "assets/projects/kubeflow-ops.svg",
        caption: "Multi-Region Cluster View - Cluster auto-rebalancing across multi-region edge brokers."
      }
    ],
    tags: ["Go (Golang)", "Kafka", "Redis", "gRPC", "Docker", "ClickHouse", "eBPF", "Prometheus"],
    problemStatement: "Monolithic pub/sub broker architecture collapsed under sudden traffic surges, producing severe consumer lag exceeding 14 seconds, memory out-of-bounds crashes, and silent message dropping during partition rebalancing.",
    solution: "Engineered a distributed Golang streaming engine leveraging Apache Kafka partition affinity, memory ring-buffers, adaptive backpressure algorithms, and ClickHouse for columnar analytics with zero data loss guarantee.",
    keyMetrics: [
      { value: "250K+", label: "Events Ingested / Sec" },
      { value: "3.8ms", label: "p99 Latency SLA" },
      { value: "0%", label: "Dropped Events on Surge" },
      { value: "-65%", label: "Memory Footprint" }
    ],
    keyFeatures: [
      "Dynamic consumer group rebalancing with sub-second heartbeats to eliminate consumer starvation.",
      "Multi-tier memory ring buffers utilizing Write-Behind disk persistence for maximum write speed.",
      "Live cluster topology visualizer displaying per-broker lag, consumer group offsets, and health states.",
      "End-to-end distributed trace propagation using OpenTelemetry and eBPF network packet inspection."
    ],
    architecture: {
      overview: "Edge traffic hits an Envoy proxy mesh. Ingestion Go services deserialize binary payloads and write to Kafka partitions. Downstream worker pools consume messages with backpressure into Redis ring buffers, flushing to ClickHouse for analytical queries.",
      diagramStages: [
        { step: "01", title: "Edge Gateway", tech: "Envoy Proxy / mTLS", desc: "Traffic routing, TCP multiplexing, security throttling." },
        { step: "02", title: "Ingestion Engine", tech: "Go (Golang) Microservices", desc: "Non-blocking binary message decoding, partition routing." },
        { step: "03", title: "Distributed Bus", tech: "Apache Kafka Cluster", desc: "Partitioned topic logs with 3x replication factor." },
        { step: "04", title: "Transform Pool", tech: "Go Worker Goroutines", desc: "Stream filtering, deduplication, dynamic backpressure." },
        { step: "05", title: "Analytic Storage", tech: "ClickHouse & Redis", desc: "Columnar OLAP real-time aggregation and instant querying." }
      ]
    },
    techStackBreakdown: {
      "Frontend & Observability": [
        { name: "HTML5 Canvas & WebSockets", purpose: "Lightweight live cluster topology visualization without DOM lag." },
        { name: "Grafana Dashboards", purpose: "Detailed operational telemetry dashboards for SREs." }
      ],
      "Backend Core Engine": [
        { name: "Golang (Go)", purpose: "High concurrency goroutines with minimal GC pauses for stream ingestion." },
        { name: "Apache Kafka", purpose: "Durable, high-throughput distributed commit log." },
        { name: "gRPC & Protobuf", purpose: "Strict typed, ultra-efficient internal service-to-service payloads." }
      ],
      "Data & In-Memory Layer": [
        { name: "ClickHouse", purpose: "Petabyte-scale analytical query engine executing aggregates in milliseconds." },
        { name: "Redis Cluster", purpose: "Sub-millisecond deduplication filter and ephemeral sliding-window cache." }
      ],
      "Infrastructure & Monitoring": [
        { name: "eBPF & Prometheus", purpose: "Kernel-level network observability and latency tracing." },
        { name: "Docker & AWS EC2", purpose: "Bare-metal optimized container nodes deployed with Terraform." }
      ]
    },
    links: {
      demo: "https://pulsestream.example.com",
      github: "https://github.com/developer/pulse-stream-engine",
      docs: "https://pulsestream.example.com/docs"
    }
  },

  {
    id: "dev-canvas",
    title: "DevCanvas - Collaborative Next-Gen Frontend UI Builder & Code Synthesizer",
    badge: "Frontend Innovation",
    category: "frontend",
    categoryLabel: "Frontend Engineering",
    tagline: "Browser-based visual layout engine with real-time CRDT multi-user collaboration, instant production React/CSS code synthesis, and sub-16ms render loops.",
    coverImage: "assets/projects/dev-canvas.jpg",
    screenshots: [
      {
        url: "assets/projects/dev-canvas.jpg",
        caption: "Component Design Studio - Drag & drop atoms, live canvas layout, and instant JSX/CSS AST code inspector."
      },
      {
        url: "assets/projects/hyperion-fin.svg",
        caption: "Real-Time Render Pipeline - 60 FPS Canvas rendering engine with interactive inspector tools."
      },
      {
        url: "assets/projects/nexus-cloud.jpg",
        caption: "Multiplayer Collaboration - Real-time multiplayer cursors and simultaneous layout editing."
      }
    ],
    tags: ["TypeScript", "Vanilla JS", "HTML5 Canvas", "WebGL", "Web Workers", "WebRTC", "CSS Grid"],
    problemStatement: "Design-to-code handoffs are historically fraught with discrepancies, bloated machine-generated HTML/CSS, and zero capability for simultaneous visual pair-programming across remote engineering teams.",
    solution: "Engineered an in-browser visual engine powered by HTML5 Canvas & WebGL with Yjs CRDTs for frictionless multiplayer editing and an AST engine that emits clean, human-readable React/CSS code.",
    keyMetrics: [
      { value: "60 FPS", label: "Render Framerate (1.5k Nodes)" },
      { value: "0", label: "CRDT Merge Conflicts" },
      { value: "5x", label: "Faster Prototype-to-Code" },
      { value: "20+", label: "Simultaneous Live Users" }
    ],
    keyFeatures: [
      "Real-time multiplayer cursor tracking and simultaneous component manipulation without locking.",
      "Intuitive CSS Flexbox and Grid spatial snapping with zero runtime performance drag.",
      "Custom AST code generator producing clean, formatted React JSX and CSS variables on the fly.",
      "Design token manager supporting instant switching between dark, light, and custom corporate themes."
    ],
    architecture: {
      overview: "Visual updates run on an optimized HTML5 Canvas loop. Mutation actions flow through a local Yjs CRDT document, replicated to peers via WebRTC data channels. An off-thread Web Worker executes Babel/PostCSS AST transformations to synthesize clean code.",
      diagramStages: [
        { step: "01", title: "Canvas Viewport", tech: "HTML5 Canvas / WebGL", desc: "60 FPS hardware accelerated layout and node transform loop." },
        { step: "02", title: "CRDT State", tech: "Yjs / IndexedDB", desc: "Conflict-free state replication, undo/redo history, local persistence." },
        { step: "03", title: "Multiplayer Mesh", tech: "WebRTC Data Channels", desc: "Peer-to-peer cursor movement and state sync with WebSocket fallback." },
        { step: "04", title: "AST Transpiler", tech: "Web Worker / Babel AST", desc: "Off-main-thread code generation from component tree." },
        { step: "05", title: "Code Export", tech: "Monaco Editor / Zip Engine", desc: "Syntax-highlighted preview and instant GitHub PR creation." }
      ]
    },
    techStackBreakdown: {
      "Frontend & Core Canvas": [
        { name: "Modern TypeScript & Vanilla JS", purpose: "Zero-overhead performance, modular architecture, strict typing." },
        { name: "HTML5 2D Canvas & WebGL", purpose: "Fluid rendering of 2,000+ interactive DOM elements at 60 FPS." },
        { name: "Web Workers API", purpose: "Offloading heavy AST parsing and code synthesis from UI thread." }
      ],
      "Real-Time Collaboration": [
        { name: "Yjs CRDT Engine", purpose: "Conflict-free replicated data types for concurrent layout editing." },
        { name: "WebRTC DataChannels", purpose: "P2P low-latency cursor synchronization and mesh data transfer." }
      ],
      "Backend & Relay Services": [
        { name: "Node.js & Express", purpose: "Lightweight signaling server for WebRTC handshake and project persistence." },
        { name: "Redis Pub/Sub", purpose: "Room presence tracking and real-time fallback synchronization." }
      ],
      "Tooling & Deployment": [
        { name: "Vite & Rollup", purpose: "Blazing fast development server and optimized production bundling." },
        { name: "Cloudflare Edge", purpose: "Global CDN delivery with sub-50ms static asset loading." }
      ]
    },
    links: {
      demo: "https://devcanvas.example.com",
      github: "https://github.com/developer/devcanvas-builder",
      docs: "https://devcanvas.example.com/docs"
    }
  },

  {
    id: "omnicart-enterprise",
    title: "OmniCart Enterprise - Headless Microservices E-Commerce Platform",
    badge: "Full-Stack Enterprise",
    category: "fullstack",
    categoryLabel: "Full Stack",
    tagline: "High-concurrency global commerce engine featuring edge checkout, dynamic inventory locking, real-time pricing algorithms, and resilient payment pipelines.",
    coverImage: "assets/projects/omnicart.svg",
    screenshots: [
      {
        url: "assets/projects/omnicart.svg",
        caption: "Enterprise Operations Command - Real-time GMV, active checkouts, and microservice cluster health status."
      },
      {
        url: "assets/projects/nexus-cloud.jpg",
        caption: "Inventory & Order Pipeline - Real-time order dispatch status and distributed lock validation."
      },
      {
        url: "assets/projects/pulse-stream.jpg",
        caption: "High-Throughput Checkout - Payment gateway resilience and webhook delivery metrics."
      }
    ],
    tags: ["Next.js", "Go (Golang)", "PostgreSQL", "Redis Redlock", "GraphQL", "Stripe", "AWS ECS", "ElasticSearch"],
    problemStatement: "Legacy e-commerce monolith suffered from overselling inventory during flash sales due to race conditions, sluggish 4.2s mobile page loads, and brittle checkout APIs causing dropped customer transactions.",
    solution: "Built a headless architecture using Next.js edge rendering, decoupled Go microservices, Redis distributed locking (Redlock) for strict inventory guarantees, and an idempotent payment webhook engine.",
    keyMetrics: [
      { value: "184ms", label: "Edge TTFB Latency" },
      { value: "100%", label: "Inventory Lock Accuracy" },
      { value: "+28%", label: "Mobile Checkout Conversion" },
      { value: "12.8K", label: "Peak Req/Sec Processed" }
    ],
    keyFeatures: [
      "Edge-rendered storefront with incremental static regeneration (ISR) delivering sub-200ms page loads.",
      "Distributed inventory reservation engine using Redis Redlock to mathematically prevent overselling.",
      "Multi-region payment processing with automated fallbacks and idempotent webhook delivery.",
      "Real-time admin control center with live GMV metrics, order fulfillment tracks, and automated fraud scoring."
    ],
    architecture: {
      overview: "Customers access the storefront via CloudFront CDN and Next.js edge nodes. Requests route through an Apollo GraphQL federated gateway to specialized Go microservices (Catalog, Inventory, Payment). Inventory holds are managed by Redis Redlock and committed to Aurora PostgreSQL.",
      diagramStages: [
        { step: "01", title: "Edge Storefront", tech: "Next.js / CloudFront / ISR", desc: "Sub-200ms page delivery, optimistic client cart state." },
        { step: "02", title: "GraphQL Gateway", tech: "Apollo Federation / Envoy", desc: "Unified schema graph, query caching, token authentication." },
        { step: "03", title: "Service Mesh", tech: "Go Microservices (ECS)", desc: "Domain-driven services for Orders, Cart, Catalog, and Pricing." },
        { step: "04", title: "Distributed Locks", tech: "Redis Redlock Cluster", desc: "Microsecond inventory holding to eliminate flash sale race conditions." },
        { step: "05", title: "Transactional DB", tech: "AWS Aurora PostgreSQL", desc: "Multi-AZ ACID database with read replicas and ElasticSearch indexing." }
      ]
    },
    techStackBreakdown: {
      "Frontend & Edge Layer": [
        { name: "Next.js 14 & React", purpose: "Hybrid SSR/ISR rendering for peak SEO and instant navigation." },
        { name: "Tailwind & Vanilla Tokens", purpose: "Responsive, accessible design system with mobile-first UI." }
      ],
      "Microservices & APIs": [
        { name: "Go (Golang)", purpose: "Blazing fast microservices for high-concurrency order and checkout processing." },
        { name: "GraphQL & REST", purpose: "Federated API composition tailored to web and mobile clients." },
        { name: "Stripe & PayPal APIs", purpose: "PCI-compliant payment capture with idempotent processing." }
      ],
      "Data & Caching Layer": [
        { name: "PostgreSQL (Aurora)", purpose: "Primary ACID ledger for orders, customer data, and financial transactions." },
        { name: "Redis (Redlock)", purpose: "Distributed locking and flash-sale cart cache." },
        { name: "ElasticSearch", purpose: "Fuzzy catalog search with typo tolerance and sub-10ms query execution." }
      ],
      "Infrastructure & Cloud": [
        { name: "AWS ECS & Fargate", purpose: "Serverless container execution auto-scaling with demand." },
        { name: "Terraform", purpose: "Infrastructure as Code across staging and multi-region production." }
      ]
    },
    links: {
      demo: "https://omnicart.example.com",
      github: "https://github.com/developer/omnicart-enterprise",
      docs: "https://omnicart.example.com/api"
    }
  },

  {
    id: "kubeflow-ops",
    title: "KubeFlow Ops - Multi-Cloud Infrastructure & Observability Orchestrator",
    badge: "Cloud & DevOps",
    category: "backend",
    categoryLabel: "Backend & Systems",
    tagline: "Autonomous infrastructure management platform providing self-healing Kubernetes clusters, continuous drift detection, and proactive cost optimization.",
    coverImage: "assets/projects/kubeflow-ops.svg",
    screenshots: [
      {
        url: "assets/projects/kubeflow-ops.svg",
        caption: "Multi-Region Orchestrator - Cross-cloud cluster topology, automated drift reconciliation log, and cost savings."
      },
      {
        url: "assets/projects/pulse-stream.jpg",
        caption: "eBPF Packet Telemetry - Kernel-level cluster network monitoring with zero agent overhead."
      },
      {
        url: "assets/projects/nexus-cloud.jpg",
        caption: "KEDA Pod Autoscaler - Real-time queue depth scaling metrics and predictive resource allocation."
      }
    ],
    tags: ["Kubernetes", "Go (Golang)", "Python", "Terraform", "eBPF", "Prometheus", "ClickHouse", "AWS/GCP"],
    problemStatement: "Organizations managing multi-cloud Kubernetes clusters faced spiraling cloud bills ($50k+/month in idle reservations), frequent security drift from manual kubectl edits, and painfully slow incident root-cause triage.",
    solution: "Engineered a centralized Golang Kubernetes operator that monitors cluster state via eBPF daemonsets, automatically remediates security configuration drift against GitOps repo definitions, and adjusts KEDA pod requests.",
    keyMetrics: [
      { value: "-$42.8K", label: "Monthly Cloud Bill Saved" },
      { value: "2.1 min", label: "Mean Time to Recovery" },
      { value: "1,489", label: "Auto-Healed Drift Events" },
      { value: "100%", label: "SOC2 Compliance Score" }
    ],
    keyFeatures: [
      "Autonomous drift remediation reversing unauthorized manual cluster changes in under 900ms.",
      "eBPF-powered network observability tracking 8M+ packets/sec with zero kernel overhead.",
      "Predictive pod right-sizing utilizing historical traffic models to scale compute before spikes hit.",
      "Automated TLS cert-manager lifecycle management and incident dispatch to PagerDuty/Slack."
    ],
    architecture: {
      overview: "Autonomous agents deployed as eBPF DaemonSets collect packet and process telemetry on worker nodes. The central Golang operator checks cluster state against GitOps configurations in Git, reconciling deviations and publishing analytical events to ClickHouse.",
      diagramStages: [
        { step: "01", title: "GitOps Source", tech: "GitHub / GitLab Webhooks", desc: "Single source of truth for desired cluster state." },
        { step: "02", title: "K8s Operator", tech: "Golang (client-go) Controller", desc: "Continuous reconciliation loop, drift detection logic." },
        { step: "03", title: "eBPF Agents", tech: "C / eBPF Kernel Probes", desc: "Low-overhead network packet, socket, and process tracking." },
        { step: "04", title: "Analytical Store", tech: "ClickHouse & etcd", desc: "Sub-second audit logging of all cluster mutations." },
        { step: "05", title: "Cloud Providers", tech: "AWS / GCP / Bare Metal APIs", desc: "Direct node group provisioning and dynamic rightsizing." }
      ]
    },
    techStackBreakdown: {
      "Dashboard & Interfaces": [
        { name: "Modern Web UI & CLI Tool", purpose: "Real-time visual cluster health map and rapid terminal diagnostics." },
        { name: "D3.js / SVG Topology", purpose: "Interactive multi-region cluster dependency diagram." }
      ],
      "Controller & Systems Engine": [
        { name: "Golang & Kubernetes client-go", purpose: "High-speed concurrent operator controller loops." },
        { name: "eBPF (Kernel BPF)", purpose: "Zero-overhead packet inspection directly in the Linux kernel." },
        { name: "Terraform & Helm", purpose: "Declarative infrastructure-as-code automation." }
      ],
      "Storage & Metrics": [
        { name: "ClickHouse", purpose: "Ultra-fast aggregation over billions of cluster audit events." },
        { name: "etcd", purpose: "Distributed, reliable key-value store for cluster state." }
      ],
      "Cloud & Observability": [
        { name: "AWS EKS & GCP GKE", purpose: "Multi-cloud production cluster management." },
        { name: "Prometheus & Alertmanager", purpose: "Automated threshold alerting and metric aggregation." }
      ]
    },
    links: {
      demo: "https://kubeflow-ops.example.com",
      github: "https://github.com/developer/kubeflow-ops-platform",
      docs: "https://kubeflow-ops.example.com/docs"
    }
  },

  {
    id: "hyperion-finance",
    title: "Hyperion Finance - High-Frequency Algorithmic Trading Terminal",
    badge: "Frontend & FinTech",
    category: "frontend",
    categoryLabel: "Frontend Engineering",
    tagline: "Institutional-grade financial terminal delivering sub-millisecond market depth visualization, off-thread algorithmic execution, and multi-monitor workspace layout.",
    coverImage: "assets/projects/hyperion-fin.svg",
    screenshots: [
      {
        url: "assets/projects/hyperion-fin.svg",
        caption: "High-Frequency Trading Terminal - 120 FPS candlestick chart, Level 2 orderbook depth, and instant order dispatch."
      },
      {
        url: "assets/projects/dev-canvas.jpg",
        caption: "Customizable Workspace - Flexible multi-monitor grid layout and dockable panels."
      },
      {
        url: "assets/projects/pulse-stream.jpg",
        caption: "Sub-Millisecond Telemetry - Real-time WebSocket throughput and tick latency monitoring."
      }
    ],
    tags: ["TypeScript", "Canvas API", "WebGL", "WebSockets", "Web Workers", "Protobuf", "SharedArrayBuffer"],
    problemStatement: "Traders and quantitative analysts suffered from sluggish browser performance during high-volatility events, with DOM-based charts dropping frames and freezing UI threads during market tick bursts exceeding 30,000 updates/sec.",
    solution: "Engineered a high-performance frontend application utilizing Web Workers for off-thread Protobuf parsing and risk calculations, coupled with a custom 120 FPS HTML5 Canvas charting engine utilizing SharedArrayBuffers for zero-copy memory access.",
    keyMetrics: [
      { value: "120 FPS", label: "Chart Render Framerate" },
      { value: "0.8ms", label: "Order Dispatch Latency" },
      { value: "50K/s", label: "Market Ticks Handled" },
      { value: "99.999%", label: "Session Uptime SLA" }
    ],
    keyFeatures: [
      "Hardware-accelerated HTML5 Canvas candlestick and real-time tick chart capable of 120 FPS data feeds.",
      "Interactive Level 2 and Level 3 orderbook with animated liquidity depth visualization.",
      "Off-thread algorithmic risk calculation running in dedicated Web Workers to protect UI responsiveness.",
      "Dockable, customizable multi-monitor workspace layout with persistent local state."
    ],
    architecture: {
      overview: "Direct market data streams enter through binary WebSockets using Protocol Buffers. Dedicated Web Worker threads decode messages directly into a SharedArrayBuffer ring buffer. The main thread's requestAnimationFrame loop renders the data to HTML5 Canvas without memory allocation.",
      diagramStages: [
        { step: "01", title: "Market Data Feeds", tech: "Exchange Binary WebSockets", desc: "Sub-millisecond compressed tick streams." },
        { step: "02", title: "Worker Deserializer", tech: "Web Worker / Protobuf", desc: "Off-thread binary unpacking and validation without main thread blocking." },
        { step: "03", title: "Shared Memory", tech: "SharedArrayBuffer / Atomics", desc: "Zero-copy memory ring buffer shared between worker and UI thread." },
        { step: "04", title: "Render Loop", tech: "HTML5 Canvas (120 FPS)", desc: "Direct pixel plotting with double-buffering and viewport culling." },
        { step: "05", title: "Execution Gateway", tech: "WebTransport / TCP", desc: "Sub-millisecond order routing with cryptographic signatures." }
      ]
    },
    techStackBreakdown: {
      "Rendering & Frontend Engine": [
        { name: "TypeScript & Vanilla Canvas API", purpose: "Maximum execution velocity with zero framework virtual DOM overhead." },
        { name: "WebGL 2.0 Shaders", purpose: "Hardware-accelerated volume profile and market depth heatmaps." },
        { name: "Custom Layout Engine", purpose: "Snappable multi-window workspace supporting dual and triple monitor setups." }
      ],
      "Concurrency & Threading": [
        { name: "Web Workers API", purpose: "Isolates high-frequency calculations from UI rendering." },
        { name: "SharedArrayBuffer & Atomics", purpose: "Zero-copy lock-free thread communication." }
      ],
      "Networking & Protocols": [
        { name: "Binary WebSockets & Protobuf", purpose: "Minimal payload size and nanosecond serialization." },
        { name: "WebTransport", purpose: "Low-latency multiplexed UDP transport for tick data." }
      ],
      "Backend & Gateways": [
        { name: "Node.js & Go Gateways", purpose: "Exchange proxying, user session authorization, and rate limiting." },
        { name: "Redis Pub/Sub", purpose: "Internal message distribution to connected terminal clients." }
      ]
    },
    links: {
      demo: "https://hyperion.example.com",
      github: "https://github.com/developer/hyperion-trading-terminal",
      docs: "https://hyperion.example.com/docs"
    }
  }
];
