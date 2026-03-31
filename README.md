# ConfigPilot-Genie-AI
Personal AI System Inspector is an intelligent AI agent that analyzes your system environment and provides smart, compatibility-aware software installation guidance.

It combines:
1.) System inspection
2.) Rule-based reasoning
3.)Retrieval-Augmented Generation (RAG)
4.) LLM-powered recommendations using Google Gemini

 Features

System Inspection,
Detect installed software (Python, CUDA, Git, etc.),
Identify PATH issues,
Detect GPU and system configuration,
Find residual/uninstalled files.

Rule-Based AI->
Logical conclusions from system facts.
Detects:
Installed but not in PATH,
Driver-only installations (CUDA),
Missing dependencies,

Fix Suggestions:
PATH configuration assistance,
Opens environment variables automatically,
Cleanup recommendations.

RAG (Knowledge Retrieval):
Uses local knowledge base,
Provides contextual installation insights.

LLM Integration:
Suggests best compatible versions. 
 Gives:
Version optimization,
Compatibility reasoning,
Step-by-step installation guide.

Architecture:
User Input->
   
Inspector (Facts)->
   
Rule Engine (Logic)->
   
Fixer (Actions)->
   
RAG (Knowledge)->
   
LLM (Gemini).

Tech Stack:
Python,
System-level inspection (os, subprocess),
Rule-based AI,
RAG architecture,
Google Gemini API-any API of our wish here i used it,
dotenv.

Setup:
1️.)Clone Repository
2.)Create Virtual Environment
3.)Install dependencies
4.)Add API key
5.)Run Project

Author:
Subiksha M

   ↓
Final Recommendation
