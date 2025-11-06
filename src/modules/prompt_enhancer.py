from typing import Dict, Any
import json

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

