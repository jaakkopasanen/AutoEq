# Dita Fealty
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.1; 25 -6.4; 28 -6.8; 31 -7.2; 34 -7.4; 37 -7.7; 41 -8.0; 45 -8.2; 49 -8.4; 54 -8.6; 60 -8.9; 66 -9.2; 72 -9.5; 79 -9.8; 87 -10.0; 96 -10.4; 106 -10.6; 116 -10.9; 128 -11.0; 141 -11.1; 155 -11.2; 170 -11.2; 187 -11.1; 206 -11.1; 227 -10.9; 249 -10.8; 274 -10.6; 302 -10.4; 332 -10.1; 365 -9.7; 402 -9.4; 442 -9.2; 486 -8.9; 535 -8.6; 588 -8.2; 647 -7.9; 712 -7.5; 783 -7.0; 861 -6.6; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.0; 1387 -6.2; 1526 -4.8; 1678 -4.2; 1846 -2.9; 2031 -1.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -2.1; 4353 -3.8; 4788 -5.7; 5267 -6.7; 5793 -4.8; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.3; 13660 -11.8; 15026 -16.8; 16529 -20.9; 18182 -24.1; 20000 -23.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Fealty GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Fealty ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 142 Hz   | 0.52 | -2.0 dB  |
| Peaking | 208 Hz   | 0.33 | -2.8 dB  |
| Peaking | 2800 Hz  | 1.08 | 7.1 dB   |
| Peaking | 11354 Hz | 0.61 | 10.4 dB  |
| Peaking | 18219 Hz | 0.3  | -20.7 dB |
| Peaking | 19 Hz    | 2.02 | 1.4 dB   |
| Peaking | 1285 Hz  | 6.34 | -1.5 dB  |
| Peaking | 5205 Hz  | 5.17 | -2.8 dB  |
| Peaking | 6501 Hz  | 4.64 | 4.1 dB   |
| Peaking | 8370 Hz  | 3.24 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -17.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dita%20Fealty/Dita%20Fealty.png)