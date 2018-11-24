# AfterShokz Trekz Air

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 5.0; 141 0.9; 155 -1.2; 170 -1.6; 187 -1.9; 206 -2.5; 227 -3.4; 249 -3.8; 274 -3.8; 302 -3.8; 332 -3.5; 365 -2.9; 402 -2.3; 442 -1.6; 486 1.5; 535 2.4; 588 1.5; 647 2.4; 712 3.4; 783 2.1; 861 1.3; 947 0.0; 1042 1.2; 1146 3.2; 1261 3.1; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 3.9; 2234 0.2; 2457 -0.5; 2703 -0.3; 2973 0.5; 3270 1.6; 3597 -0.3; 3957 -4.8; 4353 -9.8; 4788 -11.7; 5267 -3.4; 5793 1.6; 6373 0.6; 7010 2.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -2.5; 12418 -7.3; 13660 -3.0; 15026 0.0
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
| Peaking | 122 Hz   | 0.16 | 9.0 dB   |
| Peaking | 253 Hz   | 0.75 | -12.9 dB |
| Peaking | 1624 Hz  | 2.62 | 6.0 dB   |
| Peaking | 4581 Hz  | 5.63 | -13.3 dB |
| Peaking | 12495 Hz | 5.39 | -8.2 dB  |
| Peaking | 20 Hz    | 2.3  | 1.3 dB   |
| Peaking | 121 Hz   | 3.96 | 3.2 dB   |
| Peaking | 152 Hz   | 4.35 | -3.2 dB  |
| Peaking | 4953 Hz  | 7.92 | -3.6 dB  |
| Peaking | 6114 Hz  | 2.58 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/AfterShokz%20Trekz%20Air/AfterShokz%20Trekz%20Air.png)