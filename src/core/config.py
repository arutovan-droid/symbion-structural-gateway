from pydantic_settings import BaseSettings
from typing import List, Optional
import os

class Settings(BaseSettings):
    """Application settings"""
    
    # DeepSeek OCR API
    deepseek_api_key: str = ""
    deepseek_api_url: str = "https://api.deepseek.com/v1/ocr"
    
    # Server settings
    allowed_origins: List[str] = ["http://localhost:3000", "https://symbion.space"]
    max_file_size: int = 10 * 1024 * 1024  # 10MB
    log_level: str = "INFO"
    
    # API settings
    api_prefix: str = "/api/v1"
    project_name: str = "Symbion Structural Gateway"
    project_version: str = "0.1.0"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Global settings instance
settings = Settings()
