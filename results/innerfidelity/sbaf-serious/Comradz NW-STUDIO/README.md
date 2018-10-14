# Comradz NW-STUDIO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 5.9; 402 5.3; 442 4.9; 486 2.9; 535 -2.2; 588 2.7; 647 2.9; 712 2.3; 783 2.2; 861 1.5; 947 0.6; 1042 -0.6; 1146 -2.2; 1261 -4.6; 1387 -7.7; 1526 -11.3; 1678 -14.6; 1846 -17.4; 2031 -18.8; 2234 -19.1; 2457 -17.6; 2703 -16.0; 2973 -13.1; 3270 -9.3; 3597 -8.5; 3957 -9.4; 4353 -11.9; 4788 -13.2; 5267 -13.7; 5793 -15.4; 6373 -15.8; 7010 -14.6; 7711 -16.1; 8482 -19.1; 9330 -17.0; 10263 -9.0; 11289 -1.0; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Comradz NW-STUDIO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 107 Hz   | 0.06 | 6.3 dB   |
| Peaking | 2083 Hz  | 1.26 | -22.1 dB |
| Peaking | 5907 Hz  | 1.52 | -9.4 dB  |
| Peaking | 8922 Hz  | 2.22 | -17.7 dB |
| Peaking | 11751 Hz | 1.86 | 6.7 dB   |
| Peaking | 526 Hz   | 9.19 | -7.7 dB  |
| Peaking | 975 Hz   | 0.49 | 1.6 dB   |
| Peaking | 1595 Hz  | 4.21 | -3.4 dB  |
| Peaking | 2736 Hz  | 4.46 | -3.0 dB  |
| Peaking | 3437 Hz  | 6.26 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Comradz%20NW-STUDIO/Comradz%20NW-STUDIO.png)