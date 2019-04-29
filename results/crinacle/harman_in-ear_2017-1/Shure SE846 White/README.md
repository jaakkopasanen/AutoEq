# Shure SE846 White
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -8.7; 25 -8.7; 28 -8.8; 31 -8.8; 34 -8.8; 37 -8.8; 41 -8.8; 45 -8.9; 49 -8.9; 54 -8.9; 60 -9.0; 66 -9.1; 72 -9.2; 79 -9.3; 87 -9.4; 96 -9.5; 106 -9.7; 116 -9.7; 128 -9.7; 141 -9.7; 155 -9.7; 170 -9.5; 187 -9.4; 206 -9.3; 227 -9.1; 249 -9.0; 274 -8.9; 302 -8.8; 332 -8.6; 365 -8.6; 402 -8.5; 442 -8.6; 486 -8.6; 535 -8.5; 588 -8.3; 647 -8.1; 712 -7.8; 783 -7.4; 861 -7.1; 947 -7.1; 1042 -7.4; 1146 -7.9; 1261 -8.3; 1387 -8.2; 1526 -7.6; 1678 -7.0; 1846 -6.4; 2031 -5.6; 2234 -4.3; 2457 -2.8; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -1.5; 3957 -2.9; 4353 -3.2; 4788 -2.3; 5267 -1.4; 5793 -0.8; 6373 -1.5; 7010 -4.0; 7711 -6.7; 8482 -8.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.5; 15026 -14.1; 16529 -9.3; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 White GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 0.22 | -2.1 dB |
| Peaking | 920 Hz   | 0.08 | -1.6 dB |
| Peaking | 3051 Hz  | 1.71 | 7.5 dB  |
| Peaking | 5754 Hz  | 2.61 | 6.4 dB  |
| Peaking | 15216 Hz | 3.66 | -8.3 dB |
| Peaking | 909 Hz   | 2.93 | 1.1 dB  |
| Peaking | 1333 Hz  | 3.02 | -1.1 dB |
| Peaking | 8203 Hz  | 4.76 | -3.8 dB |
| Peaking | 8431 Hz  | 1.51 | 1.4 dB  |
| Peaking | 12979 Hz | 5.96 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -5.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shure%20SE846%20White/Shure%20SE846%20White.png)