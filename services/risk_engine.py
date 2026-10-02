def calculate_risk_level(score):

    if score < 10:
        return "Low"

    elif score < 20:
        return "Medium"

    elif score < 35:
        return "High"

    return "Critical"


def generate_recommendations(row):

    recommendations = []

    if row["account_public"] == 1:
        recommendations.append(
            "Consider switching your social media account to private."
        )

    if row["location_shared"] == 1:
        recommendations.append(
            "Avoid publicly sharing your precise or real-time location."
        )

    if row["phone_shared"] == 1:
        recommendations.append(
            "Remove your phone number from publicly visible profile information."
        )

    if row["email_shared"] == 1:
        recommendations.append(
            "Consider limiting public visibility of your personal email address."
        )

    if row["date_of_birth_shared"] == 1:
        recommendations.append(
            "Limit public visibility of your date of birth."
        )

    if row["workplace_shared"] == 1:
        recommendations.append(
            "Consider limiting publicly visible workplace information."
        )

    if row["education_shared"] == 1:
        recommendations.append(
            "Review whether your education information needs to be publicly visible."
        )

    if row["relationship_status_shared"] == 1:
        recommendations.append(
            "Consider limiting public visibility of relationship information."
        )

    if row["family_information_shared"] == 1:
        recommendations.append(
            "Avoid publicly exposing detailed information about family members."
        )

    if row["unknown_followers"] > 50:
        recommendations.append(
            "Review your followers and remove accounts you do not recognize."
        )

    if row["accepts_unknown_requests"] == 1:
        recommendations.append(
            "Avoid automatically accepting requests from unknown accounts."
        )

    if row["public_friend_list"] == 1:
        recommendations.append(
            "Consider hiding your public friend or follower list."
        )

    if row["public_interactions"] == 1:
        recommendations.append(
            "Review the visibility of your likes, comments and other interactions."
        )

    if row["location_posts"] == 1:
        recommendations.append(
            "Avoid regularly posting your current location."
        )

    if row["geotagging_enabled"] == 1:
        recommendations.append(
            "Consider disabling geotagging when sharing posts."
        )

    if row["travel_plans_shared"] == 1:
        recommendations.append(
            "Avoid publicly sharing detailed travel plans before or during a trip."
        )

    if row["sensitive_posts"] == 1:
        recommendations.append(
            "Review posts that contain sensitive personal information."
        )

    if row["photos_public"] == 1:
        recommendations.append(
            "Review who can view your personal photos."
        )

    if row["stories_public"] == 1:
        recommendations.append(
            "Review the audience for your temporary stories."
        )

    if row["external_links_shared"] == 1:
        recommendations.append(
            "Review external links before sharing them publicly."
        )

    if row["oversharing_personal_information"] == 1:
        recommendations.append(
            "Reduce unnecessary sharing of personal information."
        )

    if row["two_factor_auth"] == 0:
        recommendations.append(
            "Enable two-factor authentication for stronger account protection."
        )

    if row["login_alerts_enabled"] == 0:
        recommendations.append(
            "Enable login alerts so unexpected account access can be detected."
        )

    if row["password_reused"] == 1:
        recommendations.append(
            "Avoid reusing the same password across multiple services."
        )

    if row["unknown_login_detected"] == 1:
        recommendations.append(
            "Review recent login activity and secure the account if an unfamiliar login is present."
        )

    if row["third_party_apps"] > 3:
        recommendations.append(
            "Review and revoke unnecessary third-party application access."
        )

    if row["old_unused_apps"] == 1:
        recommendations.append(
            "Remove access for old or unused third-party applications."
        )

    if row["connects_social_account_to_other_apps"] == 1:
        recommendations.append(
            "Review permissions granted to applications connected to your social account."
        )

    if not recommendations:
        recommendations.append(
            "No major privacy concerns were detected from the provided answers."
        )

    return recommendations