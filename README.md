<div align="center">
  
<img width="1199" height="862" alt="explorai-banner-edited" src="https://github.com/user-attachments/assets/53bc4b56-0c4f-4d81-ad2e-f5fba59cffc2" />

# 🔎 ExplorAI

**From messy JSON to meaningful insights.**

![TCC](https://img.shields.io/badge/TCC-Computer%20Engineering%20%40%20UERJ-7c3aed)
![Status](https://img.shields.io/badge/status-early%20development-374151)

</div>

Ever opened a JSON dataset and thought, *"Why does this object have five layers of nested arrays?"* 🫠

**ExplorAI** is an AI-assisted tool for profiling, exploring, and understanding semi-structured data. It brings together distributed processing, automated metadata discovery, interactive analytics, and natural-language queries so you can spend less time untangling JSON and more time understanding your data.

> 🚧 **Work in progress:** ExplorAI is being developed as an undergraduate thesis (**TCC**) in Computer Engineering at the **State University of Rio de Janeiro (UERJ), Brazil**. Features below describe the planned system unless marked otherwise.

## ✨ What ExplorAI aims to do

| Capability | What it means |
| --- | --- |
| 🧬 **Recursive flattening** | Make heterogeneous JSON analyzable while retaining relevant structural information. |
| 📊 **Automated profiling** | Discover field types, completeness, samples, and descriptive statistics. |
| 🗂️ **Metadata catalog** | Make discovered fields and profiling results easy to find and query. |
| 🖥️ **Interactive exploration** | Browse datasets, search fields, and visualize analytical results. |
| 🤖 **AI-assisted queries** | Expose analytical tools via MCP so an agent can answer questions grounded in data. |
| 🧪 **Experimental validation** | Measure correctness, robustness, performance, and AI-answer reliability. |

The initial setup is **hybrid**: data processing and analytics in Databricks, with the web interface and MCP server running locally during development. Remote access depends on the capabilities and quotas available in the chosen Databricks workspace.

## 🧰 Technology stack

| Layer | Planned technology |
| --- | --- |
| Distributed processing | Python, **PySpark** |
| Cloud analytics | **Databricks** |
| Storage | **Delta Lake** |
| Asset organization | **Unity Catalog** |
| Analytical querying | **Databricks SQL** |
| User interface | **Streamlit** (initial choice) |
| Agent tooling | **Model Context Protocol (MCP)**, Python |
| Job orchestration | **Databricks Jobs**; **Apache Airflow** optional |

Technology choices may evolve as integration constraints and experimental findings become clearer.

## 🎓 Academic context

ExplorAI is part of a Computer Engineering undergraduate thesis (*Trabalho de Conclusão de Curso*, or **TCC**) at **UERJ**, Brazil.

**Research topic:** *AI-assisted Profiling and Analytical Exploration of Semi-Structured Data.*

The goal isn't just to build a cool interface. The research investigates how automated profiling and AI-assisted exploration can support an initial understanding of heterogeneous datasets.

### 🧪 Research and evaluation

The project aims to evaluate:

1. **Correctness:** Do flattening, field discovery, and profiling match expected results?
2. **Robustness:** How does the system handle nested arrays, nulls, and mixed types?
3. **Performance:** What happens as dataset size increases?
4. **AI reliability:** Are answers to predefined analytical questions supported by real query results?

Synthetic edge cases and public datasets will help make the experiments reproducible.

Because **"it works on my machine" is not a research methodology**. 😎

## 🗺️ Development roadmap

- [x] Define the research scope and choose the initial architecture.
- [ ] Set up the development environment and validate local-to-cloud connectivity.
- [ ] Implement recursive JSON flattening and edge-case tests.
- [ ] Build the profiling engine and reference tests.
- [ ] Persist processed data and profiling metadata in Delta Lake.
- [ ] Implement analytical SQL queries and a reusable Python access layer.
- [ ] Build an interactive exploration interface.
- [ ] Implement MCP tools and integrate an AI agent.
- [ ] Validate the full workflow with representative datasets.
- [ ] Evaluate correctness, processing performance, and AI reliability.
- [ ] Complete the thesis writing and academic review process.

Documentation is developed **alongside implementation**, not saved for the last minute.

## 🚀 Project status

**Stage:** Early development — architecture defined, implementation in progress.

The nerdy progress bars in the banner are just a **playful visual**, not measured engineering or academic completion metrics. For actual progress, follow the roadmap above.

## 💻 Getting started

Installation instructions and runnable examples will be added once the first end-to-end pipeline is available.
For now: no mysterious copy-paste commands, no fake one-click setup. We're still assembling the spaceship. 🚀

## 🤝 Feedback

Questions, suggestions, and constructive feedback are welcome. Since this is an academic project, feature requests will be evaluated against the thesis objectives and available development time.

---

<div align="center">

**ExplorAI — explore your data, discover its structure.** 💜

*Built with Python, curiosity, and a suspicious amount of JSON.*

</div>
