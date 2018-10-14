# Sony MDR-G75

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.8; 45 4.9; 49 3.8; 54 2.5; 60 1.2; 66 0.1; 72 -0.8; 79 -1.7; 87 -2.4; 96 -3.0; 106 -3.4; 116 -3.8; 128 -3.9; 141 -4.0; 155 -4.0; 170 -3.9; 187 -3.6; 206 -3.3; 227 -2.9; 249 -2.5; 274 -2.1; 302 -1.3; 332 -0.8; 365 -0.2; 402 0.2; 442 -0.2; 486 -0.1; 535 0.1; 588 0.3; 647 0.4; 712 0.5; 783 0.4; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.3; 1261 -0.5; 1387 -1.2; 1526 -2.3; 1678 -3.5; 1846 -3.3; 2031 -1.4; 2234 0.7; 2457 3.2; 2703 5.2; 2973 5.4; 3270 4.4; 3597 1.3; 3957 -2.1; 4353 -1.6; 4788 2.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.5; 9330 -1.6; 10263 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-G75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.7  | 7.2 dB  |
| Peaking | 123 Hz  | 0.79 | -5.2 dB |
| Peaking | 2952 Hz | 2.37 | 12.8 dB |
| Peaking | 3916 Hz | 0.72 | -9.6 dB |
| Peaking | 5608 Hz | 1.98 | 12.8 dB |
| Peaking | 639 Hz  | 1.4  | 0.7 dB  |
| Peaking | 1549 Hz | 0.68 | 1.3 dB  |
| Peaking | 1743 Hz | 2.87 | -3.8 dB |
| Peaking | 2387 Hz | 6.58 | 1.3 dB  |
| Peaking | 4152 Hz | 9.62 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-G75/Sony%20MDR-G75.png)