# Final Audio E3000 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.6; 25 -4.2; 28 -5.0; 31 -5.7; 34 -6.2; 37 -6.7; 41 -7.3; 45 -7.7; 49 -8.1; 54 -8.6; 60 -9.1; 66 -9.6; 72 -10.0; 79 -10.4; 87 -10.7; 96 -11.1; 106 -11.4; 116 -11.6; 128 -11.7; 141 -11.8; 155 -11.8; 170 -11.6; 187 -11.4; 206 -11.0; 227 -10.8; 249 -10.5; 274 -10.2; 302 -9.7; 332 -9.2; 365 -8.7; 402 -8.2; 442 -7.7; 486 -7.2; 535 -6.6; 588 -6.1; 647 -5.5; 712 -4.9; 783 -3.8; 861 -3.6; 947 -3.6; 1042 -3.7; 1146 -4.4; 1261 -5.1; 1387 -5.5; 1526 -5.2; 1678 -4.6; 1846 -4.2; 2031 -3.8; 2234 -3.4; 2457 -3.2; 2703 -3.6; 2973 -3.3; 3270 -2.6; 3597 -2.0; 3957 -1.2; 4353 -0.5; 4788 -0.6; 5267 -1.3; 5793 -2.3; 6373 -3.6; 7010 -4.1; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E3000 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E3000 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.13 | 4.1 dB  |
| Peaking | 93 Hz   | 0.53 | -2.0 dB |
| Peaking | 172 Hz  | 0.45 | -4.4 dB |
| Peaking | 864 Hz  | 1.3  | 3.0 dB  |
| Peaking | 4283 Hz | 1.23 | 5.4 dB  |
| Peaking | 1412 Hz | 4.85 | -1.0 dB |
| Peaking | 2209 Hz | 1.96 | 1.4 dB  |
| Peaking | 3688 Hz | 1.29 | -1.4 dB |
| Peaking | 5231 Hz | 1.34 | 1.6 dB  |
| Peaking | 8162 Hz | 1.41 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E3000%20sample%202/Final%20Audio%20E3000%20sample%202.png)