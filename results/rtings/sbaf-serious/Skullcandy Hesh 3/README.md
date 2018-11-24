# Skullcandy Hesh 3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 21 -11.1; 23 -10.8; 25 -10.4; 28 -9.9; 31 -9.4; 34 -8.8; 37 -8.2; 41 -7.4; 45 -6.8; 49 -6.1; 54 -5.4; 60 -4.8; 66 -4.7; 72 -4.8; 79 -5.2; 87 -6.0; 96 -6.8; 106 -7.4; 116 -7.5; 128 -7.3; 141 -6.8; 155 -6.0; 170 -5.1; 187 -4.2; 206 -3.2; 227 -1.9; 249 -0.7; 274 0.3; 302 1.2; 332 1.9; 365 2.5; 402 2.8; 442 2.9; 486 2.8; 535 2.5; 588 2.2; 647 1.7; 712 1.1; 783 0.5; 861 0.2; 947 0.0; 1042 0.1; 1146 0.4; 1261 1.0; 1387 1.3; 1526 1.2; 1678 0.9; 1846 0.7; 2031 0.0; 2234 -0.5; 2457 -1.2; 2703 -1.5; 2973 -1.8; 3270 -1.3; 3597 -0.7; 3957 -0.3; 4353 -1.9; 4788 -2.5; 5267 -1.6; 5793 -3.9; 6373 -5.3; 7010 -6.4; 7711 -6.7; 8482 -8.4; 9330 -7.9; 10263 -3.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.7; 16529 -0.4; 18182 0.0; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-29**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.96 | -10.1 dB |
| Peaking | 34 Hz    | 1.22 | -4.2 dB  |
| Peaking | 129 Hz   | 0.89 | -7.4 dB  |
| Peaking | 391 Hz   | 1.02 | 4.1 dB   |
| Peaking | 8008 Hz  | 1.66 | -8.3 dB  |
| Peaking | 1552 Hz  | 3.02 | 1.4 dB   |
| Peaking | 2774 Hz  | 2.8  | -1.5 dB  |
| Peaking | 9401 Hz  | 4.97 | -4.4 dB  |
| Peaking | 10924 Hz | 1.84 | 3.3 dB   |
| Peaking | 15203 Hz | 5.42 | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Skullcandy%20Hesh%203/Skullcandy%20Hesh%203.png)