# InEar StageDiver SD3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.7; 25 -7.9; 28 -8.0; 31 -8.1; 34 -8.3; 37 -8.4; 41 -8.6; 45 -8.8; 49 -8.9; 54 -9.1; 60 -9.4; 66 -9.7; 72 -10.1; 79 -10.4; 87 -10.9; 96 -11.3; 106 -11.7; 116 -12.1; 128 -12.4; 141 -12.6; 155 -12.9; 170 -13.0; 187 -13.0; 206 -13.0; 227 -12.8; 249 -12.6; 274 -12.3; 302 -11.9; 332 -11.5; 365 -11.0; 402 -10.4; 442 -9.9; 486 -9.3; 535 -8.6; 588 -8.0; 647 -7.4; 712 -6.7; 783 -6.1; 861 -5.6; 947 -5.3; 1042 -5.5; 1146 -6.1; 1261 -6.9; 1387 -7.6; 1526 -7.8; 1678 -8.0; 1846 -8.5; 2031 -9.0; 2234 -8.6; 2457 -6.3; 2703 -3.7; 2973 -2.0; 3270 -1.3; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.6; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -10.8; 16529 -11.3; 18182 -9.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar StageDiver SD3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar StageDiver SD3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 126 Hz   | 0.57 | -5.1 dB |
| Peaking | 269 Hz   | 1.14 | -3.5 dB |
| Peaking | 3442 Hz  | 2.55 | 5.2 dB  |
| Peaking | 5481 Hz  | 1.12 | 8.0 dB  |
| Peaking | 11396 Hz | 0.12 | -2.9 dB |
| Peaking | 931 Hz   | 2.81 | 2.4 dB  |
| Peaking | 2036 Hz  | 4    | -2.7 dB |
| Peaking | 7885 Hz  | 5.24 | -2.0 dB |
| Peaking | 13384 Hz | 1.21 | 3.7 dB  |
| Peaking | 15375 Hz | 1.52 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -5.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/InEar%20StageDiver%20SD3/InEar%20StageDiver%20SD3.png)