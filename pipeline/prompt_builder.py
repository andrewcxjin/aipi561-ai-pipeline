def build_prompt(city, duration):
    return(
        f"I am traveling to {city} for {duration} days."
        f"Please help me generate a packing list considering the city's current season, weather, and customs. "
    )