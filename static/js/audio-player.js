document.querySelectorAll("[data-audio-player]").forEach((player) => {
    const audio = player.querySelector("[data-post-audio]");
    const controls = player.querySelector("[data-audio-controls]");
    const toggle = player.querySelector("[data-audio-toggle]");
    const seek = player.querySelector("[data-audio-seek]");
    const progress = player.querySelector("[data-audio-progress]");
    const currentTime = player.querySelector("[data-audio-current]");
    const duration = player.querySelector("[data-audio-duration]");
    const rate = player.querySelector("[data-playback-rate]");
    const status = player.querySelector("[data-audio-status]");

    if (
        !audio ||
        !controls ||
        !toggle ||
        !seek ||
        !progress ||
        !currentTime ||
        !duration ||
        !rate ||
        !status
    ) {
        return;
    }

    const playbackRates = [1, 1.25, 1.5, 2, 0.75];
    let rateIndex = 0;
    let hasRestoredState = false;
    let lastSavedSecond = -1;
    const source = audio.querySelector("source")?.getAttribute("src") || window.location.pathname;
    const storageKey = `post-audio:${window.location.pathname}:${source}`;

    const formatTime = (seconds) => {
        if (!Number.isFinite(seconds)) {
            return "--:--";
        }

        const wholeSeconds = Math.max(0, Math.floor(seconds));
        const hours = Math.floor(wholeSeconds / 3600);
        const minutes = Math.floor((wholeSeconds % 3600) / 60);
        const remainingSeconds = String(wholeSeconds % 60).padStart(2, "0");

        if (hours > 0) {
            return `${hours}:${String(minutes).padStart(2, "0")}:${remainingSeconds}`;
        }

        return `${minutes}:${remainingSeconds}`;
    };

    const updateTimeline = () => {
        const audioDuration = Number.isFinite(audio.duration) ? audio.duration : 0;
        const played = audioDuration > 0 ? (audio.currentTime / audioDuration) * 100 : 0;
        const elapsedLabel = formatTime(audio.currentTime);
        const durationLabel = formatTime(audio.duration);

        seek.max = audioDuration || 100;
        seek.value = Math.min(audio.currentTime, audioDuration || 100);
        seek.disabled = audioDuration <= 0;
        seek.setAttribute(
            "aria-valuetext",
            `${elapsedLabel} of ${audioDuration ? durationLabel : "unknown duration"}`,
        );
        progress.style.width = `${played}%`;
        currentTime.textContent = elapsedLabel;
        duration.textContent = durationLabel;
    };

    const updateToggle = () => {
        const isPlaying = !audio.paused && !audio.ended;
        player.classList.toggle("is-playing", isPlaying);
        toggle.setAttribute("aria-label", isPlaying ? "Pause audio" : "Play audio");
    };

    const clearPlaybackState = () => {
        try {
            window.localStorage.removeItem(storageKey);
        } catch {
            // Playback still works when storage is unavailable.
        }
    };

    const savePlaybackState = (force = false) => {
        if (!Number.isFinite(audio.currentTime)) {
            return;
        }

        const currentSecond = Math.floor(audio.currentTime);
        const isAtEnd =
            audio.ended ||
            (Number.isFinite(audio.duration) && audio.duration - audio.currentTime <= 3);

        if (isAtEnd) {
            clearPlaybackState();
            lastSavedSecond = -1;
            return;
        }

        if (!force && currentSecond === lastSavedSecond) {
            return;
        }

        try {
            window.localStorage.setItem(
                storageKey,
                JSON.stringify({
                    currentTime: audio.currentTime,
                    playbackRate: audio.playbackRate,
                }),
            );
            lastSavedSecond = currentSecond;
        } catch {
            // Playback still works when storage is unavailable.
        }
    };

    const setPlaybackRate = (playbackRate, announce = true) => {
        const nextRateIndex = playbackRates.indexOf(playbackRate);

        if (nextRateIndex === -1) {
            return;
        }

        rateIndex = nextRateIndex;
        const rateLabel = `${playbackRate}×`;
        audio.defaultPlaybackRate = playbackRate;
        audio.playbackRate = playbackRate;
        rate.textContent = rateLabel;
        rate.setAttribute("aria-label", `Playback speed: ${rateLabel}. Change speed`);

        if (announce) {
            status.textContent = `Playback speed ${rateLabel}`;
        }
    };

    const restorePlaybackState = () => {
        if (hasRestoredState || !Number.isFinite(audio.duration) || audio.duration <= 0) {
            return;
        }

        hasRestoredState = true;

        try {
            const savedState = JSON.parse(window.localStorage.getItem(storageKey));
            const savedTime = Number.parseFloat(savedState?.currentTime);
            const savedRate = Number.parseFloat(savedState?.playbackRate);

            if (playbackRates.includes(savedRate)) {
                setPlaybackRate(savedRate, false);
            }

            if (Number.isFinite(savedTime) && savedTime > 0 && savedTime < audio.duration - 3) {
                audio.currentTime = savedTime;
                lastSavedSecond = Math.floor(savedTime);
                status.textContent = `Audio resumed at ${formatTime(savedTime)}`;
            } else if (Number.isFinite(savedTime)) {
                clearPlaybackState();
            }
        } catch {
            clearPlaybackState();
        }
    };

    const prepareTimeline = () => {
        restorePlaybackState();
        updateTimeline();
    };

    const seekToSelectedTime = () => {
        const nextTime = Number.parseFloat(seek.value);

        if (!Number.isFinite(nextTime) || !Number.isFinite(audio.duration)) {
            return;
        }

        audio.currentTime = Math.min(Math.max(nextTime, 0), audio.duration);
        updateTimeline();
        savePlaybackState(true);
    };

    audio.controls = false;
    controls.hidden = false;
    player.classList.add("is-enhanced");

    toggle.addEventListener("click", async () => {
        if (!audio.paused) {
            audio.pause();
            return;
        }

        try {
            await audio.play();
        } catch {
            status.textContent = "Audio could not start";
        }
    });

    seek.addEventListener("input", seekToSelectedTime);
    seek.addEventListener("change", seekToSelectedTime);

    rate.addEventListener("click", () => {
        rateIndex = (rateIndex + 1) % playbackRates.length;
        const playbackRate = playbackRates[rateIndex];
        setPlaybackRate(playbackRate);
        savePlaybackState(true);
    });

    audio.addEventListener("loadedmetadata", prepareTimeline);
    audio.addEventListener("durationchange", prepareTimeline);
    audio.addEventListener("canplay", prepareTimeline);
    audio.addEventListener("timeupdate", () => {
        updateTimeline();
        savePlaybackState();
    });
    audio.addEventListener("play", () => {
        updateToggle();
        status.textContent = "Audio playing";
    });
    audio.addEventListener("pause", () => {
        updateToggle();
        status.textContent = audio.ended ? "Audio finished" : "Audio paused";
        savePlaybackState(true);
    });
    audio.addEventListener("ended", () => {
        updateToggle();
        status.textContent = "Audio finished";
        clearPlaybackState();
    });
    audio.addEventListener("error", () => {
        status.textContent = "Audio unavailable";
        toggle.disabled = true;
        seek.disabled = true;
        rate.disabled = true;
    });
    window.addEventListener("pagehide", () => savePlaybackState(true));

    updateToggle();
    prepareTimeline();
});
