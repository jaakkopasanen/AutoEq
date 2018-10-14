# Audio Technica ATH-MSR7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.6; 31 5.3; 34 4.9; 37 4.6; 41 4.3; 45 4.0; 49 3.7; 54 3.5; 60 3.2; 66 2.9; 72 2.6; 79 2.3; 87 1.9; 96 1.5; 106 1.3; 116 1.1; 128 0.8; 141 0.7; 155 0.4; 170 0.6; 187 0.9; 206 0.7; 227 0.7; 249 0.7; 274 1.0; 302 1.3; 332 1.8; 365 2.5; 402 3.1; 442 3.6; 486 3.6; 535 3.5; 588 3.5; 647 2.7; 712 1.8; 783 1.4; 861 0.7; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.4; 1387 -1.1; 1526 -1.8; 1678 -2.2; 1846 -2.1; 2031 -1.3; 2234 0.5; 2457 2.1; 2703 3.6; 2973 4.9; 3270 5.4; 3597 5.5; 3957 4.7; 4353 1.4; 4788 1.3; 5267 5.1; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-MSR7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 23 Hz   |  0.67 | 5.8 dB  |
| Peaking | 60 Hz   |  1.01 | 1.5 dB  |
| Peaking | 487 Hz  |  1.7  | 4.0 dB  |
| Peaking | 3343 Hz |  3.09 | 6.1 dB  |
| Peaking | 5926 Hz |  3.93 | 6.4 dB  |
| Peaking | 641 Hz  |  4.68 | 0.8 dB  |
| Peaking | 1768 Hz |  2.06 | -3.1 dB |
| Peaking | 2605 Hz |  3.3  | 2.1 dB  |
| Peaking | 4585 Hz | 12.14 | -1.5 dB |
| Peaking | 8222 Hz |  5.71 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-MSR7/Audio%20Technica%20ATH-MSR7.png)