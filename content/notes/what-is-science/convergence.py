# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib",
#     "seaborn",
#     "numpy",
# ]
# ///
"""Illustration: repeated runs converge to the model's value, not to the measurement."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def main():
    """Plot the running mean evacuation time of a stochastic model against the number of runs.

    The data are synthetic: run results are drawn from a normal distribution
    (mean 200 s, sd 15 s) and compared with a fictitious drill value of
    240 s +/- 10 s.

    Parameters
    ----------
    sys.argv[1] : str, optional
        Output directory. Default: ./figures

    Saves
    -----
    convergence.pdf, convergence.png
    """
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "./figures")
    out.mkdir(exist_ok=True)

    # --- Data ---
    rng = np.random.default_rng(7)
    n = 1000
    runs = rng.normal(200, 15, n)
    k = np.arange(1, n + 1)
    mean = np.cumsum(runs) / k
    sd = np.array([runs[:i].std(ddof=1) if i > 1 else np.nan for i in k])
    ci = 1.96 * sd / np.sqrt(k)
    drill, drill_err = 240, 10

    # --- Style Setup ---
    sns.set_theme(font_scale=1.0, style="whitegrid", font="DejaVu Sans")
    pal = sns.cubehelix_palette(6, rot=-0.25, light=0.7)
    red = "#d73027"

    # --- Plot ---
    _, ax = plt.subplots(figsize=(10, 5.5), dpi=150)
    ax.scatter(k, runs, s=5, color="grey", alpha=0.3, edgecolors="none",
               label="Single runs", zorder=2)
    ax.fill_between(k[1:], (mean - ci)[1:], (mean + ci)[1:], color=pal[2],
                    alpha=0.35, linewidth=0, zorder=3)
    ax.plot(k, mean, color=pal[5], linewidth=2.2,
            label="Running mean of the runs (95 % interval)", zorder=4)
    ax.axhspan(drill - drill_err, drill + drill_err, color=red, alpha=0.12,
               linewidth=0, zorder=1)
    ax.axhline(drill, color=red, linewidth=1.5, linestyle="--",
               label="Measured in a drill (with uncertainty)", zorder=4)

    ax.set_xscale("log")
    ax.set_xlim(1, n)
    ax.set_xticks([1, 10, 100, 1000], ["1", "10", "100", "1000"])
    ax.set_ylim(150, 255)
    ax.set_xlabel("Number of runs", fontsize=12, labelpad=8, color="dimgrey")
    ax.set_ylabel("Evacuation time (s)", fontsize=12, labelpad=8, color="dimgrey")
    ax.set_title("More runs sharpen the model's answer (illustration, synthetic data)",
                 fontsize=13, loc="left", pad=7, color="dimgrey")

    # --- Annotations ---
    ax.annotate("The interval shrinks:\nwe know the model's answer\nmore precisely",
                xy=(30, mean[29] - ci[29]), xytext=(2.2, 160),
                fontsize=10, color="dimgrey", ha="left",
                arrowprops={"arrowstyle": "-", "color": "dimgrey", "lw": 0.8})
    ax.annotate("", xy=(25, drill - drill_err), xytext=(25, mean[24] + ci[24]),
                arrowprops={"arrowstyle": "<->", "color": "dimgrey", "lw": 0.9})
    ax.text(28, (drill - drill_err + mean[24] + ci[24]) / 2,
            "More runs do not shrink this gap.\nOnly data reveal it.",
            fontsize=10, color="dimgrey", ha="left", va="center")

    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=3,
              fontsize=10, frameon=True, facecolor="white",
              framealpha=0.8, edgecolor="lightgrey", labelcolor="dimgrey",
              markerscale=2.5)
    ax.tick_params(axis="both", which="both", length=0, labelcolor="dimgrey")
    ax.grid(False)
    sns.despine(left=True, bottom=True)
    ax.patch.set_edgecolor("lightgrey")
    ax.patch.set_linewidth(0.8)

    # --- Save ---
    plt.savefig(out / "convergence.pdf", dpi=150, bbox_inches="tight")
    plt.savefig(out / "convergence.png", dpi=150, bbox_inches="tight")


if __name__ == "__main__":
    main()
