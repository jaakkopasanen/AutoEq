# Bluedio T3 Plus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.5dB
GraphicEQ: 21 -27.0; 23 -27.3; 25 -27.5; 28 -27.7; 31 -27.7; 34 -27.7; 37 -27.6; 41 -27.5; 45 -27.5; 49 -27.5; 54 -27.6; 60 -27.9; 66 -28.1; 72 -28.3; 79 -28.5; 87 -28.8; 96 -29.2; 106 -29.7; 116 -30.1; 128 -30.4; 141 -30.4; 155 -30.2; 170 -29.8; 187 -29.1; 206 -28.0; 227 -26.7; 249 -24.9; 274 -22.6; 302 -20.1; 332 -17.5; 365 -14.6; 402 -11.3; 442 -8.2; 486 -7.2; 535 -7.5; 588 -5.0; 647 -2.5; 712 -4.7; 783 -3.0; 861 -0.4; 947 0.4; 1042 -0.7; 1146 -3.4; 1261 -6.6; 1387 -10.4; 1526 -14.1; 1678 -16.5; 1846 -19.9; 2031 -22.4; 2234 -23.9; 2457 -24.4; 2703 -24.5; 2973 -24.0; 3270 -22.9; 3597 -21.9; 3957 -20.1; 4353 -17.3; 4788 -13.8; 5267 -11.4; 5793 -10.4; 6373 -12.5; 7010 -12.7; 7711 -15.1; 8482 -17.9; 9330 -17.8; 10263 -14.0; 11289 -9.6; 12418 -8.0; 13660 -9.9; 15026 -12.7; 16529 -14.4; 18182 -13.2; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T3 Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-5**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T3 Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.24 | -26.7 dB |
| Peaking | 162 Hz   | 0.81 | -19.5 dB |
| Peaking | 2535 Hz  | 1.55 | -20.8 dB |
| Peaking | 7507 Hz  | 0.36 | -12.0 dB |
| Peaking | 17658 Hz | 1.38 | -10.8 dB |
| Peaking | 928 Hz   | 1.37 | 7.8 dB   |
| Peaking | 1132 Hz  | 1.78 | 5.8 dB   |
| Peaking | 1436 Hz  | 0.99 | -8.2 dB  |
| Peaking | 5688 Hz  | 4.18 | 5.6 dB   |
| Peaking | 8918 Hz  | 5.78 | -5.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bluedio%20T3%20Plus/Bluedio%20T3%20Plus.png)