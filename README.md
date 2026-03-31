ConfigPilot-Genie-AI
Overview

This project is an intelligent AI agent that analyzes a system’s environment and provides smart, compatibility-aware software installation guidance.

It combines:

System inspection,
Rule-based reasoning,
Retrieval-Augmented Generation (RAG),
LLM-powered recommendations using Google Gemini,
Features
1.) System Inspection
Detect installed software (Python, CUDA, Git, etc.),
Identify PATH configuration issues,
Detect GPU and system configuration,
Find residual/uninstalled files.
2.)Rule-Based AI
Logical conclusions from system facts

Detects:

Installed but not in PATH,
Driver-only installations (CUDA),
Missing dependencies,
Fix Suggestions,
PATH configuration assistance,
Opens environment variables automatically,
Cleanup recommendations,

RAG (Knowledge Retrieval):
Uses local knowledge base

Provides contextual installation insights:
LLM Integration

Suggests best compatible versions

Provides:

Version optimization,
Compatibility reasoning,
Step-by-step installation guide.

Architecture:
User Input,
Inspector (Facts),
Rule Engine (Logic),
Fixer (Actions),
RAG (Knowledge),
LLM (Gemini),
Final Recommendation.

Tech Stack:
Python,
OS & Subprocess (System-level inspection),
Rule-based AI,
RAG Architecture,
Google Gemini API,
dotenv.

Setup:
Clone Repository,
Create Virtual Environment,
Install Dependencies,
Add API Key,
Run Project.

Author:
Subiksha M

Final Output
The system generates:

System analysis
Logical reasoning
Fix recommendations
AI-powered optimized installation guidance
