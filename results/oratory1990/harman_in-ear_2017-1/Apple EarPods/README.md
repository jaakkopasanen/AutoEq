# Apple EarPods

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.8; 79 4.8; 87 3.8; 96 3.1; 106 2.6; 116 2.3; 128 2.1; 141 2.1; 155 2.1; 170 2.2; 187 2.3; 206 2.4; 227 2.5; 249 2.5; 274 2.5; 302 2.5; 332 2.6; 365 2.6; 402 2.4; 442 2.2; 486 2.2; 535 2.1; 588 1.9; 647 1.7; 712 1.5; 783 1.2; 861 0.8; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.9; 1387 -3.0; 1526 -4.4; 1678 -5.8; 1846 -6.7; 2031 -6.7; 2234 -6.3; 2457 -5.8; 2703 -5.4; 2973 -4.7; 3270 -3.7; 3597 -2.9; 3957 -2.5; 4353 -2.8; 4788 -3.9; 5267 -5.9; 5793 -7.7; 6373 -4.3; 7010 -1.0; 7711 -0.4; 8482 -2.6; 9330 -4.6; 10263 -3.4; 11289 -0.2; 12418 -2.5; 13660 -12.0; 15026 -17.0; 16529 -13.2; 18182 -9.2; 20000 -9.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.03 | 4.1 dB   |
| Peaking | 2103 Hz  | 1.27 | -7.2 dB  |
| Peaking | 5645 Hz  | 4.35 | -6.8 dB  |
| Peaking | 15026 Hz | 2.86 | -14.8 dB |
| Peaking | 18720 Hz | 0.89 | -8.5 dB  |
| Peaking | 108 Hz   | 0.27 | 5.9 dB   |
| Peaking | 143 Hz   | 0.52 | -7.6 dB  |
| Peaking | 7504 Hz  | 3.6  | 4.1 dB   |
| Peaking | 10644 Hz | 1.1  | -5.5 dB  |
| Peaking | 11594 Hz | 3.39 | 9.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Apple%20EarPods/Apple%20EarPods.png)