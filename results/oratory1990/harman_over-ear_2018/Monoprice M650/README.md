# Monoprice M650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -10.0; 25 -10.4; 28 -10.8; 31 -11.1; 34 -11.4; 37 -11.6; 41 -11.8; 45 -12.0; 49 -12.2; 54 -12.3; 60 -12.5; 66 -12.5; 72 -12.5; 79 -12.8; 87 -13.1; 96 -13.6; 106 -14.3; 116 -14.5; 128 -14.7; 141 -15.2; 155 -15.5; 170 -15.7; 187 -15.7; 206 -15.6; 227 -15.3; 249 -15.2; 274 -14.8; 302 -14.2; 332 -13.7; 365 -13.1; 402 -12.5; 442 -11.8; 486 -11.2; 535 -10.3; 588 -9.5; 647 -8.6; 712 -7.1; 783 -6.5; 861 -5.4; 947 -4.6; 1042 -3.6; 1146 -2.9; 1261 -2.5; 1387 -3.3; 1526 -3.4; 1678 -4.0; 1846 -5.1; 2031 -6.1; 2234 -6.9; 2457 -7.3; 2703 -8.0; 2973 -8.0; 3270 -5.7; 3597 -3.6; 3957 -0.5; 4353 -1.5; 4788 -2.7; 5267 -6.4; 5793 -9.1; 6373 -8.7; 7010 -8.8; 7711 -10.2; 8482 -7.9; 9330 -5.6; 10263 -6.4; 11289 -8.0; 12418 -6.5; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice M650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice M650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 0.27 | -7.3 dB |
| Peaking | 205 Hz   | 0.78 | -7.5 dB |
| Peaking | 430 Hz   | 1.5  | -4.1 dB |
| Peaking | 2663 Hz  | 4.44 | -4.2 dB |
| Peaking | 7461 Hz  | 2.08 | -6.0 dB |
| Peaking | 1224 Hz  | 2.93 | 2.7 dB  |
| Peaking | 3342 Hz  | 1.67 | -4.4 dB |
| Peaking | 4036 Hz  | 2    | 7.5 dB  |
| Peaking | 5669 Hz  | 5.46 | -4.4 dB |
| Peaking | 11517 Hz | 5.29 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -9.5 dB |
| Peaking | 500 Hz   | 1.41 | -5.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Monoprice%20M650/Monoprice%20M650.png)