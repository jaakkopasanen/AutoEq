# 1Custom SA05
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.3; 25 -5.7; 28 -6.1; 31 -6.4; 34 -6.6; 37 -6.8; 41 -7.1; 45 -7.4; 49 -7.7; 54 -7.9; 60 -8.1; 66 -8.4; 72 -8.7; 79 -9.0; 87 -9.4; 96 -9.8; 106 -10.1; 116 -10.4; 128 -10.7; 141 -10.9; 155 -10.9; 170 -11.0; 187 -11.0; 206 -11.0; 227 -10.8; 249 -10.5; 274 -10.3; 302 -10.1; 332 -9.7; 365 -9.3; 402 -8.9; 442 -8.5; 486 -8.0; 535 -7.4; 588 -6.9; 647 -6.3; 712 -5.6; 783 -4.9; 861 -4.3; 947 -3.9; 1042 -3.9; 1146 -4.3; 1261 -4.8; 1387 -5.0; 1526 -4.7; 1678 -4.2; 1846 -3.6; 2031 -2.6; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.9; 3957 -5.5; 4353 -6.3; 4788 -4.5; 5267 -5.7; 5793 -7.8; 6373 -6.4; 7010 -6.3; 7711 -9.4; 8482 -10.3; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.1; 16529 -14.6; 18182 -14.6; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1Custom SA05 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1Custom SA05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 184 Hz   | 0.5  | -4.7 dB |
| Peaking | 911 Hz   | 1.57 | 2.9 dB  |
| Peaking | 2708 Hz  | 1.58 | 6.7 dB  |
| Peaking | 8097 Hz  | 6.24 | -4.4 dB |
| Peaking | 17871 Hz | 1.18 | -9.7 dB |
| Peaking | 19 Hz    | 1.67 | 2.1 dB  |
| Peaking | 2806 Hz  | 6.72 | -1.0 dB |
| Peaking | 3460 Hz  | 4.96 | 2.1 dB  |
| Peaking | 4136 Hz  | 7.3  | -2.7 dB |
| Peaking | 13183 Hz | 3.05 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -6.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/1Custom%20SA05/1Custom%20SA05.png)