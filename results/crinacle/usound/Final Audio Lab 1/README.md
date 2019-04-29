# Final Audio Lab 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.9; 25 -3.4; 28 -4.0; 31 -4.5; 34 -4.8; 37 -5.2; 41 -5.6; 45 -6.1; 49 -6.5; 54 -6.9; 60 -7.3; 66 -7.7; 72 -8.2; 79 -8.6; 87 -9.1; 96 -9.5; 106 -9.9; 116 -10.3; 128 -10.6; 141 -10.8; 155 -10.8; 170 -11.0; 187 -11.0; 206 -11.0; 227 -10.9; 249 -10.6; 274 -10.4; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.2; 442 -8.8; 486 -8.4; 535 -7.9; 588 -7.4; 647 -6.8; 712 -6.2; 783 -5.5; 861 -4.9; 947 -4.5; 1042 -4.6; 1146 -5.0; 1261 -5.4; 1387 -5.5; 1526 -5.1; 1678 -4.4; 1846 -3.8; 2031 -3.5; 2234 -3.8; 2457 -5.3; 2703 -6.8; 2973 -7.1; 3270 -5.0; 3597 -2.3; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -1.2; 5793 -5.9; 6373 -7.3; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Lab 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Lab 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  0.47 | 5.6 dB  |
| Peaking | 183 Hz  |  0.44 | -4.7 dB |
| Peaking | 929 Hz  |  1.6  | 2.7 dB  |
| Peaking | 1945 Hz |  3.73 | 2.9 dB  |
| Peaking | 4422 Hz |  2.74 | 7.0 dB  |
| Peaking | 2334 Hz |  3.74 | 2.0 dB  |
| Peaking | 2868 Hz |  2.23 | -2.8 dB |
| Peaking | 3614 Hz |  5.97 | 2.7 dB  |
| Peaking | 5265 Hz | 10.08 | 2.6 dB  |
| Peaking | 6135 Hz | 10.18 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20Lab%201/Final%20Audio%20Lab%201.png)