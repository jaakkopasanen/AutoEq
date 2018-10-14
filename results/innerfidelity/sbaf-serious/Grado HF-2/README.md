# Grado HF-2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.7; 45 4.7; 49 3.5; 54 2.5; 60 1.1; 66 -0.1; 72 -1.0; 79 -1.8; 87 -2.5; 96 -2.9; 106 -3.0; 116 -2.8; 128 -2.7; 141 -2.5; 155 -2.2; 170 -1.9; 187 -1.8; 206 -1.5; 227 -1.0; 249 -0.7; 274 -0.8; 302 -0.6; 332 -0.4; 365 -0.3; 402 -0.1; 442 0.2; 486 0.2; 535 0.2; 588 0.5; 647 0.6; 712 0.5; 783 0.6; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -1.1; 1387 -2.2; 1526 -3.7; 1678 -4.4; 1846 -5.4; 2031 -8.5; 2234 -7.8; 2457 -6.0; 2703 -5.0; 2973 -3.5; 3270 -2.5; 3597 -1.4; 3957 1.0; 4353 2.1; 4788 1.2; 5267 -3.0; 5793 -0.6; 6373 -1.0; 7010 -2.7; 7711 -3.6; 8482 -7.3; 9330 -8.6; 10263 -1.5; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.51 | 7.6 dB   |
| Peaking | 92 Hz    | 0.78 | -5.9 dB  |
| Peaking | 2138 Hz  | 2.28 | -8.6 dB  |
| Peaking | 9044 Hz  | 3.33 | -10.7 dB |
| Peaking | 10577 Hz | 2.89 | 3.3 dB   |
| Peaking | 713 Hz   | 0.95 | 1.5 dB   |
| Peaking | 1578 Hz  | 0.17 | -0.5 dB  |
| Peaking | 3278 Hz  | 3.38 | -1.5 dB  |
| Peaking | 4485 Hz  | 2.54 | 4.5 dB   |
| Peaking | 5239 Hz  | 7.99 | -4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-2/Grado%20HF-2.png)