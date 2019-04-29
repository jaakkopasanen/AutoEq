# Final Audio E4000 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -6.2; 25 -6.7; 28 -7.4; 31 -8.0; 34 -8.4; 37 -8.8; 41 -9.3; 45 -9.6; 49 -9.8; 54 -10.1; 60 -10.5; 66 -10.8; 72 -11.1; 79 -11.3; 87 -11.5; 96 -11.8; 106 -12.0; 116 -12.1; 128 -12.1; 141 -12.1; 155 -12.0; 170 -11.8; 187 -11.6; 206 -11.3; 227 -10.9; 249 -10.4; 274 -10.2; 302 -9.8; 332 -9.3; 365 -8.9; 402 -8.4; 442 -8.0; 486 -7.5; 535 -7.1; 588 -6.7; 647 -6.2; 712 -5.8; 783 -5.3; 861 -4.9; 947 -4.7; 1042 -4.6; 1146 -5.2; 1261 -6.2; 1387 -6.6; 1526 -6.5; 1678 -6.0; 1846 -5.6; 2031 -5.3; 2234 -5.3; 2457 -5.3; 2703 -5.4; 2973 -5.1; 3270 -4.4; 3597 -3.7; 3957 -2.9; 4353 -2.0; 4788 -1.4; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.1; 16529 -8.2; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E4000 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E4000 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 57 Hz    | 1.04 | -1.4 dB |
| Peaking | 143 Hz   | 0.51 | -5.5 dB |
| Peaking | 883 Hz   | 1.65 | 2.3 dB  |
| Peaking | 4492 Hz  | 1.79 | 4.2 dB  |
| Peaking | 5968 Hz  | 3.81 | 4.6 dB  |
| Peaking | 1450 Hz  | 3.04 | -1.8 dB |
| Peaking | 1627 Hz  | 1.34 | 1.1 dB  |
| Peaking | 8224 Hz  | 4.31 | -1.1 dB |
| Peaking | 16097 Hz | 3.25 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E4000%20sample%202/Final%20Audio%20E4000%20sample%202.png)