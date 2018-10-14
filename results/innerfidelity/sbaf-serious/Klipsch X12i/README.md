# Klipsch X12i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.9; 23 -1.0; 25 -1.1; 28 -1.3; 31 -1.4; 34 -1.5; 37 -1.7; 41 -1.8; 45 -2.0; 49 -2.2; 54 -2.4; 60 -2.7; 66 -3.0; 72 -3.3; 79 -3.6; 87 -4.0; 96 -4.4; 106 -4.6; 116 -4.7; 128 -5.0; 141 -5.1; 155 -5.2; 170 -5.3; 187 -5.2; 206 -5.2; 227 -4.9; 249 -4.8; 274 -4.6; 302 -4.3; 332 -4.0; 365 -3.6; 402 -3.2; 442 -2.7; 486 -2.4; 535 -1.9; 588 -1.2; 647 -0.8; 712 -0.5; 783 0.1; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.2; 1387 -0.6; 1526 -0.8; 1678 -0.8; 1846 -0.3; 2031 0.2; 2234 0.5; 2457 0.9; 2703 0.8; 2973 0.8; 3270 1.8; 3597 4.4; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X12i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 128 Hz  | 0.49 | -4.5 dB |
| Peaking | 285 Hz  | 1    | -2.1 dB |
| Peaking | 3058 Hz | 4.8  | -1.3 dB |
| Peaking | 4130 Hz | 2.19 | 6.0 dB  |
| Peaking | 5885 Hz | 3.46 | 4.9 dB  |
| Peaking | 26 Hz   | 1.51 | -0.4 dB |
| Peaking | 837 Hz  | 3.22 | 0.9 dB  |
| Peaking | 1598 Hz | 3.94 | -1.1 dB |
| Peaking | 8248 Hz | 4.57 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X12i/Klipsch%20X12i.png)