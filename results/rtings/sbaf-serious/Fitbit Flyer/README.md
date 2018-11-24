# Fitbit Flyer

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.0; 45 1.5; 49 -2.3; 54 -5.6; 60 -8.3; 66 -9.5; 72 -9.5; 79 -8.4; 87 -7.3; 96 -6.3; 106 -5.4; 116 -4.9; 128 -4.1; 141 -3.0; 155 -2.1; 170 -2.0; 187 -2.1; 206 -2.1; 227 -1.9; 249 -1.7; 274 -1.5; 302 -1.4; 332 -1.5; 365 -1.6; 402 -1.3; 442 -0.6; 486 0.2; 535 0.8; 588 1.3; 647 1.8; 712 2.2; 783 2.4; 861 1.4; 947 0.5; 1042 -0.4; 1146 -1.2; 1261 -1.6; 1387 -1.9; 1526 -2.3; 1678 -2.5; 1846 -2.4; 2031 -2.3; 2234 -2.0; 2457 -1.5; 2703 -1.2; 2973 -0.0; 3270 2.3; 3597 4.2; 3957 3.7; 4353 2.1; 4788 2.8; 5267 4.4; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
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
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.73 | 14.1 dB  |
| Peaking | 64 Hz   | 0.93 | -17.5 dB |
| Peaking | 1933 Hz | 1.69 | -2.9 dB  |
| Peaking | 3681 Hz | 4.16 | 4.5 dB   |
| Peaking | 5897 Hz | 3.32 | 6.3 dB   |
| Peaking | 156 Hz  | 5.78 | 1.0 dB   |
| Peaking | 374 Hz  | 1.63 | -1.5 dB  |
| Peaking | 755 Hz  | 1.2  | 3.5 dB   |
| Peaking | 1149 Hz | 1.7  | -2.2 dB  |
| Peaking | 8109 Hz | 5.06 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Fitbit%20Flyer/Fitbit%20Flyer.png)