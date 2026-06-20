"use client";

import { useState } from "react";

import { updateProgressAfterSolvedProblem } from "../lib/progress";
import { supabase } from "../lib/supabase";

type AddProblemFormProps = {
  onProblemAdded: () => void;
};

const initialFormState = {
  name: "",
  difficulty: "Easy",
  topic: "",
  pattern: "",
  status: "Solved",
  link: "",
};

export default function AddProblemForm({ onProblemAdded }: AddProblemFormProps) {
  const [formData, setFormData] = useState(initialFormState);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [message, setMessage] = useState("");

  function updateField(field: string, value: string) {
    setFormData((current) => ({
      ...current,
      [field]: value,
    }));
  }

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setMessage("");

    if (!formData.name.trim()) {
      setMessage("Problem name is required.");
      return;
    }

    if (!formData.topic.trim()) {
      setMessage("Topic is required.");
      return;
    }

    if (!formData.pattern.trim()) {
      setMessage("Pattern is required.");
      return;
    }

    setIsSubmitting(true);

    const { error } = await supabase.from("problems").insert({
      name: formData.name.trim(),
      difficulty: formData.difficulty,
      topic: formData.topic.trim(),
      pattern: formData.pattern.trim(),
      status: formData.status,
      link: formData.link.trim() || "Custom",
    });

    if (error) {
      console.error("Insert error:", error);
      setMessage("Something went wrong while adding the problem.");
      setIsSubmitting(false);
      return;
    }

    if (formData.status === "Solved") {
      await updateProgressAfterSolvedProblem();
    }

    setFormData(initialFormState);
    setMessage("Problem added successfully.");
    setIsSubmitting(false);

    await onProblemAdded();
  }

  return (
    <form className="add-form" onSubmit={handleSubmit}>
      <div className="section-heading">
        <p>Add Problem</p>
        <h2>Track a New Problem</h2>
      </div>

      <div className="form-grid">
        <label>
          Problem Name
          <input
            value={formData.name}
            onChange={(event) => updateField("name", event.target.value)}
            placeholder="Two Sum"
          />
        </label>

        <label>
          Difficulty
          <select
            value={formData.difficulty}
            onChange={(event) => updateField("difficulty", event.target.value)}
          >
            <option>Easy</option>
            <option>Medium</option>
            <option>Hard</option>
          </select>
        </label>

        <label>
          Topic
          <input
            value={formData.topic}
            onChange={(event) => updateField("topic", event.target.value)}
            placeholder="Array"
          />
        </label>

        <label>
          Pattern
          <input
            value={formData.pattern}
            onChange={(event) => updateField("pattern", event.target.value)}
            placeholder="Hashing"
          />
        </label>

        <label>
          Status
          <select
            value={formData.status}
            onChange={(event) => updateField("status", event.target.value)}
          >
            <option>Solved</option>
            <option>Revision</option>
            <option>Unsolved</option>
          </select>
        </label>

        <label>
          Problem Link
          <input
            value={formData.link}
            onChange={(event) => updateField("link", event.target.value)}
            placeholder="https://leetcode.com/problems/two-sum/"
          />
        </label>
      </div>

      <div className="form-actions">
        <button type="submit" disabled={isSubmitting}>
          {isSubmitting ? "Adding..." : "Add Problem"}
        </button>

        {message ? <span>{message}</span> : null}
      </div>
    </form>
  );
}