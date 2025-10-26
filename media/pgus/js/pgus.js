// Wait for DOM to be ready before running navigation code
document.addEventListener("DOMContentLoaded", function() {
  // add classes for mobile navigation toggling
  var CSbody = document.querySelector("body");
  const CSnavbarMenu = document.querySelector("#cs-navigation");
  const CShamburgerMenu = document.querySelector("#cs-navigation .cs-toggle");

  // Check if navigation elements exist before adding event listeners
  if (CShamburgerMenu && CSnavbarMenu && CSbody) {
    CShamburgerMenu.addEventListener("click", function () {
      CShamburgerMenu.classList.toggle("cs-active");
      CSnavbarMenu.classList.toggle("cs-active");
      CSbody.classList.toggle("cs-open");
      // run the function to check the aria-expanded value
      ariaExpanded();
    });
  }

  // checks the value of aria expanded on the cs-ul and changes it accordingly whether it is expanded or not
  function ariaExpanded() {
    const csUL = document.querySelector("#cs-expanded");
    if (csUL) {
      const csExpanded = csUL.getAttribute("aria-expanded");

      if (csExpanded === "false") {
        csUL.setAttribute("aria-expanded", "true");
      } else {
        csUL.setAttribute("aria-expanded", "false");
      }
    }
  }

  // mobile nav toggle code
  const dropDowns = Array.from(
    document.querySelectorAll("#cs-navigation .cs-dropdown")
  );
  for (const item of dropDowns) {
    const onClick = () => {
      item.classList.toggle("cs-active");
    };
    item.addEventListener("click", onClick);
  }
});
