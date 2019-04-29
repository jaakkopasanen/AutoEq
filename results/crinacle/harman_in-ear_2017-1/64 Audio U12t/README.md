# 64 Audio U12t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -8.9; 25 -9.2; 28 -9.4; 31 -9.6; 34 -9.7; 37 -9.7; 41 -9.8; 45 -9.8; 49 -9.8; 54 -9.7; 60 -9.7; 66 -9.7; 72 -9.7; 79 -9.7; 87 -9.7; 96 -9.8; 106 -9.8; 116 -9.7; 128 -9.6; 141 -9.5; 155 -9.4; 170 -9.3; 187 -9.1; 206 -9.0; 227 -8.8; 249 -8.7; 274 -8.6; 302 -8.5; 332 -8.5; 365 -8.5; 402 -8.6; 442 -8.8; 486 -8.9; 535 -8.9; 588 -8.7; 647 -8.5; 712 -8.0; 783 -7.5; 861 -7.0; 947 -6.8; 1042 -7.0; 1146 -7.4; 1261 -7.8; 1387 -8.0; 1526 -7.9; 1678 -7.9; 1846 -8.0; 2031 -8.1; 2234 -7.4; 2457 -5.1; 2703 -2.3; 2973 -0.7; 3270 -0.5; 3597 -1.0; 3957 -2.6; 4353 -3.9; 4788 -5.5; 5267 -2.8; 5793 -2.0; 6373 -3.9; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -17.9; 15026 -30.5; 16529 -38.9; 18182 -38.8; 20000 -19.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio U12t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio U12t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 122 Hz   | 0.07 | -3.1 dB  |
| Peaking | 1790 Hz  | 1.58 | -5.2 dB  |
| Peaking | 4934 Hz  | 0.33 | 15.6 dB  |
| Peaking | 11837 Hz | 1.55 | 15.8 dB  |
| Peaking | 16852 Hz | 0.4  | -41.0 dB |
| Peaking | 2265 Hz  | 5.46 | -2.3 dB  |
| Peaking | 3072 Hz  | 2.57 | 2.7 dB   |
| Peaking | 4800 Hz  | 3.38 | -5.8 dB  |
| Peaking | 5438 Hz  | 2.77 | 3.5 dB   |
| Peaking | 18459 Hz | 4.77 | -4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 10.9 dB  |
| Peaking | 16000 Hz | 1.41 | -38.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20U12t/64%20Audio%20U12t.png)