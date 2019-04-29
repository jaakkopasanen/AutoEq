# Westone W60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -8.9; 25 -9.0; 28 -9.2; 31 -9.4; 34 -9.5; 37 -9.6; 41 -9.7; 45 -9.9; 49 -10.0; 54 -10.2; 60 -10.5; 66 -10.8; 72 -11.1; 79 -11.4; 87 -11.8; 96 -12.2; 106 -12.6; 116 -12.9; 128 -13.2; 141 -13.4; 155 -13.6; 170 -13.7; 187 -13.8; 206 -13.7; 227 -13.6; 249 -13.4; 274 -13.2; 302 -12.9; 332 -12.4; 365 -11.9; 402 -11.5; 442 -11.1; 486 -10.5; 535 -9.9; 588 -9.3; 647 -8.6; 712 -7.9; 783 -7.2; 861 -6.5; 947 -6.2; 1042 -6.3; 1146 -6.8; 1261 -7.3; 1387 -7.5; 1526 -7.0; 1678 -6.0; 1846 -4.2; 2031 -1.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -15.6; 15026 -26.2; 16529 -28.2; 18182 -25.9; 20000 -24.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.81 | -1.3 dB  |
| Peaking | 187 Hz   | 0.7  | -3.1 dB  |
| Peaking | 306 Hz   | 0.13 | -4.6 dB  |
| Peaking | 7947 Hz  | 0.2  | 16.8 dB  |
| Peaking | 16709 Hz | 0.39 | -33.5 dB |
| Peaking | 1501 Hz  | 2.01 | -6.9 dB  |
| Peaking | 1580 Hz  | 0.8  | 3.9 dB   |
| Peaking | 8347 Hz  | 4.02 | -4.2 dB  |
| Peaking | 12250 Hz | 3.03 | 8.3 dB   |
| Peaking | 15168 Hz | 1.49 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -6.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 16000 Hz | 1.41 | -26.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Westone%20W60/Westone%20W60.png)