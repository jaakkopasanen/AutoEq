# Sony MDR-SA5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.6; 87 4.6; 96 4.2; 106 4.0; 116 4.0; 128 4.1; 141 4.2; 155 4.2; 170 4.6; 187 4.7; 206 4.9; 227 4.9; 249 5.2; 274 5.3; 302 5.6; 332 5.2; 365 4.5; 402 4.7; 442 4.5; 486 4.0; 535 3.4; 588 2.6; 647 2.1; 712 1.5; 783 0.9; 861 0.2; 947 -0.3; 1042 0.5; 1146 2.5; 1261 4.0; 1387 4.4; 1526 4.1; 1678 3.5; 1846 2.3; 2031 1.0; 2234 0.2; 2457 -3.0; 2703 -6.6; 2973 -5.5; 3270 -2.8; 3597 0.7; 3957 1.2; 4353 -1.3; 4788 0.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 0.9; 7711 -3.1; 8482 -4.2; 9330 -4.6; 10263 -1.4; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-SA5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.06 | 5.3 dB  |
| Peaking | 1121 Hz | 0.22 | 2.0 dB  |
| Peaking | 2811 Hz | 4    | -9.2 dB |
| Peaking | 5935 Hz | 3.53 | 7.3 dB  |
| Peaking | 8550 Hz | 2.61 | -6.1 dB |
| Peaking | 124 Hz  | 2.07 | -1.5 dB |
| Peaking | 346 Hz  | 1.13 | 1.3 dB  |
| Peaking | 967 Hz  | 1.62 | -4.9 dB |
| Peaking | 1343 Hz | 1.56 | 5.1 dB  |
| Peaking | 2192 Hz | 0.7  | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-SA5000/Sony%20MDR-SA5000.png)