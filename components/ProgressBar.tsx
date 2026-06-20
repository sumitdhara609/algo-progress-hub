type ProgressBarProps = {
  label: string;
  value: number;
};

export default function ProgressBar({ label, value }: ProgressBarProps) {
  const safeValue = Math.max(0, Math.min(100, value));

  return (
    <div className="progress-block">
      <div className="progress-row">
        <span>{label}</span>
        <strong>{safeValue.toFixed(1)}%</strong>
      </div>

      <div className="progress-track">
        <div className="progress-fill" style={{ width: `${safeValue}%` }} />
      </div>
    </div>
  );
}