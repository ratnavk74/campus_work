def calculate_usage_score(number_of_users, usage_hours):
    """
    Calculate usage score based on number of users and hours.
    """
    return number_of_users * usage_hours


def classify_utilization(usage_score):
    """
    Classify utilization level based on usage score.
    """
    if usage_score >= 90:
        return "Over-Utilized Resource"
    elif 50 <= usage_score <= 89:
        return "Optimally Utilized Resource"
    else:
        return "Under-Utilized Resource"


def main():
    # Static data (no user input)
    facility_name = "Central Library"
    resource_type = "Library"
    number_of_users = 10
    usage_hours = 6

    usage_score = calculate_usage_score(number_of_users, usage_hours)
    status = classify_utilization(usage_score)

    print("=== Smart Campus Resource Utilization System ===")
    print(f"Facility Name: {facility_name}")
    print(f"Resource Type: {resource_type}")
    print(f"Number of Users: {number_of_users}")
    print(f"Usage Hours per Day: {usage_hours}")
    print(f"Usage Score: {usage_score}")
    print(f"Utilization Status: {status}")


if __name__ == "__main__":
    main()
