# Comradz NW-STUDIO PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.7; 25 5.3; 28 4.4; 31 3.6; 34 2.8; 37 2.2; 41 1.4; 45 0.8; 49 0.2; 54 -0.3; 60 -0.9; 66 -1.4; 72 -1.8; 79 -2.1; 87 -2.6; 96 -2.8; 106 -3.0; 116 -3.1; 128 -3.3; 141 -3.6; 155 -3.7; 170 -3.9; 187 -3.9; 206 -4.1; 227 -4.1; 249 -4.2; 274 -4.1; 302 -3.9; 332 -3.7; 365 -3.3; 402 -2.9; 442 -2.4; 486 -2.1; 535 -1.4; 588 -0.5; 647 0.3; 712 1.1; 783 2.2; 861 2.6; 947 1.5; 1042 -1.6; 1146 -5.4; 1261 -10.0; 1387 -14.0; 1526 -16.4; 1678 -16.2; 1846 -14.7; 2031 -12.5; 2234 -10.2; 2457 -7.5; 2703 -5.4; 2973 -2.7; 3270 -0.7; 3597 -0.2; 3957 -1.4; 4353 -4.6; 4788 -6.5; 5267 -6.3; 5793 -4.5; 6373 -1.7; 7010 -1.3; 7711 -5.1; 8482 -4.4; 9330 -0.2; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Comradz NW-STUDIO PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 1.37 | 6.2 dB   |
| Peaking | 171 Hz   | 0.68 | -4.4 dB  |
| Peaking | 1682 Hz  | 2.25 | -18.1 dB |
| Peaking | 5179 Hz  | 3    | -6.1 dB  |
| Peaking | 22692 Hz | 2.41 | -2.1 dB  |
| Peaking | 871 Hz   | 2.67 | 6.1 dB   |
| Peaking | 1346 Hz  | 5.39 | -5.1 dB  |
| Peaking | 2265 Hz  | 4.58 | -3.2 dB  |
| Peaking | 3452 Hz  | 4.8  | 3.3 dB   |
| Peaking | 8048 Hz  | 7.41 | -5.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Comradz%20NW-STUDIO%20PRO/Comradz%20NW-STUDIO%20PRO.png)