import ClipboardJS from "clipboard";

const copyIcon =
  '<svg xmlns="http://www.w3.org/2000/svg" height="24" width="24" viewBox="0 96 960 960" fill="currentColor" stroke="none" class="copy-icon h-[14px] w-[14px] transition-all transform scale-100 absolute"><path d="M200 976q-33 0-56.5-23.5T120 896V376q0-17 11.5-28.5T160 336q17 0 28.5 11.5T200 376v520h400q17 0 28.5 11.5T640 936q0 17-11.5 28.5T600 976H200Zm160-160q-33 0-56.5-23.5T280 736V256q0-33 23.5-56.5T360 176h360q33 0 56.5 23.5T800 256v480q0 33-23.5 56.5T720 816H360Zm0-80h360V256H360v480Zm0 0V256v480Z"/></svg>';
const successIcon =
  '<svg xmlns="http://www.w3.org/2000/svg" height="24" width="24" viewBox="0 96 960 960" fill="currentColor" stroke="none" class="copy-success-icon h-[14px] w-[14px] transition-all transform scale-0 absolute"><path d="M382 799q-8 0-15-2.5t-13-8.5L182 616q-11-11-10.5-28.5T183 559q11-11 28-11t28 11l143 143 339-339q11-11 28.5-11t28.5 11q11 11 11 28.5T778 420L410 788q-6 6-13 8.5t-15 2.5Z"/></svg>';
const btn = `<button class="copy z-20 inline-flex h-6 w-6 items-center justify-center rounded-md border border-border bg-background opacity-0 focus:opacity-100 text-sm font-medium transition-all hover:bg-muted absolute right-4 top-4 tooltipped tooltipped-n" data-tooltip="Copy code" type="button"><span class="sr-only">Copy code</span>${copyIcon}${successIcon}</button>`;

/** Add copy buttons to code blocks */
export function addCodeButtons() {
  const highlighted = document.querySelectorAll(".highlight, .literal-block");
  if (!highlighted) {
    return;
  }

  highlighted.forEach((item) => {
    const pre = item.querySelector("pre");
    if (pre) {
      pre.insertAdjacentHTML("beforeend", btn);
    } else {
      item.insertAdjacentHTML("beforeend", btn);
    }
  });

  const clipboard = new ClipboardJS("button.copy", {
    target: (trigger) => {
      return trigger.parentElement;
    },
  });

  clipboard.on("success", ({ trigger }) => {
    const tooltip = trigger.getAttribute("data-tooltip");
    const copyIcon = trigger.querySelector(".copy-icon");
    const successIcon = trigger.querySelector(".copy-success-icon");
    swapIcons(copyIcon, successIcon);
    trigger.setAttribute("data-tooltip", "Copied!");

    setTimeout(() => {
      swapIcons(successIcon, copyIcon);
      trigger.setAttribute("data-tooltip", tooltip);
    }, 2000);
  });
}

function swapIcons(first, second) {
  first.classList.remove("scale-100");
  second.classList.add("scale-100");
  first.classList.add("scale-0");
  second.classList.remove("scale-0");
}
