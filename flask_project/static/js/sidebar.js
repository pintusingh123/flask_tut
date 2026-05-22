 
      function toggleSidebar() {
        const sidebar = document.getElementById("sidebar");
        const overlay = document.getElementById("sidebarOverlay");

        sidebar.classList.toggle("translate-x-full");
        overlay.classList.toggle("hidden");
      }

      // Close sidebar when clicking on a link
      document.querySelectorAll("#sidebar a").forEach((link) => {
        link.addEventListener("click", function () {
          const sidebar = document.getElementById("sidebar");
          const overlay = document.getElementById("sidebarOverlay");

          if (window.innerWidth < 768) {
            sidebar.classList.add("translate-x-full");
            overlay.classList.add("hidden");
          }
        });
      });

      // Close sidebar on window resize
      window.addEventListener("resize", function () {
        const sidebar = document.getElementById("sidebar");
        const overlay = document.getElementById("sidebarOverlay");

        if (window.innerWidth >= 768) {
          sidebar.classList.remove("translate-x-full");
          overlay.classList.add("hidden");
        } else {
          sidebar.classList.add("translate-x-full");
        }
      });
    