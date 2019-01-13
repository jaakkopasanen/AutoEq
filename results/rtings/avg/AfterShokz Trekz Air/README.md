# AfterShokz Trekz Air
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 4.6; 141 0.3; 155 -1.8; 170 -2.3; 187 -2.5; 206 -3.1; 227 -3.8; 249 -4.3; 274 -4.5; 302 -4.6; 332 -4.5; 365 -3.9; 402 -3.4; 442 -2.7; 486 0.3; 535 1.2; 588 0.4; 647 1.3; 712 2.5; 783 1.7; 861 1.1; 947 0.0; 1042 1.1; 1146 3.0; 1261 2.9; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 3.5; 2234 -0.3; 2457 -1.0; 2703 -1.1; 2973 -1.1; 3270 -1.0; 3597 -3.5; 3957 -7.2; 4353 -11.1; 4788 -13.3; 5267 -6.4; 5793 -2.2; 6373 -3.1; 7010 -0.1; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -7.8; 12418 -15.1; 13660 -10.0; 15026 -1.3; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AfterShokz Trekz Air GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AfterShokz Trekz Air ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 123 Hz   | 0.18 | 9.6 dB   |
| Peaking | 257 Hz   | 0.68 | -14.1 dB |
| Peaking | 1611 Hz  | 2.57 | 6.5 dB   |
| Peaking | 4575 Hz  | 3.57 | -13.9 dB |
| Peaking | 12619 Hz | 4.39 | -16.9 dB |
| Peaking | 19 Hz    | 2.34 | 1.3 dB   |
| Peaking | 119 Hz   | 3.82 | 3.4 dB   |
| Peaking | 150 Hz   | 4.23 | -3.5 dB  |
| Peaking | 2433 Hz  | 6.22 | -2.0 dB  |
| Peaking | 8726 Hz  | 2.42 | 2.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AfterShokz%20Trekz%20Air/AfterShokz%20Trekz%20Air.png)