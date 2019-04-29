# Ambient Acoustics AM16
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -6.0; 25 -6.3; 28 -6.7; 31 -7.0; 34 -7.3; 37 -7.4; 41 -7.6; 45 -7.8; 49 -8.0; 54 -8.2; 60 -8.3; 66 -8.6; 72 -8.8; 79 -9.0; 87 -9.3; 96 -9.5; 106 -9.7; 116 -9.9; 128 -10.0; 141 -10.1; 155 -10.1; 170 -10.0; 187 -10.0; 206 -9.9; 227 -9.8; 249 -9.6; 274 -9.4; 302 -9.2; 332 -8.9; 365 -8.5; 402 -8.3; 442 -8.1; 486 -7.9; 535 -7.7; 588 -7.5; 647 -7.2; 712 -7.0; 783 -6.8; 861 -6.7; 947 -6.9; 1042 -7.5; 1146 -8.2; 1261 -8.9; 1387 -9.1; 1526 -8.8; 1678 -8.1; 1846 -7.2; 2031 -6.3; 2234 -5.6; 2457 -0.9; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.3; 4353 -2.5; 4788 -6.5; 5267 -7.4; 5793 -3.4; 6373 -4.5; 7010 -12.1; 7711 -13.3; 8482 -7.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.2; 15026 -23.9; 16529 -32.8; 18182 -25.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM16 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM16 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 166 Hz   | 0.41 | -3.7 dB  |
| Peaking | 1502 Hz  | 1.47 | -6.4 dB  |
| Peaking | 6145 Hz  | 0.23 | 7.7 dB   |
| Peaking | 7359 Hz  | 3.57 | -11.9 dB |
| Peaking | 16716 Hz | 1.51 | -32.8 dB |
| Peaking | 20 Hz    | 1.83 | 1.4 dB   |
| Peaking | 2828 Hz  | 3.9  | 2.2 dB   |
| Peaking | 5008 Hz  | 7.84 | -6.9 dB  |
| Peaking | 13340 Hz | 2.3  | 8.4 dB   |
| Peaking | 15084 Hz | 2.33 | -9.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB   |
| Peaking | 62 Hz    | 1.41 | -1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -22.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ambient%20Acoustics%20AM16/Ambient%20Acoustics%20AM16.png)