# Vision Ears VE8 custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -6.0; 25 -6.4; 28 -6.8; 31 -7.2; 34 -7.4; 37 -7.6; 41 -7.9; 45 -8.1; 49 -8.3; 54 -8.6; 60 -8.9; 66 -9.2; 72 -9.4; 79 -9.8; 87 -10.1; 96 -10.5; 106 -10.8; 116 -11.1; 128 -11.3; 141 -11.5; 155 -11.6; 170 -11.6; 187 -11.6; 206 -11.6; 227 -11.5; 249 -11.2; 274 -11.0; 302 -10.8; 332 -10.4; 365 -10.0; 402 -9.7; 442 -9.3; 486 -9.0; 535 -8.6; 588 -8.2; 647 -7.7; 712 -7.3; 783 -6.8; 861 -6.5; 947 -6.5; 1042 -6.9; 1146 -7.6; 1261 -8.2; 1387 -8.4; 1526 -8.0; 1678 -7.0; 1846 -5.5; 2031 -3.7; 2234 -2.2; 2457 -1.2; 2703 -0.6; 2973 -0.5; 3270 -0.6; 3597 -0.9; 3957 -1.1; 4353 -1.0; 4788 -1.1; 5267 -1.0; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -9.1; 15026 -16.5; 16529 -17.6; 18182 -14.9; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears VE8 custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears VE8 custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 92 Hz    | 0.75 | -0.7 dB  |
| Peaking | 192 Hz   | 0.45 | -4.8 dB  |
| Peaking | 2823 Hz  | 2.1  | 5.4 dB   |
| Peaking | 5255 Hz  | 1.31 | 5.9 dB   |
| Peaking | 17044 Hz | 0.98 | -11.8 dB |
| Peaking | 19 Hz    | 2.39 | 1.4 dB   |
| Peaking | 1430 Hz  | 2.67 | -3.4 dB  |
| Peaking | 2386 Hz  | 0.34 | 1.5 dB   |
| Peaking | 12534 Hz | 3.18 | 4.8 dB   |
| Peaking | 17867 Hz | 0.05 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB   |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -12.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vision%20Ears%20VE8%20custom/Vision%20Ears%20VE8%20custom.png)