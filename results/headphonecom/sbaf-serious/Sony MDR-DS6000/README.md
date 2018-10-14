# Sony MDR-DS6000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.9; 54 5.0; 60 4.0; 66 2.6; 72 1.2; 79 0.0; 87 -1.0; 96 -1.8; 106 -2.3; 116 -2.7; 128 -2.8; 141 -2.7; 155 -2.6; 170 -2.2; 187 -2.2; 206 -1.6; 227 -1.5; 249 -1.5; 274 -1.2; 302 -0.8; 332 -0.6; 365 -0.4; 402 -0.2; 442 0.3; 486 -0.0; 535 -0.4; 588 -0.6; 647 -0.9; 712 -1.4; 783 -1.6; 861 -1.2; 947 0.1; 1042 -0.5; 1146 -1.6; 1261 -2.7; 1387 -2.9; 1526 -3.7; 1678 -4.6; 1846 -5.2; 2031 -5.7; 2234 -4.8; 2457 -2.8; 2703 -0.4; 2973 1.4; 3270 3.3; 3597 5.5; 3957 6.0; 4353 4.2; 4788 5.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-DS6000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.41 | 8.5 dB  |
| Peaking | 105 Hz  | 0.72 | -7.5 dB |
| Peaking | 1990 Hz | 1.43 | -6.6 dB |
| Peaking | 3697 Hz | 1.94 | 6.6 dB  |
| Peaking | 5750 Hz | 3.03 | 5.6 dB  |
| Peaking | 446 Hz  | 5.06 | 0.9 dB  |
| Peaking | 797 Hz  | 2.75 | -1.3 dB |
| Peaking | 977 Hz  | 4.73 | 1.8 dB  |
| Peaking | 1254 Hz | 6.93 | -0.7 dB |
| Peaking | 8238 Hz | 4.66 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-DS6000/Sony%20MDR-DS6000.png)