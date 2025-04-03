# Medical AI – Daily Free Doctor

This project provides an AI-based diagnostic system that:
- Scrapes data from sources (openFDA, ClinicalTrials.gov, Mayo Clinic, drugs.com, medlineplus, dailymed, webmd, Kaggle, and image sources).
- Builds a dataset covering disease overview, symptoms, and OTC drugs for common diseases.
- Trains a custom multimodal TensorFlow model (handling text and images) with cross-validation.
- Offers a chat-based interface with a REST API for diagnosis.
- Integrates diagnostic frameworks (ASMETHOD, ENCORE, SIT DOWN SIR) to guide the questioning process.
- Is containerized using Docker for deployment on GCP using a microservices architecture.

## Getting Started

### Prerequisites
- Python 3.9+
- Docker & docker-compose
- GCP account (for deployment; configure Kubernetes if scaling is needed)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/amoufaq5/medical-ai.git
   cd medical-ai
