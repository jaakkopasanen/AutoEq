# Panasonic RP-HC56

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.3; 28 5.1; 31 4.9; 34 4.8; 37 4.7; 41 4.6; 45 4.6; 49 4.6; 54 4.5; 60 4.3; 66 4.1; 72 4.0; 79 3.9; 87 3.6; 96 3.5; 106 3.2; 116 3.0; 128 2.8; 141 2.7; 155 2.7; 170 2.8; 187 2.7; 206 2.7; 227 2.6; 249 2.5; 274 2.2; 302 1.7; 332 1.1; 365 0.3; 402 -0.7; 442 -1.6; 486 -2.7; 535 -3.6; 588 -3.9; 647 -3.5; 712 -2.4; 783 -1.0; 861 0.2; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 0.1; 1387 0.6; 1526 1.4; 1678 2.4; 1846 3.3; 2031 4.2; 2234 5.6; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.9; 5267 3.7; 5793 1.0; 6373 0.2; 7010 0.8; 7711 -1.3; 8482 -7.4; 9330 -13.0; 10263 -13.6; 11289 -8.4; 12418 -3.8; 13660 -3.0; 15026 -0.9; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC56 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC56 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 16 Hz   | 0.15 | 5.3 dB   |
| Peaking | 264 Hz  | 0.9  | 2.3 dB   |
| Peaking | 563 Hz  | 1.37 | -5.0 dB  |
| Peaking | 3558 Hz | 0.71 | 7.2 dB   |
| Peaking | 9873 Hz | 2.46 | -16.7 dB |
| Peaking | 897 Hz  | 3.56 | 2.0 dB   |
| Peaking | 1139 Hz | 1.71 | -1.7 dB  |
| Peaking | 2277 Hz | 4.62 | 1.5 dB   |
| Peaking | 7323 Hz | 5.18 | 5.3 dB   |
| Peaking | 7371 Hz | 2.27 | -2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Panasonic%20RP-HC56/Panasonic%20RP-HC56.png)