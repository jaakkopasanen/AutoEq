# Polk Audio UltraFocus 8000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -6.7; 23 -6.2; 25 -5.7; 28 -5.1; 31 -4.6; 34 -4.2; 37 -3.9; 41 -3.6; 45 -3.5; 49 -3.3; 54 -3.1; 60 -2.8; 66 -2.6; 72 -2.3; 79 -1.9; 87 -1.7; 96 -1.5; 106 -1.5; 116 -1.5; 128 -1.5; 141 -1.3; 155 -1.2; 170 -1.3; 187 -1.4; 206 -1.4; 227 -1.4; 249 -1.3; 274 -1.0; 302 -0.6; 332 -0.1; 365 0.1; 402 0.2; 442 0.4; 486 0.6; 535 0.7; 588 0.6; 647 0.9; 712 0.5; 783 0.2; 861 -0.0; 947 0.1; 1042 -0.0; 1146 0.2; 1261 0.2; 1387 -0.3; 1526 -1.2; 1678 -1.7; 1846 -1.5; 2031 -1.0; 2234 -0.2; 2457 0.9; 2703 2.1; 2973 3.0; 3270 3.2; 3597 2.4; 3957 -0.5; 4353 -2.0; 4788 -1.6; 5267 1.5; 5793 4.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFocus 8000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFocus 8000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.65 | -6.7 dB |
| Peaking | 48 Hz   | 0.29 | -1.7 dB |
| Peaking | 3294 Hz | 2.1  | 8.9 dB  |
| Peaking | 4214 Hz | 0.95 | -7.5 dB |
| Peaking | 6049 Hz | 2.77 | 9.6 dB  |
| Peaking | 235 Hz  | 2.31 | -0.9 dB |
| Peaking | 553 Hz  | 1.13 | 1.0 dB  |
| Peaking | 1306 Hz | 3.04 | 1.3 dB  |
| Peaking | 1645 Hz | 1.78 | -1.7 dB |
| Peaking | 2553 Hz | 4.42 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Polk%20Audio%20UltraFocus%208000/Polk%20Audio%20UltraFocus%208000.png)