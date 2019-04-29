# Dunu DK-4001
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.4; 25 -6.6; 28 -6.9; 31 -7.0; 34 -7.2; 37 -7.3; 41 -7.5; 45 -7.6; 49 -7.6; 54 -7.7; 60 -7.9; 66 -8.0; 72 -8.2; 79 -8.4; 87 -8.5; 96 -8.7; 106 -8.9; 116 -9.0; 128 -9.1; 141 -9.1; 155 -9.2; 170 -9.3; 187 -9.3; 206 -9.2; 227 -9.0; 249 -8.9; 274 -8.8; 302 -8.6; 332 -8.4; 365 -8.2; 402 -8.1; 442 -8.0; 486 -8.0; 535 -7.9; 588 -7.8; 647 -7.8; 712 -7.8; 783 -7.7; 861 -7.8; 947 -8.1; 1042 -8.4; 1146 -9.2; 1261 -9.9; 1387 -10.1; 1526 -10.0; 1678 -9.6; 1846 -8.6; 2031 -6.9; 2234 -4.7; 2457 -2.5; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.4; 5267 -4.1; 5793 -6.5; 6373 -6.9; 7010 -7.3; 7711 -7.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -11.8; 16529 -23.0; 18182 -28.1; 20000 -18.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DK-4001 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DK-4001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 114 Hz   | 0.41 | -0.6 dB  |
| Peaking | 176 Hz   | 0.45 | -2.2 dB  |
| Peaking | 1605 Hz  | 1.21 | -6.3 dB  |
| Peaking | 3119 Hz  | 0.96 | 8.4 dB   |
| Peaking | 18320 Hz | 1.32 | -24.5 dB |
| Peaking | 16 Hz    | 1.78 | 0.9 dB   |
| Peaking | 3391 Hz  | 5.17 | -0.9 dB  |
| Peaking | 4641 Hz  | 3.25 | 2.7 dB   |
| Peaking | 6003 Hz  | 2.51 | -2.9 dB  |
| Peaking | 13202 Hz | 2.63 | 5.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -15.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dunu%20DK-4001/Dunu%20DK-4001.png)