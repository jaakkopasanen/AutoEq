# 1Custom SA03
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.7; 25 -6.0; 28 -6.4; 31 -6.6; 34 -6.8; 37 -6.9; 41 -7.2; 45 -7.5; 49 -7.7; 54 -7.9; 60 -8.1; 66 -8.4; 72 -8.7; 79 -9.0; 87 -9.4; 96 -9.8; 106 -10.2; 116 -10.5; 128 -10.7; 141 -10.9; 155 -11.0; 170 -11.0; 187 -11.1; 206 -11.1; 227 -11.0; 249 -10.7; 274 -10.5; 302 -10.3; 332 -10.0; 365 -9.6; 402 -9.2; 442 -8.8; 486 -8.3; 535 -7.8; 588 -7.2; 647 -6.6; 712 -5.9; 783 -5.2; 861 -4.6; 947 -4.2; 1042 -4.2; 1146 -4.6; 1261 -5.0; 1387 -5.2; 1526 -4.8; 1678 -4.0; 1846 -3.2; 2031 -2.1; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -2.8; 4353 -4.4; 4788 -3.8; 5267 -4.0; 5793 -5.4; 6373 -8.3; 7010 -6.6; 7711 -6.8; 8482 -10.6; 9330 -12.3; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.1; 16529 -9.6; 18182 -10.2; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1Custom SA03 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1Custom SA03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 188 Hz   |  0.48 | -4.8 dB |
| Peaking | 894 Hz   |  1.97 | 2.5 dB  |
| Peaking | 2822 Hz  |  1.16 | 6.7 dB  |
| Peaking | 9086 Hz  |  4.63 | -6.7 dB |
| Peaking | 18092 Hz |  1.23 | -4.3 dB |
| Peaking | 19 Hz    |  1.63 | 1.6 dB  |
| Peaking | 3570 Hz  | 13.26 | 1.2 dB  |
| Peaking | 5257 Hz  |  8.31 | 1.2 dB  |
| Peaking | 6390 Hz  |  9.1  | -2.9 dB |
| Peaking | 12402 Hz |  1.78 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/1Custom%20SA03/1Custom%20SA03.png)