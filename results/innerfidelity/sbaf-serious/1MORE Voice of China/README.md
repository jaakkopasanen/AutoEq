# 1MORE Voice of China

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 21 0.0; 23 0.4; 25 -0.2; 28 -0.9; 31 -1.5; 34 -2.0; 37 -2.4; 41 -2.9; 45 -3.4; 49 -3.8; 54 -4.2; 60 -4.7; 66 -5.1; 72 -5.4; 79 -5.9; 87 -6.3; 96 -6.7; 106 -6.8; 116 -7.0; 128 -7.1; 141 -7.2; 155 -7.1; 170 -7.0; 187 -6.8; 206 -6.6; 227 -6.2; 249 -5.8; 274 -5.4; 302 -4.8; 332 -4.4; 365 -3.8; 402 -3.2; 442 -2.5; 486 -2.1; 535 -1.6; 588 -0.7; 647 -0.3; 712 -0.1; 783 0.4; 861 0.5; 947 0.3; 1042 0.0; 1146 -0.2; 1261 -0.5; 1387 -0.9; 1526 -1.4; 1678 -2.0; 1846 -2.2; 2031 -2.3; 2234 -2.8; 2457 -3.4; 2703 -3.8; 2973 -3.4; 3270 -2.4; 3597 -1.6; 3957 -2.5; 4353 -5.4; 4788 -7.5; 5267 -6.4; 5793 -1.4; 6373 2.1; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.4; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.4dB` and instead set Global volume in the UI for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Voice of China ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.2dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 104 Hz  |  0.58 | -6.2 dB |
| Peaking | 239 Hz  |  1.03 | -3.4 dB |
| Peaking | 2505 Hz |  1.87 | -3.4 dB |
| Peaking | 4935 Hz |  3.4  | -8.3 dB |
| Peaking | 6556 Hz |  4.18 | 4.8 dB  |
| Peaking | 18 Hz   |  2.47 | 1.8 dB  |
| Peaking | 410 Hz  |  2.54 | -0.6 dB |
| Peaking | 813 Hz  |  1.82 | 1.3 dB  |
| Peaking | 1688 Hz |  4.38 | -0.9 dB |
| Peaking | 3670 Hz | 10.18 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Voice%20of%20China/1MORE%20Voice%20of%20China.png)