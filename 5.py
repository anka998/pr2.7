class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

fitness_sessions = [
    FitnessCenter(client_code=1, year=2021, month=10, duration=3600),
    FitnessCenter(client_code=2, year=2021, month=5, duration=4500),
    FitnessCenter(client_code=3, year=2025, month=2, duration=360),
    FitnessCenter(client_code=4, year=2022, month=9, duration=900),
    FitnessCenter(client_code=5, year=2023, month=6, duration=500),
    FitnessCenter(client_code=6, year=2024, month=3, duration=600),
    FitnessCenter(client_code=7, year=2023, month=7, duration=850),
    FitnessCenter(client_code=8, year=2022, month=1, duration=760),
    FitnessCenter(client_code=9, year=2023, month=4, duration=890),
    FitnessCenter(client_code=10, year=2021, month=12, duration=7200),
]
yearly_durations = {}

for session in fitness_sessions:
    if session.year in yearly_durations:
        yearly_durations[session.year] += session.duration
    else:
        yearly_durations[session.year] = session.duration

max_year = None
max_duration = 0

for year, total_duration in yearly_durations.items():
    if total_duration > max_duration or (total_duration == max_duration and (max_year is None or year < max_year)):
        max_year = year
        max_duration = total_duration

print(f"Год с наибольшей суммарной продолжительностью занятий: {max_year}")
print(f"Наибольшая суммарная продолжительность: {max_duration} минут")