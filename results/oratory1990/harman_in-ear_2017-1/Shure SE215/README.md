# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.5; 25 -9.6; 28 -9.7; 31 -9.9; 34 -10.0; 37 -10.1; 41 -10.2; 45 -10.4; 49 -10.5; 54 -10.7; 60 -10.9; 66 -11.1; 72 -11.4; 79 -11.6; 87 -11.9; 96 -12.2; 106 -12.4; 116 -12.6; 128 -12.7; 141 -12.7; 155 -12.7; 170 -12.6; 187 -12.4; 206 -12.1; 227 -11.8; 249 -11.4; 274 -11.0; 302 -10.5; 332 -10.0; 365 -9.4; 402 -8.9; 442 -8.4; 486 -7.9; 535 -7.4; 588 -6.9; 647 -6.4; 712 -6.0; 783 -5.6; 861 -5.5; 947 -5.6; 1042 -6.1; 1146 -6.6; 1261 -6.6; 1387 -6.4; 1526 -6.6; 1678 -6.8; 1846 -7.1; 2031 -7.3; 2234 -7.2; 2457 -6.2; 2703 -4.3; 2973 -2.6; 3270 -1.6; 3597 -1.8; 3957 -3.0; 4353 -5.6; 4788 -9.3; 5267 -7.9; 5793 -2.9; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -6.0; 10263 -5.9; 11289 -6.1; 12418 -8.6; 13660 -11.3; 15026 -15.2; 16529 -18.0; 18182 -17.6; 20000 -15.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.27 | -4.0 dB  |
| Peaking | 181 Hz   | 0.63 | -4.5 dB  |
| Peaking | 3354 Hz  | 4.4  | 5.0 dB   |
| Peaking | 10621 Hz | 0.63 | 7.9 dB   |
| Peaking | 16952 Hz | 0.37 | -14.8 dB |
| Peaking | 797 Hz   | 3.07 | 1.3 dB   |
| Peaking | 2045 Hz  | 2.23 | -2.1 dB  |
| Peaking | 5023 Hz  | 3.75 | -10.1 dB |
| Peaking | 6257 Hz  | 1.36 | 10.2 dB  |
| Peaking | 7752 Hz  | 1.78 | -6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -14.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20SE215/Shure%20SE215.png)