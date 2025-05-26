# AI Pipeline

This mini-project shows how AI workflows are orchestrated effectivelly to ensure reliable operations. The program generates a city-specific packing list using a local LLM via Ollama. The user will be prompted to enter the city they are traveling to and the duration in days. This will send a prompt to the LLM in the format: 

"I am traveling to {city} for {duration} days. Please help me generate a packing list considering the city's current season, weather, and customs."

The LLM will then generate a packing list. Logs containing previous responses will be saved for monitoring and retry mechanisms have also been implemented for reliability. 

## Architecture
![Architecture](architecture.jpg)

## Monitoring
The saved logs can be found in the logs folder where all errors and responses have been saved with time stamps. The monitoring folder contains a Jupyter notebook that reads from the logs and plots statistics. For example, I have plotted a bar chart showing the frequency of cities that have been prompted. Additionally, there is a pie chart that shows the percentage of successful and failed calls out of the total calls. 