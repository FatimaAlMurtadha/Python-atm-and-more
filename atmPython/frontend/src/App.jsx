import './App.css'
import { useState } from "react";
import WelcomeScreen from "./components/WelcomeScreen";

function App() {
  const [state, setState] = useState("IDLE");

  async function handleInsertCard() {
    const respons = await fetch("http://localhost:8000/insert_card", {
      method: "POST",
      headers: {
        body: JSON.stringify({ card_number: "1234-5678" })
      }
    });
    const data = await respons.json();
    console.log(data);
    setState(data.state);
  }

  return (
    <>
      {state === "IDLE" && <WelcomeScreen onInsert={handleInsertCard} />}
      {state === "CARD_INSERTED" && <h2>Card Inserted. Please enter your PIN.</h2>}
    </>
  )
}

export default App
