# Grado SR225i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.6; 41 4.7; 45 3.7; 49 2.9; 54 2.0; 60 1.3; 66 0.5; 72 -0.2; 79 -0.9; 87 -1.4; 96 -1.8; 106 -2.0; 116 -2.0; 128 -2.1; 141 -2.1; 155 -1.9; 170 -1.7; 187 -1.6; 206 -1.4; 227 -1.0; 249 -0.7; 274 -0.4; 302 -0.4; 332 -0.4; 365 -0.1; 402 -0.3; 442 0.0; 486 -0.0; 535 0.1; 588 0.4; 647 0.4; 712 0.3; 783 0.5; 861 0.3; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.8; 1387 -1.7; 1526 -3.0; 1678 -3.9; 1846 -5.9; 2031 -8.6; 2234 -7.6; 2457 -5.4; 2703 -4.1; 2973 -3.4; 3270 -2.1; 3597 -3.6; 3957 -2.4; 4353 -0.5; 4788 -0.6; 5267 -2.3; 5793 -1.2; 6373 -2.6; 7010 -5.8; 7711 -5.9; 8482 -7.4; 9330 -9.4; 10263 -4.7; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 28 Hz    |  0.67 | 6.7 dB   |
| Peaking | 105 Hz   |  0.83 | -3.2 dB  |
| Peaking | 2116 Hz  |  2.37 | -8.4 dB  |
| Peaking | 9283 Hz  |  1.83 | -11.9 dB |
| Peaking | 11125 Hz |  2.06 | 5.9 dB   |
| Peaking | 796 Hz   |  1.39 | 0.9 dB   |
| Peaking | 3777 Hz  |  4.5  | -2.8 dB  |
| Peaking | 4320 Hz  |  3.5  | 2.1 dB   |
| Peaking | 7095 Hz  | 11.82 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i/Grado%20SR225i.png)