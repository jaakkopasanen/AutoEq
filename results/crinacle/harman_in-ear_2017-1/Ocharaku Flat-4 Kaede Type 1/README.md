# Ocharaku Flat-4 Kaede Type 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.7; 25 -4.1; 28 -4.7; 31 -5.3; 34 -5.7; 37 -6.1; 41 -6.6; 45 -7.0; 49 -7.2; 54 -7.4; 60 -7.8; 66 -8.2; 72 -8.5; 79 -8.9; 87 -9.4; 96 -10.0; 106 -10.4; 116 -10.6; 128 -10.8; 141 -11.1; 155 -11.4; 170 -11.3; 187 -11.3; 206 -11.2; 227 -11.0; 249 -10.8; 274 -10.6; 302 -10.2; 332 -9.6; 365 -9.0; 402 -8.5; 442 -8.1; 486 -7.8; 535 -7.2; 588 -6.7; 647 -6.2; 712 -5.8; 783 -5.5; 861 -5.5; 947 -5.7; 1042 -6.2; 1146 -6.8; 1261 -7.0; 1387 -6.1; 1526 -4.1; 1678 -1.3; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.1; 3270 -2.9; 3597 -2.4; 3957 -2.3; 4353 -3.3; 4788 -6.3; 5267 -8.8; 5793 -1.0; 6373 -1.0; 7010 -10.4; 7711 -16.9; 8482 -13.6; 9330 -8.0; 10263 -6.5; 11289 -6.9; 12418 -10.2; 13660 -15.9; 15026 -21.5; 16529 -25.7; 18182 -28.5; 20000 -25.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat-4 Kaede Type 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat-4 Kaede Type 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 184 Hz   | 0.57 | -5.1 dB  |
| Peaking | 4949 Hz  | 0.33 | 8.7 dB   |
| Peaking | 7857 Hz  | 5.34 | -12.5 dB |
| Peaking | 11252 Hz | 1.41 | 9.2 dB   |
| Peaking | 18099 Hz | 0.25 | -23.8 dB |
| Peaking | 21 Hz    | 1.5  | 3.5 dB   |
| Peaking | 1319 Hz  | 2.67 | -4.7 dB  |
| Peaking | 1801 Hz  | 1.68 | 3.3 dB   |
| Peaking | 5133 Hz  | 5.46 | -7.0 dB  |
| Peaking | 6050 Hz  | 6.28 | 7.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB   |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -23.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ocharaku%20Flat-4%20Kaede%20Type%201/Ocharaku%20Flat-4%20Kaede%20Type%201.png)