import "../sass/WelcomeScreen.scss";

export default function WelcomeScreen({ onInsert }) {
  return (
    <section className="welcome-screen">
      <h1>ATM Machine</h1>
      <button onClick={onInsert}>Insert Card</button>
    </section>
  );
}