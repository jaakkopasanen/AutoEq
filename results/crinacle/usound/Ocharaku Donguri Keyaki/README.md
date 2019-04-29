# Ocharaku Donguri Keyaki
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.1; 60 -1.7; 66 -2.3; 72 -2.9; 79 -3.4; 87 -4.1; 96 -4.8; 106 -5.5; 116 -6.0; 128 -6.5; 141 -7.1; 155 -7.8; 170 -8.2; 187 -8.5; 206 -8.8; 227 -9.0; 249 -9.1; 274 -9.2; 302 -9.2; 332 -9.1; 365 -8.8; 402 -8.4; 442 -7.9; 486 -7.3; 535 -6.5; 588 -5.6; 647 -4.7; 712 -3.7; 783 -2.7; 861 -2.0; 947 -1.6; 1042 -1.8; 1146 -2.7; 1261 -3.3; 1387 -3.8; 1526 -3.9; 1678 -3.9; 1846 -4.0; 2031 -4.7; 2234 -5.9; 2457 -5.8; 2703 -6.6; 2973 -10.5; 3270 -10.1; 3597 -7.4; 3957 -6.4; 4353 -7.2; 4788 -10.0; 5267 -8.8; 5793 -2.7; 6373 -5.2; 7010 -5.9; 7711 -8.3; 8482 -11.4; 9330 -8.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.5; 15026 -13.4; 16529 -11.5; 18182 -7.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Donguri Keyaki GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Donguri Keyaki ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.85 | 7.1 dB  |
| Peaking | 1043 Hz  | 1.61 | 5.1 dB  |
| Peaking | 3096 Hz  | 6.43 | -5.2 dB |
| Peaking | 15409 Hz | 1.89 | -7.4 dB |
| Peaking | 22050 Hz | 1.67 | -4.9 dB |
| Peaking | 268 Hz   | 1.14 | -3.4 dB |
| Peaking | 4920 Hz  | 5.71 | -6.6 dB |
| Peaking | 7311 Hz  | 0.93 | 5.1 dB  |
| Peaking | 8384 Hz  | 3.03 | -9.3 dB |
| Peaking | 18982 Hz | 3.18 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ocharaku%20Donguri%20Keyaki/Ocharaku%20Donguri%20Keyaki.png)