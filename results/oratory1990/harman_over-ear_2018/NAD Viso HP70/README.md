# NAD Viso HP70
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.2; 28 -2.4; 31 -3.5; 34 -4.4; 37 -5.0; 41 -5.5; 45 -5.9; 49 -6.2; 54 -6.7; 60 -7.2; 66 -7.6; 72 -7.9; 79 -8.2; 87 -8.6; 96 -8.8; 106 -8.7; 116 -8.3; 128 -7.5; 141 -6.5; 155 -6.5; 170 -6.9; 187 -6.9; 206 -6.5; 227 -5.8; 249 -5.1; 274 -4.3; 302 -3.8; 332 -4.2; 365 -4.4; 402 -4.5; 442 -5.0; 486 -5.7; 535 -6.2; 588 -6.0; 647 -6.2; 712 -6.6; 783 -6.1; 861 -6.1; 947 -6.3; 1042 -6.4; 1146 -6.6; 1261 -7.2; 1387 -6.3; 1526 -5.0; 1678 -3.9; 1846 -3.5; 2031 -3.4; 2234 -3.2; 2457 -3.5; 2703 -4.0; 2973 -4.6; 3270 -5.5; 3597 -7.2; 3957 -6.8; 4353 -9.3; 4788 -9.0; 5267 -7.7; 5793 -7.7; 6373 -8.3; 7010 -9.5; 7711 -7.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -10.8; 15026 -8.2; 16529 -6.5; 18182 -6.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD Viso HP70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD Viso HP70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.4  | 6.2 dB  |
| Peaking | 91 Hz    | 1.33 | -2.6 dB |
| Peaking | 327 Hz   | 1.59 | 2.9 dB  |
| Peaking | 2327 Hz  | 1.05 | 7.8 dB  |
| Peaking | 3010 Hz  | 0.46 | -4.5 dB |
| Peaking | 4145 Hz  | 5.75 | 0.8 dB  |
| Peaking | 4449 Hz  | 6.12 | -2.5 dB |
| Peaking | 6975 Hz  | 6.92 | -2.7 dB |
| Peaking | 9970 Hz  | 0.61 | 1.6 dB  |
| Peaking | 13752 Hz | 3.16 | -5.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/NAD%20Viso%20HP70/NAD%20Viso%20HP70.png)