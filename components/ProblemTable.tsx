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
};

function getStatusClass(status: string) {
  return status.toLowerCase().replace(/\s+/g, "-");
}

function hasValidLink(link: string) {
  return link && link !== "Custom" && link.startsWith("http");
}

export default function ProblemTable({ problems }: ProblemTableProps) {
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
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}