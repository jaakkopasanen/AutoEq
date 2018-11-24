# Rovking V1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 -15.2; 23 -15.2; 25 -15.3; 28 -15.3; 31 -15.4; 34 -15.4; 37 -15.4; 41 -15.4; 45 -15.4; 49 -15.4; 54 -15.4; 60 -15.3; 66 -15.2; 72 -14.9; 79 -14.7; 87 -14.4; 96 -14.3; 106 -14.2; 116 -14.1; 128 -13.9; 141 -13.5; 155 -12.9; 170 -12.2; 187 -11.6; 206 -11.0; 227 -10.5; 249 -10.0; 274 -9.4; 302 -8.5; 332 -7.5; 365 -6.4; 402 -5.3; 442 -4.2; 486 -3.0; 535 -2.0; 588 -1.1; 647 -0.6; 712 -0.4; 783 -0.4; 861 -0.3; 947 -0.1; 1042 0.3; 1146 0.8; 1261 1.0; 1387 0.7; 1526 0.6; 1678 1.3; 1846 2.5; 2031 3.6; 2234 4.3; 2457 3.9; 2703 3.5; 2973 2.5; 3270 1.9; 3597 1.2; 3957 -1.0; 4353 -3.7; 4788 -5.7; 5267 -4.0; 5793 -1.3; 6373 0.1; 7010 0.4; 7711 -4.5; 8482 -5.0; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 -0.1; 13660 -0.5; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rovking V1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rovking V1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.09 | -15.4 dB |
| Peaking | 616 Hz   | 0.86 | 4.5 dB   |
| Peaking | 2381 Hz  | 1.35 | 4.6 dB   |
| Peaking | 4754 Hz  | 4.11 | -6.9 dB  |
| Peaking | 8172 Hz  | 7.47 | -6.5 dB  |
| Peaking | 6754 Hz  | 6.94 | 3.9 dB   |
| Peaking | 7281 Hz  | 2.86 | -1.9 dB  |
| Peaking | 9633 Hz  | 3.67 | 0.9 dB   |
| Peaking | 13189 Hz | 6.74 | -0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Rovking%20V1/Rovking%20V1.png)