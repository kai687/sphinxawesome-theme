const SITE_ORIGIN = "https://sphinxawesome-theme.netlify.app";

const getHeader = (headers, name) => {
  const lowerName = name.toLowerCase();
  const entry = Object.entries(headers ?? {}).find(
    ([key]) => key.toLowerCase() === lowerName
  );

  return entry?.[1];
};

const isAllowedReferrer = (referrer) => {
  if (!referrer) {
    return false;
  }

  try {
    return new URL(referrer).origin === SITE_ORIGIN;
  } catch {
    return false;
  }
};

export const handler = async (event) => {
  const origin = getHeader(event.headers, "origin");
  const referrer = getHeader(event.headers, "referer");
  const forwardedFor = getHeader(event.headers, "x-forwarded-for");
  const callerIp = forwardedFor?.split(",")[0]?.trim() ?? "unknown";
  const userAgent = getHeader(event.headers, "user-agent") ?? "unknown";

  console.info("trigger-crawl request", {
    callerIp,
    userAgent,
  });

  if (origin !== SITE_ORIGIN || !isAllowedReferrer(referrer)) {
    return { statusCode: 403 };
  }

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
