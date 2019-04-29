# Fake Shure SE846
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.5; 25 -3.1; 28 -3.8; 31 -4.3; 34 -4.8; 37 -5.2; 41 -5.6; 45 -5.9; 49 -6.2; 54 -6.6; 60 -7.0; 66 -7.4; 72 -7.8; 79 -8.2; 87 -8.6; 96 -9.2; 106 -9.6; 116 -9.9; 128 -10.2; 141 -10.6; 155 -10.8; 170 -10.9; 187 -11.0; 206 -11.0; 227 -10.8; 249 -10.7; 274 -10.5; 302 -10.2; 332 -9.7; 365 -9.3; 402 -8.9; 442 -8.5; 486 -8.0; 535 -7.5; 588 -7.0; 647 -6.4; 712 -5.9; 783 -5.4; 861 -5.1; 947 -5.2; 1042 -5.7; 1146 -6.8; 1261 -7.9; 1387 -9.1; 1526 -10.5; 1678 -12.5; 1846 -11.9; 2031 -11.7; 2234 -14.8; 2457 -13.6; 2703 -11.9; 2973 -9.4; 3270 -7.0; 3597 -1.9; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.5; 5793 -2.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fake Shure SE846 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fake Shure SE846 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.01 | 4.8 dB  |
| Peaking | 180 Hz  | 0.73 | -4.8 dB |
| Peaking | 2319 Hz | 1.69 | -8.9 dB |
| Peaking | 3898 Hz | 3.36 | 6.2 dB  |
| Peaking | 5253 Hz | 1.58 | 4.9 dB  |
| Peaking | 362 Hz  | 1.9  | -0.9 dB |
| Peaking | 876 Hz  | 1.85 | 2.6 dB  |
| Peaking | 1642 Hz | 6.08 | -2.7 dB |
| Peaking | 6487 Hz | 6.26 | 4.4 dB  |
| Peaking | 6986 Hz | 1.73 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB   |
| Peaking | 62 Hz    | 1.41 | -0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Fake%20Shure%20SE846/Fake%20Shure%20SE846.png)