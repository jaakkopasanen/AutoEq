# Audio Technica ATH-WS55

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.4; 25 2.7; 28 1.9; 31 1.3; 34 0.7; 37 0.3; 41 0.0; 45 -0.4; 49 -0.8; 54 -1.2; 60 -1.5; 66 -1.7; 72 -1.8; 79 -2.0; 87 -2.1; 96 -2.2; 106 -2.5; 116 -2.8; 128 -3.3; 141 -3.4; 155 -3.5; 170 -3.3; 187 -3.3; 206 -3.0; 227 -2.0; 249 -0.9; 274 -0.3; 302 0.0; 332 0.6; 365 0.6; 402 1.2; 442 2.0; 486 2.2; 535 2.2; 588 2.2; 647 1.8; 712 1.3; 783 1.0; 861 0.5; 947 0.1; 1042 -0.1; 1146 1.6; 1261 0.4; 1387 -0.2; 1526 -0.1; 1678 0.9; 1846 2.0; 2031 3.8; 2234 5.6; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.3; 7010 1.7; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-WS55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.08 | 4.9 dB  |
| Peaking | 75 Hz   | 0.71 | -1.7 dB |
| Peaking | 163 Hz  | 1.38 | -3.1 dB |
| Peaking | 493 Hz  | 1.83 | 2.6 dB  |
| Peaking | 3662 Hz | 0.91 | 7.0 dB  |
| Peaking | 1540 Hz | 2.78 | -2.1 dB |
| Peaking | 2315 Hz | 3.31 | 2.6 dB  |
| Peaking | 3663 Hz | 2.8  | -1.2 dB |
| Peaking | 5894 Hz | 2.38 | 4.5 dB  |
| Peaking | 7159 Hz | 1.27 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-WS55/Audio%20Technica%20ATH-WS55.png)