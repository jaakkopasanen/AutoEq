# Bluedio U Plus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.4; 23 -5.9; 25 -6.3; 28 -6.7; 31 -6.9; 34 -7.0; 37 -7.1; 41 -7.2; 45 -7.4; 49 -7.6; 54 -7.7; 60 -7.9; 66 -8.0; 72 -8.0; 79 -8.0; 87 -8.1; 96 -8.3; 106 -8.5; 116 -8.7; 128 -8.7; 141 -8.5; 155 -7.8; 170 -6.8; 187 -5.4; 206 -3.8; 227 -1.5; 249 1.3; 274 3.2; 302 4.9; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 6.0; 783 6.0; 861 5.6; 947 1.8; 1042 -0.7; 1146 -0.6; 1261 0.1; 1387 -0.3; 1526 -1.3; 1678 -2.1; 1846 -1.7; 2031 -2.2; 2234 -3.8; 2457 -4.8; 2703 -5.2; 2973 -4.7; 3270 -2.8; 3597 0.4; 3957 2.7; 4353 5.1; 4788 3.2; 5267 1.7; 5793 3.9; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -3.6; 10263 -0.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio U Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio U Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.48 | -5.8 dB |
| Peaking | 99 Hz   | 0.7  | -5.2 dB |
| Peaking | 168 Hz  | 1.15 | -7.1 dB |
| Peaking | 375 Hz  | 0.64 | 9.0 dB  |
| Peaking | 2450 Hz | 2.51 | -6.0 dB |
| Peaking | 828 Hz  | 2.36 | 8.1 dB  |
| Peaking | 953 Hz  | 1.49 | -6.5 dB |
| Peaking | 4326 Hz | 5.31 | 5.5 dB  |
| Peaking | 6304 Hz | 4.7  | 5.7 dB  |
| Peaking | 9531 Hz | 7.73 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bluedio%20U%20Plus/Bluedio%20U%20Plus.png)