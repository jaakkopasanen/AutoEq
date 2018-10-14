# Xiaomi Piston 3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 21 -2.9; 23 -3.4; 25 -3.8; 28 -4.4; 31 -4.9; 34 -5.3; 37 -5.7; 41 -6.0; 45 -6.4; 49 -6.7; 54 -7.0; 60 -7.4; 66 -7.7; 72 -7.9; 79 -8.3; 87 -8.6; 96 -8.9; 106 -8.9; 116 -8.9; 128 -9.0; 141 -8.9; 155 -8.8; 170 -8.6; 187 -8.3; 206 -7.9; 227 -7.4; 249 -7.0; 274 -6.4; 302 -5.8; 332 -5.3; 365 -4.6; 402 -4.0; 442 -3.2; 486 -2.6; 535 -2.0; 588 -1.1; 647 -0.5; 712 -0.1; 783 0.4; 861 0.5; 947 0.4; 1042 -0.2; 1146 -1.0; 1261 -1.9; 1387 -3.0; 1526 -3.8; 1678 -4.4; 1846 -4.7; 2031 -4.8; 2234 -5.0; 2457 -4.7; 2703 -4.3; 2973 -2.9; 3270 -1.4; 3597 -0.9; 3957 -2.6; 4353 -5.8; 4788 -6.4; 5267 -2.3; 5793 2.0; 6373 4.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.3; 10263 -1.2; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.8dB` and instead set Global volume in the UI for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Piston 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 76 Hz   | 0.41 | -7.5 dB |
| Peaking | 207 Hz  | 0.84 | -4.3 dB |
| Peaking | 2083 Hz | 1.64 | -5.3 dB |
| Peaking | 4676 Hz | 4.73 | -7.3 dB |
| Peaking | 6398 Hz | 4.66 | 5.8 dB  |
| Peaking | 852 Hz  | 2.36 | 2.0 dB  |
| Peaking | 1502 Hz | 3.32 | -1.6 dB |
| Peaking | 2676 Hz | 1.64 | 1.8 dB  |
| Peaking | 2688 Hz | 3.97 | -2.9 dB |
| Peaking | 9933 Hz | 7.62 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Piston%203/Xiaomi%20Piston%203.png)