# Empire Ears Legend X sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.8; 25 -12.8; 28 -12.8; 31 -12.7; 34 -12.6; 37 -12.6; 41 -12.5; 45 -12.4; 49 -12.3; 54 -12.1; 60 -12.0; 66 -12.0; 72 -11.9; 79 -11.9; 87 -11.9; 96 -11.9; 106 -11.9; 116 -11.8; 128 -11.6; 141 -11.4; 155 -11.2; 170 -10.8; 187 -10.5; 206 -10.1; 227 -9.6; 249 -9.1; 274 -8.7; 302 -8.2; 332 -7.7; 365 -7.2; 402 -6.7; 442 -6.2; 486 -5.8; 535 -5.3; 588 -5.0; 647 -4.6; 712 -3.9; 783 -2.9; 861 -2.7; 947 -3.0; 1042 -3.9; 1146 -5.1; 1261 -6.2; 1387 -7.1; 1526 -7.6; 1678 -7.7; 1846 -7.6; 2031 -7.3; 2234 -6.7; 2457 -5.9; 2703 -4.8; 2973 -3.9; 3270 -2.9; 3597 -1.7; 3957 -1.3; 4353 -2.8; 4788 -0.5; 5267 -0.9; 5793 -3.3; 6373 -2.7; 7010 -5.0; 7711 -8.3; 8482 -8.8; 9330 -6.9; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -8.7; 15026 -11.7; 16529 -10.2; 18182 -8.6; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Legend X sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Legend X sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.24 | -6.3 dB |
| Peaking | 148 Hz   | 0.8  | -3.1 dB |
| Peaking | 809 Hz   | 2.29 | 4.1 dB  |
| Peaking | 4566 Hz  | 1.68 | 5.7 dB  |
| Peaking | 15853 Hz | 1.23 | -5.1 dB |
| Peaking | 1768 Hz  | 2.35 | -2.2 dB |
| Peaking | 3335 Hz  | 4.3  | 1.6 dB  |
| Peaking | 6539 Hz  | 5.75 | 2.4 dB  |
| Peaking | 8063 Hz  | 3.92 | -3.7 dB |
| Peaking | 12196 Hz | 3.29 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -5.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Empire%20Ears%20Legend%20X%20sample%201/Empire%20Ears%20Legend%20X%20sample%201.png)