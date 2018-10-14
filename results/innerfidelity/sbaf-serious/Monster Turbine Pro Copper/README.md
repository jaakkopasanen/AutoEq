# Monster Turbine Pro Copper

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 -6.6; 23 -6.7; 25 -6.7; 28 -6.8; 31 -6.7; 34 -6.5; 37 -6.4; 41 -6.4; 45 -6.3; 49 -6.3; 54 -6.3; 60 -6.2; 66 -6.4; 72 -6.3; 79 -6.3; 87 -6.3; 96 -6.4; 106 -6.3; 116 -6.2; 128 -6.2; 141 -6.1; 155 -5.9; 170 -5.7; 187 -5.5; 206 -5.3; 227 -4.9; 249 -4.6; 274 -4.2; 302 -3.9; 332 -3.5; 365 -3.1; 402 -2.7; 442 -2.1; 486 -1.8; 535 -1.4; 588 -0.6; 647 -0.3; 712 -0.0; 783 0.4; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.5; 1387 -1.1; 1526 -1.8; 1678 -2.4; 1846 -2.5; 2031 -2.8; 2234 -2.6; 2457 -1.6; 2703 -2.3; 2973 -0.3; 3270 1.8; 3597 3.1; 3957 2.1; 4353 -0.8; 4788 -1.7; 5267 0.4; 5793 3.4; 6373 5.2; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine Pro Copper ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.17 | -6.8 dB |
| Peaking | 2147 Hz | 1.92 | -3.1 dB |
| Peaking | 3681 Hz | 3.68 | 4.7 dB  |
| Peaking | 4649 Hz | 3.12 | -3.2 dB |
| Peaking | 6243 Hz | 4.27 | 5.9 dB  |
| Peaking | 22 Hz   | 0.69 | -0.9 dB |
| Peaking | 52 Hz   | 0.77 | 0.9 dB  |
| Peaking | 231 Hz  | 0.58 | -0.7 dB |
| Peaking | 758 Hz  | 1.42 | 1.5 dB  |
| Peaking | 1612 Hz | 5.04 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Turbine%20Pro%20Copper/Monster%20Turbine%20Pro%20Copper.png)