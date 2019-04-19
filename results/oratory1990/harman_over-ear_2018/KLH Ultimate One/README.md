# KLH Ultimate One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.7; 25 -6.3; 28 -6.9; 31 -7.3; 34 -7.6; 37 -7.8; 41 -8.0; 45 -8.3; 49 -8.6; 54 -8.9; 60 -9.4; 66 -9.4; 72 -9.0; 79 -9.1; 87 -9.6; 96 -10.1; 106 -10.5; 116 -10.8; 128 -11.1; 141 -11.4; 155 -11.7; 170 -11.9; 187 -12.1; 206 -12.1; 227 -11.8; 249 -11.8; 274 -11.4; 302 -10.4; 332 -9.3; 365 -7.9; 402 -6.4; 442 -5.1; 486 -4.0; 535 -3.2; 588 -2.6; 647 -2.4; 712 -2.1; 783 -1.7; 861 -1.1; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.7; 1678 -2.6; 1846 -3.9; 2031 -5.2; 2234 -7.0; 2457 -8.5; 2703 -9.7; 2973 -9.6; 3270 -7.6; 3597 -7.1; 3957 -6.5; 4353 -5.9; 4788 -6.1; 5267 -7.6; 5793 -11.0; 6373 -10.9; 7010 -10.1; 7711 -9.7; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -7.0; 12418 -10.9; 13660 -8.9; 15026 -6.5; 16529 -10.4; 18182 -16.6; 20000 -15.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KLH Ultimate One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KLH Ultimate One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 232 Hz   | 0.47 | -13.1 dB |
| Peaking | 782 Hz   | 0.19 | 10.5 dB  |
| Peaking | 2634 Hz  | 1.41 | -9.9 dB  |
| Peaking | 6402 Hz  | 2.24 | -6.6 dB  |
| Peaking | 19072 Hz | 0.92 | -11.6 dB |
| Peaking | 19 Hz    | 2.81 | 1.9 dB   |
| Peaking | 777 Hz   | 5.91 | -0.6 dB  |
| Peaking | 11069 Hz | 2.92 | 2.1 dB   |
| Peaking | 12589 Hz | 3.05 | -4.8 dB  |
| Peaking | 15080 Hz | 3.28 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/KLH%20Ultimate%20One/KLH%20Ultimate%20One.png)