# Polk Audio UltraFit 3000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.9; 23 -10.0; 25 -10.1; 28 -10.3; 31 -10.4; 34 -10.4; 37 -10.4; 41 -10.5; 45 -10.5; 49 -10.6; 54 -10.7; 60 -10.8; 66 -10.9; 72 -11.0; 79 -11.1; 87 -11.1; 96 -11.1; 106 -11.0; 116 -10.9; 128 -10.7; 141 -10.6; 155 -10.3; 170 -10.0; 187 -9.6; 206 -9.1; 227 -8.6; 249 -8.1; 274 -7.5; 302 -6.8; 332 -6.0; 365 -5.2; 402 -4.5; 442 -3.9; 486 -3.2; 535 -2.5; 588 -1.9; 647 -1.2; 712 -0.8; 783 -0.3; 861 0.1; 947 -0.1; 1042 0.0; 1146 -0.1; 1261 -0.5; 1387 -1.2; 1526 -2.0; 1678 -2.5; 1846 -2.7; 2031 -2.8; 2234 -2.5; 2457 -1.5; 2703 0.1; 2973 2.1; 3270 4.0; 3597 4.7; 3957 3.8; 4353 2.8; 4788 3.3; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 38 Hz   | 0.22 | -10.2 dB |
| Peaking | 189 Hz  | 0.65 | -4.9 dB  |
| Peaking | 2059 Hz | 2.22 | -3.5 dB  |
| Peaking | 3481 Hz | 2.81 | 4.9 dB   |
| Peaking | 5756 Hz | 3.06 | 6.4 dB   |
| Peaking | 402 Hz  | 1.7  | -0.7 dB  |
| Peaking | 886 Hz  | 1.19 | 1.3 dB   |
| Peaking | 1564 Hz | 4.17 | -1.1 dB  |
| Peaking | 8226 Hz | 4.75 | -1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%203000/Polk%20Audio%20UltraFit%203000.png)