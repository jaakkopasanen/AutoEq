# iHarmonix iHX Pro ev-Series

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 -3.7; 23 -3.7; 25 -3.7; 28 -3.8; 31 -3.7; 34 -3.7; 37 -3.7; 41 -3.7; 45 -3.7; 49 -3.8; 54 -3.9; 60 -4.0; 66 -4.2; 72 -4.3; 79 -4.4; 87 -4.5; 96 -4.5; 106 -4.5; 116 -4.5; 128 -4.4; 141 -4.4; 155 -4.3; 170 -4.1; 187 -3.8; 206 -3.5; 227 -3.0; 249 -2.6; 274 -2.6; 302 -2.2; 332 -1.7; 365 -1.2; 402 -0.7; 442 -0.3; 486 -0.1; 535 0.1; 588 0.5; 647 0.8; 712 1.0; 783 0.9; 861 0.7; 947 0.3; 1042 -0.3; 1146 -0.8; 1261 -1.4; 1387 -2.3; 1526 -4.0; 1678 -5.8; 1846 -7.1; 2031 -8.3; 2234 -9.5; 2457 -10.3; 2703 -8.3; 2973 -4.1; 3270 -0.3; 3597 1.5; 3957 0.2; 4353 -3.2; 4788 -6.3; 5267 -4.4; 5793 1.4; 6373 4.7; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.5; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iHarmonix iHX Pro ev-Series GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iHarmonix iHX Pro ev-Series ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.31 | -3.7 dB  |
| Peaking | 151 Hz  | 0.9  | -3.0 dB  |
| Peaking | 2239 Hz | 2.27 | -10.8 dB |
| Peaking | 4955 Hz | 6.57 | -7.4 dB  |
| Peaking | 6383 Hz | 4.52 | 5.8 dB   |
| Peaking | 752 Hz  | 1.74 | 1.7 dB   |
| Peaking | 1655 Hz | 5.57 | -2.2 dB  |
| Peaking | 2690 Hz | 7.1  | -3.5 dB  |
| Peaking | 3622 Hz | 3.17 | 4.4 dB   |
| Peaking | 4440 Hz | 5.26 | -2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/iHarmonix%20iHX%20Pro%20ev-Series/iHarmonix%20iHX%20Pro%20ev-Series.png)