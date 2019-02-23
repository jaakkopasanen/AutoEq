# Microsoft Surface Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.4; 25 -7.8; 28 -8.4; 31 -8.8; 34 -9.2; 37 -9.4; 41 -9.7; 45 -10.1; 49 -10.5; 54 -11.1; 60 -11.7; 66 -12.3; 72 -12.6; 79 -12.9; 87 -13.1; 96 -13.2; 106 -13.2; 116 -13.1; 128 -12.8; 141 -12.5; 155 -12.0; 170 -11.4; 187 -10.8; 206 -10.3; 227 -10.0; 249 -10.0; 274 -10.2; 302 -10.5; 332 -10.9; 365 -11.0; 402 -10.6; 442 -9.7; 486 -8.5; 535 -7.4; 588 -6.6; 647 -6.3; 712 -6.8; 783 -8.0; 861 -8.6; 947 -7.7; 1042 -6.5; 1146 -4.5; 1261 -3.5; 1387 -3.4; 1526 -3.5; 1678 -3.3; 1846 -3.0; 2031 -2.5; 2234 -1.3; 2457 -0.5; 2703 -0.5; 2973 -1.8; 3270 -1.8; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -5.6; 5267 -3.7; 5793 -1.1; 6373 -2.4; 7010 -4.1; 7711 -7.3; 8482 -9.5; 9330 -9.4; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -8.0; 15026 -10.6; 16529 -7.4; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Microsoft Surface Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Microsoft Surface Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 90 Hz    | 0.92 | -3.2 dB |
| Peaking | 143 Hz   | 0.26 | -3.9 dB |
| Peaking | 1369 Hz  | 2.62 | 3.0 dB  |
| Peaking | 2389 Hz  | 2.13 | 4.5 dB  |
| Peaking | 3905 Hz  | 1.49 | 4.9 dB  |
| Peaking | 379 Hz   | 4.1  | -1.8 dB |
| Peaking | 596 Hz   | 4.84 | 2.2 dB  |
| Peaking | 6215 Hz  | 5.03 | 4.0 dB  |
| Peaking | 8738 Hz  | 3.88 | -4.3 dB |
| Peaking | 14982 Hz | 3.53 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Microsoft%20Surface%20Headphones/Microsoft%20Surface%20Headphones.png)