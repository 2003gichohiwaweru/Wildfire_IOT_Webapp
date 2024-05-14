#include <HttpClient.h> // Include the HTTP client library

const char* INFLUXDB_URL = "http://localhost:8086/write?db=sensor_data"; // Replace with your details
// Optional: Set authorization credentials if needed
// const char* INFLUXDB_USER = "your_username";
// const char* INFLUXDB_PASSWORD = "your_password";

int soilMoisturePin = A1; // Analog pin for soil moisture sensor (adjust)
int pumpPin = 8; // Digital pin for pump control (adjust)

void setup() {
  Serial.begin(9600);
  pinMode(soilMoisturePin, INPUT);
  pinMode(pumpPin, OUTPUT);
  digitalWrite(pumpPin, LOW); // Start with pump off
}

void loop() {
  // Read sensor data
  float temperature = analogRead(A0) * 5.0 / 1023.0; // Example: Voltage reading (adjust for your sensor)
  float humidity = ...; // Read humidity sensor (replace with your code)
  int soilMoisture = analogRead(soilMoisturePin); // Read soil moisture (adjust for sensor scale)
  
  // Determine pump state based on current soil moisture level
  bool pumpStatus = isPumpNeeded(soilMoisture);
  digitalWrite(pumpPin, pumpStatus ? HIGH : LOW); // Control pump

  // Prepare data in InfluxDB Line Protocol format
  String data = "temperature,sensor_id=1 ";
  data += String(millis()); // Use millis() for an approximate timestamp
  data += " temperature=";
  data += temperature;
  data += ",humidity=";
  data += humidity;
  data += ",soil_moisture=";
  data += soilMoisture;
  data += ",pump_status=";
  data += pumpStatus ? "on" : "off";
  
  // Add moisture level category directly to data (adjust categories as needed)
  data += ",moisture_level=";
  if (soilMoisture < 20) {
    data += "low";
  } else if (soilMoisture >= 20.5 && soilMoisture <= 24.5) {
    data += "low"; // Adjust category based on your preference for "low" range
  } else if (soilMoisture >= 25.0 && soilMoisture <= 28.5) {
    data += "moderate";
  } else if (soilMoisture >= 29.0 && soil moisture <= 31.5) {
    data += "high";
  } else {
    data += "excess"; // Add a category for very high moisture levels
  }
  
  data += "\n";

  // Send data to InfluxDB
  HttpClient client;
  // Optional: Set authorization headers if needed
  // client.setAuthorization(INFLUXDB_USER, INFLUXDB_PASSWORD);
  int httpResponseCode = client.post(INFLUXDB_URL, data);
  
  if (httpResponseCode > 0) {
    Serial.println("Data sent successfully!");
  } else {
    Serial.print("Error sending data: ");
    Serial.println(httpResponseCode);
  }
  
  delay(5000); // Adjust delay based on data transmission frequency
}

bool isPumpNeeded(int moistureReading) {
  return (moistureReading < 20); // Turn pump on only if moisture is below 20
}
