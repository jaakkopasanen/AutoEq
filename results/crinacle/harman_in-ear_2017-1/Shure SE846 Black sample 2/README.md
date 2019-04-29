# Shure SE846 Black sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.5; 25 -10.6; 28 -10.6; 31 -10.7; 34 -10.7; 37 -10.7; 41 -10.8; 45 -10.8; 49 -10.8; 54 -10.8; 60 -10.8; 66 -10.9; 72 -11.0; 79 -11.1; 87 -11.2; 96 -11.4; 106 -11.5; 116 -11.5; 128 -11.5; 141 -11.5; 155 -11.5; 170 -11.3; 187 -11.2; 206 -11.1; 227 -10.9; 249 -10.7; 274 -10.6; 302 -10.4; 332 -10.2; 365 -10.0; 402 -10.0; 442 -9.8; 486 -9.7; 535 -9.5; 588 -9.1; 647 -8.8; 712 -8.4; 783 -7.8; 861 -7.4; 947 -7.2; 1042 -7.4; 1146 -7.8; 1261 -8.0; 1387 -7.8; 1526 -7.0; 1678 -6.1; 1846 -5.3; 2031 -4.3; 2234 -3.1; 2457 -1.8; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -1.1; 3957 -2.0; 4353 -1.8; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -12.3; 16529 -7.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Black sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.54 | -3.2 dB |
| Peaking | 125 Hz   | 0.38 | -3.9 dB |
| Peaking | 2909 Hz  | 1.33 | 7.2 dB  |
| Peaking | 3120 Hz  | 0.05 | -1.8 dB |
| Peaking | 5627 Hz  | 1.76 | 6.7 dB  |
| Peaking | 913 Hz   | 3.51 | 1.1 dB  |
| Peaking | 1319 Hz  | 4.22 | -1.0 dB |
| Peaking | 13362 Hz | 2.15 | 3.2 dB  |
| Peaking | 15096 Hz | 2.53 | -7.0 dB |
| Peaking | 17409 Hz | 1.16 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shure%20SE846%20Black%20sample%202/Shure%20SE846%20Black%20sample%202.png)