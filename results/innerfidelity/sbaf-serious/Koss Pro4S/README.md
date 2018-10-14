# Koss Pro4S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.3; 28 1.6; 31 1.1; 34 0.7; 37 0.4; 41 0.0; 45 -0.3; 49 -0.5; 54 -0.8; 60 -1.0; 66 -1.2; 72 -1.4; 79 -1.6; 87 -1.8; 96 -1.8; 106 -1.6; 116 -1.1; 128 -0.0; 141 0.7; 155 0.1; 170 1.4; 187 3.1; 206 3.2; 227 4.0; 249 5.6; 274 4.4; 302 2.4; 332 0.9; 365 0.8; 402 0.6; 442 0.5; 486 0.0; 535 -0.2; 588 0.1; 647 -0.1; 712 -0.3; 783 -0.2; 861 -0.3; 947 -0.1; 1042 0.1; 1146 -0.1; 1261 -0.6; 1387 -1.0; 1526 -1.2; 1678 -1.5; 1846 -1.7; 2031 -2.1; 2234 -1.9; 2457 -2.9; 2703 -3.3; 2973 -2.6; 3270 -1.3; 3597 -0.1; 3957 2.5; 4353 5.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.67 | 3.6 dB  |
| Peaking | 85 Hz   |  1.36 | -2.2 dB |
| Peaking | 241 Hz  |  2.2  | 5.4 dB  |
| Peaking | 2786 Hz |  1.18 | -4.3 dB |
| Peaking | 5017 Hz |  1.74 | 8.2 dB  |
| Peaking | 182 Hz  | 13.3  | 1.4 dB  |
| Peaking | 416 Hz  |  1.23 | -0.3 dB |
| Peaking | 5301 Hz |  7.82 | -1.6 dB |
| Peaking | 6524 Hz |  2.87 | 3.5 dB  |
| Peaking | 7458 Hz |  2.19 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4S/Koss%20Pro4S.png)