"use client";

import { useEffect } from "react";

export default function ProfileModalController() {
  useEffect(() => {
    const profileThumb = document.getElementById("profileThumb");
    const imageModal = document.getElementById("imageModal");
    const modalCloseBtn = document.getElementById("modalCloseBtn");
    const imageModalOverlay = document.getElementById("imageModalOverlay");
    const imageModalPanel = document.getElementById("imageModalPanel");

    function openModal() {
      if (!imageModal) return;
      imageModal.classList.remove("hidden");
      
      // Trigger animation frame for CSS transitions
      requestAnimationFrame(() => {
        imageModalOverlay?.classList.remove("opacity-0");
        if (imageModalPanel) {
          imageModalPanel.classList.remove("opacity-0", "scale-95");
          imageModalPanel.classList.add("opacity-100", "scale-100");
        }
      });
      imageModal.setAttribute("aria-hidden", "false");
    }

    function closeModal() {
      if (!imageModal) return;
      imageModalOverlay?.classList.add("opacity-0");
      if (imageModalPanel) {
        imageModalPanel.classList.remove("opacity-100", "scale-100");
        imageModalPanel.classList.add("opacity-0", "scale-95");
      }
      
      setTimeout(() => {
        imageModal.classList.add("hidden");
        imageModal.setAttribute("aria-hidden", "true");
      }, 300); // match duration-300
    }

    profileThumb?.addEventListener("click", openModal);
    modalCloseBtn?.addEventListener("click", closeModal);
    imageModalOverlay?.addEventListener("click", closeModal);

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape" && imageModal?.getAttribute("aria-hidden") === "false") {
        closeModal();
      }
    };
    window.addEventListener("keydown", handleKeyDown);

    return () => {
      profileThumb?.removeEventListener("click", openModal);
      modalCloseBtn?.removeEventListener("click", closeModal);
      imageModalOverlay?.removeEventListener("click", closeModal);
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, []);

  return null;
}
