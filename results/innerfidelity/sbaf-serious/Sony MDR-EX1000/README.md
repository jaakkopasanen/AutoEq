# Sony MDR-EX1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.2; 25 4.0; 28 3.7; 31 3.5; 34 3.3; 37 3.1; 41 2.9; 45 2.7; 49 2.5; 54 2.2; 60 1.9; 66 1.5; 72 1.1; 79 0.7; 87 0.3; 96 -0.1; 106 -0.4; 116 -0.7; 128 -1.0; 141 -1.4; 155 -1.6; 170 -1.7; 187 -1.7; 206 -1.9; 227 -1.8; 249 -1.8; 274 -1.7; 302 -1.5; 332 -1.4; 365 -1.2; 402 -1.1; 442 -0.7; 486 -0.6; 535 -0.3; 588 0.2; 647 0.5; 712 0.5; 783 0.9; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.7; 1261 -1.3; 1387 -2.2; 1526 -3.1; 1678 -3.7; 1846 -3.6; 2031 -3.0; 2234 -1.8; 2457 0.3; 2703 2.2; 2973 4.8; 3270 6.0; 3597 6.0; 3957 4.8; 4353 0.4; 4788 -4.5; 5267 -5.8; 5793 -1.2; 6373 1.4; 7010 0.4; 7711 -3.8; 8482 -4.4; 9330 -0.5; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.98 | 4.3 dB  |
| Peaking | 1834 Hz | 1.91 | -4.9 dB |
| Peaking | 3441 Hz | 2.13 | 7.9 dB  |
| Peaking | 4900 Hz | 4.61 | -3.2 dB |
| Peaking | 5111 Hz | 5.04 | -5.5 dB |
| Peaking | 60 Hz   | 1.54 | 1.3 dB  |
| Peaking | 210 Hz  | 0.61 | -2.0 dB |
| Peaking | 755 Hz  | 1.92 | 1.5 dB  |
| Peaking | 6547 Hz | 5.21 | 2.8 dB  |
| Peaking | 8098 Hz | 5.13 | -5.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-EX1000/Sony%20MDR-EX1000.png)