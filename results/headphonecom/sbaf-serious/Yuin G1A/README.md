# Yuin G1A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.8; 54 4.9; 60 3.7; 66 2.6; 72 1.9; 79 1.4; 87 0.4; 96 -0.5; 106 -1.2; 116 -1.7; 128 -2.2; 141 -2.5; 155 -2.8; 170 -2.7; 187 -2.6; 206 -2.6; 227 -2.4; 249 -2.1; 274 -2.0; 302 -1.7; 332 -1.3; 365 -1.0; 402 -0.7; 442 -0.4; 486 -0.3; 535 0.1; 588 0.1; 647 0.3; 712 0.5; 783 0.5; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.4; 1261 -0.6; 1387 -0.9; 1526 -1.4; 1678 -2.8; 1846 -3.6; 2031 -4.3; 2234 -4.2; 2457 -3.7; 2703 -1.1; 2973 1.8; 3270 6.0; 3597 6.0; 3957 3.7; 4353 -3.0; 4788 -8.6; 5267 -3.8; 5793 0.9; 6373 5.3; 7010 1.4; 7711 -0.1; 8482 -1.6; 9330 -4.0; 10263 -2.2; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin G1A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.4dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 1.18 | 7.3 dB   |
| Peaking | 2242 Hz | 1.8  | -6.2 dB  |
| Peaking | 3572 Hz | 2.35 | 10.9 dB  |
| Peaking | 4753 Hz | 3.41 | -11.9 dB |
| Peaking | 6285 Hz | 6.66 | 7.2 dB   |
| Peaking | 32 Hz   | 1.71 | -6.5 dB  |
| Peaking | 35 Hz   | 0.43 | 5.7 dB   |
| Peaking | 138 Hz  | 0.58 | -4.4 dB  |
| Peaking | 693 Hz  | 1.19 | 1.1 dB   |
| Peaking | 9454 Hz | 5.77 | -4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20G1A/Yuin%20G1A.png)