# Sennheiser IE 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.1; 25 -0.4; 28 -0.7; 31 -0.9; 34 -1.1; 37 -1.3; 41 -1.6; 45 -1.8; 49 -2.0; 54 -2.2; 60 -2.5; 66 -2.7; 72 -3.0; 79 -3.2; 87 -3.5; 96 -3.7; 106 -3.8; 116 -3.8; 128 -4.0; 141 -3.9; 155 -4.0; 170 -3.8; 187 -3.6; 206 -3.5; 227 -3.1; 249 -2.9; 274 -2.6; 302 -2.3; 332 -1.9; 365 -1.6; 402 -1.3; 442 -0.8; 486 -0.6; 535 -0.3; 588 0.3; 647 0.4; 712 0.5; 783 0.8; 861 0.5; 947 0.3; 1042 -0.1; 1146 -0.3; 1261 -0.5; 1387 -0.6; 1526 -0.9; 1678 -0.7; 1846 0.2; 2031 1.5; 2234 3.1; 2457 5.2; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.3; 5267 3.0; 5793 2.0; 6373 4.9; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -3.1; 10263 -4.6; 11289 -3.0; 12418 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 102 Hz   | 0.59 | -3.4 dB |
| Peaking | 216 Hz   | 1.09 | -1.7 dB |
| Peaking | 2704 Hz  | 3.69 | 4.0 dB  |
| Peaking | 4100 Hz  | 1.28 | 5.7 dB  |
| Peaking | 10220 Hz | 3.69 | -5.7 dB |
| Peaking | 16 Hz    | 1.72 | 0.8 dB  |
| Peaking | 725 Hz   | 2.5  | 1.0 dB  |
| Peaking | 1537 Hz  | 3    | -1.8 dB |
| Peaking | 5684 Hz  | 4.56 | -1.7 dB |
| Peaking | 6482 Hz  | 7.94 | 4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800/Sennheiser%20IE%20800.png)