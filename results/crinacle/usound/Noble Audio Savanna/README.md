# Noble Audio Savanna
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.1; 45 -1.6; 49 -2.0; 54 -2.5; 60 -3.0; 66 -3.6; 72 -4.1; 79 -4.7; 87 -5.3; 96 -5.9; 106 -6.4; 116 -6.9; 128 -7.3; 141 -7.8; 155 -8.1; 170 -8.4; 187 -8.6; 206 -8.8; 227 -8.9; 249 -9.0; 274 -9.0; 302 -9.0; 332 -9.0; 365 -8.9; 402 -8.8; 442 -8.6; 486 -8.5; 535 -8.3; 588 -8.0; 647 -7.7; 712 -7.3; 783 -6.9; 861 -6.5; 947 -6.3; 1042 -6.4; 1146 -7.0; 1261 -7.4; 1387 -7.6; 1526 -7.2; 1678 -6.4; 1846 -5.5; 2031 -4.9; 2234 -4.8; 2457 -4.7; 2703 -3.8; 2973 -2.3; 3270 -1.2; 3597 -0.9; 3957 -1.9; 4353 -1.8; 4788 -0.5; 5267 -1.0; 5793 -6.2; 6373 -10.1; 7010 -11.0; 7711 -10.9; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -9.0; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio Savanna GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio Savanna ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.35 | 6.6 dB   |
| Peaking | 197 Hz   | 0.35 | -3.3 dB  |
| Peaking | 5062 Hz  | 0.96 | 9.8 dB   |
| Peaking | 6715 Hz  | 1.93 | -11.8 dB |
| Peaking | 18707 Hz | 1.87 | -3.0 dB  |
| Peaking | 918 Hz   | 2.96 | 1.0 dB   |
| Peaking | 1382 Hz  | 3.33 | -1.6 dB  |
| Peaking | 3401 Hz  | 3.22 | 3.0 dB   |
| Peaking | 4165 Hz  | 1.81 | -2.7 dB  |
| Peaking | 5084 Hz  | 5.28 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Noble%20Audio%20Savanna/Noble%20Audio%20Savanna.png)