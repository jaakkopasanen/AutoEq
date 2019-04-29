# 64 Audio N8 modded
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.1; 25 -10.9; 28 -10.7; 31 -10.4; 34 -10.1; 37 -9.8; 41 -9.5; 45 -9.2; 49 -9.0; 54 -8.8; 60 -8.5; 66 -8.4; 72 -8.4; 79 -8.4; 87 -8.4; 96 -8.5; 106 -8.6; 116 -8.8; 128 -8.9; 141 -9.1; 155 -9.1; 170 -9.3; 187 -9.4; 206 -9.5; 227 -9.6; 249 -9.6; 274 -9.7; 302 -9.7; 332 -9.5; 365 -9.4; 402 -9.3; 442 -9.2; 486 -9.0; 535 -8.7; 588 -8.5; 647 -8.1; 712 -7.8; 783 -7.4; 861 -7.0; 947 -7.0; 1042 -7.3; 1146 -7.9; 1261 -8.6; 1387 -9.1; 1526 -9.2; 1678 -9.1; 1846 -8.7; 2031 -7.9; 2234 -6.6; 2457 -5.0; 2703 -3.4; 2973 -2.1; 3270 -1.4; 3597 -1.5; 3957 -2.1; 4353 -2.9; 4788 -3.8; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -8.2; 10263 -8.0; 11289 -6.5; 12418 -8.2; 13660 -17.2; 15026 -25.0; 16529 -29.5; 18182 -31.8; 20000 -25.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 modded GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 modded ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.87 | -4.4 dB  |
| Peaking | 471 Hz   | 0.15 | -2.9 dB  |
| Peaking | 5753 Hz  | 0.57 | 14.4 dB  |
| Peaking | 11931 Hz | 2.08 | 12.7 dB  |
| Peaking | 17545 Hz | 0.26 | -27.6 dB |
| Peaking | 938 Hz   | 0.9  | 6.7 dB   |
| Peaking | 1471 Hz  | 0.45 | -6.7 dB  |
| Peaking | 3025 Hz  | 1.41 | 5.9 dB   |
| Peaking | 4781 Hz  | 4.29 | -3.3 dB  |
| Peaking | 5804 Hz  | 3.43 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 16000 Hz | 1.41 | -30.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20modded/64%20Audio%20N8%20modded.png)