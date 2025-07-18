# LinkedIn Profile Analyzer

A sophisticated AI-powered web application that automatically finds LinkedIn profiles and generates intelligent summaries using LangChain and OpenAI GPT models.

## 🎯 Features

- **Smart Profile Search**: Automatically searches for LinkedIn profiles using person's name and additional details
- **AI-Powered Analysis**: Generates comprehensive summaries and interesting facts about profiles
- **Caching System**: Intelligent caching to reduce API calls and improve performance
- **Web Interface**: Clean, responsive web interface for easy interaction
- **Profile Image Extraction**: Retrieves and displays profile images
- **Error Handling**: Robust error handling and user feedback

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **AI Framework**: LangChain with OpenAI GPT-4o-mini
- **Web Search**: Tavily API for LinkedIn profile discovery
- **Profile Scraping**: RapidAPI for LinkedIn data extraction
- **Data Validation**: Pydantic for structured data handling
- **Frontend**: HTML/CSS/JavaScript with modern styling

## 📋 Prerequisites

Before running this project, you need to obtain API keys from:

1. **OpenAI API**: Get your API key from [OpenAI Platform](https://platform.openai.com/)
2. **Tavily API**: Sign up at [Tavily](https://tavily.com/) for web search capabilities
3. **RapidAPI**: Get LinkedIn scraping access from [RapidAPI LinkedIn Data Service](https://rapidapi.com/)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/LinkedlnAgent.git
   cd LinkedlnAgent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   RAPIDAPI_KEY=your_rapidapi_key_here
   ```

## 🎮 Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   
   Navigate to `http://localhost:5000`

3. **Search for profiles**
   - Enter the person's full name
   - Add additional details (company, location, etc.) to help identify the right person
   - Click "Analyze Profile"

4. **View results**
   - AI-generated summary of the person's professional background
   - Interesting facts about their career and achievements
   - Profile image (if available)

## 📁 Project Structure

```
LinkedlnAgent/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                      # Project documentation
├── .env                           # Environment variables (create this)
├── agents/                        # AI agent modules
│   ├── linkedin_lookup_agent.py   # Profile search agent
│   └── linkedin_summary_agent.py  # Summary generation agent
├── services/                      # Core services
│   ├── linkedin_scraper.py        # LinkedIn data scraping
│   └── output_parser.py           # Data parsing and validation
├── tools/                         # Utility tools
│   ├── __init__.py
│   └── tools.py                   # Web search tools
├── templates/                     # HTML templates
│   └── index.html                 # Web interface
└── cache/                         # Caching directory
    ├── linkedin_profile_cache.json
    └── linkedin_tavily_cache.json
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT models | Yes |
| `TAVILY_API_KEY` | Tavily API key for web search | Yes |
| `RAPIDAPI_KEY` | RapidAPI key for LinkedIn scraping | Yes |

### Caching

The application uses intelligent caching to:
- Store LinkedIn profile search results
- Cache scraped profile data
- Reduce API usage and costs
- Improve response times

## 🤖 How It Works

1. **Profile Discovery**: Uses Tavily API to search for LinkedIn profiles based on name and details
2. **Data Extraction**: Scrapes public LinkedIn data using RapidAPI
3. **AI Analysis**: Processes the data through LangChain agents with OpenAI GPT-4o-mini
4. **Summary Generation**: Creates structured summaries with interesting facts
5. **Web Display**: Presents results through a clean web interface

## 🎯 API Endpoints

- `GET /` - Main web interface
- `POST /search` - Profile analysis endpoint
  ```json
  {
    "name": "John Doe",
    "details": "Software Engineer at Google"
  }
  ```

## 🛡️ Error Handling

The application includes comprehensive error handling for:
- Invalid or missing API keys
- Network connectivity issues
- Profile not found scenarios
- API rate limiting
- Invalid input data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the AI framework
- [OpenAI](https://openai.com/) for GPT models
- [Tavily](https://tavily.com/) for web search capabilities
- [RapidAPI](https://rapidapi.com/) for LinkedIn data access

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/your-username/LinkedlnAgent/issues) page
2. Create a new issue with detailed information
3. Contact the maintainer

---

**Note**: This tool is for educational and professional networking purposes. Please respect LinkedIn's terms of service and data privacy regulations.
