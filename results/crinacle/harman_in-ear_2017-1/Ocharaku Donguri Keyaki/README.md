# Ocharaku Donguri Keyaki
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.8; 37 -0.9; 41 -1.2; 45 -1.5; 49 -1.8; 54 -2.3; 60 -2.9; 66 -3.5; 72 -4.0; 79 -4.6; 87 -5.2; 96 -5.9; 106 -6.6; 116 -7.1; 128 -7.7; 141 -8.3; 155 -9.0; 170 -9.4; 187 -9.6; 206 -9.9; 227 -10.2; 249 -10.3; 274 -10.3; 302 -10.3; 332 -10.1; 365 -9.6; 402 -9.3; 442 -8.7; 486 -8.1; 535 -7.2; 588 -6.3; 647 -5.4; 712 -4.3; 783 -3.4; 861 -2.7; 947 -2.4; 1042 -2.6; 1146 -3.4; 1261 -3.7; 1387 -3.9; 1526 -3.9; 1678 -3.7; 1846 -3.8; 2031 -4.2; 2234 -4.7; 2457 -4.1; 2703 -4.5; 2973 -8.2; 3270 -7.9; 3597 -5.4; 3957 -4.8; 4353 -6.0; 4788 -9.1; 5267 -8.0; 5793 -1.6; 6373 -3.7; 7010 -4.3; 7711 -6.2; 8482 -9.7; 9330 -9.9; 10263 -6.6; 11289 -6.5; 12418 -7.8; 13660 -19.4; 15026 -29.7; 16529 -30.3; 18182 -23.6; 20000 -16.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Donguri Keyaki GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Donguri Keyaki ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.32 | 9.2 dB   |
| Peaking | 417 Hz   | 0.2  | -20.2 dB |
| Peaking | 828 Hz   | 0.24 | 20.8 dB  |
| Peaking | 11585 Hz | 0.55 | 21.3 dB  |
| Peaking | 15486 Hz | 0.51 | -39.9 dB |
| Peaking | 3116 Hz  | 7.38 | -4.5 dB  |
| Peaking | 5011 Hz  | 4.53 | -10.5 dB |
| Peaking | 5542 Hz  | 1.69 | 8.5 dB   |
| Peaking | 8866 Hz  | 4.43 | -5.6 dB  |
| Peaking | 17053 Hz | 4.46 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB   |
| Peaking | 62 Hz    | 1.41 | 2.8 dB   |
| Peaking | 125 Hz   | 1.41 | -1.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 16000 Hz | 1.41 | -28.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ocharaku%20Donguri%20Keyaki/Ocharaku%20Donguri%20Keyaki.png)