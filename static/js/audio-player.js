document.querySelectorAll("[data-audio-player]").forEach((player) => {
    const audio = player.querySelector("[data-post-audio]");
    const speedControl = player.querySelector("[data-playback-speed]");

    if (!audio || !speedControl) {
        return;
    }

    speedControl.addEventListener("change", () => {
        const playbackRate = Number.parseFloat(speedControl.value);

        if (Number.isFinite(playbackRate)) {
            audio.defaultPlaybackRate = playbackRate;
            audio.playbackRate = playbackRate;
        }
    });
});
