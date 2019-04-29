# FitEar Parterre
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.5; 25 -9.5; 28 -9.5; 31 -9.6; 34 -9.7; 37 -9.8; 41 -9.9; 45 -10.0; 49 -10.1; 54 -10.3; 60 -10.5; 66 -10.8; 72 -11.0; 79 -11.3; 87 -11.6; 96 -11.9; 106 -12.2; 116 -12.4; 128 -12.6; 141 -12.8; 155 -12.8; 170 -12.8; 187 -12.8; 206 -12.5; 227 -12.3; 249 -12.0; 274 -11.7; 302 -11.3; 332 -10.9; 365 -10.5; 402 -10.0; 442 -9.5; 486 -8.9; 535 -8.3; 588 -7.7; 647 -6.9; 712 -6.1; 783 -5.3; 861 -4.5; 947 -3.9; 1042 -3.6; 1146 -3.8; 1261 -3.9; 1387 -3.7; 1526 -3.1; 1678 -2.3; 1846 -1.7; 2031 -1.6; 2234 -1.5; 2457 -1.3; 2703 -0.9; 2973 -0.6; 3270 -0.5; 3597 -0.6; 3957 -0.9; 4353 -1.6; 4788 -1.1; 5267 -0.7; 5793 -0.9; 6373 -2.1; 7010 -6.4; 7711 -9.5; 8482 -6.7; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Parterre GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Parterre ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.21 | -3.0 dB |
| Peaking | 122 Hz  | 0.79 | -2.3 dB |
| Peaking | 263 Hz  | 0.55 | -4.7 dB |
| Peaking | 1701 Hz | 0.53 | 3.9 dB  |
| Peaking | 4090 Hz | 1.23 | 4.2 dB  |
| Peaking | 929 Hz  | 3.81 | 0.9 dB  |
| Peaking | 1342 Hz | 4.66 | -1.2 dB |
| Peaking | 4337 Hz | 4.72 | -2.0 dB |
| Peaking | 6192 Hz | 1.97 | 4.1 dB  |
| Peaking | 7532 Hz | 3.52 | -6.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20Parterre/FitEar%20Parterre.png)