class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration
    def __repr__(self):
        return f"FitnessCenter(client_code={self.client_code}, year={self.year}, month={self.month}, duration={self.duration})"

fitness_sessions = [
    FitnessCenter(client_code=1, year=2025, month=4, duration=60),
    FitnessCenter(client_code=2, year=2025, month=2, duration=45),
    FitnessCenter(client_code=3, year=2023, month=10, duration=37),
    FitnessCenter(client_code=4, year=2024, month=7, duration=90),
    FitnessCenter(client_code=5, year=2025, month=3, duration=56),
]
longest_session = max(fitness_sessions, key=lambda session: session.duration)
shortest_session = min(fitness_sessions, key=lambda session: session.duration)

print("Самое продолжительное занятие:")
print(f"Код клиента: {longest_session.client_code}, Год: {longest_session.year}, "
      f"Месяц: {longest_session.month}, Продолжительность: {longest_session.duration} минут")

print("\nСамое короткое занятие:")
print(f"Код клиента: {shortest_session.client_code}, Год: {shortest_session.year}, "
      f"Месяц: {shortest_session.month}, Продолжительность: {shortest_session.duration} минут")