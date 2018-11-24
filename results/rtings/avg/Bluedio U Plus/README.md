# Bluedio U Plus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.8; 23 -6.2; 25 -6.6; 28 -6.9; 31 -7.0; 34 -7.0; 37 -7.0; 41 -7.0; 45 -7.1; 49 -7.2; 54 -7.4; 60 -7.6; 66 -7.8; 72 -8.0; 79 -8.2; 87 -8.5; 96 -8.7; 106 -9.0; 116 -9.2; 128 -9.2; 141 -9.0; 155 -8.4; 170 -7.4; 187 -6.0; 206 -4.3; 227 -2.0; 249 0.8; 274 2.5; 302 4.1; 332 5.9; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 6.0; 783 6.0; 861 5.5; 947 1.8; 1042 -0.7; 1146 -0.8; 1261 -0.2; 1387 -0.3; 1526 -1.0; 1678 -1.8; 1846 -1.7; 2031 -2.6; 2234 -4.2; 2457 -5.2; 2703 -6.0; 2973 -6.2; 3270 -5.4; 3597 -2.8; 3957 0.3; 4353 3.8; 4788 1.6; 5267 -1.2; 5793 -0.0; 6373 3.1; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -2.5; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio U Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio U Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.37 | -6.4 dB |
| Peaking | 108 Hz  | 0.97 | -5.0 dB |
| Peaking | 170 Hz  | 1.33 | -6.6 dB |
| Peaking | 405 Hz  | 0.68 | 8.4 dB  |
| Peaking | 2610 Hz | 2    | -6.9 dB |
| Peaking | 836 Hz  | 2.86 | 6.3 dB  |
| Peaking | 986 Hz  | 1.9  | -5.2 dB |
| Peaking | 2720 Hz | 2.85 | 2.1 dB  |
| Peaking | 3182 Hz | 3.47 | -3.7 dB |
| Peaking | 4355 Hz | 4.93 | 5.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20U%20Plus/Bluedio%20U%20Plus.png)