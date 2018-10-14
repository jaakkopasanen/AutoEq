# Grado SR225i Reverse Bowls

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.1; 45 3.9; 49 3.0; 54 1.9; 60 1.0; 66 0.2; 72 -0.5; 79 -1.2; 87 -1.7; 96 -2.1; 106 -2.3; 116 -2.4; 128 -2.5; 141 -2.5; 155 -2.4; 170 -2.3; 187 -2.1; 206 -1.9; 227 -1.7; 249 -1.5; 274 -1.1; 302 -1.1; 332 -1.1; 365 -0.7; 402 -0.7; 442 -0.5; 486 -0.4; 535 -0.3; 588 0.2; 647 0.2; 712 0.1; 783 0.4; 861 0.1; 947 0.0; 1042 -0.0; 1146 -0.2; 1261 -0.7; 1387 -1.6; 1526 -2.6; 1678 -3.3; 1846 -4.7; 2031 -7.8; 2234 -6.7; 2457 -3.8; 2703 -1.7; 2973 -0.9; 3270 0.4; 3597 -0.9; 3957 0.4; 4353 2.3; 4788 2.1; 5267 0.4; 5793 2.0; 6373 0.2; 7010 -3.6; 7711 -4.5; 8482 -5.5; 9330 -6.1; 10263 -1.6; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i Reverse Bowls ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.58 | 7.6 dB  |
| Peaking | 96 Hz    | 0.55 | -4.4 dB |
| Peaking | 2081 Hz  | 3.04 | -8.2 dB |
| Peaking | 5050 Hz  | 1.51 | 2.8 dB  |
| Peaking | 8432 Hz  | 2.45 | -6.9 dB |
| Peaking | 840 Hz   | 1.39 | 0.6 dB  |
| Peaking | 1507 Hz  | 6.68 | -1.1 dB |
| Peaking | 9658 Hz  | 7.2  | -3.1 dB |
| Peaking | 10608 Hz | 2.81 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20Reverse%20Bowls/Grado%20SR225i%20Reverse%20Bowls.png)