# movie-recommendation-system
A content-based movie recommendation system that suggests movies based on the similarity of their features, such as genre, cast, and plot description.

📌 Features
Movie Recommendations: Suggests movies similar to a selected movie.

Search Functionality: Allows users to search for movies by title.

Genre Filtering: Filters movies based on selected genres.

Movie Details: Provides detailed information about each movie, including cast, release date, and overview.

User Interface: Interactive and user-friendly interface built with Streamlit.

🛠️ Tech Stack
Frontend: Streamlit

Backend: Python

Libraries:

pandas: Data manipulation and analysis

scikit-learn: Machine learning algorithms
🚀 How to Set Up and Run This Project
Follow these steps to set up and run the movie recommendation system on your local machine or in Google Colab.

🖥️ Option A: Run Locally (on your PC)
1. Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
2. Install required dependencies:
bash
Copy code
pip install -r requirements.txt
If requirements.txt is missing, install manually:

bash
Copy code
pip install pandas numpy scikit-learn streamlit requests
3. Add or download the dataset:
Place your dataset (e.g., movies.csv, movies_metadata.csv, etc.) into the root folder of the project.

You can use the TMDB 5000 Movie Dataset or any similar dataset.

4. Run the Streamlit app:
bash
Copy code
streamlit run app.py
Then open http://localhost:8501 in your browser.

💻 Option B: Run in Google Colab (with ngrok)
1. Upload your files:
Upload app.py, movies.csv, and any necessary files using the Colab file upload tool.

2. Install Streamlit and ngrok:
python
Copy code
!pip install streamlit pyngrok
3. Authenticate with ngrok (once per session):
python
Copy code
!ngrok config add-authtoken YOUR_NGROK_TOKEN
Get your token from: https://dashboard.ngrok.com/get-started/your-authtoken

4. Start the app and tunnel:
python
Copy code
from pyngrok import ngrok
import threading
import os

# Start tunnel
public_url = ngrok.connect(8501)
print("🌐 Public URL:", public_url)

# Run Streamlit
def run():
    os.system('streamlit run app.py')

threading.Thread(target=run).start()
📦 Dependencies
The app relies on the following Python libraries:

Library	Purpose
pandas	Data loading and manipulation
numpy	Numerical operations
scikit-learn	For computing cosine similarity
streamlit	Web app framework
requests	(Optional) To fetch poster images via API
pyngrok	(Only in Colab) Tunnel to localhost
requirements.txt Example:
nginx
Copy code
pandas
numpy
scikit-learn
streamlit
requests
pyngrok

requests: HTTP requests for API calls

numpy: Numerical computing

Dataset: TMDB 5000 Movie Dataset
