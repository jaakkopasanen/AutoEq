# Final Audio E5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.7; 25 -10.1; 28 -10.6; 31 -11.0; 34 -11.3; 37 -11.6; 41 -11.8; 45 -11.9; 49 -12.0; 54 -12.1; 60 -12.2; 66 -12.3; 72 -12.4; 79 -12.5; 87 -12.5; 96 -12.6; 106 -12.6; 116 -12.5; 128 -12.4; 141 -12.3; 155 -12.1; 170 -11.9; 187 -11.5; 206 -11.3; 227 -10.9; 249 -10.6; 274 -10.2; 302 -9.8; 332 -9.4; 365 -9.0; 402 -8.6; 442 -8.3; 486 -7.9; 535 -7.5; 588 -7.2; 647 -6.7; 712 -6.2; 783 -5.9; 861 -5.6; 947 -5.5; 1042 -5.7; 1146 -6.3; 1261 -6.9; 1387 -7.2; 1526 -7.0; 1678 -6.6; 1846 -6.0; 2031 -5.6; 2234 -5.3; 2457 -5.2; 2703 -5.3; 2973 -5.5; 3270 -5.2; 3597 -4.3; 3957 -3.1; 4353 -1.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.67 | -3.0 dB |
| Peaking | 126 Hz  | 0.42 | -5.5 dB |
| Peaking | 835 Hz  | 2.09 | 1.6 dB  |
| Peaking | 4734 Hz | 2.21 | 5.6 dB  |
| Peaking | 6104 Hz | 4.38 | 4.0 dB  |
| Peaking | 1043 Hz | 5.35 | 0.6 dB  |
| Peaking | 1413 Hz | 2.74 | -1.0 dB |
| Peaking | 2214 Hz | 2.81 | 1.1 dB  |
| Peaking | 6756 Hz | 8.44 | 1.5 dB  |
| Peaking | 7839 Hz | 2.39 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E5000/Final%20Audio%20E5000.png)