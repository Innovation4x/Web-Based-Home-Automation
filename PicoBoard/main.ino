#include <SPI.h>
#include <EthernetClient.h>
#include <Ethernet.h>
#include <PubSubClient.h>

// HI METH
int ledpin=LED_BUILTIN;
// Update these with values suitable for your network.
byte mac[]    = {  0xAF, 0xED, 0xBF, 0xFE, 0xFE, 0x00 };
IPAddress ip(172, 16, 255, 101);
IPAddress myDns(192, 168, 0, 100);

IPAddress server(10,5,15,103); 
//char server [] ="broker.hivemq.com";
EthernetClient ethClient;
PubSubClient client(ethClient);


void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  char messageBuffer[30];
  memcpy(messageBuffer, payload, length);
  messageBuffer[length] = '\0';

  Serial.println(messageBuffer);
  char message[3];
  for (int i=0;i<length;i++) {
    message[i] = payload[i];
    Serial.print((char)payload[i]);
  }

  String msg = String(message);
  int command = msg.toInt();
  int pinNum = command/10;
  int val = command % 10;
  digitalWrite(pinNum, val);

  Serial.println();

  /*

  First two digit = pinNum
  last digit = on or off
  

 */

}



void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("arduinoClient")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("tTopic","12th April 2022 MQTT test");
      // ... and resubscribe
      client.subscribe("led");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup()
{

  // SETUP ALL pins as output
  for(int i = 1; i < 29; i += 1){
    pinMode(i, OUTPUT);
  }




  Ethernet.init(17);  // WIZnet W5100S-EVB-Pico
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

    Serial.println("Initialize Ethernet with DHCP:");
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    // Check for Ethernet hardware present
    if (Ethernet.hardwareStatus() == EthernetNoHardware) {
      Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
      while (true) {
        delay(1); // do nothing, no point running without Ethernet hardware
      }
    }
    if (Ethernet.linkStatus() == LinkOFF) {
      Serial.println("Ethernet cable is not connected.");
    }
    // try to congifure using IP address instead of DHCP:
    Ethernet.begin(mac, ip, myDns);
  } else {
    Serial.print("  DHCP assigned IP ");
    Serial.println(Ethernet.localIP());
  }
  // give the Ethernet shield a second to initialize:
  delay(1000);
  Serial.print("connecting to ");
  Serial.print(server);
  Serial.println("...");

  client.setClient(ethClient);
  client.setServer(server, 1883);
  client.setCallback(callback);
  // Allow the hardware to sort itself out
  delay(1500);
  
  pinMode(ledpin, OUTPUT);

}

void loop()
{
  client.publish("tTopic","12th April 2022 MQTT test main loop");
  delay(1000);
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
