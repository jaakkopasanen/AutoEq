# Microsoft Surface Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.9; 25 -7.3; 28 -7.8; 31 -8.3; 34 -8.6; 37 -8.9; 41 -9.2; 45 -9.5; 49 -10.0; 54 -10.5; 60 -11.2; 66 -11.7; 72 -12.0; 79 -12.3; 87 -12.5; 96 -12.7; 106 -12.7; 116 -12.6; 128 -12.3; 141 -11.9; 155 -11.4; 170 -10.8; 187 -10.3; 206 -9.8; 227 -9.4; 249 -9.4; 274 -9.6; 302 -10.0; 332 -10.3; 365 -10.5; 402 -10.1; 442 -9.2; 486 -8.0; 535 -6.8; 588 -6.0; 647 -5.8; 712 -6.2; 783 -7.4; 861 -8.1; 947 -7.1; 1042 -5.9; 1146 -4.0; 1261 -3.0; 1387 -2.9; 1526 -2.9; 1678 -2.7; 1846 -2.4; 2031 -1.9; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -1.3; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -5.0; 5267 -3.1; 5793 -0.6; 6373 -1.9; 7010 -4.0; 7711 -6.8; 8482 -8.9; 9330 -8.9; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -7.6; 15026 -10.0; 16529 -7.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Microsoft Surface Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Microsoft Surface Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 87 Hz    | 0.89 | -3.4 dB |
| Peaking | 157 Hz   | 0.3  | -3.3 dB |
| Peaking | 2196 Hz  | 0.92 | 5.5 dB  |
| Peaking | 3844 Hz  | 3.31 | 3.9 dB  |
| Peaking | 5988 Hz  | 5.68 | 5.1 dB  |
| Peaking | 397 Hz   | 1.85 | -4.2 dB |
| Peaking | 531 Hz   | 0.77 | 3.4 dB  |
| Peaking | 861 Hz   | 3.58 | -3.6 dB |
| Peaking | 8833 Hz  | 4.98 | -3.7 dB |
| Peaking | 14870 Hz | 3.74 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Microsoft%20Surface%20Headphones/Microsoft%20Surface%20Headphones.png)