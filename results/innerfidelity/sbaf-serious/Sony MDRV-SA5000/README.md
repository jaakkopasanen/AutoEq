# Sony MDRV-SA5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.2; 72 4.2; 79 3.3; 87 2.4; 96 1.7; 106 1.4; 116 1.3; 128 1.4; 141 1.4; 155 1.2; 170 1.8; 187 2.1; 206 2.2; 227 2.5; 249 2.8; 274 3.2; 302 3.4; 332 3.7; 365 2.8; 402 1.6; 442 2.7; 486 2.5; 535 2.1; 588 1.9; 647 1.7; 712 0.9; 783 0.3; 861 -0.5; 947 -0.5; 1042 0.6; 1146 2.0; 1261 3.1; 1387 3.0; 1526 2.3; 1678 1.4; 1846 0.4; 2031 -0.9; 2234 -2.8; 2457 -3.8; 2703 -2.9; 2973 -0.6; 3270 2.3; 3597 5.9; 3957 5.8; 4353 2.9; 4788 4.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.9; 9330 -4.2; 10263 -0.2; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDRV-SA5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.62 | 6.8 dB  |
| Peaking | 340 Hz  | 0.92 | 3.0 dB  |
| Peaking | 3747 Hz | 6.98 | 6.0 dB  |
| Peaking | 5767 Hz | 2.64 | 6.8 dB  |
| Peaking | 8970 Hz | 4.88 | -5.6 dB |
| Peaking | 63 Hz   | 3.72 | 1.6 dB  |
| Peaking | 104 Hz  | 2.14 | -0.9 dB |
| Peaking | 944 Hz  | 2.61 | -3.7 dB |
| Peaking | 1239 Hz | 1.33 | 3.9 dB  |
| Peaking | 2424 Hz | 3.44 | -5.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDRV-SA5000/Sony%20MDRV-SA5000.png)