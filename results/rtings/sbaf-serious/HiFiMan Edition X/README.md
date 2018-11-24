# HiFiMan Edition X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.4; 31 4.7; 34 4.2; 37 3.8; 41 3.4; 45 3.0; 49 2.7; 54 2.5; 60 2.3; 66 2.2; 72 2.1; 79 2.2; 87 2.1; 96 2.0; 106 1.7; 116 1.5; 128 1.2; 141 1.0; 155 0.7; 170 0.5; 187 0.3; 206 0.2; 227 0.7; 249 0.7; 274 0.7; 302 1.1; 332 1.4; 365 2.1; 402 1.4; 442 0.9; 486 0.7; 535 0.6; 588 0.4; 647 -0.0; 712 1.7; 783 3.0; 861 1.2; 947 0.6; 1042 1.0; 1146 4.9; 1261 2.6; 1387 2.4; 1526 3.5; 1678 1.6; 1846 1.7; 2031 0.9; 2234 1.3; 2457 0.8; 2703 1.2; 2973 0.9; 3270 2.7; 3597 3.6; 3957 2.9; 4353 1.4; 4788 2.6; 5267 5.8; 5793 6.0; 6373 3.9; 7010 2.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Edition X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 1149 Hz | 9.58 | 3.5 dB  |
| Peaking | 1263 Hz | 0.22 | 1.2 dB  |
| Peaking | 1486 Hz | 6.88 | 2.2 dB  |
| Peaking | 5619 Hz | 3.34 | 5.8 dB  |
| Peaking | 21 Hz   | 0.67 | 6.0 dB  |
| Peaking | 69 Hz   | 1.57 | 0.5 dB  |
| Peaking | 95 Hz   | 2.07 | 1.0 dB  |
| Peaking | 626 Hz  | 6.87 | -1.1 dB |
| Peaking | 3585 Hz | 7.34 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/HiFiMan%20Edition%20X/HiFiMan%20Edition%20X.png)