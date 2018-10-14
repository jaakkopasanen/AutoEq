# Sony MDR-7502

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 5.9; 535 4.3; 588 2.9; 647 1.8; 712 1.3; 783 1.3; 861 0.7; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.5; 1387 -1.5; 1526 -2.6; 1678 -2.1; 1846 -1.9; 2031 -0.7; 2234 0.6; 2457 2.3; 2703 3.7; 2973 5.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7502 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.13 | 6.2 dB  |
| Peaking | 398 Hz  | 1.3  | 3.3 dB  |
| Peaking | 1698 Hz | 1.19 | -4.1 dB |
| Peaking | 3384 Hz | 1.3  | 6.8 dB  |
| Peaking | 5644 Hz | 2.84 | 4.6 dB  |
| Peaking | 498 Hz  | 5.54 | 1.7 dB  |
| Peaking | 606 Hz  | 1.71 | -0.9 dB |
| Peaking | 1247 Hz | 6.79 | 0.9 dB  |
| Peaking | 6520 Hz | 7.29 | 2.2 dB  |
| Peaking | 7883 Hz | 2.24 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7502/Sony%20MDR-7502.png)