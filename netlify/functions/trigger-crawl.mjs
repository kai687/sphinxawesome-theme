export default {
  async deploySucceeded(event) {
    if (event.deploy.context !== "production") return;

    const response = await fetch(
      "https://api.github.com/repos/kai687/sphinxawesome-theme/dispatches",
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
          Accept: "application/vnd.github+json",
          "X-GitHub-Api-Version": "2022-11-28",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          event_type: "site_deployed",
          client_payload: {
            deploy_id: event.deploy.id,
            commit: event.deploy.commitRef,
          },
        }),
      },
    );

    if (!response.ok) {
      throw new Error(
        `GitHub dispatch failed: ${response.status} ${await response.text()}`,
      );
    }
  },
};
