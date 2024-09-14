# DABSTER (Database-Augmented Boosted System for Tracking, Engaging, and Retrieving)

DABSTER is a prototype system designed to demonstrate the implementation of RAG (Retrieval-Augmented Generation), graph RAG, and agent memory (both short-term and long-term) using a microservices architecture. This system serves as a foundation for the transition of ADAPT-CamelDEV to a microservices architecture.

## Project Structure

```
DABSTER/
├── src/
│   ├── rag_service/
│   │   └── rag_service.py
│   ├── graph_rag_service/
│   │   └── graph_rag_service.py
│   ├── agent_memory_service/
│   │   └── agent_memory_service.py
│   ├── api_gateway/
│   │   └── api_gateway.py
│   ├── config/
│   │   └── database.py
│   └── models/
│       └── postgres_models.py
├── tests/
├── main.py
├── requirements.txt
├── README.md
├── DATA_DBs.md
└── start_dabster.sh
```

## Setup and Running

Please refer to the main ADAPT-CamelDEV documentation for setup and running instructions. DABSTER is now being integrated into the main ADAPT-CamelDEV project as part of its microservices architecture.

## API Endpoints

The API endpoints implemented in DABSTER serve as prototypes for the microservices in ADAPT-CamelDEV. For the most up-to-date API documentation, please refer to the main ADAPT-CamelDEV project documentation.

## Next Steps

DABSTER is being refactored and integrated into the ADAPT-CamelDEV project. Future development will occur within the main ADAPT-CamelDEV repository. Please refer to the Project-Progress/ADAPT-CamelDEV.md file for the latest updates and next steps.

## Contributing

Please read the contributing guidelines in the main ADAPT-CamelDEV project before submitting pull requests.

## License

[MIT License](LICENSE)