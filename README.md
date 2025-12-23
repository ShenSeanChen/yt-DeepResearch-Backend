# 🔬 Deep Research Agent - Backend

A powerful FastAPI backend that provides intelligent deep research capabilities using multiple AI models (OpenAI, Anthropic, Kimi K2). Built with LangGraph for complex research workflows and designed for deployment on GCP Cloud Run. The backend is designed to work with the [Deep Research Frontend](https://github.com/ShenSeanChen/yt-deepresearch-frontend).

📹 Full YouTube Guide: [Youtube link](https://www.youtube.com/watch?v=dw9Vkig47S0&list=PLE9hy4A7ZTmpGq7GHf5tgGFWh2277AeDR&index=29)

🚀 X Post: [X link](https://x.com/ShenSeanChen/status/1969013359010873513)

💻 Launch Full Stack Product: [Github Repo](https://github.com/ShenSeanChen/launch-mvp-stripe-nextjs-supabase)

☕️ Buy me a coffee: [Cafe Latte](https://buy.stripe.com/5kA176bA895ggog4gh)

🤖️ Discord: [Invite link](https://discord.com/invite/TKKPzZheua)

## ✨ Features

- **Multi-Model Support**: OpenAI GPT-4o, Anthropic Claude, and Kimi K2 0905
- **Streaming Research**: Real-time progress updates with detailed step visibility
- **LangGraph Integration**: Complex research workflows with clarification, briefing, execution, and reporting
- **Cloud Ready**: Docker containerized for GCP Cloud Run deployment
- **Secure API Keys**: Environment-based configuration with user-provided keys
- **Health Monitoring**: Built-in health checks and metrics collection

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker (for containerization)
- GCP Account (for deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShenSeanChen/yt-DeepResearch-Backend.git
   cd yt-DeepResearch-Backend
   ```

2. **Install dependencies**
   ```bash
   # Create a virtual environment (you can name it .venv or venv)
   python3 -m venv venv

   # Activate the virtual environment
   source venv/bin/activate   # On macOS/Linux
   # .\venv\Scripts\activate  # On Windows (PowerShell)

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration (optional - API keys can be provided via frontend)
   ```

4. **Run the development server**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8080 --reload
   ```

5. **Test the API**
   ```bash
   curl http://localhost:8080/health
   ```

## 🏗️ Architecture

### Core Components

- **`main.py`**: FastAPI application with streaming endpoints
- **`services/deep_research_service.py`**: Core research logic with LangGraph integration
- **`services/model_service.py`**: AI model management and configuration
- **`models/research_models.py`**: Pydantic models for API contracts
- **`open_deep_research/`**: Research agent implementation

### Research Workflow

1. **Clarification**: Optional query clarification with user
2. **Research Brief**: Generate research strategy and plan
3. **Research Execution**: Conduct multi-source research with real-time updates
4. **Final Report**: Synthesize findings into comprehensive report

## 🔧 Configuration

### Supported Models

| Model | Provider | Configuration |
|-------|----------|---------------|
| `openai` | OpenAI | GPT-4o with 128k context |
| `anthropic` | Anthropic | Claude-3-5-Sonnet |
| `kimi` | Moonshot AI | K2 0905 via Anthropic API |

### Environment Variables

```bash
# Optional - API keys can be provided via frontend
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key

# For Kimi K2 (uses Anthropic API format)
ANTHROPIC_API_KEY=your_kimi_key  # When using Kimi
ANTHROPIC_BASE_URL=https://api.moonshot.ai/anthropic  # Auto-configured for Kimi
```

## 📡 API Endpoints

### Health Check
```bash
GET /health
HEAD /health  # For Cloud Run health checks
```

### Streaming Research
```bash
POST /research/stream
Content-Type: application/json

{
  "query": "Your research question",
  "model": "anthropic",  # openai, anthropic, or kimi
  "api_key": "your_api_key"
}
```

### Response Format (Server-Sent Events)
```
data: {"type": "session_start", "content": "Starting research..."}
data: {"type": "stage_start", "stage": "clarification", "content": "..."}
data: {"type": "research_step", "stage": "research_planning", "content": "🎯 Planning research strategy..."}
data: {"type": "research_finding", "content": "🔍 Research Finding 1: ..."}
data: {"type": "research_complete", "content": "Final report content"}
```

## 🐳 Docker Deployment

### Build Image
```bash
docker build -t deep-research-backend .
```

### Run Container
```bash
docker run -p 8080:8080 deep-research-backend
```

## ☁️ GCP Cloud Run Deployment

### Prerequisites
- GCP CLI installed and authenticated
- Docker configured for GCP

### Deploy
```bash
# Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/deep-research-backend

# Deploy to Cloud Run - BEST PRACTICE: Optimized for long-running research
gcloud run deploy deep-research-backend \
  --image gcr.io/YOUR_PROJECT_ID/deep-research-backend \
  --platform managed \
  --region europe-west1 \
  --allow-unauthenticated \
  --memory 4Gi \
  --cpu 2 \
  --timeout 3600s \
  --max-instances 5 \
  --min-instances 1 \
  --concurrency 10
```

### Environment Variables in Cloud Run
Set these in the GCP Console under Cloud Run > Service > Edit & Deploy New Revision > Variables:

- `GET_API_KEYS_FROM_CONFIG=true` (enables user-provided API keys)

## 🔗 Connecting to Frontend

The backend is designed to work with the [Deep Research Frontend](https://github.com/ShenSeanChen/yt-deepresearch-frontend).

### Frontend Configuration
In your frontend `.env.local`:
```bash
# For local development
NEXT_PUBLIC_BACKEND_URL=http://localhost:8080

# For production
NEXT_PUBLIC_BACKEND_URL=https://your-backend-url.run.app
```

## 🧪 Testing

### API Testing with curl
```bash
# Health check
curl -X GET http://localhost:8080/health

# Research stream (replace with your API key)
curl -X POST http://localhost:8080/research/stream \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are the latest developments in AI?",
    "model": "anthropic",
    "api_key": "your_api_key"
  }'
```

### Model-Specific Testing
```bash
# Test Kimi K2 integration
python test_kimi_model.py
```

## 📊 Monitoring

- Health checks available at `/health`
- Structured logging for debugging
- Request/response metrics collection
- Error tracking and reporting

## 🔒 Security

- API keys never stored server-side
- CORS configured for frontend origins
- Input validation with Pydantic models
- Rate limiting and timeout protection

## 🐛 Troubleshooting

### Common Issues

1. **HTTP 405 Errors in GCP Logs**
   - Fixed: HEAD method support added for health checks

2. **Token Limit Errors**
   - Solution: Upgraded to GPT-4o (128k context) for OpenAI

3. **Kimi K2 Connection Issues**
   - Check base URL: `https://api.moonshot.ai/anthropic`
   - Verify API key format matches Anthropic

4. **Streaming Interruptions**
   - Keep-alive headers configured
   - Timeout set to 300s for long research

## 📝 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

- Create an issue for bugs or feature requests
- Check existing issues for solutions
- Review logs for debugging information

---

Built with ❤️ using FastAPI, LangGraph, and modern AI models.
