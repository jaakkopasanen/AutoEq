# Oppo PM1 Velour Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.3; 25 2.9; 28 2.6; 31 2.3; 34 2.2; 37 2.2; 41 2.1; 45 1.9; 49 2.1; 54 2.1; 60 1.1; 66 0.2; 72 -0.2; 79 -0.5; 87 -1.0; 96 -1.4; 106 -1.7; 116 -1.9; 128 -2.2; 141 -2.5; 155 -2.7; 170 -2.8; 187 -3.0; 206 -3.0; 227 -3.0; 249 -2.9; 274 -3.1; 302 -3.4; 332 -3.4; 365 -2.9; 402 -0.7; 442 -0.8; 486 -1.9; 535 -2.2; 588 -2.0; 647 -2.3; 712 -2.7; 783 -2.6; 861 -3.1; 947 -1.5; 1042 0.2; 1146 -0.0; 1261 -0.1; 1387 -0.4; 1526 -0.7; 1678 -0.5; 1846 0.1; 2031 0.7; 2234 1.4; 2457 2.1; 2703 2.4; 2973 2.9; 3270 3.1; 3597 3.0; 3957 3.4; 4353 3.3; 4788 4.2; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.7; 9330 -2.9; 10263 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 Velour Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.23 | 3.5 dB  |
| Peaking | 177 Hz  | 0.44 | -3.6 dB |
| Peaking | 795 Hz  | 2.8  | -2.4 dB |
| Peaking | 6492 Hz | 0.89 | 9.3 dB  |
| Peaking | 8403 Hz | 1.53 | -8.8 dB |
| Peaking | 344 Hz  | 4.2  | -1.2 dB |
| Peaking | 412 Hz  | 6.37 | 2.2 dB  |
| Peaking | 1095 Hz | 3.02 | 1.9 dB  |
| Peaking | 1795 Hz | 0.65 | -1.7 dB |
| Peaking | 2594 Hz | 1.7  | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1%20Velour%20Pads/Oppo%20PM1%20Velour%20Pads.png)