# Vision Ears VE6X1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.1; 25 -6.2; 28 -6.4; 31 -6.7; 34 -6.9; 37 -7.0; 41 -7.3; 45 -7.4; 49 -7.6; 54 -7.8; 60 -8.1; 66 -8.4; 72 -8.8; 79 -9.2; 87 -9.6; 96 -10.0; 106 -10.4; 116 -10.8; 128 -11.1; 141 -11.4; 155 -11.7; 170 -11.8; 187 -11.9; 206 -11.9; 227 -11.9; 249 -11.9; 274 -11.8; 302 -11.5; 332 -11.2; 365 -10.9; 402 -10.7; 442 -10.4; 486 -10.0; 535 -9.6; 588 -9.2; 647 -8.8; 712 -8.3; 783 -7.8; 861 -7.4; 947 -7.0; 1042 -6.9; 1146 -6.9; 1261 -6.8; 1387 -6.3; 1526 -5.4; 1678 -4.5; 1846 -3.6; 2031 -2.8; 2234 -2.3; 2457 -2.5; 2703 -2.6; 2973 -1.5; 3270 -0.8; 3597 -1.4; 3957 -3.0; 4353 -4.0; 4788 -2.7; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -15.0; 16529 -17.8; 18182 -14.7; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears VE6X1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears VE6X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 222 Hz   | 0.42 | -5.6 dB  |
| Peaking | 2902 Hz  | 0.96 | 5.5 dB   |
| Peaking | 5932 Hz  | 2.69 | 6.4 dB   |
| Peaking | 13632 Hz | 0.84 | 16.4 dB  |
| Peaking | 15645 Hz | 0.62 | -22.6 dB |
| Peaking | 19 Hz    | 1.07 | 0.8 dB   |
| Peaking | 1350 Hz  | 3.1  | -1.3 dB  |
| Peaking | 2209 Hz  | 1.1  | 2.1 dB   |
| Peaking | 2903 Hz  | 1.59 | -3.5 dB  |
| Peaking | 3274 Hz  | 4.05 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB   |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -11.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vision%20Ears%20VE6X1/Vision%20Ears%20VE6X1.png)