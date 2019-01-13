# Pioneer HDJ-2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.1; 31 4.0; 34 2.8; 37 1.8; 41 0.5; 45 -0.5; 49 -1.3; 54 -2.2; 60 -3.1; 66 -3.7; 72 -4.1; 79 -4.4; 87 -4.9; 96 -5.3; 106 -5.3; 116 -5.2; 128 -5.2; 141 -5.4; 155 -5.5; 170 -5.2; 187 -5.3; 206 -5.3; 227 -5.3; 249 -5.3; 274 -5.2; 302 -4.7; 332 -4.2; 365 -3.3; 402 -2.2; 442 -0.9; 486 -0.2; 535 -0.2; 588 0.2; 647 0.2; 712 -0.3; 783 -0.7; 861 -0.6; 947 -0.2; 1042 -0.4; 1146 -1.2; 1261 -1.6; 1387 -2.0; 1526 -2.7; 1678 -2.6; 1846 -1.8; 2031 -0.3; 2234 2.5; 2457 5.4; 2703 6.0; 2973 6.0; 3270 5.7; 3597 2.8; 3957 0.6; 4353 2.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.3; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.02 | 7.4 dB  |
| Peaking | 102 Hz  | 0.5  | -5.6 dB |
| Peaking | 266 Hz  | 1.73 | -3.1 dB |
| Peaking | 2848 Hz | 3.54 | 6.8 dB  |
| Peaking | 5507 Hz | 2.69 | 6.7 dB  |
| Peaking | 550 Hz  | 2.98 | 1.3 dB  |
| Peaking | 1649 Hz | 1.73 | -5.1 dB |
| Peaking | 2242 Hz | 0.76 | 2.3 dB  |
| Peaking | 3940 Hz | 8.96 | -3.0 dB |
| Peaking | 9106 Hz | 3.49 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Pioneer%20HDJ-2000/Pioneer%20HDJ-2000.png)