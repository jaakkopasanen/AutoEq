# FitEar Monet 17
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.5; 25 -7.7; 28 -8.1; 31 -8.3; 34 -8.5; 37 -8.7; 41 -8.9; 45 -9.1; 49 -9.3; 54 -9.5; 60 -9.7; 66 -10.0; 72 -10.3; 79 -10.6; 87 -10.9; 96 -11.4; 106 -11.7; 116 -11.9; 128 -12.1; 141 -12.3; 155 -12.4; 170 -12.3; 187 -12.2; 206 -12.1; 227 -11.8; 249 -11.5; 274 -11.1; 302 -10.7; 332 -10.2; 365 -9.6; 402 -9.1; 442 -8.5; 486 -7.9; 535 -7.2; 588 -6.4; 647 -5.6; 712 -4.7; 783 -3.7; 861 -2.9; 947 -2.2; 1042 -1.8; 1146 -1.8; 1261 -1.9; 1387 -1.6; 1526 -1.1; 1678 -0.6; 1846 -0.5; 2031 -0.7; 2234 -1.8; 2457 -3.1; 2703 -3.2; 2973 -2.7; 3270 -2.7; 3597 -2.4; 3957 -2.0; 4353 -2.9; 4788 -6.0; 5267 -10.3; 5793 -10.8; 6373 -9.3; 7010 -8.2; 7711 -6.3; 8482 -6.5; 9330 -6.8; 10263 -8.8; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Monet 17 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Monet 17 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 163 Hz   | 0.37 | -5.9 dB |
| Peaking | 973 Hz   | 0.99 | 4.7 dB  |
| Peaking | 1856 Hz  | 1.69 | 4.5 dB  |
| Peaking | 4171 Hz  | 1.75 | 6.0 dB  |
| Peaking | 5483 Hz  | 2.49 | -7.7 dB |
| Peaking | 31 Hz    | 2.04 | -0.5 dB |
| Peaking | 8289 Hz  | 3.85 | 0.8 dB  |
| Peaking | 10301 Hz | 6.27 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20Monet%2017/FitEar%20Monet%2017.png)