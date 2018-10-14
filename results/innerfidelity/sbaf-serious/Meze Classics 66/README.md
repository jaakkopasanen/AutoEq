# Meze Classics 66

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 21 -3.6; 23 -4.0; 25 -4.3; 28 -4.8; 31 -5.2; 34 -5.5; 37 -5.6; 41 -5.8; 45 -5.9; 49 -6.0; 54 -6.0; 60 -6.1; 66 -6.2; 72 -6.4; 79 -6.7; 87 -6.9; 96 -7.2; 106 -7.1; 116 -7.4; 128 -7.8; 141 -7.8; 155 -8.2; 170 -7.8; 187 -8.3; 206 -8.5; 227 -8.4; 249 -7.5; 274 -6.3; 302 -6.4; 332 -6.8; 365 -6.6; 402 -5.8; 442 -3.7; 486 -2.1; 535 -0.1; 588 1.9; 647 2.4; 712 1.4; 783 0.3; 861 -0.8; 947 -0.7; 1042 0.8; 1146 3.0; 1261 5.1; 1387 5.7; 1526 5.2; 1678 5.7; 1846 5.8; 2031 5.4; 2234 5.4; 2457 5.1; 2703 2.7; 2973 3.2; 3270 6.2; 3597 3.7; 3957 4.1; 4353 6.0; 4788 6.0; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Classics 66 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 61 Hz   | 0.34 | -6.0 dB |
| Peaking | 202 Hz  | 1.09 | -5.6 dB |
| Peaking | 366 Hz  | 3.51 | -4.1 dB |
| Peaking | 1765 Hz | 0.99 | 5.9 dB  |
| Peaking | 5095 Hz | 1.73 | 5.8 dB  |
| Peaking | 632 Hz  | 4.04 | 3.7 dB  |
| Peaking | 937 Hz  | 2.52 | -3.0 dB |
| Peaking | 1272 Hz | 4.77 | 2.2 dB  |
| Peaking | 6465 Hz | 5.16 | 3.2 dB  |
| Peaking | 7600 Hz | 1.86 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%20Classics%2066/Meze%20Classics%2066.png)