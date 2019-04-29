# 64 Audio N8 custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -4.0; 25 -4.4; 28 -5.0; 31 -5.4; 34 -5.8; 37 -6.1; 41 -6.4; 45 -6.8; 49 -7.0; 54 -7.3; 60 -7.7; 66 -8.0; 72 -8.3; 79 -8.7; 87 -9.2; 96 -9.5; 106 -9.7; 116 -10.1; 128 -10.3; 141 -10.5; 155 -10.7; 170 -10.8; 187 -10.9; 206 -10.9; 227 -10.9; 249 -10.8; 274 -10.7; 302 -10.5; 332 -10.2; 365 -10.0; 402 -9.7; 442 -9.5; 486 -9.2; 535 -8.8; 588 -8.4; 647 -8.1; 712 -7.6; 783 -7.1; 861 -6.7; 947 -6.6; 1042 -6.8; 1146 -7.4; 1261 -8.1; 1387 -8.5; 1526 -8.5; 1678 -8.2; 1846 -7.7; 2031 -6.8; 2234 -5.5; 2457 -4.0; 2703 -2.6; 2973 -1.5; 3270 -0.8; 3597 -0.9; 3957 -1.6; 4353 -2.3; 4788 -3.1; 5267 -1.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.3; 15026 -25.9; 16529 -30.2; 18182 -28.8; 20000 -18.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 0.49 | 4.9 dB   |
| Peaking | 202 Hz   | 0.36 | -4.4 dB  |
| Peaking | 5338 Hz  | 0.64 | 13.3 dB  |
| Peaking | 12198 Hz | 1.18 | 17.6 dB  |
| Peaking | 16163 Hz | 0.36 | -31.1 dB |
| Peaking | 952 Hz   | 1.34 | 2.8 dB   |
| Peaking | 1551 Hz  | 0.87 | -3.9 dB  |
| Peaking | 3071 Hz  | 1.57 | 4.2 dB   |
| Peaking | 4854 Hz  | 2.63 | -3.6 dB  |
| Peaking | 5886 Hz  | 4.23 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB   |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 16000 Hz | 1.41 | -27.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20custom/64%20Audio%20N8%20custom.png)