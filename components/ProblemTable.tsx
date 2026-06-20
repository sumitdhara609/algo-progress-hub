export type Problem = {
  id?: string;
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

export default function ProblemTable({ problems }: ProblemTableProps) {
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
            <tr key={problem.id ?? problem.name}>
              <td>{problem.name}</td>
              <td>{problem.difficulty}</td>
              <td>{problem.topic}</td>
              <td>{problem.pattern}</td>
              <td>
                <span className={`status ${problem.status.toLowerCase()}`}>
                  {problem.status}
                </span>
              </td>
              <td>
                {problem.link === "Custom" ? (
                  <span className="muted">Custom</span>
                ) : (
                  <a href={problem.link} target="_blank">
                    Open
                  </a>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}