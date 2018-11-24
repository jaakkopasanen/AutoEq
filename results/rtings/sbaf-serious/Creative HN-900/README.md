# Creative HN-900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.7; 41 4.6; 45 3.2; 49 1.5; 54 -0.2; 60 -1.0; 66 -0.0; 72 -1.7; 79 -4.4; 87 -6.3; 96 -7.3; 106 -8.0; 116 -8.3; 128 -8.4; 141 -8.2; 155 -8.1; 170 -7.9; 187 -7.3; 206 -6.9; 227 -6.4; 249 -5.7; 274 -5.1; 302 -4.5; 332 -3.9; 365 -3.5; 402 -3.4; 442 -3.4; 486 -3.7; 535 -4.4; 588 -5.4; 647 -6.3; 712 -6.2; 783 -5.0; 861 -2.9; 947 -0.7; 1042 -0.4; 1146 -1.7; 1261 0.3; 1387 2.0; 1526 2.6; 1678 3.6; 1846 6.0; 2031 5.4; 2234 4.0; 2457 2.3; 2703 4.6; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.4; 5267 2.0; 5793 4.2; 6373 2.8; 7010 2.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.7; 15026 -1.4; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative HN-900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative HN-900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.45 | 8.8 dB   |
| Peaking | 117 Hz   | 0.54 | -11.3 dB |
| Peaking | 679 Hz   | 2.4  | -5.7 dB  |
| Peaking | 1851 Hz  | 3.1  | 4.9 dB   |
| Peaking | 3753 Hz  | 1.25 | 6.4 dB   |
| Peaking | 5301 Hz  | 8.76 | -3.6 dB  |
| Peaking | 5753 Hz  | 2.81 | 2.7 dB   |
| Peaking | 8149 Hz  | 2    | -1.3 dB  |
| Peaking | 14622 Hz | 5.08 | -1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Creative%20HN-900/Creative%20HN-900.png)