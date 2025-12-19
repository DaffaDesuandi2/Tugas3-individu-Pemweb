import { useState } from "react";
import { createReview } from "../api/reviewApi";

function ReviewForm({ onNewReview }) {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);

    const result = await createReview(text);
    onNewReview(result);

    setText("");
    setLoading(false);
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Input Review</h2>

      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        required
        rows={4}
      />

      <button type="submit" disabled={loading}>
        {loading ? "Processing..." : "Submit"}
      </button>
    </form>
  );
}

export default ReviewForm;
