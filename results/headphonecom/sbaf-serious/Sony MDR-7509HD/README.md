# Sony MDR-7509HD

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 5.8; 141 5.0; 155 4.2; 170 4.0; 187 3.3; 206 3.0; 227 2.9; 249 3.9; 274 4.4; 302 3.7; 332 3.0; 365 0.8; 402 -1.3; 442 -2.4; 486 -2.3; 535 -2.8; 588 -2.3; 647 -0.7; 712 -0.5; 783 -1.1; 861 -1.3; 947 -0.5; 1042 0.3; 1146 0.3; 1261 0.3; 1387 -1.3; 1526 -3.2; 1678 -5.0; 1846 -4.7; 2031 -5.9; 2234 -4.7; 2457 -2.1; 2703 1.4; 2973 2.9; 3270 4.4; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.1; 5793 4.7; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -4.8; 9330 -7.4; 10263 -1.3; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7509HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.28 | 6.6 dB  |
| Peaking | 2048 Hz | 1.6  | -8.8 dB |
| Peaking | 3749 Hz | 0.99 | 8.0 dB  |
| Peaking | 6364 Hz | 6.33 | 3.5 dB  |
| Peaking | 9084 Hz | 4.73 | -9.6 dB |
| Peaking | 15 Hz   | 2.12 | 1.1 dB  |
| Peaking | 306 Hz  | 2.28 | 3.8 dB  |
| Peaking | 459 Hz  | 1.51 | -4.4 dB |
| Peaking | 1240 Hz | 3.12 | 2.1 dB  |
| Peaking | 1574 Hz | 6.11 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7509HD/Sony%20MDR-7509HD.png)