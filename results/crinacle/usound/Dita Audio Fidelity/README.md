# Dita Audio Fidelity
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.0; 25 -5.9; 28 -5.8; 31 -5.7; 34 -5.5; 37 -5.4; 41 -5.2; 45 -5.1; 49 -4.9; 54 -4.7; 60 -4.6; 66 -4.5; 72 -4.5; 79 -4.6; 87 -4.6; 96 -4.8; 106 -4.8; 116 -4.8; 128 -5.1; 141 -5.1; 155 -5.2; 170 -5.7; 187 -5.3; 206 -5.1; 227 -4.9; 249 -4.8; 274 -4.5; 302 -4.3; 332 -4.1; 365 -3.8; 402 -3.5; 442 -3.2; 486 -2.9; 535 -2.6; 588 -2.2; 647 -1.8; 712 -1.4; 783 -1.0; 861 -0.6; 947 -0.5; 1042 -0.8; 1146 -1.4; 1261 -2.1; 1387 -2.5; 1526 -2.3; 1678 -1.8; 1846 -1.4; 2031 -1.2; 2234 -1.2; 2457 -1.5; 2703 -2.0; 2973 -2.7; 3270 -3.7; 3597 -4.8; 3957 -6.2; 4353 -7.8; 4788 -8.7; 5267 -7.0; 5793 -3.8; 6373 -1.8; 7010 -2.1; 7711 -6.0; 8482 -8.0; 9330 -4.6; 10263 -3.6; 11289 -4.0; 12418 -4.7; 13660 -3.6; 15026 -3.6; 16529 -3.6; 18182 -5.8; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Fidelity GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Fidelity ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.05 | -1.6 dB |
| Peaking | 833 Hz   | 1.08 | 3.3 dB  |
| Peaking | 2255 Hz  | 2.04 | 2.4 dB  |
| Peaking | 4599 Hz  | 3.41 | -5.6 dB |
| Peaking | 19789 Hz | 1.41 | -7.1 dB |
| Peaking | 22 Hz    | 0.65 | -0.9 dB |
| Peaking | 64 Hz    | 1.01 | 0.8 dB  |
| Peaking | 174 Hz   | 3.35 | -0.9 dB |
| Peaking | 6645 Hz  | 5.09 | 3.5 dB  |
| Peaking | 8297 Hz  | 5.22 | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dita%20Audio%20Fidelity/Dita%20Audio%20Fidelity.png)