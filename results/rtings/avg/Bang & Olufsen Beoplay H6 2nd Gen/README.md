# Bang & Olufsen Beoplay H6 2nd Gen
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.1; 23 -2.3; 25 -2.4; 28 -2.6; 31 -2.7; 34 -2.8; 37 -2.7; 41 -2.6; 45 -2.3; 49 -2.0; 54 -1.6; 60 -1.3; 66 -1.3; 72 -1.3; 79 -1.4; 87 -1.6; 96 -1.6; 106 -1.6; 116 -1.5; 128 -1.2; 141 -0.6; 155 0.3; 170 1.6; 187 3.1; 206 4.6; 227 5.5; 249 5.9; 274 5.4; 302 4.3; 332 3.2; 365 2.1; 402 1.4; 442 1.0; 486 0.6; 535 0.4; 588 0.3; 647 0.1; 712 -0.0; 783 -0.0; 861 0.0; 947 0.0; 1042 0.0; 1146 0.1; 1261 0.2; 1387 0.1; 1526 -0.1; 1678 -0.7; 1846 -1.5; 2031 -2.0; 2234 -1.5; 2457 -0.1; 2703 1.3; 2973 2.9; 3270 3.6; 3597 3.5; 3957 5.3; 4353 5.5; 4788 5.8; 5267 6.0; 5793 6.0; 6373 4.6; 7010 1.1; 7711 -2.5; 8482 -4.8; 9330 -3.4; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.4; 18182 -3.7; 20000 -0.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H6 2nd Gen GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H6 2nd Gen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.07 | -2.4 dB |
| Peaking | 251 Hz   | 1.35 | 8.2 dB  |
| Peaking | 5210 Hz  | 1.3  | 7.2 dB  |
| Peaking | 8392 Hz  | 3.3  | -7.5 dB |
| Peaking | 18312 Hz | 2.3  | -4.1 dB |
| Peaking | 65 Hz    | 2.98 | 0.9 dB  |
| Peaking | 125 Hz   | 3.3  | -0.8 dB |
| Peaking | 2103 Hz  | 3.36 | -3.0 dB |
| Peaking | 3146 Hz  | 2.98 | 1.5 dB  |
| Peaking | 7438 Hz  | 3.69 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen.png)