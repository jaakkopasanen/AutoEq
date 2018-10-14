# Sennheiser HD 580 (HD600 headband)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.6; 41 5.0; 45 4.4; 49 4.0; 54 3.6; 60 3.2; 66 2.6; 72 2.0; 79 1.8; 87 1.1; 96 0.3; 106 -0.1; 116 -0.4; 128 -0.7; 141 -1.0; 155 -1.2; 170 -1.1; 187 -1.1; 206 -1.2; 227 -1.1; 249 -0.9; 274 -0.8; 302 -0.6; 332 -0.5; 365 -0.3; 402 -0.1; 442 0.1; 486 -0.0; 535 -0.0; 588 0.3; 647 0.3; 712 0.1; 783 0.2; 861 -0.1; 947 -0.2; 1042 -0.2; 1146 -0.8; 1261 -0.9; 1387 -1.5; 1526 -1.9; 1678 -2.2; 1846 -2.2; 2031 -1.9; 2234 -1.6; 2457 -1.4; 2703 -1.4; 2973 -1.3; 3270 -1.7; 3597 -1.7; 3957 -0.7; 4353 -0.9; 4788 -0.9; 5267 1.5; 5793 4.1; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 580 (HD600 headband) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.49 | 6.2 dB  |
| Peaking | 148 Hz  | 0.91 | -2.0 dB |
| Peaking | 1717 Hz | 2.32 | -1.9 dB |
| Peaking | 4681 Hz | 0.71 | -2.0 dB |
| Peaking | 6183 Hz | 3.48 | 7.6 dB  |
| Peaking | 652 Hz  | 2.31 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20580%20(HD600%20headband)/Sennheiser%20HD%20580%20(HD600%20headband).png)