# SoundMAGIC HP200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 21 -3.0; 23 -3.0; 25 -3.0; 28 -2.8; 31 -2.6; 34 -2.3; 37 -2.0; 41 -1.4; 45 -0.9; 49 -0.3; 54 0.6; 60 1.8; 66 0.8; 72 -1.8; 79 -3.5; 87 -3.3; 96 -4.3; 106 -5.5; 116 -5.8; 128 -6.2; 141 -6.1; 155 -5.4; 170 -5.0; 187 -5.6; 206 -5.1; 227 -4.4; 249 -3.9; 274 -3.2; 302 -2.5; 332 -1.8; 365 -0.9; 402 -0.1; 442 0.7; 486 1.1; 535 1.5; 588 2.1; 647 2.0; 712 1.7; 783 1.7; 861 1.2; 947 0.4; 1042 -0.2; 1146 -0.7; 1261 -1.2; 1387 -2.2; 1526 -3.6; 1678 -4.9; 1846 -6.4; 2031 -7.8; 2234 -9.2; 2457 -9.3; 2703 -8.6; 2973 -7.1; 3270 -6.6; 3597 -6.6; 3957 -6.5; 4353 -6.3; 4788 -4.1; 5267 -1.8; 5793 -1.2; 6373 1.9; 7010 -0.4; 7711 -5.5; 8482 -12.3; 9330 -15.1; 10263 -11.6; 11289 -4.3; 12418 -0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.1; 20000 -7.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.2dB` and instead set Global volume in the UI for both channels to **-22**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC HP200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 121 Hz  | 1.6  | -5.9 dB  |
| Peaking | 209 Hz  | 2.12 | -4.1 dB  |
| Peaking | 2337 Hz | 1.91 | -9.6 dB  |
| Peaking | 3899 Hz | 3.07 | -4.9 dB  |
| Peaking | 9343 Hz | 3.87 | -16.8 dB |
| Peaking | 15 Hz   | 0.31 | -3.1 dB  |
| Peaking | 59 Hz   | 3.68 | 4.3 dB   |
| Peaking | 655 Hz  | 1.82 | 2.8 dB   |
| Peaking | 6491 Hz | 5.44 | 5.1 dB   |
| Peaking | 8335 Hz | 7.66 | -3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SoundMAGIC%20HP200/SoundMAGIC%20HP200.png)