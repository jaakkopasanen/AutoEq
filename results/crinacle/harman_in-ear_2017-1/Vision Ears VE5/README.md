# Vision Ears VE5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.9; 25 -3.2; 28 -3.5; 31 -3.8; 34 -4.0; 37 -4.3; 41 -4.5; 45 -4.8; 49 -5.1; 54 -5.4; 60 -5.7; 66 -6.0; 72 -6.5; 79 -6.9; 87 -7.3; 96 -7.9; 106 -8.3; 116 -8.6; 128 -9.0; 141 -9.3; 155 -9.6; 170 -9.9; 187 -10.0; 206 -10.2; 227 -10.2; 249 -10.2; 274 -10.2; 302 -10.1; 332 -10.0; 365 -9.8; 402 -9.7; 442 -9.5; 486 -9.3; 535 -9.1; 588 -8.9; 647 -8.6; 712 -8.3; 783 -8.0; 861 -7.8; 947 -7.7; 1042 -7.9; 1146 -8.2; 1261 -8.3; 1387 -7.9; 1526 -7.2; 1678 -6.3; 1846 -5.5; 2031 -4.7; 2234 -4.1; 2457 -4.1; 2703 -4.1; 2973 -2.6; 3270 -0.8; 3597 -2.3; 3957 -5.1; 4353 -5.9; 4788 -4.0; 5267 -2.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -14.4; 16529 -20.8; 18182 -20.2; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears VE5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears VE5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.29 | 3.9 dB   |
| Peaking | 238 Hz   | 0.26 | -4.0 dB  |
| Peaking | 5898 Hz  | 0.47 | 6.1 dB   |
| Peaking | 13469 Hz | 1.56 | 10.5 dB  |
| Peaking | 16731 Hz | 0.5  | -18.2 dB |
| Peaking | 1326 Hz  | 4.62 | -1.6 dB  |
| Peaking | 3353 Hz  | 4.03 | 3.7 dB   |
| Peaking | 4244 Hz  | 2.95 | -4.9 dB  |
| Peaking | 6130 Hz  | 2.36 | 4.0 dB   |
| Peaking | 7561 Hz  | 3.48 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB   |
| Peaking | 62 Hz    | 1.41 | 0.6 dB   |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 16000 Hz | 1.41 | -13.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vision%20Ears%20VE5/Vision%20Ears%20VE5.png)