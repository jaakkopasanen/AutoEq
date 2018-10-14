# Ultrasone PRO 900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 -1.9; 23 -2.8; 25 -3.6; 28 -4.7; 31 -5.5; 34 -6.2; 37 -6.7; 41 -7.3; 45 -7.6; 49 -7.8; 54 -8.0; 60 -7.0; 66 -5.1; 72 -5.8; 79 -7.5; 87 -8.4; 96 -8.0; 106 -7.6; 116 -7.9; 128 -7.9; 141 -7.0; 155 -6.9; 170 -5.9; 187 -5.5; 206 -3.7; 227 -1.1; 249 2.2; 274 4.6; 302 3.3; 332 1.4; 365 0.2; 402 -0.7; 442 -0.8; 486 -0.8; 535 2.8; 588 2.8; 647 0.3; 712 0.1; 783 0.3; 861 -0.2; 947 -0.2; 1042 0.4; 1146 1.1; 1261 1.3; 1387 0.1; 1526 -1.0; 1678 -1.2; 1846 -0.3; 2031 1.0; 2234 0.7; 2457 -1.3; 2703 -5.7; 2973 -4.3; 3270 -4.3; 3597 -4.5; 3957 -4.5; 4353 -4.6; 4788 0.2; 5267 3.5; 5793 -1.7; 6373 -8.9; 7010 -6.1; 7711 -0.2; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -1.2; 13660 -5.9; 15026 -9.2; 16529 -8.7; 18182 -6.4; 20000 -4.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.9dB` and instead set Global volume in the UI for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.1dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 47 Hz    |  0.82 | -7.3 dB |
| Peaking | 122 Hz   |  1.58 | -7.0 dB |
| Peaking | 3423 Hz  |  1.87 | -5.1 dB |
| Peaking | 15205 Hz |  2.94 | -6.8 dB |
| Peaking | 17854 Hz |  1.14 | -6.5 dB |
| Peaking | 188 Hz   |  3.45 | -3.1 dB |
| Peaking | 275 Hz   |  4.01 | 6.5 dB  |
| Peaking | 562 Hz   | 11.23 | 5.2 dB  |
| Peaking | 5145 Hz  |  9.7  | 7.2 dB  |
| Peaking | 6527 Hz  |  7.39 | -9.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20900/Ultrasone%20PRO%20900.png)