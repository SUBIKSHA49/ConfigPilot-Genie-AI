# ConfigPilot-Genie-AI
Personal AI System Inspector is an intelligent AI agent that analyzes your system environment and provides smart, compatibility-aware software installation guidance.

It combines:
🔍 System inspection
🧠 Rule-based reasoning
📚 Retrieval-Augmented Generation (RAG)
🤖 LLM-powered recommendations using Google Gemini

 Features

System Inspection
Detect installed software (Python, CUDA, Git, etc.)
Identify PATH issues
Detect GPU and system configuration
Find residual/uninstalled files

Rule-Based AI
Logical conclusions from system facts
Detects:
Installed but not in PATH
Driver-only installations (CUDA)
Missing dependencies

Fix Suggestions
PATH configuration assistance
Opens environment variables automatically
Cleanup recommendations

RAG (Knowledge Retrieval)
Uses local knowledge base
Provides contextual installation insights

LLM Integration
Suggests best compatible versions
Gives:
Version optimization
Compatibility reasoning
Step-by-step installation guide

Architecture
User Input
   ↓
Inspector (Facts)
   ↓
Rule Engine (Logic)
   ↓
Fixer (Actions)
   ↓
RAG (Knowledge)
   ↓
LLM (Gemini)
   ↓
Final Recommendation
