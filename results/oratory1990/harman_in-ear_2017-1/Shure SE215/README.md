# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.3; 25 -8.5; 28 -8.6; 31 -8.8; 34 -8.9; 37 -9.0; 41 -9.1; 45 -9.2; 49 -9.4; 54 -9.6; 60 -9.8; 66 -10.0; 72 -10.2; 79 -10.5; 87 -10.8; 96 -11.0; 106 -11.3; 116 -11.4; 128 -11.5; 141 -11.6; 155 -11.5; 170 -11.4; 187 -11.2; 206 -11.0; 227 -10.7; 249 -10.3; 274 -9.9; 302 -9.4; 332 -8.8; 365 -8.3; 402 -7.8; 442 -7.3; 486 -6.8; 535 -6.2; 588 -5.7; 647 -5.3; 712 -4.9; 783 -4.5; 861 -4.4; 947 -4.5; 1042 -4.9; 1146 -5.4; 1261 -5.5; 1387 -5.3; 1526 -5.5; 1678 -5.6; 1846 -6.0; 2031 -6.2; 2234 -6.1; 2457 -5.0; 2703 -3.2; 2973 -1.4; 3270 -0.5; 3597 -0.6; 3957 -1.9; 4353 -4.5; 4788 -8.2; 5267 -6.8; 5793 -1.8; 6373 -0.7; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -7.5; 13660 -10.2; 15026 -14.1; 16529 -16.9; 18182 -16.5; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 66 Hz    | 0.44 | -3.4 dB  |
| Peaking | 178 Hz   | 0.96 | -3.9 dB  |
| Peaking | 3328 Hz  | 2.91 | 6.4 dB   |
| Peaking | 6334 Hz  | 5.42 | 6.5 dB   |
| Peaking | 17869 Hz | 0.82 | -12.1 dB |
| Peaking | 837 Hz   | 1.77 | 2.2 dB   |
| Peaking | 2149 Hz  | 6.49 | -1.1 dB  |
| Peaking | 4935 Hz  | 9.49 | -4.3 dB  |
| Peaking | 11543 Hz | 1.64 | 2.3 dB   |
| Peaking | 15352 Hz | 2.75 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 16000 Hz | 1.41 | -12.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20SE215/Shure%20SE215.png)