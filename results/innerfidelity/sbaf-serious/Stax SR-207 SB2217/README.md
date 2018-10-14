# Stax SR-207 SB2217

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.8dB
GraphicEQ: 21 0.0; 23 5.4; 25 4.8; 28 4.2; 31 3.8; 34 3.7; 37 3.7; 41 3.8; 45 3.9; 49 4.1; 54 4.2; 60 4.2; 66 4.1; 72 3.9; 79 3.6; 87 3.3; 96 3.0; 106 2.8; 116 2.6; 128 2.3; 141 2.2; 155 2.2; 170 2.1; 187 2.0; 206 1.9; 227 2.0; 249 2.0; 274 2.0; 302 2.0; 332 1.8; 365 1.9; 402 1.8; 442 1.9; 486 1.7; 535 1.7; 588 1.9; 647 1.7; 712 1.3; 783 1.3; 861 0.8; 947 0.3; 1042 -0.1; 1146 -0.7; 1261 -1.3; 1387 -2.3; 1526 -3.1; 1678 -3.5; 1846 -2.5; 2031 -0.1; 2234 1.7; 2457 3.1; 2703 2.1; 2973 1.7; 3270 1.2; 3597 1.6; 3957 2.5; 4353 1.5; 4788 0.9; 5267 1.7; 5793 0.0; 6373 1.7; 7010 2.4; 7711 0.3; 8482 -1.2; 9330 -3.4; 10263 -0.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.9; 20000 -2.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.8dB` and instead set Global volume in the UI for both channels to **-68**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-207 SB2217 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  0.11 | 4.7 dB  |
| Peaking | 445 Hz  |  0.63 | 1.5 dB  |
| Peaking | 1646 Hz |  1.56 | -8.2 dB |
| Peaking | 2158 Hz |  0.76 | 5.2 dB  |
| Peaking | 9293 Hz |  6.77 | -4.2 dB |
| Peaking | 36 Hz   |  2.45 | -0.8 dB |
| Peaking | 62 Hz   |  3.24 | 0.4 dB  |
| Peaking | 2521 Hz |  5.23 | 2.4 dB  |
| Peaking | 2778 Hz |  2.9  | -1.7 dB |
| Peaking | 6792 Hz | 10.56 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-207%20SB2217/Stax%20SR-207%20SB2217.png)