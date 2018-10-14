# Shure SE315

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.3; 25 4.2; 28 4.2; 31 4.2; 34 4.0; 37 3.9; 41 3.7; 45 3.6; 49 3.4; 54 3.2; 60 2.9; 66 2.6; 72 2.4; 79 2.0; 87 1.7; 96 1.4; 106 1.2; 116 0.9; 128 0.9; 141 0.6; 155 0.3; 170 0.2; 187 0.3; 206 0.2; 227 0.1; 249 0.3; 274 0.4; 302 0.4; 332 0.7; 365 1.0; 402 1.1; 442 1.2; 486 1.3; 535 1.4; 588 1.7; 647 1.8; 712 1.7; 783 1.5; 861 1.2; 947 0.5; 1042 -0.3; 1146 -1.1; 1261 -2.0; 1387 -3.1; 1526 -4.1; 1678 -4.7; 1846 -4.3; 2031 -2.7; 2234 -0.2; 2457 3.0; 2703 5.9; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.65 | 4.1 dB  |
| Peaking | 58 Hz   | 1.06 | 1.6 dB  |
| Peaking | 666 Hz  | 1.15 | 2.0 dB  |
| Peaking | 1751 Hz | 1.49 | -9.2 dB |
| Peaking | 3306 Hz | 0.77 | 8.6 dB  |
| Peaking | 2167 Hz | 5.9  | -0.8 dB |
| Peaking | 2675 Hz | 5.34 | 1.8 dB  |
| Peaking | 3567 Hz | 2.95 | -1.2 dB |
| Peaking | 6252 Hz | 2.24 | 5.4 dB  |
| Peaking | 7424 Hz | 1.47 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE315/Shure%20SE315.png)