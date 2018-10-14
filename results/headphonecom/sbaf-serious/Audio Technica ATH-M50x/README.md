# Audio Technica ATH-M50x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.4; 23 -2.7; 25 -2.9; 28 -3.2; 31 -3.3; 34 -3.4; 37 -3.4; 41 -3.4; 45 -3.2; 49 -2.9; 54 -2.7; 60 -2.3; 66 -1.1; 72 0.5; 79 1.9; 87 0.2; 96 -2.8; 106 -4.5; 116 -3.4; 128 -4.0; 141 -4.7; 155 -3.7; 170 -2.3; 187 -2.7; 206 -1.4; 227 0.0; 249 1.2; 274 2.3; 302 3.3; 332 3.7; 365 3.8; 402 3.2; 442 2.5; 486 1.5; 535 0.9; 588 0.4; 647 0.1; 712 -0.2; 783 -0.3; 861 -0.1; 947 -0.1; 1042 0.1; 1146 0.6; 1261 -0.1; 1387 -0.7; 1526 -1.8; 1678 -2.7; 1846 -2.9; 2031 -2.4; 2234 -1.6; 2457 -0.6; 2703 0.6; 2973 2.4; 3270 4.0; 3597 5.1; 3957 3.6; 4353 0.8; 4788 3.5; 5267 6.0; 5793 5.4; 6373 4.9; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 1.25 | -3.8 dB |
| Peaking | 139 Hz  | 1.75 | -4.8 dB |
| Peaking | 340 Hz  | 2.02 | 4.6 dB  |
| Peaking | 3525 Hz | 5.39 | 5.0 dB  |
| Peaking | 5654 Hz | 3.15 | 6.3 dB  |
| Peaking | 55 Hz   | 2.68 | -1.7 dB |
| Peaking | 79 Hz   | 3.41 | 3.9 dB  |
| Peaking | 103 Hz  | 6.31 | -2.9 dB |
| Peaking | 1837 Hz | 2.98 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-M50x/Audio%20Technica%20ATH-M50x.png)