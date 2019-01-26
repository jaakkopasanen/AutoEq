# Microsoft Surface Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.4; 25 -0.8; 28 -1.3; 31 -1.8; 34 -2.1; 37 -2.4; 41 -2.7; 45 -3.0; 49 -3.5; 54 -4.0; 60 -4.7; 66 -5.2; 72 -5.5; 79 -5.8; 87 -6.0; 96 -6.2; 106 -6.2; 116 -6.1; 128 -5.8; 141 -5.4; 155 -4.9; 170 -4.3; 187 -3.8; 206 -3.3; 227 -2.9; 249 -2.9; 274 -3.1; 302 -3.5; 332 -3.8; 365 -4.0; 402 -3.6; 442 -2.7; 486 -1.5; 535 -0.3; 588 0.5; 647 0.7; 712 0.3; 783 -0.9; 861 -1.6; 947 -0.6; 1042 0.6; 1146 2.5; 1261 3.5; 1387 3.6; 1526 3.6; 1678 3.8; 1846 4.1; 2031 4.6; 2234 5.7; 2457 6.0; 2703 6.0; 2973 5.2; 3270 5.2; 3597 6.0; 3957 6.0; 4353 5.6; 4788 1.5; 5267 3.4; 5793 5.9; 6373 4.6; 7010 2.5; 7711 -0.3; 8482 -2.4; 9330 -2.4; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 -1.1; 15026 -3.5; 16529 -0.5; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Microsoft Surface Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Microsoft Surface Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 87 Hz    | 0.89 | -3.4 dB |
| Peaking | 157 Hz   | 0.3  | -3.3 dB |
| Peaking | 2196 Hz  | 0.92 | 5.5 dB  |
| Peaking | 3844 Hz  | 3.31 | 3.9 dB  |
| Peaking | 5988 Hz  | 5.68 | 5.1 dB  |
| Peaking | 396 Hz   | 1.85 | -4.2 dB |
| Peaking | 531 Hz   | 0.77 | 3.4 dB  |
| Peaking | 863 Hz   | 3.58 | -3.6 dB |
| Peaking | 8833 Hz  | 4.98 | -3.7 dB |
| Peaking | 14870 Hz | 3.74 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Microsoft%20Surface%20Headphones/Microsoft%20Surface%20Headphones.png)