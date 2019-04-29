# Shure SE846 Blue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.9; 25 -10.0; 28 -10.1; 31 -10.1; 34 -10.1; 37 -10.1; 41 -10.1; 45 -10.1; 49 -10.1; 54 -10.1; 60 -10.2; 66 -10.3; 72 -10.4; 79 -10.5; 87 -10.6; 96 -10.8; 106 -10.8; 116 -10.9; 128 -10.9; 141 -10.9; 155 -10.9; 170 -10.8; 187 -10.7; 206 -10.5; 227 -10.4; 249 -10.3; 274 -10.2; 302 -10.1; 332 -9.9; 365 -9.8; 402 -9.8; 442 -9.8; 486 -9.7; 535 -9.5; 588 -9.3; 647 -9.0; 712 -8.6; 783 -8.2; 861 -7.8; 947 -7.7; 1042 -7.9; 1146 -8.4; 1261 -8.7; 1387 -8.6; 1526 -8.0; 1678 -7.2; 1846 -6.3; 2031 -5.2; 2234 -3.9; 2457 -2.4; 2703 -0.8; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -11.2; 16529 -6.9; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Blue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.39 | -3.0 dB |
| Peaking | 169 Hz   | 0.21 | -4.2 dB |
| Peaking | 1516 Hz  | 1.36 | -4.4 dB |
| Peaking | 4450 Hz  | 0.45 | 9.9 dB  |
| Peaking | 9208 Hz  | 0.43 | -5.1 dB |
| Peaking | 3982 Hz  | 6.34 | -1.2 dB |
| Peaking | 6369 Hz  | 3.28 | 3.1 dB  |
| Peaking | 7566 Hz  | 2.2  | -3.3 dB |
| Peaking | 14411 Hz | 0.85 | 3.2 dB  |
| Peaking | 14966 Hz | 3.15 | -6.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shure%20SE846%20Blue/Shure%20SE846%20Blue.png)