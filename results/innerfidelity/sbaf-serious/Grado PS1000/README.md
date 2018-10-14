# Grado PS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.4; 41 4.1; 45 2.9; 49 1.8; 54 0.4; 60 -1.0; 66 -2.2; 72 -3.2; 79 -4.1; 87 -4.8; 96 -5.3; 106 -5.3; 116 -5.1; 128 -4.7; 141 -4.2; 155 -3.8; 170 -3.3; 187 -2.7; 206 -2.2; 227 -1.7; 249 -1.3; 274 -0.7; 302 -0.4; 332 -0.4; 365 0.0; 402 -0.1; 442 0.1; 486 0.1; 535 0.2; 588 0.4; 647 0.5; 712 0.2; 783 0.5; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.6; 1261 -1.1; 1387 -1.8; 1526 -2.2; 1678 -1.7; 1846 -1.9; 2031 -1.2; 2234 -1.2; 2457 -1.3; 2703 -1.7; 2973 -1.9; 3270 -2.4; 3597 -1.0; 3957 -4.5; 4353 -6.6; 4788 -6.1; 5267 -7.3; 5793 -8.8; 6373 -11.9; 7010 -10.0; 7711 -6.9; 8482 -7.5; 9330 -10.4; 10263 -8.3; 11289 -2.1; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.74 | 7.4 dB   |
| Peaking | 97 Hz    | 0.88 | -6.8 dB  |
| Peaking | 1570 Hz  | 3    | -1.9 dB  |
| Peaking | 6250 Hz  | 1.52 | -10.7 dB |
| Peaking | 9613 Hz  | 4.98 | -8.2 dB  |
| Peaking | 613 Hz   | 1.06 | 0.8 dB   |
| Peaking | 3648 Hz  | 6.51 | 4.3 dB   |
| Peaking | 4140 Hz  | 2.13 | -3.3 dB  |
| Peaking | 5383 Hz  | 4.91 | 2.5 dB   |
| Peaking | 12583 Hz | 3.89 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20PS1000/Grado%20PS1000.png)