# Vision Ears VE8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -5.9; 25 -6.1; 28 -6.4; 31 -6.6; 34 -6.8; 37 -6.9; 41 -7.2; 45 -7.4; 49 -7.6; 54 -7.8; 60 -8.0; 66 -8.4; 72 -8.7; 79 -9.1; 87 -9.4; 96 -9.9; 106 -10.2; 116 -10.5; 128 -10.8; 141 -11.0; 155 -11.2; 170 -11.2; 187 -11.2; 206 -11.2; 227 -11.1; 249 -10.9; 274 -10.7; 302 -10.4; 332 -9.9; 365 -9.5; 402 -9.2; 442 -8.8; 486 -8.4; 535 -7.9; 588 -7.4; 647 -7.0; 712 -6.4; 783 -5.9; 861 -5.6; 947 -5.5; 1042 -5.8; 1146 -6.5; 1261 -7.1; 1387 -7.3; 1526 -7.0; 1678 -6.3; 1846 -5.2; 2031 -4.0; 2234 -2.9; 2457 -2.1; 2703 -1.7; 2973 -1.4; 3270 -1.1; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -1.4; 5793 -3.0; 6373 -3.1; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.9; 15026 -16.3; 16529 -20.5; 18182 -21.7; 20000 -23.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears VE8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears VE8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.51 | 1.3 dB   |
| Peaking | 171 Hz   | 0.83 | -1.0 dB  |
| Peaking | 189 Hz   | 0.41 | -3.9 dB  |
| Peaking | 801 Hz   | 2.67 | 1.8 dB   |
| Peaking | 3773 Hz  | 1.11 | 6.7 dB   |
| Peaking | 1495 Hz  | 2.09 | -2.8 dB  |
| Peaking | 3626 Hz  | 1.86 | -3.6 dB  |
| Peaking | 5839 Hz  | 0.37 | 6.5 dB   |
| Peaking | 12727 Hz | 1.56 | 10.0 dB  |
| Peaking | 18196 Hz | 0.21 | -17.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -15.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vision%20Ears%20VE8/Vision%20Ears%20VE8.png)