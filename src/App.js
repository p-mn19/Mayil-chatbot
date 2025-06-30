import React, { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);

  const handleSend = async () => {
    if (!message.trim()) return;

    // Add user message
    setChatHistory((prev) => [...prev, { sender: "user", text: message }]);

    try {
      const res = await axios.post("http://localhost:5000/chat", {
        message,
      });

      // Handle bot response with multi-language reply
      if (res.data.en && res.data.ml && res.data.manglish) {
        const combinedText = `English: ${res.data.en}\nManglish: ${res.data.manglish}\nMalayalam: ${res.data.ml}`;
        setChatHistory((prev) => [...prev, { sender: "bot", text: combinedText }]);
      } else {
        // Fallback for basic string replies
        setChatHistory((prev) => [
          ...prev,
          { sender: "bot", text: res.data.reply || "Sorry, I didn't understand that." },
        ]);
      }
    } catch (error) {
      console.error("API error:", error);
      setChatHistory((prev) => [
        ...prev,
        { sender: "bot", text: "Something went wrong. Please try again." },
      ]);
    }

    setMessage("");
  };

  return (
    <div style={styles.appContainer}>
      <div style={styles.chatBox}>
        <h1 style={styles.title}>Mayil</h1>

        <div style={styles.chatDisplay}>
          {chatHistory.map((chat, i) => (
            <div
              key={i}
              style={chat.sender === "user" ? styles.userMessage : styles.botReply}
            >
              {chat.text.split("\n").map((line, j) => (
                <div key={j}>{line}</div>
              ))}
            </div>
          ))}
        </div>

        <div style={styles.inputContainer}>
          <input
            type="text"
            placeholder="Type your message..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            style={styles.inputField}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
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
    backgroundColor: "#1E1E2F",
    height: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    fontFamily: "'Poppins', sans-serif",
  },
  chatBox: {
    backgroundColor: "#292B40",
    borderRadius: "10px",
    boxShadow: "0px 5px 15px rgba(0, 0, 0, 0.3)",
    width: "400px",
    height: "600px",
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
    height: "80%",
    overflowY: "auto",
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
    whiteSpace: "pre-wrap",
  },
  botReply: {
    backgroundColor: "#51537B",
    color: "#FFFFFF",
    padding: "8px 12px",
    borderRadius: "10px",
    textAlign: "left",
    marginBottom: "8px",
    whiteSpace: "pre-wrap",
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
