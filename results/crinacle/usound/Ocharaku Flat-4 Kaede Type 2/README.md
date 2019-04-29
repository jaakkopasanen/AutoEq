# Ocharaku Flat-4 Kaede Type 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.2; 37 -1.7; 41 -2.4; 45 -2.8; 49 -2.9; 54 -3.1; 60 -3.5; 66 -4.0; 72 -4.5; 79 -5.0; 87 -5.8; 96 -6.7; 106 -6.9; 116 -7.2; 128 -7.5; 141 -8.0; 155 -8.8; 170 -8.6; 187 -8.7; 206 -8.7; 227 -8.7; 249 -8.4; 274 -8.3; 302 -8.1; 332 -8.0; 365 -7.8; 402 -7.3; 442 -7.2; 486 -6.9; 535 -6.5; 588 -6.1; 647 -5.8; 712 -5.5; 783 -5.3; 861 -5.3; 947 -5.5; 1042 -6.0; 1146 -6.6; 1261 -7.0; 1387 -6.5; 1526 -4.9; 1678 -2.4; 1846 -0.6; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -2.3; 3270 -5.0; 3597 -5.4; 3957 -5.0; 4353 -5.2; 4788 -7.1; 5267 -10.6; 5793 -3.5; 6373 -4.9; 7010 -14.9; 7711 -20.8; 8482 -16.2; 9330 -8.4; 10263 -6.5; 11289 -8.1; 12418 -9.2; 13660 -7.6; 15026 -6.9; 16529 -9.6; 18182 -12.5; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat-4 Kaede Type 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat-4 Kaede Type 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 1.36 | 6.6 dB   |
| Peaking | 53 Hz    | 2.73 | 2.5 dB   |
| Peaking | 2295 Hz  | 1.72 | 7.0 dB   |
| Peaking | 7808 Hz  | 5.28 | -16.2 dB |
| Peaking | 18722 Hz | 1.02 | -6.5 dB  |
| Peaking | 203 Hz   | 1.12 | -2.6 dB  |
| Peaking | 1306 Hz  | 6.63 | -2.1 dB  |
| Peaking | 5263 Hz  | 7.15 | -7.4 dB  |
| Peaking | 6010 Hz  | 3.56 | 7.5 dB   |
| Peaking | 7107 Hz  | 7.78 | -5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.3 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ocharaku%20Flat-4%20Kaede%20Type%202/Ocharaku%20Flat-4%20Kaede%20Type%202.png)