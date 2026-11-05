"use strict";

const printResumeButton = document.getElementById("print-resume");
if (printResumeButton) {
  printResumeButton.hidden = false;
  printResumeButton.addEventListener("click", () => window.print());
}
