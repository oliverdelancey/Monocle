# Monocle

Monocle is a simple, no-nonsense WAV file oscilloscope for quick analysis of waveforms. It leverages the power of Matplotlib to render the graphics.

## Usage

Monocle uses the concept of a "window" to define the coordinates of the graph.

```
                      ┏━━The Window━━━━━┓
┌──The WAV File───────╂─────────────────╂────┐
│                     ┃                 ┃    │
│                     ┃                 ┃    │
│                     ┃                 ┃    │
│                     ┃                 ┃    │
│                     ┃                 ┃    │
│                     ┃                 ┃    │
└─────────────────────╂─────────────────╂────┘
                      ┗━━━━━━━━━━━━━━━━━┛
```

1. Load a WAV file (`File -> Open`).
2. Set the beginning X point of the window with the `X Start` slider.
3. Set the ending X point of the window with the `X End` slider.
4. Set the starting point/shift of the graph with the `X Pos` slider.

That is, the X coordinates of the window are:
```
x_min = (X Start) + (X Pos)
x_max = (X End) + (X Pos)
```
And the Y coordinates:
```
y_min = (Minimum Amplitude of the WAV File) + 10%
y_max = (Maximum Amplitude of the WAV File) + 10%
```

The Matplotlib toolbar can be used to configure the graph and export it in a variety of formats.
