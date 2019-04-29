# Taobao 3 driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.0; 37 -1.5; 41 -2.0; 45 -2.5; 49 -2.8; 54 -3.1; 60 -3.5; 66 -4.0; 72 -4.5; 79 -5.0; 87 -5.5; 96 -6.1; 106 -6.7; 116 -7.1; 128 -7.5; 141 -8.0; 155 -8.3; 170 -8.6; 187 -8.8; 206 -8.9; 227 -9.0; 249 -9.1; 274 -9.1; 302 -9.1; 332 -8.9; 365 -8.7; 402 -8.6; 442 -8.5; 486 -8.3; 535 -8.2; 588 -7.9; 647 -7.7; 712 -7.4; 783 -7.0; 861 -6.8; 947 -6.9; 1042 -7.2; 1146 -7.7; 1261 -8.1; 1387 -7.9; 1526 -7.3; 1678 -6.5; 1846 -6.0; 2031 -5.8; 2234 -5.0; 2457 -3.3; 2703 -1.7; 2973 -1.1; 3270 -1.7; 3597 -3.7; 3957 -5.5; 4353 -6.5; 4788 -7.4; 5267 -7.9; 5793 -5.8; 6373 -2.3; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.1; 16529 -10.3; 18182 -6.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Taobao 3 driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Taobao 3 driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.36 | 6.2 dB  |
| Peaking | 216 Hz   | 0.54 | -3.0 dB |
| Peaking | 2929 Hz  | 2.5  | 6.8 dB  |
| Peaking | 6537 Hz  | 5.98 | 5.1 dB  |
| Peaking | 8214 Hz  | 0.08 | -0.9 dB |
| Peaking | 875 Hz   | 3.37 | 0.8 dB  |
| Peaking | 1295 Hz  | 4.78 | -1.2 dB |
| Peaking | 5111 Hz  | 5.28 | -1.9 dB |
| Peaking | 15967 Hz | 0.48 | 1.8 dB  |
| Peaking | 16422 Hz | 2.52 | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Taobao%203%20driver/Taobao%203%20driver.png)