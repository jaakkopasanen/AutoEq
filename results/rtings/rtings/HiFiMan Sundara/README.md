# HiFiMan Sundara

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.4; 28 3.8; 31 3.3; 34 2.9; 37 2.7; 41 2.3; 45 2.0; 49 1.8; 54 1.6; 60 1.3; 66 1.1; 72 0.9; 79 0.6; 87 0.3; 96 0.0; 106 -0.3; 116 -0.5; 128 -0.8; 141 -1.0; 155 -1.2; 170 -1.3; 187 -1.5; 206 -1.5; 227 -1.6; 249 -1.6; 274 -1.7; 302 -1.8; 332 -2.1; 365 -2.2; 402 -2.2; 442 -1.6; 486 -1.2; 535 -1.7; 588 -1.9; 647 -1.9; 712 -1.8; 783 -1.7; 861 -1.6; 947 -0.5; 1042 0.1; 1146 0.1; 1261 0.2; 1387 0.3; 1526 0.7; 1678 0.7; 1846 1.1; 2031 1.2; 2234 2.7; 2457 1.4; 2703 0.9; 2973 -1.5; 3270 -2.2; 3597 -2.7; 3957 -2.7; 4353 -2.1; 4788 -3.8; 5267 -0.7; 5793 4.7; 6373 -1.0; 7010 -3.8; 7711 -3.2; 8482 -4.4; 9330 -4.6; 10263 -0.6; 11289 0.0; 12418 -0.1; 13660 -1.8; 15026 -2.4; 16529 -1.4; 18182 -0.4; 20000 -1.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Sundara GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Sundara ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.34 | 6.6 dB  |
| Peaking | 468 Hz   | 0.31 | -2.3 dB |
| Peaking | 3486 Hz  | 0.55 | 6.2 dB  |
| Peaking | 3751 Hz  | 1.48 | -8.9 dB |
| Peaking | 8421 Hz  | 2.08 | -6.3 dB |
| Peaking | 4904 Hz  | 7.37 | -3.8 dB |
| Peaking | 5801 Hz  | 6.02 | 6.0 dB  |
| Peaking | 6669 Hz  | 7.05 | -3.7 dB |
| Peaking | 11324 Hz | 3.1  | 1.7 dB  |
| Peaking | 14886 Hz | 1.85 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/HiFiMan%20Sundara/HiFiMan%20Sundara.png)