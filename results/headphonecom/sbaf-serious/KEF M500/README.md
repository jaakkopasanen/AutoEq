# KEF M500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.9; 23 -4.9; 25 -4.9; 28 -4.9; 31 -4.9; 34 -4.9; 37 -4.8; 41 -4.7; 45 -4.8; 49 -4.9; 54 -4.9; 60 -4.9; 66 -5.1; 72 -5.3; 79 -5.5; 87 -5.4; 96 -5.3; 106 -5.7; 116 -5.7; 128 -6.4; 141 -7.0; 155 -7.2; 170 -7.1; 187 -7.0; 206 -6.9; 227 -7.1; 249 -6.8; 274 -6.0; 302 -4.9; 332 -3.3; 365 -2.3; 402 -2.1; 442 -2.2; 486 -2.6; 535 -3.1; 588 -3.2; 647 -3.1; 712 -2.5; 783 -1.8; 861 -1.1; 947 -0.4; 1042 0.3; 1146 1.1; 1261 1.3; 1387 1.1; 1526 1.2; 1678 1.2; 1846 1.4; 2031 1.4; 2234 1.4; 2457 1.3; 2703 0.9; 2973 0.7; 3270 0.3; 3597 0.8; 3957 1.8; 4353 3.9; 4788 5.2; 5267 5.2; 5793 6.0; 6373 4.9; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.18 | -4.8 dB |
| Peaking | 200 Hz  | 0.98 | -5.3 dB |
| Peaking | 650 Hz  | 2.23 | -2.7 dB |
| Peaking | 1456 Hz | 1.02 | 1.6 dB  |
| Peaking | 5448 Hz | 2.33 | 6.4 dB  |
| Peaking | 275 Hz  | 5.2  | -1.0 dB |
| Peaking | 367 Hz  | 4.51 | 1.2 dB  |
| Peaking | 3352 Hz | 7.99 | -1.0 dB |
| Peaking | 6581 Hz | 5.89 | 2.2 dB  |
| Peaking | 7731 Hz | 2.49 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KEF%20M500/KEF%20M500.png)