# 64 Audio A6t M20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.2; 25 -10.5; 28 -11.0; 31 -11.2; 34 -11.4; 37 -11.6; 41 -11.7; 45 -11.8; 49 -11.9; 54 -11.9; 60 -11.9; 66 -12.0; 72 -12.0; 79 -12.0; 87 -12.1; 96 -12.1; 106 -12.1; 116 -12.0; 128 -12.0; 141 -11.9; 155 -11.6; 170 -11.5; 187 -11.2; 206 -11.1; 227 -10.8; 249 -10.5; 274 -10.4; 302 -10.2; 332 -9.9; 365 -9.7; 402 -9.5; 442 -9.4; 486 -9.3; 535 -9.1; 588 -8.8; 647 -8.4; 712 -7.9; 783 -7.2; 861 -6.6; 947 -6.2; 1042 -6.1; 1146 -6.3; 1261 -6.5; 1387 -6.3; 1526 -5.9; 1678 -5.4; 1846 -5.2; 2031 -4.8; 2234 -4.3; 2457 -3.4; 2703 -2.6; 2973 -1.6; 3270 -0.6; 3597 -0.5; 3957 -0.8; 4353 -1.9; 4788 -2.6; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.9; 15026 -24.4; 16529 -31.5; 18182 -33.5; 20000 -24.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A6t M20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A6t M20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 68 Hz    | 0.23 | -3.8 dB  |
| Peaking | 239 Hz   | 0.09 | -2.0 dB  |
| Peaking | 5448 Hz  | 0.44 | 15.0 dB  |
| Peaking | 12364 Hz | 1.53 | 14.9 dB  |
| Peaking | 17109 Hz | 0.29 | -31.9 dB |
| Peaking | 937 Hz   | 3.59 | 1.3 dB   |
| Peaking | 3492 Hz  | 1.59 | 5.5 dB   |
| Peaking | 4860 Hz  | 0.68 | -5.6 dB  |
| Peaking | 6036 Hz  | 2.89 | 5.5 dB   |
| Peaking | 9816 Hz  | 2.18 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 16000 Hz | 1.41 | -29.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20A6t%20M20/64%20Audio%20A6t%20M20.png)