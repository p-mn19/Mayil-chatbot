import React, { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]); // Store chat history

  const handleSend = async () => {
    if (!message) return; // Prevent empty messages
    // Add user message to chat history
    setChatHistory((prev) => [...prev, { sender: "user", text: message }]);

    try {
      // Send user message to the backend
      const response = await axios.post("http://localhost:5000/chat", {
        message,
      });

      // Add bot reply to chat history
      setChatHistory((prev) => [
        ...prev,
        { sender: "bot", text: response.data.reply },
      ]);
    } catch (error) {
      console.error("Error sending message:", error);
      setChatHistory((prev) => [
        ...prev,
        { sender: "bot", text: "Something went wrong. Please try again." },
      ]);
    }

    setMessage(""); // Clear input field
  };

  return (
    <div style={styles.appContainer}>
      <div style={styles.chatBox}>
        {/* Title */}
        <h1 style={styles.title}>Mayil</h1>

        {/* Chat History */}
        <div style={styles.chatDisplay}>
          {chatHistory.map((chat, index) => (
            <div
              key={index}
              style={
                chat.sender === "user" ? styles.userMessage : styles.botReply
              }
            >
              {chat.text}
            </div>
          ))}
        </div>

        {/* Input and Send Button */}
        <div style={styles.inputContainer}>
          <input
            type="text"
            placeholder="Type your message..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            style={styles.inputField}
          />
          <button onClick={handleSend} style={styles.sendButton}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

const styles = {
  appContainer: {
    backgroundColor: "#1E1E2F", // Dark background
    height: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    fontFamily: "'Poppins', sans-serif",
  },
  chatBox: {
    backgroundColor: "#292B40", // Chatbox background
    borderRadius: "10px",
    boxShadow: "0px 5px 15px rgba(0, 0, 0, 0.3)",
    width: "400px",
    height: "600px", // Set a fixed height
    padding: "20px",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  title: {
    fontSize: "24px",
    color: "#FFFFFF",
    marginBottom: "20px",
  },
  chatDisplay: {
    backgroundColor: "#202233",
    borderRadius: "8px",
    width: "100%",
    height: "80%", // Take up most of the chatbox height
    overflowY: "auto", // Enable scrolling
    padding: "10px",
    color: "#A6A6A6",
    marginBottom: "20px",
  },
  userMessage: {
    backgroundColor: "#4C5F8A",
    color: "#FFFFFF",
    padding: "8px 12px",
    borderRadius: "10px",
    textAlign: "right",
    marginBottom: "8px",
    wordWrap: "break-word",
  },
  botReply: {
    backgroundColor: "#51537B",
    color: "#FFFFFF",
    padding: "8px 12px",
    borderRadius: "10px",
    textAlign: "left",
    marginBottom: "8px",
    wordWrap: "break-word",
  },
  inputContainer: {
    display: "flex",
    width: "100%",
  },
  inputField: {
    flex: 1,
    padding: "10px",
    borderRadius: "8px 0 0 8px",
    border: "none",
    outline: "none",
    fontSize: "16px",
  },
  sendButton: {
    backgroundColor: "#6C63FF",
    color: "#FFFFFF",
    border: "none",
    padding: "10px 20px",
    borderRadius: "0 8px 8px 0",
    cursor: "pointer",
    fontSize: "16px",
    fontWeight: "bold",
  },
};

export default App;

