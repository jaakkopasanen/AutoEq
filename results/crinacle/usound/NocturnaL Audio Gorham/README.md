# NocturnaL Audio Gorham
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.6; 25 -6.0; 28 -6.4; 31 -6.7; 34 -7.0; 37 -7.2; 41 -7.4; 45 -7.7; 49 -7.9; 54 -8.2; 60 -8.4; 66 -8.7; 72 -9.1; 79 -9.4; 87 -9.8; 96 -10.1; 106 -10.5; 116 -10.9; 128 -11.1; 141 -11.3; 155 -11.4; 170 -11.5; 187 -11.5; 206 -11.6; 227 -11.4; 249 -11.2; 274 -11.0; 302 -10.7; 332 -10.4; 365 -10.1; 402 -9.7; 442 -9.2; 486 -8.8; 535 -8.3; 588 -7.7; 647 -7.2; 712 -6.5; 783 -5.8; 861 -5.2; 947 -4.8; 1042 -4.8; 1146 -5.2; 1261 -5.6; 1387 -5.7; 1526 -5.5; 1678 -4.9; 1846 -4.4; 2031 -4.1; 2234 -4.0; 2457 -3.8; 2703 -2.7; 2973 -1.3; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.2; 5793 -4.6; 6373 -6.7; 7010 -9.9; 7711 -7.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -10.2; 15026 -12.2; 16529 -8.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NocturnaL Audio Gorham GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NocturnaL Audio Gorham ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 145 Hz   | 0.65 | -4.6 dB |
| Peaking | 317 Hz   | 1.27 | -2.4 dB |
| Peaking | 4382 Hz  | 0.72 | 7.1 dB  |
| Peaking | 6946 Hz  | 2.59 | -7.3 dB |
| Peaking | 14828 Hz | 2.41 | -6.6 dB |
| Peaking | 21 Hz    | 2.22 | 1.5 dB  |
| Peaking | 504 Hz   | 3.26 | -0.6 dB |
| Peaking | 927 Hz   | 2.89 | 1.7 dB  |
| Peaking | 2675 Hz  | 1.9  | -1.2 dB |
| Peaking | 3076 Hz  | 3.96 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/NocturnaL%20Audio%20Gorham/NocturnaL%20Audio%20Gorham.png)