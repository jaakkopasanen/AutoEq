# Advanced M55D
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.8; 25 -7.9; 28 -8.1; 31 -8.3; 34 -8.3; 37 -8.4; 41 -8.5; 45 -8.5; 49 -8.6; 54 -8.6; 60 -8.7; 66 -8.8; 72 -8.9; 79 -9.1; 87 -9.3; 96 -9.5; 106 -9.7; 116 -9.8; 128 -10.0; 141 -10.1; 155 -10.2; 170 -10.1; 187 -10.1; 206 -10.0; 227 -9.9; 249 -9.7; 274 -9.5; 302 -9.3; 332 -9.1; 365 -8.8; 402 -8.6; 442 -8.3; 486 -8.1; 535 -7.8; 588 -7.5; 647 -7.1; 712 -6.6; 783 -6.1; 861 -5.7; 947 -5.3; 1042 -5.2; 1146 -5.3; 1261 -5.4; 1387 -5.2; 1526 -4.5; 1678 -3.9; 1846 -3.6; 2031 -3.8; 2234 -3.9; 2457 -3.3; 2703 -1.8; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -5.7; 5793 -7.0; 6373 -8.7; 7010 -11.5; 7711 -14.9; 8482 -12.1; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -10.0; 15026 -13.2; 16529 -15.6; 18182 -18.3; 20000 -20.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced M55D GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced M55D ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 47 Hz    | 0.22 | -1.4 dB |
| Peaking | 218 Hz   | 0.43 | -2.9 dB |
| Peaking | 1442 Hz  | 0.53 | 1.7 dB  |
| Peaking | 3792 Hz  | 1.33 | 6.6 dB  |
| Peaking | 7600 Hz  | 2.72 | -9.5 dB |
| Peaking | 7900 Hz  | 0.52 | 1.0 dB  |
| Peaking | 9702 Hz  | 3.73 | 3.1 dB  |
| Peaking | 12325 Hz | 2.09 | 4.8 dB  |
| Peaking | 18678 Hz | 0.26 | -7.3 dB |
| Peaking | 20011 Hz | 0.41 | -6.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | -9.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20M55D/Advanced%20M55D.png)