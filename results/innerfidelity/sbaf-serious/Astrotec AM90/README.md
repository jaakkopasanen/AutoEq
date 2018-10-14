# Astrotec AM90

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.1; 25 3.0; 28 3.0; 31 2.9; 34 2.8; 37 2.6; 41 2.5; 45 2.3; 49 2.2; 54 2.0; 60 1.7; 66 1.3; 72 1.0; 79 0.6; 87 0.1; 96 -0.4; 106 -0.6; 116 -0.8; 128 -1.2; 141 -1.4; 155 -1.7; 170 -1.8; 187 -2.0; 206 -2.0; 227 -2.0; 249 -2.1; 274 -1.9; 302 -1.9; 332 -1.7; 365 -1.6; 402 -1.4; 442 -1.0; 486 -0.9; 535 -0.7; 588 -0.1; 647 0.1; 712 0.2; 783 0.7; 861 0.5; 947 0.3; 1042 -0.1; 1146 -0.4; 1261 -0.5; 1387 -0.3; 1526 0.6; 1678 0.7; 1846 0.4; 2031 0.3; 2234 -0.3; 2457 -1.2; 2703 -3.0; 2973 -1.0; 3270 5.2; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AM90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.67 | 3.1 dB  |
| Peaking | 53 Hz   | 1.36 | 1.2 dB  |
| Peaking | 213 Hz  | 0.69 | -2.3 dB |
| Peaking | 2734 Hz | 4.48 | -6.7 dB |
| Peaking | 4264 Hz | 1.18 | 7.4 dB  |
| Peaking | 1282 Hz | 7.58 | -1.0 dB |
| Peaking | 3381 Hz | 7.21 | 3.0 dB  |
| Peaking | 4219 Hz | 1.35 | -1.4 dB |
| Peaking | 6311 Hz | 2.57 | 5.3 dB  |
| Peaking | 7350 Hz | 1.68 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AM90/Astrotec%20AM90.png)