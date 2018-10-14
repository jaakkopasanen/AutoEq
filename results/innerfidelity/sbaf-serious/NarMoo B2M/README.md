# NarMoo B2M

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.4; 23 -7.4; 25 -7.3; 28 -7.2; 31 -7.0; 34 -6.8; 37 -6.7; 41 -6.5; 45 -6.3; 49 -6.2; 54 -6.0; 60 -5.8; 66 -5.7; 72 -5.6; 79 -5.6; 87 -5.6; 96 -5.5; 106 -5.3; 116 -5.2; 128 -5.0; 141 -4.9; 155 -4.8; 170 -4.5; 187 -4.3; 206 -4.0; 227 -3.7; 249 -3.5; 274 -3.2; 302 -2.9; 332 -2.5; 365 -2.2; 402 -2.0; 442 -1.5; 486 -1.4; 535 -1.1; 588 -0.5; 647 -0.3; 712 -0.2; 783 0.2; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.2; 1261 -0.3; 1387 -0.8; 1526 -1.1; 1678 -1.3; 1846 0.2; 2031 0.4; 2234 0.4; 2457 0.9; 2703 1.7; 2973 3.7; 3270 5.9; 3597 6.0; 3957 6.0; 4353 4.5; 4788 2.2; 5267 4.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo B2M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.29 | -7.1 dB |
| Peaking | 149 Hz  | 0.49 | -3.7 dB |
| Peaking | 3592 Hz | 2.68 | 6.4 dB  |
| Peaking | 6084 Hz | 2.95 | 6.5 dB  |
| Peaking | 7708 Hz | 2.08 | -1.6 dB |
| Peaking | 795 Hz  | 2.77 | 0.8 dB  |
| Peaking | 1591 Hz | 4.76 | -1.6 dB |
| Peaking | 3101 Hz | 2.92 | -0.7 dB |
| Peaking | 3141 Hz | 8.1  | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20B2M/NarMoo%20B2M.png)