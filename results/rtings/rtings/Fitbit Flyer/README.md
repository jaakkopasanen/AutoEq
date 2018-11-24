# Fitbit Flyer

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.3; 45 1.7; 49 -1.9; 54 -5.3; 60 -8.0; 66 -9.4; 72 -9.5; 79 -8.6; 87 -7.7; 96 -6.7; 106 -5.9; 116 -5.4; 128 -4.6; 141 -3.5; 155 -2.7; 170 -2.7; 187 -2.7; 206 -2.6; 227 -2.4; 249 -2.2; 274 -2.2; 302 -2.2; 332 -2.4; 365 -2.7; 402 -2.4; 442 -1.7; 486 -1.0; 535 -0.4; 588 0.2; 647 0.8; 712 1.3; 783 1.9; 861 1.3; 947 0.5; 1042 -0.4; 1146 -1.4; 1261 -1.8; 1387 -1.9; 1526 -1.9; 1678 -2.1; 1846 -2.4; 2031 -2.7; 2234 -2.4; 2457 -2.0; 2703 -1.8; 2973 -1.1; 3270 0.4; 3597 2.0; 3957 2.5; 4353 2.1; 4788 2.9; 5267 4.0; 5793 4.7; 6373 5.1; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.3; 10263 -1.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.0; 18182 -0.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fitbit Flyer GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fitbit Flyer ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.72 | 14.7 dB  |
| Peaking | 64 Hz    | 0.87 | -17.6 dB |
| Peaking | 362 Hz   | 3.25 | -2.0 dB  |
| Peaking | 2007 Hz  | 1.74 | -3.1 dB  |
| Peaking | 5592 Hz  | 2.1  | 5.2 dB   |
| Peaking | 20 Hz    | 2.62 | 1.6 dB   |
| Peaking | 772 Hz   | 3.98 | 2.5 dB   |
| Peaking | 6526 Hz  | 9.84 | 2.2 dB   |
| Peaking | 10243 Hz | 2.37 | -3.8 dB  |
| Peaking | 10895 Hz | 3.79 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Fitbit%20Flyer/Fitbit%20Flyer.png)