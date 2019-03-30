# NAD Viso HP50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -11.7; 25 -11.6; 28 -11.5; 31 -11.4; 34 -11.2; 37 -11.0; 41 -10.8; 45 -10.6; 49 -10.4; 54 -10.2; 60 -9.7; 66 -9.2; 72 -8.8; 79 -8.8; 87 -9.4; 96 -10.6; 106 -11.1; 116 -10.9; 128 -11.0; 141 -11.5; 155 -11.6; 170 -11.2; 187 -10.5; 206 -9.5; 227 -8.6; 249 -8.0; 274 -7.6; 302 -7.0; 332 -6.2; 365 -5.6; 402 -5.2; 442 -4.5; 486 -4.1; 535 -3.6; 588 -3.1; 647 -2.6; 712 -1.9; 783 -1.2; 861 -1.0; 947 -1.0; 1042 -0.7; 1146 -0.7; 1261 -0.7; 1387 -0.8; 1526 -0.6; 1678 -0.5; 1846 -0.9; 2031 -1.6; 2234 -2.4; 2457 -3.3; 2703 -4.1; 2973 -4.2; 3270 -4.4; 3597 -4.9; 3957 -6.0; 4353 -7.9; 4788 -10.1; 5267 -11.3; 5793 -11.8; 6373 -12.0; 7010 -11.3; 7711 -8.8; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD Viso HP50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD Viso HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.89 | -5.6 dB |
| Peaking | 45 Hz   | 1.55 | -2.2 dB |
| Peaking | 147 Hz  | 0.83 | -5.9 dB |
| Peaking | 1223 Hz | 0.51 | 5.5 dB  |
| Peaking | 5812 Hz | 1.82 | -7.8 dB |
| Peaking | 1809 Hz | 5.36 | 0.6 dB  |
| Peaking | 2618 Hz | 5.52 | -0.8 dB |
| Peaking | 7240 Hz | 4.58 | -2.7 dB |
| Peaking | 8378 Hz | 3.27 | 1.6 dB  |
| Peaking | 8638 Hz | 1.09 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/NAD%20Viso%20HP50/NAD%20Viso%20HP50.png)