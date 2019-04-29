# Shure SE846 Black sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.4; 25 -9.5; 28 -9.7; 31 -9.8; 34 -9.9; 37 -9.9; 41 -10.0; 45 -10.1; 49 -10.1; 54 -10.1; 60 -10.2; 66 -10.4; 72 -10.5; 79 -10.6; 87 -10.7; 96 -10.8; 106 -10.9; 116 -11.0; 128 -10.9; 141 -10.9; 155 -10.9; 170 -10.7; 187 -10.6; 206 -10.4; 227 -10.3; 249 -10.2; 274 -10.0; 302 -9.9; 332 -9.6; 365 -9.4; 402 -9.4; 442 -9.4; 486 -9.2; 535 -9.1; 588 -8.9; 647 -8.7; 712 -8.4; 783 -8.0; 861 -7.7; 947 -7.6; 1042 -7.9; 1146 -8.4; 1261 -8.8; 1387 -8.7; 1526 -8.2; 1678 -7.6; 1846 -6.8; 2031 -5.8; 2234 -4.4; 2457 -2.8; 2703 -1.4; 2973 -0.5; 3270 -0.5; 3597 -1.1; 3957 -1.7; 4353 -1.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -15.2; 16529 -12.3; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Black sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 0.23 | -2.9 dB  |
| Peaking | 555 Hz   | 0.12 | -2.6 dB  |
| Peaking | 3921 Hz  | 0.8  | 8.0 dB   |
| Peaking | 13552 Hz | 3.32 | 4.7 dB   |
| Peaking | 15161 Hz | 1.89 | -10.8 dB |
| Peaking | 1536 Hz  | 2.93 | -1.6 dB  |
| Peaking | 2827 Hz  | 3.23 | 1.9 dB   |
| Peaking | 4007 Hz  | 3.9  | -2.4 dB  |
| Peaking | 6388 Hz  | 2.26 | 3.6 dB   |
| Peaking | 7588 Hz  | 2.67 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -7.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shure%20SE846%20Black%20sample%201/Shure%20SE846%20Black%20sample%201.png)