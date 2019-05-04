# Microsoft Surface Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.3; 25 -7.7; 28 -8.2; 31 -8.6; 34 -9.0; 37 -9.3; 41 -9.6; 45 -10.0; 49 -10.4; 54 -11.0; 60 -11.6; 66 -12.1; 72 -12.4; 79 -12.7; 87 -12.9; 96 -13.0; 106 -13.0; 116 -12.9; 128 -12.7; 141 -12.3; 155 -11.8; 170 -11.2; 187 -10.7; 206 -10.2; 227 -9.9; 249 -9.9; 274 -10.1; 302 -10.5; 332 -10.8; 365 -11.0; 402 -10.6; 442 -9.7; 486 -8.6; 535 -7.4; 588 -6.6; 647 -6.4; 712 -7.0; 783 -8.1; 861 -8.7; 947 -7.8; 1042 -6.6; 1146 -4.7; 1261 -3.7; 1387 -3.6; 1526 -3.7; 1678 -3.5; 1846 -3.3; 2031 -3.0; 2234 -2.1; 2457 -0.6; 2703 -0.8; 2973 -1.9; 3270 -1.6; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -5.8; 5267 -4.2; 5793 -1.2; 6373 -1.3; 7010 -4.0; 7711 -8.1; 8482 -9.1; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -10.1; 16529 -7.3; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Microsoft Surface Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Microsoft Surface Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 88 Hz    | 0.88 | -3.4 dB |
| Peaking | 167 Hz   | 0.24 | -3.6 dB |
| Peaking | 2029 Hz  | 0.79 | 3.5 dB  |
| Peaking | 3719 Hz  | 1.24 | 4.1 dB  |
| Peaking | 22050 Hz | 2.47 | 3.1 dB  |
| Peaking | 617 Hz   | 4.6  | 2.1 dB  |
| Peaking | 868 Hz   | 5.53 | -2.2 dB |
| Peaking | 6333 Hz  | 5.46 | 4.9 dB  |
| Peaking | 8257 Hz  | 3.68 | -4.0 dB |
| Peaking | 15070 Hz | 3.54 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Microsoft%20Surface%20Headphones/Microsoft%20Surface%20Headphones.png)