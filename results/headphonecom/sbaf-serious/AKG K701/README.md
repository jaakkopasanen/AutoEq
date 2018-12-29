# AKG K701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.6; 45 5.0; 49 4.3; 54 3.6; 60 3.7; 66 4.5; 72 2.8; 79 1.8; 87 1.1; 96 0.7; 106 0.4; 116 -0.1; 128 -0.6; 141 -0.8; 155 -1.0; 170 -1.1; 187 -1.4; 206 -1.2; 227 -1.4; 249 -1.4; 274 -1.1; 302 -1.0; 332 -0.8; 365 -0.7; 402 -0.5; 442 -0.2; 486 -0.1; 535 0.3; 588 1.8; 647 1.0; 712 1.1; 783 0.7; 861 0.4; 947 0.0; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -0.9; 1526 -1.6; 1678 -2.1; 1846 -3.2; 2031 -4.3; 2234 -4.7; 2457 -4.0; 2703 -2.9; 2973 -2.6; 3270 -2.1; 3597 -2.0; 3957 -2.4; 4353 -3.0; 4788 -2.0; 5267 -2.5; 5793 -5.3; 6373 -5.1; 7010 -3.9; 7711 -4.4; 8482 -3.8; 9330 -2.6; 10263 -0.4; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.46 | 6.3 dB  |
| Peaking | 162 Hz   | 0.91 | -2.3 dB |
| Peaking | 2237 Hz  | 1.94 | -4.6 dB |
| Peaking | 6093 Hz  | 2.26 | -4.7 dB |
| Peaking | 8251 Hz  | 3.71 | -2.9 dB |
| Peaking | 65 Hz    | 8.08 | 1.3 dB  |
| Peaking | 648 Hz   | 2.72 | 1.6 dB  |
| Peaking | 4531 Hz  | 2.97 | -1.7 dB |
| Peaking | 5015 Hz  | 6.88 | 2.6 dB  |
| Peaking | 11101 Hz | 4.46 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K701/AKG%20K701.png)