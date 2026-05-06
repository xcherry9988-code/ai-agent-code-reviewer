# AI Agent Code Reviewer

AI Agent Code Reviewer is a lightweight multi-agent prototype for GitHub repository analysis, code review, refactoring suggestions, and Markdown report generation.

The project is designed for AI Coding and Agent workflow experiments. It simulates a practical software-engineering assistant that reads a codebase, builds repository context, detects maintainability issues, and generates structured improvement reports.

---

## Project Goal

Modern code projects often contain scattered files, repeated logic, weak documentation, missing tests, and hidden technical debt.

This project explores a multi-agent workflow for repository-level understanding and automated engineering analysis.

Core workflow:

1. Understand repository structure
2. Select important source files
3. Analyze code quality
4. Generate refactoring suggestions
5. Build testing recommendations
6. Export Markdown reports

---

## Multi-Agent Architecture

```text
User Repository
↓
Planner Agent
↓
Repo Reader Agent
↓
Code Review Agent
↓
Test Suggestion Agent
↓
Report Agent
```

---

## Agents

### Planner Agent

Breaks review tasks into structured execution steps.

### Repo Reader Agent

Scans repository folders and builds project context.

### Code Review Agent

Detects:

- TODO/FIXME
- Long functions
- Weak naming
- Missing error handling
- Maintainability risks

### Test Suggestion Agent

Suggests:

- Unit tests
- Edge cases
- Integration testing targets

### Report Agent

Exports structured Markdown reports.

---

## Features

- Local repository scanning
- Multi-agent workflow simulation
- Python code analysis
- TODO detection
- Long-function detection
- Markdown report generation
- Extensible AI Coding architecture

---

## Tech Stack

- Python 3.10+
- Markdown
- GitHub
- AI Agent workflow
- Future LLM integration support

---

## Quick Start

```bash
git clone https://github.com/xcherry9988-code/ai-agent-code-reviewer.git

cd ai-agent-code-reviewer

python main.py --path .
```

Generated reports will be saved into:

```text
reports/code_review_report.md
```

---

## Project Structure

```text
ai-agent-code-reviewer/
├── agents/
├── core/
├── reports/
├── examples/
├── main.py
├── requirements.txt
└── README.md
```

---

## Roadmap

- GitHub repository ingestion
- Automatic issue generation
- PR draft generation
- AI-powered semantic review
- Test generation
- Cross-file reasoning
- Multi-language support

---

## Token Usage Scenario

This project is designed for long-context AI Coding workflows, repository-level code understanding, multi-agent collaboration, automated report generation, and future large-scale code refactoring experiments.

---

## License

MIT License
