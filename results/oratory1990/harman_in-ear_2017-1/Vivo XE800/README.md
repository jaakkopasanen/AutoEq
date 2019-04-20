# Vivo XE800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -4.8; 25 -4.9; 28 -4.9; 31 -5.0; 34 -5.0; 37 -5.0; 41 -5.0; 45 -5.0; 49 -5.1; 54 -5.1; 60 -5.2; 66 -5.4; 72 -5.5; 79 -5.7; 87 -6.0; 96 -6.2; 106 -6.5; 116 -6.7; 128 -6.9; 141 -7.0; 155 -7.1; 170 -7.2; 187 -7.2; 206 -7.1; 227 -7.0; 249 -7.6; 274 -7.6; 302 -7.5; 332 -7.3; 365 -7.2; 402 -7.1; 442 -7.1; 486 -7.0; 535 -7.0; 588 -6.9; 647 -6.9; 712 -6.9; 783 -6.9; 861 -7.0; 947 -7.4; 1042 -7.9; 1146 -8.3; 1261 -8.5; 1387 -8.3; 1526 -8.2; 1678 -8.0; 1846 -7.6; 2031 -7.0; 2234 -6.1; 2457 -4.9; 2703 -3.5; 2973 -2.2; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -2.0; 5267 -3.6; 5793 -5.4; 6373 -5.1; 7010 -4.0; 7711 -5.9; 8482 -9.4; 9330 -10.8; 10263 -6.6; 11289 -6.2; 12418 -10.2; 13660 -15.6; 15026 -16.8; 16529 -18.2; 18182 -18.0; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vivo XE800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vivo XE800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 2304 Hz  | 0.51 | -11.3 dB |
| Peaking | 3354 Hz  | 0.6  | 15.7 dB  |
| Peaking | 9097 Hz  | 6.75 | -4.3 dB  |
| Peaking | 11211 Hz | 2.78 | 6.6 dB   |
| Peaking | 16555 Hz | 0.44 | -13.2 dB |
| Peaking | 20 Hz    | 0.59 | 1.4 dB   |
| Peaking | 55 Hz    | 1.29 | 0.8 dB   |
| Peaking | 189 Hz   | 0.92 | -1.1 dB  |
| Peaking | 5909 Hz  | 5.48 | -2.1 dB  |
| Peaking | 6936 Hz  | 7.3  | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB   |
| Peaking | 62 Hz    | 1.41 | 0.9 dB   |
| Peaking | 125 Hz   | 1.41 | -0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -15.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Vivo%20XE800/Vivo%20XE800.png)