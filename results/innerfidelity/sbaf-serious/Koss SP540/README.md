# Koss SP540

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.9dB
GraphicEQ: 21 -8.9; 23 -9.3; 25 -9.5; 28 -9.8; 31 -10.1; 34 -10.2; 37 -10.4; 41 -10.6; 45 -10.7; 49 -10.8; 54 -10.9; 60 -11.1; 66 -11.3; 72 -11.4; 79 -11.6; 87 -11.8; 96 -12.0; 106 -12.0; 116 -11.9; 128 -11.8; 141 -11.8; 155 -12.2; 170 -11.5; 187 -10.9; 206 -10.8; 227 -10.9; 249 -11.2; 274 -10.5; 302 -9.2; 332 -9.6; 365 -8.4; 402 -6.8; 442 -5.9; 486 -5.2; 535 -4.3; 588 -3.1; 647 -2.8; 712 -2.4; 783 -1.7; 861 -1.2; 947 -0.5; 1042 0.4; 1146 1.3; 1261 1.4; 1387 1.0; 1526 -0.0; 1678 -1.3; 1846 -2.2; 2031 -3.0; 2234 -4.4; 2457 -5.5; 2703 -6.6; 2973 -7.2; 3270 -7.5; 3597 -6.2; 3957 -4.4; 4353 -1.6; 4788 1.7; 5267 -2.5; 5793 -0.2; 6373 1.1; 7010 -1.3; 7711 -1.9; 8482 -1.8; 9330 -1.6; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.0; 16529 -1.8; 18182 -2.5; 20000 -3.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.9dB` and instead set Global volume in the UI for both channels to **-19**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SP540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 40 Hz   |  0.32 | -9.2 dB |
| Peaking | 145 Hz  |  0.67 | -6.4 dB |
| Peaking | 311 Hz  |  1.18 | -5.6 dB |
| Peaking | 3019 Hz |  2.09 | -8.1 dB |
| Peaking | 20 Hz   |  1.14 | -1.1 dB |
| Peaking | 1251 Hz |  1.65 | 5.7 dB  |
| Peaking | 1351 Hz |  0.81 | -3.1 dB |
| Peaking | 4785 Hz | 10.92 | 4.1 dB  |
| Peaking | 8430 Hz |  4.16 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20SP540/Koss%20SP540.png)