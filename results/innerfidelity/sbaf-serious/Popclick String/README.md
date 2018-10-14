# Popclick String

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 -10.7; 23 -10.7; 25 -10.7; 28 -10.7; 31 -10.6; 34 -10.5; 37 -10.4; 41 -10.3; 45 -10.2; 49 -10.1; 54 -9.9; 60 -9.8; 66 -9.8; 72 -9.6; 79 -9.6; 87 -9.5; 96 -9.4; 106 -9.1; 116 -8.8; 128 -8.5; 141 -8.2; 155 -7.9; 170 -7.4; 187 -6.9; 206 -6.3; 227 -5.6; 249 -5.1; 274 -4.4; 302 -3.8; 332 -3.0; 365 -2.4; 402 -1.8; 442 -1.0; 486 -0.7; 535 -0.2; 588 0.3; 647 0.5; 712 0.4; 783 0.8; 861 0.9; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -1.2; 1387 -2.3; 1526 -3.5; 1678 -4.5; 1846 -5.0; 2031 -5.7; 2234 -6.3; 2457 -6.0; 2703 -4.2; 2973 -0.9; 3270 2.1; 3597 3.6; 3957 2.8; 4353 -0.1; 4788 -2.6; 5267 -6.0; 5793 -8.6; 6373 -2.1; 7010 1.8; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.3; 11289 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.7dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Popclick String ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.25 | -10.5 dB |
| Peaking | 150 Hz  | 0.82 | -4.2 dB  |
| Peaking | 2234 Hz | 1.79 | -7.3 dB  |
| Peaking | 3565 Hz | 3.22 | 6.1 dB   |
| Peaking | 5580 Hz | 6.04 | -9.8 dB  |
| Peaking | 286 Hz  | 2.02 | -1.0 dB  |
| Peaking | 749 Hz  | 1.06 | 1.7 dB   |
| Peaking | 1564 Hz | 3.95 | -1.7 dB  |
| Peaking | 6214 Hz | 4.41 | -2.0 dB  |
| Peaking | 6883 Hz | 5.33 | 3.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Popclick%20String/Popclick%20String.png)