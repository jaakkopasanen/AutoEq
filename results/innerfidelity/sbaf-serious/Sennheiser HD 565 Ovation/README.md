# Sennheiser HD 565 Ovation

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.4; 87 4.5; 96 3.6; 106 3.0; 116 2.5; 128 2.0; 141 1.5; 155 1.1; 170 0.9; 187 0.6; 206 0.4; 227 0.4; 249 0.3; 274 0.3; 302 0.3; 332 0.3; 365 0.4; 402 0.4; 442 0.5; 486 0.4; 535 0.3; 588 0.5; 647 0.5; 712 0.2; 783 0.3; 861 -0.1; 947 -0.1; 1042 -0.2; 1146 -0.7; 1261 -1.1; 1387 -1.5; 1526 -1.7; 1678 -2.0; 1846 -1.5; 2031 -1.4; 2234 -1.8; 2457 -1.3; 2703 -0.3; 2973 1.0; 3270 1.4; 3597 0.5; 3957 -0.3; 4353 -0.5; 4788 2.2; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 565 Ovation ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.34 | 7.2 dB  |
| Peaking | 634 Hz   | 0.43 | 4.8 dB  |
| Peaking | 783 Hz   | 0.13 | -4.7 dB |
| Peaking | 3113 Hz  | 3.31 | 3.7 dB  |
| Peaking | 5791 Hz  | 2.54 | 8.7 dB  |
| Peaking | 18 Hz    | 1.15 | 1.7 dB  |
| Peaking | 42 Hz    | 0.56 | -0.8 dB |
| Peaking | 72 Hz    | 2.69 | 1.4 dB  |
| Peaking | 1475 Hz  | 3.93 | -0.2 dB |
| Peaking | 12685 Hz | 2.1  | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20565%20Ovation/Sennheiser%20HD%20565%20Ovation.png)