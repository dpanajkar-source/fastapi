import logging
from datetime import datetime
from fastapi import HTTPException
from app.models.request import AdditionRequest
from app.models.response import AdditionResponse
from app.utils.multiprocessing import add_lists

# Configure logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def process_addition(request: AdditionRequest) -> AdditionResponse:
    try:
        logging.info(f"Received batch ID {request.batchid} with payload: {request.payload}")
        started_at = datetime.utcnow()
        
        result = add_lists(request.payload)
        
        completed_at = datetime.utcnow()
        response = AdditionResponse(
            batchid=request.batchid,
            response=result,
            status="complete",
            started_at=started_at,
            completed_at=completed_at
        )
        
        logging.info(f"Completed processing batch ID {request.batchid} with result: {response.response}")
        return response
    except Exception as e:
        logging.error(f"Error processing batch ID {request.batchid}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
