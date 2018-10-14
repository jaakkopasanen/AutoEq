# Monster Beats Solo

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.7; 25 0.3; 28 -0.2; 31 -0.6; 34 -0.9; 37 -1.3; 41 -1.8; 45 -1.8; 49 -1.7; 54 -1.8; 60 -2.3; 66 -2.7; 72 -3.2; 79 -4.1; 87 -4.8; 96 -5.7; 106 -6.7; 116 -6.9; 128 -6.8; 141 -7.1; 155 -7.7; 170 -7.5; 187 -7.6; 206 -6.8; 227 -6.2; 249 -6.0; 274 -5.2; 302 -3.3; 332 -1.3; 365 0.5; 402 1.7; 442 3.0; 486 3.7; 535 3.5; 588 2.9; 647 1.8; 712 0.7; 783 0.3; 861 -0.1; 947 -0.1; 1042 0.2; 1146 0.8; 1261 1.3; 1387 1.4; 1526 1.7; 1678 2.1; 1846 2.7; 2031 3.6; 2234 4.0; 2457 4.8; 2703 5.1; 2973 5.7; 3270 5.6; 3597 5.7; 3957 4.7; 4353 2.6; 4788 3.4; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Solo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 107 Hz  | 2.15 | -1.7 dB |
| Peaking | 205 Hz  | 0.53 | -8.2 dB |
| Peaking | 456 Hz  | 1.38 | 7.9 dB  |
| Peaking | 2932 Hz | 1.17 | 5.8 dB  |
| Peaking | 5840 Hz | 3.74 | 5.4 dB  |
| Peaking | 19 Hz   | 1.96 | 1.5 dB  |
| Peaking | 589 Hz  | 6.23 | 0.8 dB  |
| Peaking | 947 Hz  | 1.85 | -1.4 dB |
| Peaking | 1167 Hz | 1.61 | 0.9 dB  |
| Peaking | 8403 Hz | 3.86 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Solo/Monster%20Beats%20Solo.png)