# Bluedio T3 Plus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.5dB
GraphicEQ: 21 -27.4; 23 -27.6; 25 -27.7; 28 -27.8; 31 -27.8; 34 -27.6; 37 -27.5; 41 -27.3; 45 -27.2; 49 -27.1; 54 -27.2; 60 -27.6; 66 -28.0; 72 -28.3; 79 -28.7; 87 -29.2; 96 -29.7; 106 -30.2; 116 -30.6; 128 -31.0; 141 -31.0; 155 -30.8; 170 -30.5; 187 -29.7; 206 -28.5; 227 -27.1; 249 -25.4; 274 -23.3; 302 -20.9; 332 -18.4; 365 -15.6; 402 -12.3; 442 -9.3; 486 -8.4; 535 -8.7; 588 -6.1; 647 -3.5; 712 -5.6; 783 -3.5; 861 -0.5; 947 0.4; 1042 -0.7; 1146 -3.6; 1261 -6.9; 1387 -10.3; 1526 -13.7; 1678 -16.1; 1846 -20.0; 2031 -22.8; 2234 -24.4; 2457 -24.8; 2703 -25.4; 2973 -25.6; 3270 -25.5; 3597 -25.1; 3957 -22.5; 4353 -18.6; 4788 -15.4; 5267 -14.3; 5793 -14.3; 6373 -16.3; 7010 -15.9; 7711 -16.7; 8482 -17.4; 9330 -16.6; 10263 -15.2; 11289 -14.9; 12418 -15.8; 13660 -17.0; 15026 -18.5; 16529 -20.8; 18182 -20.7; 20000 -13.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T3 Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-4**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T3 Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.2  | -26.4 dB |
| Peaking | 165 Hz   | 0.76 | -19.7 dB |
| Peaking | 2132 Hz  | 2.39 | -14.9 dB |
| Peaking | 3279 Hz  | 1.58 | -17.9 dB |
| Peaking | 17175 Hz | 0.19 | -19.2 dB |
| Peaking | 287 Hz   | 2.19 | -4.8 dB  |
| Peaking | 485 Hz   | 1.06 | 2.3 dB   |
| Peaking | 958 Hz   | 2.68 | 5.9 dB   |
| Peaking | 1092 Hz  | 1.88 | 1.5 dB   |
| Peaking | 1527 Hz  | 2.58 | -4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20T3%20Plus/Bluedio%20T3%20Plus.png)