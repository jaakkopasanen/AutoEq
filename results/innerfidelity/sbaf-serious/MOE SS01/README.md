# MOE SS01

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.7dB
GraphicEQ: 21 -5.2; 23 -5.3; 25 -5.4; 28 -5.4; 31 -5.5; 34 -5.5; 37 -5.6; 41 -5.6; 45 -5.6; 49 -5.7; 54 -5.8; 60 -5.8; 66 -6.0; 72 -6.2; 79 -6.3; 87 -6.5; 96 -6.7; 106 -6.7; 116 -6.7; 128 -6.7; 141 -6.6; 155 -6.5; 170 -6.3; 187 -6.0; 206 -5.8; 227 -5.3; 249 -4.9; 274 -4.5; 302 -4.0; 332 -3.5; 365 -2.9; 402 -2.4; 442 -1.8; 486 -1.4; 535 -0.9; 588 -0.2; 647 0.1; 712 0.2; 783 0.6; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.5; 1526 -2.3; 1678 -2.3; 1846 -2.0; 2031 -2.3; 2234 -2.8; 2457 -2.9; 2703 -3.4; 2973 -3.3; 3270 -1.7; 3597 -0.5; 3957 -1.4; 4353 -4.2; 4788 -6.3; 5267 -6.5; 5793 -4.4; 6373 -1.9; 7010 -0.6; 7711 -0.8; 8482 -2.7; 9330 -3.2; 10263 -0.4; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.7dB` and instead set Global volume in the UI for both channels to **-6**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MOE SS01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.28 | -5.2 dB |
| Peaking | 132 Hz  | 0.82 | -4.1 dB |
| Peaking | 256 Hz  | 1.4  | -2.4 dB |
| Peaking | 2322 Hz | 1.53 | -2.9 dB |
| Peaking | 5116 Hz | 3.17 | -6.8 dB |
| Peaking | 785 Hz  | 2.73 | 1.2 dB  |
| Peaking | 1535 Hz | 4.28 | -1.5 dB |
| Peaking | 2873 Hz | 8.21 | -1.7 dB |
| Peaking | 4515 Hz | 0.29 | 0.5 dB  |
| Peaking | 9047 Hz | 5.22 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MOE%20SS01/MOE%20SS01.png)