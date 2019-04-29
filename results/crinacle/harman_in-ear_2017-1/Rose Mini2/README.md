# Rose Mini2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.1; 25 -2.7; 28 -3.5; 31 -4.1; 34 -4.7; 37 -5.2; 41 -5.7; 45 -6.1; 49 -6.4; 54 -6.8; 60 -7.2; 66 -7.7; 72 -8.3; 79 -8.7; 87 -9.2; 96 -9.8; 106 -10.3; 116 -10.7; 128 -11.1; 141 -11.5; 155 -11.8; 170 -12.0; 187 -12.1; 206 -12.1; 227 -12.2; 249 -12.2; 274 -12.2; 302 -12.1; 332 -11.8; 365 -11.5; 402 -11.3; 442 -11.0; 486 -10.7; 535 -10.2; 588 -9.6; 647 -9.1; 712 -8.6; 783 -8.0; 861 -7.5; 947 -7.2; 1042 -7.3; 1146 -7.7; 1261 -7.9; 1387 -7.8; 1526 -7.1; 1678 -6.3; 1846 -5.5; 2031 -4.6; 2234 -3.8; 2457 -3.4; 2703 -3.3; 2973 -2.5; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -14.9; 15026 -22.2; 16529 -25.0; 18182 -28.0; 20000 -34.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rose Mini2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rose Mini2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.71 | 6.3 dB   |
| Peaking | 119 Hz   | 1.27 | -0.7 dB  |
| Peaking | 234 Hz   | 0.45 | -5.6 dB  |
| Peaking | 455 Hz   | 1.85 | -0.5 dB  |
| Peaking | 4141 Hz  | 1.19 | 7.1 dB   |
| Peaking | 6214 Hz  | 2.2  | 4.7 dB   |
| Peaking | 11773 Hz | 1.76 | 10.7 dB  |
| Peaking | 19266 Hz | 0.25 | -13.5 dB |
| Peaking | 20746 Hz | 0.18 | -13.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB   |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 16000 Hz | 1.41 | -25.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Rose%20Mini2/Rose%20Mini2.png)