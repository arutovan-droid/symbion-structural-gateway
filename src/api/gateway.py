from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import aiofiles
import os
import uuid
from typing import Optional

from src.core.config import settings
from src.modules.ocr_engine import DeepSeekOCRProcessor
from src.modules.prompt_enhancer import StructuralPromptEngine

app = FastAPI(
    title=settings.project_name,
    version=settings.project_version,
    description="Structural document understanding gateway for AI systems"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize processors
ocr_processor = DeepSeekOCRProcessor()
prompt_engine = StructuralPromptEngine()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Symbion Structural Gateway API",
        "version": settings.project_version,
        "status": "active"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "structural-gateway"}

@app.post("/api/v1/enhance")
async def enhance_document(
    file: UploadFile = File(..., description="Document to enhance"),
    provider: str = "chatgpt",
    enhancement_level: str = "full"
):
    """
    Enhance document with structural understanding for AI processing
    """
    try:
        # Validate file type
        allowed_types = ['.pdf', '.jpg', '.jpeg', '.png']
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in allowed_types:
            raise HTTPException(
                status_code=400, 
                detail=f"File type {file_ext} not supported. Use: {allowed_types}"
            )
        
        # Save uploaded file temporarily
        file_id = str(uuid.uuid4())
        temp_path = f"/tmp/{file_id}{file_ext}"
        
        async with aiofiles.open(temp_path, 'wb') as f:
            content = await file.read()
            await f.write(content)
        
        # Process document structure
        structured_data = await ocr_processor.extract_structured_document(temp_path)
        
        # Generate enhanced prompt
        enhanced_prompt = prompt_engine.enhance_for_provider(
            structured_data["semantic_map"],
            structured_data["cleaned_text"],
            provider=provider,
            level=enhancement_level
        )
        
        # Cleanup temp file
        os.unlink(temp_path)
        
        return {
            "status": "success",
            "enhanced_prompt": enhanced_prompt,
            "semantic_map": structured_data["semantic_map"],
            "original_structure": structured_data.get("layout_descriptor", {}),
            "processing_time": structured_data.get("processing_time", 0),
            "provider": provider
        }
        
    except Exception as e:
        # Cleanup on error
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.unlink(temp_path)
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

@app.post("/api/v1/analyze-structure")
async def analyze_structure_only(file: UploadFile = File(...)):
    """
    Analyze document structure without prompt enhancement
    """
    try:
        file_id = str(uuid.uuid4())
        temp_path = f"/tmp/{file_id}.pdf"
        
        async with aiofiles.open(temp_path, 'wb') as f:
            content = await file.read()
            await f.write(content)
        
        structured_data = await ocr_processor.extract_structured_document(temp_path)
        
        os.unlink(temp_path)
        
        return {
            "status": "success",
            "semantic_map": structured_data["semantic_map"],
            "layout_descriptor": structured_data.get("layout_descriptor", {}),
            "cleaned_text": structured_data.get("cleaned_text", "")
        }
        
    except Exception as e:
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.unlink(temp_path)
        raise HTTPException(status_code=500, detail=f"Analysis error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
