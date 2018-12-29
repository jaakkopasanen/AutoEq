# AKG K712
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 -0.1; 25 -0.5; 28 -1.0; 31 -1.4; 34 -1.7; 37 -2.0; 41 -2.3; 45 -2.6; 49 -2.8; 54 -3.1; 60 -3.3; 66 -3.5; 72 -3.7; 79 -3.9; 87 -4.1; 96 -4.7; 106 -5.0; 116 -5.0; 128 -5.3; 141 -5.6; 155 -5.8; 170 -5.5; 187 -5.9; 206 -6.0; 227 -6.2; 249 -6.2; 274 -6.1; 302 -6.0; 332 -5.7; 365 -5.4; 402 -5.3; 442 -5.1; 486 -4.8; 535 -4.1; 588 -3.6; 647 -3.6; 712 -2.9; 783 -2.2; 861 -1.4; 947 -0.5; 1042 0.6; 1146 1.6; 1261 1.6; 1387 0.9; 1526 -0.2; 1678 -1.7; 1846 -3.4; 2031 -5.7; 2234 -4.9; 2457 -1.8; 2703 2.4; 2973 4.9; 3270 2.6; 3597 1.2; 3957 -0.5; 4353 -3.0; 4788 -2.1; 5267 -2.7; 5793 -3.2; 6373 -4.3; 7010 -7.4; 7711 -6.5; 8482 -4.6; 9330 -3.5; 10263 -3.5; 11289 -1.9; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.7; 18182 -2.5; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 159 Hz   | 0.36 | -5.1 dB  |
| Peaking | 451 Hz   | 0.71 | -2.7 dB  |
| Peaking | 2120 Hz  | 2.31 | -15.4 dB |
| Peaking | 2383 Hz  | 0.77 | 10.9 dB  |
| Peaking | 6538 Hz  | 0.9  | -7.7 dB  |
| Peaking | 1654 Hz  | 8.04 | -1.3 dB  |
| Peaking | 2997 Hz  | 6.54 | 3.5 dB   |
| Peaking | 5545 Hz  | 1.13 | -3.6 dB  |
| Peaking | 5640 Hz  | 2.88 | 5.4 dB   |
| Peaking | 12738 Hz | 2.96 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K712/AKG%20K712.png)