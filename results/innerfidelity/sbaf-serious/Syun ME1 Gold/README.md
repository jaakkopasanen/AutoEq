# Syun ME1 Gold

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 5.5; 25 5.0; 28 4.3; 31 3.5; 34 2.9; 37 2.4; 41 1.9; 45 1.4; 49 0.9; 54 0.4; 60 -0.2; 66 -0.7; 72 -1.2; 79 -1.7; 87 -2.3; 96 -2.9; 106 -3.4; 116 -3.7; 128 -4.1; 141 -4.5; 155 -4.9; 170 -5.2; 187 -5.3; 206 -5.5; 227 -5.5; 249 -5.5; 274 -5.4; 302 -5.3; 332 -5.1; 365 -4.8; 402 -4.4; 442 -3.7; 486 -3.4; 535 -2.8; 588 -2.0; 647 -1.5; 712 -1.3; 783 -0.8; 861 -0.2; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.3; 1526 -1.8; 1678 -2.1; 1846 -2.0; 2031 -1.8; 2234 -1.4; 2457 -0.5; 2703 0.3; 2973 1.6; 3270 2.8; 3597 2.8; 3957 0.9; 4353 -2.9; 4788 -5.4; 5267 -2.9; 5793 2.0; 6373 4.8; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.3dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Syun ME1 Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.76 | 6.2 dB   |
| Peaking | 213 Hz   | 0.54 | -5.9 dB  |
| Peaking | 3620 Hz  | 2.24 | 9.7 dB   |
| Peaking | 4918 Hz  | 1.23 | -14.0 dB |
| Peaking | 6143 Hz  | 2.08 | 12.6 dB  |
| Peaking | 403 Hz   | 2.5  | -0.7 dB  |
| Peaking | 1013 Hz  | 1.33 | 2.3 dB   |
| Peaking | 1688 Hz  | 0.8  | -2.0 dB  |
| Peaking | 2769 Hz  | 2.71 | 1.5 dB   |
| Peaking | 11753 Hz | 1.52 | 0.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Syun%20ME1%20Gold/Syun%20ME1%20Gold.png)