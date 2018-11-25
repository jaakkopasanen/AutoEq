# Bang & Olufsen Beoplay H6 2nd Gen

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.2; 25 3.5; 28 2.6; 31 1.8; 34 1.2; 37 0.7; 41 0.2; 45 -0.1; 49 -0.4; 54 -0.6; 60 -0.6; 66 -0.6; 72 -0.4; 79 -0.3; 87 -0.1; 96 0.5; 106 1.4; 116 1.5; 128 0.5; 141 0.4; 155 2.8; 170 5.4; 187 4.9; 206 5.7; 227 6.0; 249 6.0; 274 5.7; 302 4.7; 332 3.8; 365 3.2; 402 2.8; 442 2.4; 486 1.8; 535 1.5; 588 1.6; 647 1.3; 712 0.8; 783 0.6; 861 0.2; 947 0.1; 1042 -0.0; 1146 0.1; 1261 0.2; 1387 -0.1; 1526 -0.3; 1678 -0.5; 1846 -0.2; 2031 0.4; 2234 1.3; 2457 3.0; 2703 4.7; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.8; 9330 -2.3; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H6 2nd Gen GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H6 2nd Gen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 2.34 | 4.9 dB  |
| Peaking | 177 Hz  | 4.65 | 2.7 dB  |
| Peaking | 256 Hz  | 1.44 | 5.9 dB  |
| Peaking | 4550 Hz | 0.95 | 7.1 dB  |
| Peaking | 8980 Hz | 2.85 | -4.1 dB |
| Peaking | 54 Hz   | 2.49 | -0.9 dB |
| Peaking | 74 Hz   | 2.8  | -0.6 dB |
| Peaking | 1867 Hz | 1.74 | -2.2 dB |
| Peaking | 2886 Hz | 2.9  | 2.7 dB  |
| Peaking | 4346 Hz | 4.99 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen.png)