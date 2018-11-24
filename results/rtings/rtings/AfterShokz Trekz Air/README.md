# AfterShokz Trekz Air

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 4.6; 141 0.3; 155 -1.8; 170 -2.3; 187 -2.5; 206 -3.1; 227 -3.8; 249 -4.3; 274 -4.5; 302 -4.6; 332 -4.5; 365 -3.9; 402 -3.4; 442 -2.7; 486 0.3; 535 1.2; 588 0.4; 647 1.3; 712 2.5; 783 1.7; 861 1.1; 947 0.0; 1042 1.1; 1146 3.0; 1261 2.9; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 3.5; 2234 -0.3; 2457 -1.0; 2703 -0.9; 2973 -0.6; 3270 -0.3; 3597 -2.5; 3957 -6.0; 4353 -9.8; 4788 -11.5; 5267 -3.8; 5793 0.2; 6373 -1.9; 7010 0.8; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.1; 11289 -7.0; 12418 -11.8; 13660 -6.8; 15026 -0.2; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AfterShokz Trekz Air GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AfterShokz Trekz Air ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 122 Hz   | 0.17 | 9.6 dB   |
| Peaking | 256 Hz   | 0.69 | -14.0 dB |
| Peaking | 1603 Hz  | 2.63 | 6.4 dB   |
| Peaking | 4540 Hz  | 4.21 | -12.3 dB |
| Peaking | 12462 Hz | 4.38 | -13.3 dB |
| Peaking | 19 Hz    | 2.32 | 1.4 dB   |
| Peaking | 121 Hz   | 3.65 | 3.6 dB   |
| Peaking | 140 Hz   | 4.9  | -2.3 dB  |
| Peaking | 159 Hz   | 5.23 | -2.2 dB  |
| Peaking | 2430 Hz  | 6.33 | -2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/AfterShokz%20Trekz%20Air/AfterShokz%20Trekz%20Air.png)