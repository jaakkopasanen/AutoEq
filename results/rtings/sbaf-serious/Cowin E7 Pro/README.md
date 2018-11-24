# Cowin E7 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 4.9; 41 3.0; 45 1.4; 49 0.3; 54 -0.7; 60 -1.7; 66 -2.8; 72 -2.9; 79 -1.7; 87 -0.6; 96 -0.1; 106 0.2; 116 0.3; 128 0.4; 141 0.5; 155 0.7; 170 0.9; 187 1.2; 206 1.5; 227 1.9; 249 2.4; 274 2.9; 302 3.7; 332 5.1; 365 6.0; 402 6.0; 442 6.0; 486 5.5; 535 4.9; 588 4.9; 647 5.0; 712 4.5; 783 3.9; 861 2.5; 947 0.9; 1042 -0.6; 1146 -2.1; 1261 -4.2; 1387 -6.1; 1526 -7.0; 1678 -6.4; 1846 -3.9; 2031 -1.7; 2234 0.5; 2457 3.1; 2703 5.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.7; 4353 2.7; 4788 1.4; 5267 1.3; 5793 4.0; 6373 2.4; 7010 0.1; 7711 -0.3; 8482 -2.5; 9330 -4.9; 10263 -2.7; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.3; 16529 -1.0; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-8.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 1.93 | 7.4 dB   |
| Peaking | 513 Hz  | 0.79 | 6.6 dB   |
| Peaking | 1564 Hz | 1.58 | -10.5 dB |
| Peaking | 3066 Hz | 1.19 | 7.9 dB   |
| Peaking | 9324 Hz | 4.41 | -5.8 dB  |
| Peaking | 12 Hz   | 0.29 | 0.9 dB   |
| Peaking | 67 Hz   | 2.47 | -3.9 dB  |
| Peaking | 356 Hz  | 7.13 | 1.5 dB   |
| Peaking | 4901 Hz | 5.58 | -2.0 dB  |
| Peaking | 5919 Hz | 7.73 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Cowin%20E7%20Pro/Cowin%20E7%20Pro.png)