# Audio Technica ATH-M10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 5.1; 54 4.9; 60 4.7; 66 5.0; 72 6.0; 79 5.8; 87 3.2; 96 4.6; 106 2.8; 116 1.9; 128 1.4; 141 1.0; 155 0.9; 170 1.1; 187 0.8; 206 0.9; 227 0.7; 249 0.7; 274 0.7; 302 0.8; 332 1.0; 365 1.2; 402 1.3; 442 1.2; 486 1.2; 535 1.0; 588 1.0; 647 0.7; 712 0.4; 783 0.2; 861 -0.2; 947 -0.5; 1042 0.9; 1146 3.8; 1261 1.4; 1387 1.4; 1526 2.8; 1678 4.1; 1846 3.4; 2031 4.3; 2234 5.9; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 28 Hz   |  0.5  | 6.2 dB  |
| Peaking | 76 Hz   |  2.35 | 3.0 dB  |
| Peaking | 410 Hz  |  2.15 | 1.1 dB  |
| Peaking | 2786 Hz |  0.95 | 6.1 dB  |
| Peaking | 5420 Hz |  2.34 | 4.6 dB  |
| Peaking | 973 Hz  |  3.51 | -1.9 dB |
| Peaking | 1114 Hz | 10.53 | 4.0 dB  |
| Peaking | 6464 Hz |  6.55 | 2.1 dB  |
| Peaking | 6569 Hz |  4.37 | 0.5 dB  |
| Peaking | 7852 Hz |  2.06 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-M10/Audio%20Technica%20ATH-M10.png)