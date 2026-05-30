from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from collections import deque

app = FastAPI()

# 1. The CORS Bypass 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rpm_history = deque(maxlen=10)

# 2. Your original test route
@app.get("/")
def home():
    return {"message": "Server is running"}

# 3. The Live Sensor Route
@app.get("/api/data")
def get_sensor_data():
    # Because this is INSIDE the function, a new number generates on every refresh!
    current_rpm = random.randint(900, 1200)
   # 2. Push it into our sliding window queue
    rpm_history.append(current_rpm)
    
    # 3. Calculate the moving average of the current window
    moving_avg = sum(rpm_history) / len(rpm_history)
    
    # 4. Return the complete payload
    return {
        "rpm_raw": current_rpm, 
        "rpm_avg": round(moving_avg, 2),
        "window_size": len(rpm_history)
    }