# AKG Q701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.7; 28 5.1; 31 4.5; 34 3.9; 37 3.5; 41 3.0; 45 2.7; 49 2.4; 54 2.0; 60 1.8; 66 1.5; 72 1.4; 79 1.1; 87 0.8; 96 0.4; 106 -0.0; 116 -0.4; 128 -0.9; 141 -1.2; 155 -1.4; 170 -1.5; 187 -1.7; 206 -1.7; 227 -1.8; 249 -1.7; 274 -1.6; 302 -1.5; 332 -1.4; 365 -1.3; 402 -1.3; 442 -1.2; 486 -0.7; 535 -0.1; 588 0.4; 647 0.3; 712 0.4; 783 0.4; 861 0.2; 947 -0.1; 1042 0.1; 1146 0.1; 1261 -0.2; 1387 -0.9; 1526 -2.2; 1678 -3.7; 1846 -4.7; 2031 -5.5; 2234 -5.9; 2457 -4.9; 2703 -3.6; 2973 -1.6; 3270 0.9; 3597 0.9; 3957 -0.4; 4353 -1.8; 4788 -1.2; 5267 -0.3; 5793 -0.9; 6373 -4.0; 7010 -4.1; 7711 -4.4; 8482 -6.2; 9330 -3.6; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.69 | 6.0 dB  |
| Peaking | 72 Hz   | 1.59 | 0.7 dB  |
| Peaking | 205 Hz  | 0.88 | -2.1 dB |
| Peaking | 2120 Hz | 2.54 | -6.4 dB |
| Peaking | 8023 Hz | 2.61 | -5.9 dB |
| Peaking | 878 Hz  | 1.43 | 0.8 dB  |
| Peaking | 3369 Hz | 1.5  | -2.5 dB |
| Peaking | 3429 Hz | 3.77 | 5.0 dB  |
| Peaking | 9005 Hz | 7.06 | -3.4 dB |
| Peaking | 9797 Hz | 2.5  | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/AKG%20Q701/AKG%20Q701.png)