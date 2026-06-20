export type Problem = {
  id: string;
  name: string;
  difficulty: string;
  topic: string;
  pattern: string;
  status: string;
  link: string;
  created_at?: string;
};

type ProblemTableProps = {
  problems: Problem[];
  onDeleteProblem: (id: string) => void;
  onEditProblem: (problem: Problem) => void;
};

function getStatusClass(status: string) {
  return status.toLowerCase().replace(/\s+/g, "-");
}

function hasValidLink(link: string) {
  return link && link !== "Custom" && link.startsWith("http");
}

export default function ProblemTable({
  problems,
  onDeleteProblem,
  onEditProblem,
}: ProblemTableProps) {
  if (problems.length === 0) {
    return (
      <div className="empty-state">
        <p>No problems found.</p>
        <span>Try changing your search or filter settings.</span>
      </div>
    );
  }

  return (
    <div className="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Problem</th>
            <th>Difficulty</th>
            <th>Topic</th>
            <th>Pattern</th>
            <th>Status</th>
            <th>Link</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {problems.map((problem) => (
            <tr key={problem.id}>
              <td>{problem.name}</td>
              <td>{problem.difficulty}</td>
              <td>{problem.topic}</td>
              <td>{problem.pattern}</td>
              <td>
                <span className={`status ${getStatusClass(problem.status)}`}>
                  {problem.status}
                </span>
              </td>
              <td>
                {hasValidLink(problem.link) ? (
                  <a href={problem.link} target="_blank" rel="noreferrer">
                    Open
                  </a>
                ) : (
                  <span className="muted">Custom</span>
                )}
              </td>
              <td>
                <div className="table-actions">
                  <button
                    type="button"
                    className="edit-button"
                    onClick={() => onEditProblem(problem)}
                  >
                    Edit
                  </button>

                  <button
                    type="button"
                    className="delete-button"
                    onClick={() => onDeleteProblem(problem.id)}
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}