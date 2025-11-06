# symbion-structural-gateway
First open-source framework for structural document understanding in AI.  Turns any LLM into architecturally-aware system using DeepSeek OCR.
# 🏛️ Symbion Structural Gateway

**First open-source framework for structural document understanding in AI**

> Turning any LLM into an architecturally-aware system

## 🎯 The Problem

Traditional AI sees documents as flat text streams, losing crucial structural meaning. This leads to hallucinations and poor context understanding.

## 💡 Our Solution

Symbion Structural Gateway adds **structural intelligence layer** to any LLM:

- **DeepSeek OCR** for semantic layout understanding  
- **Structural Prompt Engineering** for context enhancement
- **Universal API Gateway** for seamless integration

## 🚀 Quick Start

```python
from symbion_gateway import StructuralGateway

gateway = StructuralGateway()
enhanced_prompt = gateway.enhance_document(
    "research_paper.pdf", 
    ai_provider="chatgpt"
🏗️ Architecture
Raw Document → DeepSeek OCR → Semantic Mapping → Prompt Enhancement → Enhanced AI Response

📚 Supported Document Types
Research Papers & Academic PDFs

Technical Documentation

Business Reports with Tables/Charts

Legal Documents with Hierarchical Structure

Multi-column Layouts

🔧 Installation
pip install symbion-gateway
💻 Usage Example

import asyncio
from symbion_gateway import StructuralGateway

async def main():
    gateway = StructuralGateway()
    result = await gateway.process_document(
        "my_document.pdf",
        provider="claude",
        enhancement_level="full"
    )
    
    print(f"Enhanced prompt: {result.enhanced_prompt}")
    print(f"Semantic map: {result.semantic_map}")

asyncio.run(main())
🛠️ API Reference
POST /api/v1/enhance
Enhance document with structural understanding

Parameters:

file: Document file (PDF, JPG, PNG)

provider: AI provider (chatgpt, claude, gemini)

enhancement_level: basic | full

Response:
{
  "status": "success",
  "enhanced_prompt": "Optimized prompt with structural context",
  "semantic_map": {"hierarchy": [], "blocks": []},
  "processing_time": 1.23}
🏗️ Core Modules
OCR Engine
from src.modules.ocr_engine import DeepSeekOCRProcessor

processor = DeepSeekOCRProcessor()
structure = await processor.extract_structured_document("doc.pdf")
Prompt Enhancer
from src.modules.prompt_enhancer import StructuralPromptEngine

enhancer = StructuralPromptEngine()
prompt = enhancer.enhance_for_chatgpt(semantic_map, text)
🧪 Testing
pytest tests/ -v
🐳 Docker Deployment
docker-compose up -d
🤝 Contributing
We're building the future of document understanding. Join us!

Fork the repository

Create your feature branch

Commit your changes

Push to the branch

Create a Pull Request



