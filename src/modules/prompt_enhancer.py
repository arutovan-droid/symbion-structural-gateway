from typing import Dict, Any

class StructuralPromptEngine:
    """Engine for enhancing prompts with structural document context"""
    
    def __init__(self):
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict[str, str]:
        """Load prompt templates for different AI providers"""
        return {
            "chatgpt": """
ANALYZE THIS DOCUMENT WITH STRUCTURAL CONTEXT:

DOCUMENT STRUCTURE:
{semantic_map}

DOCUMENT CONTENT:
{document_text}

INSTRUCTIONS:
1. Use the hierarchical structure to understand document organization
2. Maintain context relationships between sections
3. Reference specific document sections when answering
4. Respect the original document flow and organization

RESPONSE FORMAT: Provide comprehensive analysis considering the document structure.
""",
            "claude": """
<document_analysis>
<structure>
{semantic_map}
</structure>

<content>
{document_text}
</content>

<instructions>
Analyze this document using its structural hierarchy. Pay attention to:
- Section relationships and dependencies
- Content organization patterns
- Hierarchical importance of information
- Contextual connections between blocks

Provide insights that respect the original document architecture.
</instructions>
</document_analysis>
""",
            "gemini": """
**DOCUMENT STRUCTURAL ANALYSIS REQUEST**

**SEMANTIC MAP:**
```json
{semantic_map}
{document_text}

ANALYSIS GUIDELINES:

Leverage the document structure for deeper understanding

Map responses to specific hierarchical elements

Maintain contextual relationships in your analysis

Consider spatial and logical connections between content blocks

Please provide a structured response that aligns with the document's organization.
"""
}
 def enhance_for_provider(self, semantic_map: Dict[str, Any], document_text: str, 
                       provider: str = "chatgpt", level: str = "full") -> str:
    """
    Generate enhanced prompt for specific AI provider
    
    Args:
        semantic_map: Document structure analysis
        document_text: Cleaned document text
        provider: AI provider (chatgpt, claude, gemini)
        level: Enhancement level (basic, full)
    """
    template = self.templates.get(provider, self.templates["chatgpt"])
    
    # Convert semantic map to readable format
    structure_str = self._format_semantic_map(semantic_map)
    
    enhanced_prompt = template.format(
        semantic_map=structure_str,
        document_text=document_text
    )
    
    return enhanced_prompt

def _format_semantic_map(self, semantic_map: Dict[str, Any]) -> str:
    """Format semantic map for prompt inclusion"""
    try:
        # Format hierarchy
        hierarchy_str = "Hierarchy:\n"
        for item in semantic_map.get("hierarchy", []):
            hierarchy_str += f"- {item.get('type', 'unknown').title()}: {item.get('content', '')}\n"
        
        # Format blocks
        blocks_str = "Content Blocks:\n"
        for block in semantic_map.get("blocks", []):
            blocks_str += f"- {block.get('type', 'unknown')}: {block.get('content', '')}\n"
        
        return f"{hierarchy_str}\n{blocks_str}"
        
    except Exception as e:
        return f"Structure parsing error: {str(e)}"     
      Global instance
prompt_engine = StructuralPromptEngine()
4. **Commit changes**

---

**Создайте эти файлы в папке `modules`:**

- ✅ `src/modules/__init__.py`
- ✅ `src/modules/ocr_engine.py` 
- ✅ `src/modules/prompt_enhancer.py`

**После этого у нас будет полная базовая структура проекта!** 🚀

Покажите когда готово!
