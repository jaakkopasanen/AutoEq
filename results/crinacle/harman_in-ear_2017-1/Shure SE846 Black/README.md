# Shure SE846 Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.9; 25 -10.0; 28 -10.2; 31 -10.2; 34 -10.3; 37 -10.3; 41 -10.4; 45 -10.4; 49 -10.4; 54 -10.5; 60 -10.5; 66 -10.6; 72 -10.7; 79 -10.9; 87 -11.0; 96 -11.1; 106 -11.2; 116 -11.2; 128 -11.2; 141 -11.2; 155 -11.2; 170 -11.0; 187 -10.9; 206 -10.7; 227 -10.6; 249 -10.5; 274 -10.3; 302 -10.2; 332 -9.9; 365 -9.7; 402 -9.7; 442 -9.6; 486 -9.5; 535 -9.3; 588 -9.0; 647 -8.7; 712 -8.4; 783 -7.9; 861 -7.5; 947 -7.4; 1042 -7.6; 1146 -8.1; 1261 -8.4; 1387 -8.2; 1526 -7.6; 1678 -6.8; 1846 -6.1; 2031 -5.0; 2234 -3.7; 2457 -2.3; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -1.1; 3957 -1.9; 4353 -1.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -13.7; 16529 -10.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 57 Hz    | 0.18 | -3.6 dB |
| Peaking | 900 Hz   | 0.09 | -1.8 dB |
| Peaking | 2979 Hz  | 1.52 | 7.2 dB  |
| Peaking | 5501 Hz  | 1.86 | 6.6 dB  |
| Peaking | 15368 Hz | 3.54 | -8.2 dB |
| Peaking | 909 Hz   | 3.14 | 1.1 dB  |
| Peaking | 1332 Hz  | 3.62 | -1.1 dB |
| Peaking | 6571 Hz  | 7.34 | 1.9 dB  |
| Peaking | 7579 Hz  | 3.4  | -1.4 dB |
| Peaking | 13111 Hz | 5.08 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -5.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shure%20SE846%20Black/Shure%20SE846%20Black.png)