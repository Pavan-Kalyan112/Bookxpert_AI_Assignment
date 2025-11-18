from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from ai_generate import RecipeGenerator
import logging
import sys
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Recipe Generator API", version="1.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize generator
generator = None
try:
    generator = RecipeGenerator()
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {str(e)}")

class RecipeRequest(BaseModel):
    ingredients: str
    category: Optional[str] = None
    cooking_time: Optional[int] = None
    difficulty: Optional[str] = None

@app.get("/")
async def read_root():
    return {
        "status": "Recipe API is running",
        "endpoints": {
            "POST /generate": "Generate a recipe with given ingredients",
            "GET /health": "Check API health"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy" if generator is not None else "error",
        "model_loaded": generator is not None
    }

@app.post("/generate")
async def generate_recipe(recipe_request: RecipeRequest):
    if generator is None:
        raise HTTPException(
            status_code=503,
            detail="Recipe generator is not available. Please try again later."
        )
    
    try:
        logger.info(f"Generating recipe for: {recipe_request.ingredients}")
        recipe = generator.generate_recipe(
            ingredients=recipe_request.ingredients,
            category=recipe_request.category,
            cooking_time=recipe_request.cooking_time,
            difficulty=recipe_request.difficulty
        )
        return {
            "status": "success",
            "ingredients": recipe_request.ingredients,
            "recipe": recipe
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error in generate_recipe: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate recipe: {str(e)}"
        )

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
        workers=1
    )