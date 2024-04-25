# Import required modules
express = require('express')
dotenv = require('dotenv')
axios = require('axios')

# Load environment variables from .env file
dotenv.config()

# Create Express app
app = express()

# Set up middleware to parse JSON and URL-encoded bodies
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

# Define route to serve the HTML page
app.get('/', (req, res) ->
  res.sendFile(`${__dirname}/index.html`)
)

# Define route to handle form submission
app.post('/weather', (req, res) ->
  city = req.body.city
  apiKey = process.env.OPENWEATHER_API_KEY

  # Make API call to OpenWeather to get weather data for the input city
  axios.get(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`)
    .then((response) ->
      weather = response.data.weather[0].description
      res.send(`The weather in ${city} is ${weather}`)
    )
    .catch((error) ->
      res.status(500).send('Error fetching weather data')
    )
)

# Start the server
port = process.env.PORT || 3000
app.listen(port, () ->
  console.log(`Server is running on port ${port}`)
)
