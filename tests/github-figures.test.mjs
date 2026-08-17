import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readdirSync } from "node:fs";
import { readFileSync } from "node:fs";
import test from "node:test";

test("build renders the live GitHub figures immediately after Projects", () => {
    execFileSync("bun", ["run", "build"], { stdio: "pipe" });

    const page = readFileSync("dist/index.html", "utf8");
    const projects = page.indexOf("Projects");
    const figures = page.indexOf('id="github-figures"');

    assert.ok(figures > projects, "GitHub figures should follow Projects");
    assert.match(
        page,
        /id="github-stars" aria-live="polite"[^>]*>\s*58/,
        "Star count should remain visible when GitHub's unauthenticated API is rate-limited",
    );
    assert.match(page, /id="github-contributions"/);

    const css = readdirSync("dist/_astro")
        .filter((file) => file.endsWith(".css"))
        .map((file) => readFileSync(`dist/_astro/${file}`, "utf8"))
        .join("\n");
    assert.match(
        css,
        /grid-template-rows:repeat\(19,minmax\(0,1fr\)\)/,
        "Contribution activity should use the reference's dense near-square grid",
    );
    assert.match(
        css,
        /height:clamp\(12rem,24vw,16rem\)/,
        "Figures should stay compact instead of dominating the portfolio",
    );
});
