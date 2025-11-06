from typing import Dict, Any

class StructuralPromptEngine:
    def __init__(self):
        self.templates = self._load_templates()
    
    def _load_templates(self):
        return {
            "chatgpt": """
ANALYZE DOCUMENT WITH STRUCTURAL CONTEXT:

DOCUMENT STRUCTURE:
{semantic_map}

DOCUMENT CONTENT:
{document_text}

INSTRUCTIONS:
Use the hierarchical structure to understand document organization.
Maintain context relationships between sections.
Reference specific document sections when answering.
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
Analyze using structural hierarchy. Consider section relationships.
</instructions>
</document_analysis>
""",
            "gemini": """
DOCUMENT STRUCTURAL ANALYSIS:

SEMANTIC MAP:
{semantic_map}

DOCUMENT TEXT:
{document_text}

ANALYSIS GUIDELINES:
Leverage document structure for deeper understanding.
Map responses to specific hierarchical elements.
"""
        }
    
    def enhance_for_provider(self, semantic_map, document_text, provider="chatgpt", level="full"):
        template = self.templates.get(provider, self.templates["chatgpt"])
        structure_str = self._format_semantic_map(semantic_map)
        enhanced_prompt = template.format(
            semantic_map=structure_str,
            document_text=document_text
        )
        return enhanced_prompt
    
    def _format_semantic_map(self, semantic_map):
        try:
            hierarchy_str = "Hierarchy:\n"
            for item in semantic_map.get("hierarchy", []):
                hierarchy_str += f"- {item.get('type', 'unknown')}: {item.get('content', '')}\n"
            
            blocks_str = "Content Blocks:\n"
            for block in semantic_map.get("blocks", []):
                blocks_str += f"- {block.get('type', 'unknown')}: {block.get('content', '')}\n"
            
            return f"{hierarchy_str}\n{blocks_str}"
        except Exception as e:
            return f"Structure error: {str(e)}"

prompt_engine = StructuralPromptEngine()



