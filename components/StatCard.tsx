type StatCardProps = {
  label: string;
  value: string | number;
  note?: string;
};

export default function StatCard({ label, value, note }: StatCardProps) {
  return (
    <div className="stat-card">
      <p className="stat-label">{label}</p>
      <h2 className="stat-value">{value}</h2>
      {note ? <p className="stat-note">{note}</p> : null}
    </div>
  );
}