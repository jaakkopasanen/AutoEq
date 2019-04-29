# Westone W30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.3; 25 -7.5; 28 -7.8; 31 -8.0; 34 -8.2; 37 -8.3; 41 -8.6; 45 -8.8; 49 -9.0; 54 -9.2; 60 -9.5; 66 -9.8; 72 -10.2; 79 -10.5; 87 -10.9; 96 -11.5; 106 -11.9; 116 -12.2; 128 -12.5; 141 -12.8; 155 -13.0; 170 -13.3; 187 -13.3; 206 -13.4; 227 -13.3; 249 -13.3; 274 -13.2; 302 -13.0; 332 -12.7; 365 -12.4; 402 -12.1; 442 -11.8; 486 -11.4; 535 -10.9; 588 -10.4; 647 -9.9; 712 -9.2; 783 -8.5; 861 -7.9; 947 -7.5; 1042 -7.4; 1146 -7.5; 1261 -7.5; 1387 -7.1; 1526 -6.2; 1678 -5.0; 1846 -3.6; 2031 -1.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -9.7; 9330 -10.5; 10263 -8.3; 11289 -6.5; 12418 -6.6; 13660 -15.1; 15026 -23.6; 16529 -23.7; 18182 -22.1; 20000 -23.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 213 Hz   | 0.5  | -4.1 dB  |
| Peaking | 309 Hz   | 0.14 | -3.0 dB  |
| Peaking | 3403 Hz  | 0.58 | 8.0 dB   |
| Peaking | 15648 Hz | 2.24 | -12.7 dB |
| Peaking | 19337 Hz | 0.55 | -16.7 dB |
| Peaking | 1429 Hz  | 4.01 | -1.4 dB  |
| Peaking | 2169 Hz  | 6.14 | 2.0 dB   |
| Peaking | 6172 Hz  | 4.08 | 3.0 dB   |
| Peaking | 8813 Hz  | 3.07 | -4.9 dB  |
| Peaking | 11823 Hz | 3.7  | 5.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -6.0 dB  |
| Peaking | 500 Hz   | 1.41 | -3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -22.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Westone%20W30/Westone%20W30.png)