# Syun Mix1 Gold

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -2.9; 23 -3.5; 25 -3.9; 28 -4.5; 31 -4.9; 34 -5.3; 37 -5.7; 41 -6.1; 45 -6.5; 49 -6.7; 54 -7.1; 60 -7.6; 66 -7.9; 72 -8.2; 79 -8.6; 87 -8.9; 96 -9.3; 106 -9.5; 116 -9.6; 128 -9.7; 141 -9.8; 155 -9.8; 170 -9.6; 187 -9.4; 206 -9.2; 227 -8.7; 249 -8.4; 274 -7.9; 302 -7.4; 332 -6.8; 365 -6.2; 402 -5.5; 442 -4.7; 486 -4.2; 535 -3.4; 588 -2.5; 647 -1.9; 712 -1.4; 783 -0.8; 861 -0.5; 947 -0.3; 1042 0.3; 1146 0.8; 1261 0.5; 1387 -0.2; 1526 -0.7; 1678 -0.9; 1846 -0.8; 2031 -0.4; 2234 -0.1; 2457 0.7; 2703 1.6; 2973 2.6; 3270 3.4; 3597 3.1; 3957 1.4; 4353 -1.3; 4788 -0.8; 5267 3.1; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Syun Mix1 Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 67 Hz    | 0.39 | -6.5 dB |
| Peaking | 166 Hz   | 0.76 | -5.1 dB |
| Peaking | 334 Hz   | 1.17 | -3.3 dB |
| Peaking | 3272 Hz  | 4.35 | 3.8 dB  |
| Peaking | 6051 Hz  | 4.83 | 6.7 dB  |
| Peaking | 1149 Hz  | 2.86 | 1.5 dB  |
| Peaking | 1702 Hz  | 2.67 | -1.2 dB |
| Peaking | 4505 Hz  | 2.04 | 2.2 dB  |
| Peaking | 4518 Hz  | 5.21 | -5.2 dB |
| Peaking | 24000 Hz | 1.75 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Syun%20Mix1%20Gold/Syun%20Mix1%20Gold.png)