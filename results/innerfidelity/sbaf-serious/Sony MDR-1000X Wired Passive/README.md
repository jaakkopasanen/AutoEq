# Sony MDR-1000X Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 -2.1; 23 -3.0; 25 -3.8; 28 -4.8; 31 -5.6; 34 -6.4; 37 -7.0; 41 -7.7; 45 -8.3; 49 -8.8; 54 -9.4; 60 -9.8; 66 -10.1; 72 -10.2; 79 -10.0; 87 -9.7; 96 -9.3; 106 -9.3; 116 -10.1; 128 -10.1; 141 -8.6; 155 -8.2; 170 -5.7; 187 -6.7; 206 -5.8; 227 -4.5; 249 -3.4; 274 -2.7; 302 -2.3; 332 -2.1; 365 -2.2; 402 -2.3; 442 -2.4; 486 -2.9; 535 -3.0; 588 -2.6; 647 -3.3; 712 -3.3; 783 -1.9; 861 -1.9; 947 -0.9; 1042 0.5; 1146 2.1; 1261 3.4; 1387 3.5; 1526 2.3; 1678 0.8; 1846 0.2; 2031 1.0; 2234 3.0; 2457 4.2; 2703 2.4; 2973 -0.8; 3270 -3.0; 3597 -4.7; 3957 -7.3; 4353 -7.4; 4788 -4.4; 5267 -5.6; 5793 -2.8; 6373 0.6; 7010 1.7; 7711 -1.6; 8482 -4.7; 9330 -3.9; 10263 -0.3; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.3dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.86 | -3.4 dB |
| Peaking | 100 Hz  | 0.47 | -8.7 dB |
| Peaking | 2534 Hz | 1.04 | 4.5 dB  |
| Peaking | 4043 Hz | 2.03 | -9.9 dB |
| Peaking | 8819 Hz | 6.57 | -5.2 dB |
| Peaking | 298 Hz  | 2.17 | 1.8 dB  |
| Peaking | 727 Hz  | 1.11 | -2.9 dB |
| Peaking | 1299 Hz | 2.14 | 4.0 dB  |
| Peaking | 1832 Hz | 5    | -3.0 dB |
| Peaking | 6795 Hz | 9.63 | 4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wired%20Passive/Sony%20MDR-1000X%20Wired%20Passive.png)