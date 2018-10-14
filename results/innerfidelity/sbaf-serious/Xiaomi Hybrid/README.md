# Xiaomi Hybrid

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.4; 23 -5.8; 25 -6.1; 28 -6.4; 31 -6.7; 34 -6.8; 37 -7.0; 41 -7.2; 45 -7.3; 49 -7.4; 54 -7.6; 60 -7.7; 66 -7.8; 72 -7.9; 79 -8.0; 87 -8.1; 96 -8.3; 106 -8.0; 116 -7.9; 128 -7.8; 141 -7.6; 155 -7.3; 170 -7.0; 187 -6.6; 206 -6.2; 227 -5.7; 249 -5.2; 274 -4.5; 302 -3.9; 332 -3.4; 365 -2.8; 402 -2.3; 442 -1.6; 486 -1.2; 535 -0.6; 588 0.1; 647 0.4; 712 0.6; 783 0.8; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.2; 1387 -2.3; 1526 -3.5; 1678 -4.7; 1846 -5.6; 2031 -6.0; 2234 -6.0; 2457 -4.1; 2703 -1.8; 2973 0.3; 3270 1.4; 3597 0.4; 3957 -1.4; 4353 -0.1; 4788 3.2; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.2; 15026 -2.0; 16529 -0.1; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Hybrid ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.39 | -6.5 dB |
| Peaking | 120 Hz   | 0.85 | -4.5 dB |
| Peaking | 235 Hz   | 1.42 | -2.9 dB |
| Peaking | 2000 Hz  | 2.35 | -6.8 dB |
| Peaking | 5729 Hz  | 3.08 | 7.1 dB  |
| Peaking | 788 Hz   | 1.1  | 3.8 dB  |
| Peaking | 843 Hz   | 0.58 | -2.3 dB |
| Peaking | 3201 Hz  | 4.92 | 2.6 dB  |
| Peaking | 4022 Hz  | 8.28 | -2.6 dB |
| Peaking | 14962 Hz | 4.8  | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Hybrid/Xiaomi%20Hybrid.png)