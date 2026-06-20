"use client";

import { useEffect, useState } from "react";

import { updateProgressAfterSolvedProblem } from "../lib/progress";
import { supabase } from "../lib/supabase";
import { Problem } from "./ProblemTable";

type EditProblemModalProps = {
  problem: Problem | null;
  onClose: () => void;
  onProblemUpdated: () => void;
};

const defaultFormState = {
  name: "",
  difficulty: "Easy",
  topic: "",
  pattern: "",
  status: "Solved",
  link: "",
};

export default function EditProblemModal({
  problem,
  onClose,
  onProblemUpdated,
}: EditProblemModalProps) {
  const [formData, setFormData] = useState(defaultFormState);
  const [isSaving, setIsSaving] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    if (!problem) {
      setFormData(defaultFormState);
      setMessage("");
      return;
    }

    setFormData({
      name: problem.name ?? "",
      difficulty: problem.difficulty ?? "Easy",
      topic: problem.topic ?? "",
      pattern: problem.pattern ?? "",
      status: problem.status ?? "Solved",
      link: problem.link ?? "",
    });

    setMessage("");
  }, [problem]);

  if (!problem) {
    return null;
  }

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

    setIsSaving(true);

    const previousStatus = problem!.status;
    const nextStatus = formData.status;

    const { error } = await supabase
      .from("problems")
      .update({
        name: formData.name.trim(),
        difficulty: formData.difficulty,
        topic: formData.topic.trim(),
        pattern: formData.pattern.trim(),
        status: nextStatus,
        link: formData.link.trim() || "Custom",
      })
      .eq("id", problem!.id);

    if (error) {
      console.error("Update error:", error);
      setMessage("Something went wrong while updating the problem.");
      setIsSaving(false);
      return;
    }

    if (previousStatus !== "Solved" && nextStatus === "Solved") {
      await updateProgressAfterSolvedProblem();
    }

    setIsSaving(false);
    await onProblemUpdated();
    onClose();
  }

  return (
    <div className="modal-backdrop">
      <div className="modal-card">
        <div className="modal-header">
          <div>
            <p>Edit Problem</p>
            <h2>Update Problem Details</h2>
          </div>

          <button type="button" className="modal-close" onClick={onClose}>
            ×
          </button>
        </div>

        <form className="add-form" onSubmit={handleSubmit}>
          <div className="form-grid">
            <label>
              Problem Name
              <input
                value={formData.name}
                onChange={(event) => updateField("name", event.target.value)}
              />
            </label>

            <label>
              Difficulty
              <select
                value={formData.difficulty}
                onChange={(event) =>
                  updateField("difficulty", event.target.value)
                }
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
              />
            </label>

            <label>
              Pattern
              <input
                value={formData.pattern}
                onChange={(event) => updateField("pattern", event.target.value)}
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
              />
            </label>
          </div>

          <div className="form-actions">
            <button type="submit" disabled={isSaving}>
              {isSaving ? "Saving..." : "Save Changes"}
            </button>

            {message ? <span>{message}</span> : null}
          </div>
        </form>
      </div>
    </div>
  );
}