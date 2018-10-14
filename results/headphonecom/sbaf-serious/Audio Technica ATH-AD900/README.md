# Audio Technica ATH-AD900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 5.6; 72 5.2; 79 5.4; 87 5.8; 96 4.0; 106 3.4; 116 3.2; 128 2.5; 141 1.9; 155 1.5; 170 1.3; 187 1.1; 206 1.0; 227 0.8; 249 0.6; 274 0.7; 302 0.8; 332 1.0; 365 1.0; 402 1.0; 442 0.9; 486 0.8; 535 0.8; 588 0.8; 647 0.9; 712 0.9; 783 0.8; 861 0.3; 947 0.3; 1042 -0.1; 1146 -0.2; 1261 -0.9; 1387 -2.0; 1526 -4.0; 1678 -3.6; 1846 -1.9; 2031 -0.3; 2234 0.9; 2457 2.3; 2703 1.3; 2973 0.8; 3270 1.8; 3597 -2.1; 3957 -4.9; 4353 -5.9; 4788 -3.6; 5267 -0.4; 5793 2.4; 6373 2.7; 7010 2.4; 7711 0.3; 8482 -0.6; 9330 -3.1; 10263 -1.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.4  | 6.5 dB   |
| Peaking | 1628 Hz  | 2.72 | -6.1 dB  |
| Peaking | 4231 Hz  | 2.33 | -13.0 dB |
| Peaking | 4552 Hz  | 0.55 | 6.9 dB   |
| Peaking | 9340 Hz  | 2.67 | -5.5 dB  |
| Peaking | 39 Hz    | 2.56 | -0.6 dB  |
| Peaking | 85 Hz    | 6.77 | 1.7 dB   |
| Peaking | 159 Hz   | 2.5  | -0.7 dB  |
| Peaking | 13468 Hz | 3.7  | -0.6 dB  |
| Peaking | 16298 Hz | 1.77 | -0.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-AD900/Audio%20Technica%20ATH-AD900.png)