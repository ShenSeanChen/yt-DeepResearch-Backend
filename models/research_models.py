# Directory: yt-DeepResearch-Backend/models/research_models.py
"""
Pydantic models for Deep Research Agent API
Defines request/response schemas and data structures
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field


class ModelType(str, Enum):
    """Supported AI model types"""
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    KIMI = "kimi"


class ResearchStage(str, Enum):
    """Research workflow stages"""
    INITIALIZATION = "initialization"
    CLARIFICATION = "clarification"
    RESEARCH_BRIEF = "research_brief"
    RESEARCH_EXECUTION = "research_execution"
    TOOL_USAGE = "tool_usage"
    THINKING = "thinking"
    FINAL_REPORT = "final_report"
    COMPLETED = "completed"
    ERROR = "error"


class ResearchRequest(BaseModel):
    """Request model for deep research API"""
    query: str = Field(..., description="Research question or topic", min_length=1)
    model: ModelType = Field(..., description="AI model to use for research")
    api_key: str = Field(..., description="User's API key for the selected model", min_length=1)
    
    class Config:
        """Pydantic configuration"""
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class StreamingEvent(BaseModel):
    """Streaming event model for real-time updates"""
    type: str = Field(..., description="Event type (stage_start, stage_update, stage_complete, etc.)")
    stage: Optional[ResearchStage] = Field(None, description="Current research stage")
    content: str = Field(..., description="Event content or message")
    timestamp: str = Field(..., description="ISO timestamp of the event")
    research_id: str = Field(..., description="Unique research session identifier")
    model: str = Field(..., description="AI model being used")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional event metadata")
    error: Optional[str] = Field(None, description="Error message if applicable")
    
    class Config:
        """Pydantic configuration"""
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class ResearchResponse(BaseModel):
    """Response model for completed research"""
    research_id: str = Field(..., description="Unique research session identifier")
    query: str = Field(..., description="Original research query")
    model: str = Field(..., description="AI model used")
    final_report: str = Field(..., description="Complete research report")
    sources: List[Dict[str, str]] = Field(default_factory=list, description="Research sources")
    duration: float = Field(..., description="Research duration in seconds")
    stages: List[Dict[str, Any]] = Field(default_factory=list, description="Research stages completed")
    timestamp: str = Field(..., description="Completion timestamp")
    
    class Config:
        """Pydantic configuration"""
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class ModelMetrics(BaseModel):
    """Performance metrics for a specific model"""
    model: str = Field(..., description="Model identifier")
    total_requests: int = Field(default=0, description="Total number of requests")
    average_duration: float = Field(default=0.0, description="Average request duration in seconds")
    success_rate: float = Field(default=0.0, description="Success rate percentage")
    last_used: Optional[str] = Field(None, description="Last usage timestamp")


class ModelComparison(BaseModel):
    """Comparison metrics between different models"""
    models: List[ModelMetrics] = Field(default_factory=list, description="Metrics for each model")
    total_requests: int = Field(default=0, description="Total requests across all models")
    generated_at: str = Field(..., description="Comparison generation timestamp")
    
    class Config:
        """Pydantic configuration"""
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class ResearchHistory(BaseModel):
    """Historical research session data"""
    research_id: str = Field(..., description="Unique research session identifier")
    query: str = Field(..., description="Research query")
    model: str = Field(..., description="AI model used")
    duration: float = Field(..., description="Research duration in seconds")
    success: bool = Field(..., description="Whether research completed successfully")
    timestamp: str = Field(..., description="Research timestamp")
    summary: Optional[str] = Field(None, description="Brief summary of results")
    
    class Config:
        """Pydantic configuration"""
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class AvailableModel(BaseModel):
    """Available AI model information"""
    id: str = Field(..., description="Model identifier")
    name: str = Field(..., description="Human-readable model name")
    provider: str = Field(..., description="Model provider (OpenAI, Anthropic, etc.)")
    description: str = Field(..., description="Model description")
    capabilities: List[str] = Field(default_factory=list, description="Model capabilities")
    max_tokens: Optional[int] = Field(None, description="Maximum token limit")
    
    class Config:
        """Pydantic configuration"""
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
