# Taobao 6 driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.2; 28 -7.6; 31 -7.9; 34 -8.1; 37 -8.4; 41 -8.6; 45 -8.9; 49 -9.1; 54 -9.3; 60 -9.6; 66 -10.0; 72 -10.4; 79 -10.7; 87 -11.1; 96 -11.5; 106 -11.9; 116 -12.2; 128 -12.5; 141 -12.8; 155 -12.9; 170 -13.0; 187 -13.0; 206 -12.9; 227 -12.7; 249 -12.5; 274 -12.2; 302 -11.8; 332 -11.2; 365 -10.5; 402 -9.8; 442 -9.1; 486 -8.3; 535 -7.4; 588 -6.5; 647 -5.6; 712 -4.8; 783 -4.2; 861 -4.0; 947 -4.2; 1042 -4.7; 1146 -5.4; 1261 -6.0; 1387 -5.9; 1526 -5.4; 1678 -4.6; 1846 -3.8; 2031 -3.0; 2234 -2.3; 2457 -1.9; 2703 -1.7; 2973 -1.3; 3270 -0.8; 3597 -0.5; 3957 -0.6; 4353 -0.6; 4788 -0.5; 5267 -1.4; 5793 -3.6; 6373 -3.7; 7010 -5.8; 7711 -7.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.1; 15026 -22.2; 16529 -26.0; 18182 -24.9; 20000 -19.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Taobao 6 driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Taobao 6 driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 63 Hz    | 0.41 | -0.4 dB  |
| Peaking | 186 Hz   | 0.41 | -6.4 dB  |
| Peaking | 723 Hz   | 1.96 | 3.3 dB   |
| Peaking | 9733 Hz  | 0.22 | 12.9 dB  |
| Peaking | 17035 Hz | 0.44 | -29.9 dB |
| Peaking | 1431 Hz  | 3.38 | -1.9 dB  |
| Peaking | 4173 Hz  | 1.11 | 1.6 dB   |
| Peaking | 7512 Hz  | 2.21 | -3.9 dB  |
| Peaking | 12646 Hz | 2.42 | 6.3 dB   |
| Peaking | 14676 Hz | 2.93 | -5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -5.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -22.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Taobao%206%20driver/Taobao%206%20driver.png)