async function loadDashboard() {

    try {

        const response = await fetch(
            "/api/dashboard/stats"
        );

        const data = await response.json();

        document.getElementById(
            "totalAssessments"
        ).textContent = data.total_assessments;

        document.getElementById(
            "averageScore"
        ).textContent = data.average_score;

        createRiskChart(
            data.risk_distribution
        );

    } catch (error) {

        console.error(
            "Dashboard error:",
            error
        );
    }
}


function createRiskChart(distribution) {

    const labels = distribution.map(
        item => item.risk_level
    );

    const values = distribution.map(
        item => item.count
    );

    const canvas =
        document.getElementById("riskChart");

    new Chart(canvas, {

        type: "doughnut",

        data: {
            labels: labels,

            datasets: [{
                label: "Assessments",
                data: values
            }]
        },

        options: {
            responsive: true
        }
    });
}


loadDashboard();