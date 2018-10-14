# AKG K240 MKII

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.2; 28 3.3; 31 2.6; 34 1.9; 37 1.2; 41 0.5; 45 0.2; 49 -0.3; 54 -1.0; 60 -0.9; 66 -1.2; 72 -2.7; 79 -3.8; 87 -4.7; 96 -5.4; 106 -5.9; 116 -6.3; 128 -6.5; 141 -6.7; 155 -6.4; 170 -6.1; 187 -5.9; 206 -5.6; 227 -5.1; 249 -4.6; 274 -4.6; 302 -4.4; 332 -4.2; 365 -3.8; 402 -3.5; 442 -3.4; 486 -3.3; 535 0.1; 588 -1.0; 647 -1.1; 712 -0.9; 783 -0.7; 861 -0.4; 947 -0.1; 1042 0.2; 1146 0.5; 1261 0.5; 1387 -0.1; 1526 -1.0; 1678 -1.7; 1846 -2.9; 2031 -3.1; 2234 -3.9; 2457 -3.4; 2703 -1.5; 2973 -0.6; 3270 1.2; 3597 2.0; 3957 0.5; 4353 -0.5; 4788 -0.8; 5267 1.6; 5793 1.7; 6373 -0.3; 7010 -2.4; 7711 -5.2; 8482 -8.9; 9330 -9.5; 10263 -5.5; 11289 -1.0; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.2dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 13 Hz   | 0.16 | 6.4 dB   |
| Peaking | 122 Hz  | 0.38 | -8.2 dB  |
| Peaking | 2193 Hz | 1.8  | -6.0 dB  |
| Peaking | 4019 Hz | 0.21 | 2.6 dB   |
| Peaking | 8926 Hz | 2.51 | -12.6 dB |
| Peaking | 38 Hz   | 3.02 | -0.6 dB  |
| Peaking | 446 Hz  | 7.21 | -1.1 dB  |
| Peaking | 3524 Hz | 4.38 | 2.6 dB   |
| Peaking | 4742 Hz | 1.95 | -3.5 dB  |
| Peaking | 5533 Hz | 4.12 | 4.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K240%20MKII/AKG%20K240%20MKII.png)