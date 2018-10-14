# AKG K271 MKII

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.8; 79 5.1; 87 4.6; 96 4.4; 106 4.6; 116 5.3; 128 6.0; 141 6.0; 155 6.0; 170 5.2; 187 3.4; 206 2.1; 227 0.9; 249 0.2; 274 -0.4; 302 -0.6; 332 -0.7; 365 -0.7; 402 -0.7; 442 -0.8; 486 -1.0; 535 -1.3; 588 -2.1; 647 -4.2; 712 -0.1; 783 1.9; 861 1.3; 947 0.5; 1042 -0.3; 1146 -0.8; 1261 -1.4; 1387 -2.1; 1526 -2.9; 1678 -3.4; 1846 -3.6; 2031 -1.9; 2234 1.0; 2457 1.8; 2703 3.5; 2973 4.6; 3270 3.7; 3597 3.8; 3957 5.8; 4353 6.0; 4788 6.0; 5267 6.0; 5793 2.8; 6373 0.4; 7010 -3.1; 7711 -3.9; 8482 -2.9; 9330 -0.1; 10263 0.0; 11289 -1.3; 12418 -4.9; 13660 -2.2; 15026 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.45 | 6.6 dB  |
| Peaking | 145 Hz   | 2.4  | 4.8 dB  |
| Peaking | 2908 Hz  | 1.98 | 7.6 dB  |
| Peaking | 4150 Hz  | 0.4  | -7.3 dB |
| Peaking | 4728 Hz  | 1.64 | 12.7 dB |
| Peaking | 688 Hz   | 2.18 | -9.0 dB |
| Peaking | 765 Hz   | 2.65 | 10.3 dB |
| Peaking | 7722 Hz  | 3.16 | -4.7 dB |
| Peaking | 11132 Hz | 1.01 | 5.4 dB  |
| Peaking | 12430 Hz | 3.12 | -8.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K271%20MKII/AKG%20K271%20MKII.png)