# InEar StageDiver SD2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.9; 25 -4.0; 28 -4.2; 31 -4.4; 34 -4.5; 37 -4.7; 41 -4.8; 45 -5.0; 49 -5.2; 54 -5.4; 60 -5.7; 66 -6.0; 72 -6.4; 79 -6.8; 87 -7.2; 96 -7.6; 106 -8.1; 116 -8.4; 128 -8.8; 141 -9.1; 155 -9.4; 170 -9.6; 187 -9.7; 206 -9.7; 227 -9.8; 249 -9.7; 274 -9.7; 302 -9.6; 332 -9.5; 365 -9.4; 402 -9.3; 442 -9.0; 486 -8.7; 535 -8.4; 588 -8.0; 647 -7.6; 712 -7.1; 783 -6.6; 861 -6.2; 947 -6.0; 1042 -6.2; 1146 -6.9; 1261 -7.8; 1387 -8.3; 1526 -8.4; 1678 -8.4; 1846 -8.4; 2031 -8.4; 2234 -7.9; 2457 -5.9; 2703 -3.5; 2973 -1.8; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -4.2; 5793 -3.8; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.3; 15026 -12.9; 16529 -12.2; 18182 -11.2; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar StageDiver SD2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar StageDiver SD2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.2  | 2.9 dB  |
| Peaking | 194 Hz   | 0.4  | -3.9 dB |
| Peaking | 3912 Hz  | 1.95 | 7.1 dB  |
| Peaking | 6406 Hz  | 6.09 | 4.6 dB  |
| Peaking | 17138 Hz | 0.82 | -6.3 dB |
| Peaking | 922 Hz   | 2.21 | 2.1 dB  |
| Peaking | 1988 Hz  | 1.02 | -3.2 dB |
| Peaking | 2914 Hz  | 3.18 | 3.7 dB  |
| Peaking | 13024 Hz | 1.8  | 3.1 dB  |
| Peaking | 14536 Hz | 3.08 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -7.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/InEar%20StageDiver%20SD2/InEar%20StageDiver%20SD2.png)