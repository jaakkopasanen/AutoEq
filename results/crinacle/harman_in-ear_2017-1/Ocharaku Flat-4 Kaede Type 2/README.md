# Ocharaku Flat-4 Kaede Type 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.7; 34 -2.3; 37 -2.9; 41 -3.5; 45 -3.9; 49 -4.1; 54 -4.3; 60 -4.7; 66 -5.1; 72 -5.6; 79 -6.2; 87 -6.9; 96 -7.9; 106 -8.0; 116 -8.4; 128 -8.6; 141 -9.2; 155 -9.9; 170 -9.8; 187 -9.9; 206 -9.8; 227 -9.8; 249 -9.6; 274 -9.5; 302 -9.2; 332 -8.9; 365 -8.6; 402 -8.2; 442 -8.0; 486 -7.6; 535 -7.3; 588 -6.8; 647 -6.4; 712 -6.2; 783 -6.0; 861 -6.1; 947 -6.3; 1042 -6.8; 1146 -7.4; 1261 -7.4; 1387 -6.7; 1526 -4.8; 1678 -2.3; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.6; 3270 -2.8; 3597 -3.4; 3957 -3.4; 4353 -4.0; 4788 -6.2; 5267 -9.8; 5793 -2.4; 6373 -3.4; 7010 -12.6; 7711 -17.8; 8482 -14.5; 9330 -9.3; 10263 -8.1; 11289 -9.5; 12418 -11.8; 13660 -16.5; 15026 -23.2; 16529 -28.5; 18182 -28.9; 20000 -22.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat-4 Kaede Type 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat-4 Kaede Type 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.3  | 6.8 dB   |
| Peaking | 187 Hz   | 0.61 | -3.8 dB  |
| Peaking | 2484 Hz  | 1.34 | 7.2 dB   |
| Peaking | 16954 Hz | 0.87 | -19.7 dB |
| Peaking | 19383 Hz | 0.93 | -11.5 dB |
| Peaking | 1291 Hz  | 3.79 | -2.6 dB  |
| Peaking | 1800 Hz  | 5.56 | 2.5 dB   |
| Peaking | 6205 Hz  | 6.29 | 9.6 dB   |
| Peaking | 7739 Hz  | 2.89 | -12.2 dB |
| Peaking | 10265 Hz | 1.87 | 5.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB   |
| Peaking | 62 Hz    | 1.41 | 1.0 dB   |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -26.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ocharaku%20Flat-4%20Kaede%20Type%202/Ocharaku%20Flat-4%20Kaede%20Type%202.png)