# Fischer Audio FA-003

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 21 0.0; 23 2.7; 25 2.2; 28 1.5; 31 1.0; 34 0.5; 37 0.2; 41 -0.2; 45 -0.5; 49 -0.7; 54 -0.9; 60 -1.0; 66 -1.0; 72 -1.0; 79 -1.3; 87 -2.0; 96 -3.3; 106 -4.2; 116 -4.3; 128 -4.8; 141 -5.2; 155 -5.1; 170 -4.5; 187 -4.6; 206 -3.7; 227 -2.3; 249 -0.3; 274 2.6; 302 4.5; 332 3.3; 365 1.4; 402 0.7; 442 -0.6; 486 -1.2; 535 -1.5; 588 -1.3; 647 -1.4; 712 -1.2; 783 -0.5; 861 -0.5; 947 -0.4; 1042 0.2; 1146 0.6; 1261 0.9; 1387 0.6; 1526 0.3; 1678 -0.0; 1846 -0.2; 2031 -0.3; 2234 -0.2; 2457 -0.3; 2703 -0.8; 2973 -1.6; 3270 0.0; 3597 0.1; 3957 -1.8; 4353 -3.5; 4788 -3.6; 5267 -2.4; 5793 -3.9; 6373 -0.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.9; 20000 -4.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.6dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.45 | 3.5 dB  |
| Peaking | 157 Hz  | 0.87 | -5.7 dB |
| Peaking | 302 Hz  | 2.87 | 7.0 dB  |
| Peaking | 563 Hz  | 2.46 | -1.5 dB |
| Peaking | 4758 Hz | 3.04 | -4.0 dB |
| Peaking | 1266 Hz | 4.01 | 1.1 dB  |
| Peaking | 3006 Hz | 5.06 | -1.7 dB |
| Peaking | 3413 Hz | 6.28 | 1.9 dB  |
| Peaking | 5994 Hz | 7.79 | -3.8 dB |
| Peaking | 6780 Hz | 7.11 | 4.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20FA-003/Fischer%20Audio%20FA-003.png)