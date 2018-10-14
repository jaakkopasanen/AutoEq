# Polk Audio UltraFit 1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.9; 60 5.0; 66 4.1; 72 3.2; 79 2.5; 87 1.7; 96 1.1; 106 0.4; 116 -0.1; 128 -0.7; 141 -1.4; 155 -1.9; 170 -2.3; 187 -2.8; 206 -3.2; 227 -3.5; 249 -3.8; 274 -4.0; 302 -4.1; 332 -4.0; 365 -4.1; 402 -3.9; 442 -3.8; 486 -3.4; 535 -3.4; 588 -3.5; 647 -3.6; 712 -3.6; 783 -3.6; 861 -3.5; 947 -2.4; 1042 1.3; 1146 -0.5; 1261 -1.2; 1387 -2.0; 1526 -2.4; 1678 -1.6; 1846 0.6; 2031 3.2; 2234 5.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 36 Hz   |  0.44 | 6.9 dB  |
| Peaking | 280 Hz  |  0.42 | -4.7 dB |
| Peaking | 785 Hz  |  2.89 | -2.6 dB |
| Peaking | 1574 Hz |  2.97 | -5.8 dB |
| Peaking | 3106 Hz |  0.62 | 7.3 dB  |
| Peaking | 1057 Hz | 12.42 | 2.9 dB  |
| Peaking | 2300 Hz |  4.93 | 1.9 dB  |
| Peaking | 5397 Hz |  0.38 | -1.6 dB |
| Peaking | 6264 Hz |  1.66 | 5.9 dB  |
| Peaking | 7592 Hz |  2.16 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%201000/Polk%20Audio%20UltraFit%201000.png)