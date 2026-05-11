export const handler = async () => {
  const res = await fetch(
    "https://api.github.com/repos/kai687/sphinxawesome-theme/dispatches",
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
        Accept: "application/vnd.github+json",
      },
      body: JSON.stringify({ event_type: "site_deployed" }),
    }
  );

  if (!res.ok) {
    console.error("GitHub dispatch failed:", res.status, await res.text());
    return { statusCode: 500 };
  }

  return { statusCode: 200 };
};
