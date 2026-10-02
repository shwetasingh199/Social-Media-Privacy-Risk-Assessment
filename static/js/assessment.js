const form = document.getElementById("assessmentForm");
const resultContainer = document.getElementById("result");

form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const formData = new FormData(form);

    const data = {};

    for (const [key, value] of formData.entries()) {
        data[key] = value;
    }

    resultContainer.innerHTML = `
        <div class="loading">
            Analyzing privacy exposure...
        </div>
    `;

    try {

        const response = await fetch(
            "/api/assessment",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        );

        const result = await response.json();

        if (!response.ok) {
            throw new Error(
                result.error || "Assessment failed."
            );
        }

        displayResult(result);

    } catch (error) {

        resultContainer.innerHTML = `
            <div class="error">
                ${escapeHtml(error.message)}
            </div>
        `;
    }
});


function displayResult(result) {

    const findings = result.findings || [];

    const recommendations =
        result.recommendations || [];

    resultContainer.innerHTML = `

        <section class="result-card">

            <div class="result-header">

                <div>

                    <p class="muted">
                        Overall Privacy Risk
                    </p>

                    <div class="score">
                        ${result.overall_score}
                    </div>

                </div>

                <div class="risk-badge">
                    ${result.risk_level}
                </div>

            </div>

            <h2>Top Findings</h2>

            <ul class="finding-list">

                ${findings.slice(0, 5).map(
                    finding => `
                    <li>
                        <strong>
                            ${escapeHtml(
                                finding.finding_type
                            )}
                        </strong>

                        <br>

                        ${escapeHtml(
                            finding.description
                        )}
                    </li>
                    `
                ).join("")}

            </ul>

            <h2>Recommendations</h2>

            <ul class="recommendation-list">

                ${recommendations.slice(0, 5).map(
                    item => `
                    <li>
                        <strong>
                            ${escapeHtml(
                                item.priority
                            )}
                        </strong>

                        <br>

                        ${escapeHtml(
                            item.recommendation
                        )}
                    </li>
                    `
                ).join("")}

            </ul>

            <div class="result-actions">

                <a
                    class="button primary"
                    href="${result.report_url}">
                    Open Privacy Report
                </a>

                <a
                    class="button secondary"
                    href="/dashboard">
                    Dashboard
                </a>

            </div>

        </section>
    `;
}


function escapeHtml(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}