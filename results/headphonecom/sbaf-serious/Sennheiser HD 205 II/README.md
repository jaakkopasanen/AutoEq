# Sennheiser HD 205 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.4; 23 -0.6; 25 -0.7; 28 -0.7; 31 -0.7; 34 -0.9; 37 -1.2; 41 -1.4; 45 -1.6; 49 -1.7; 54 -1.9; 60 -1.6; 66 -1.3; 72 -2.1; 79 -3.0; 87 -3.4; 96 -3.8; 106 -3.8; 116 -3.9; 128 -3.6; 141 -2.7; 155 -2.9; 170 -2.8; 187 -3.0; 206 -2.6; 227 -2.8; 249 -2.3; 274 -2.2; 302 -1.6; 332 -0.4; 365 1.0; 402 2.3; 442 2.5; 486 1.4; 535 0.2; 588 0.1; 647 1.8; 712 4.3; 783 4.0; 861 2.1; 947 0.6; 1042 -0.4; 1146 -1.2; 1261 -1.6; 1387 -2.0; 1526 -2.5; 1678 -2.4; 1846 -1.8; 2031 -1.2; 2234 -0.1; 2457 1.5; 2703 3.6; 2973 4.2; 3270 4.8; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.9; 5267 2.9; 5793 5.2; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.5; 9330 -0.3; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 205 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 106 Hz  | 0.81 | -3.6 dB |
| Peaking | 280 Hz  | 1.3  | -4.0 dB |
| Peaking | 394 Hz  | 1.07 | 4.2 dB  |
| Peaking | 3857 Hz | 2.2  | 6.7 dB  |
| Peaking | 6183 Hz | 5.12 | 5.1 dB  |
| Peaking | 577 Hz  | 4.66 | -2.8 dB |
| Peaking | 744 Hz  | 3.14 | 4.7 dB  |
| Peaking | 1567 Hz | 1.23 | -3.2 dB |
| Peaking | 2783 Hz | 3.88 | 2.8 dB  |
| Peaking | 8731 Hz | 5.6  | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20205%20II/Sennheiser%20HD%20205%20II.png)