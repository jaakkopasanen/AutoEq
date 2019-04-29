# Westone W80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.4; 25 -9.5; 28 -9.6; 31 -9.8; 34 -9.9; 37 -10.0; 41 -10.2; 45 -10.3; 49 -10.4; 54 -10.6; 60 -10.8; 66 -11.1; 72 -11.4; 79 -11.7; 87 -12.0; 96 -12.5; 106 -12.8; 116 -13.0; 128 -13.3; 141 -13.4; 155 -13.6; 170 -13.7; 187 -13.7; 206 -13.7; 227 -13.5; 249 -13.4; 274 -13.2; 302 -12.9; 332 -12.5; 365 -12.1; 402 -11.8; 442 -11.4; 486 -11.0; 535 -10.6; 588 -10.1; 647 -9.7; 712 -9.2; 783 -8.7; 861 -8.4; 947 -8.3; 1042 -8.5; 1146 -9.0; 1261 -9.4; 1387 -9.1; 1526 -8.1; 1678 -6.5; 1846 -4.5; 2031 -2.1; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -2.3; 5793 -0.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.7; 15026 -14.2; 16529 -16.9; 18182 -21.8; 20000 -22.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.12 | -2.5 dB |
| Peaking | 225 Hz   | 0.4  | -6.0 dB |
| Peaking | 1429 Hz  | 1.92 | -4.6 dB |
| Peaking | 2450 Hz  | 1.08 | 6.9 dB  |
| Peaking | 4924 Hz  | 1.61 | 4.5 dB  |
| Peaking | 6351 Hz  | 6.37 | 3.4 dB  |
| Peaking | 12388 Hz | 1.86 | 5.0 dB  |
| Peaking | 19229 Hz | 0.35 | -8.1 dB |
| Peaking | 19404 Hz | 0.47 | -8.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -6.0 dB  |
| Peaking | 500 Hz   | 1.41 | -2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -13.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Westone%20W80/Westone%20W80.png)