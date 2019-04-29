# 64 Audio N8 M15 custom sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.7; 25 -8.9; 28 -9.2; 31 -9.3; 34 -9.5; 37 -9.6; 41 -9.8; 45 -9.9; 49 -10.0; 54 -10.1; 60 -10.4; 66 -10.7; 72 -10.9; 79 -11.2; 87 -11.6; 96 -11.8; 106 -11.8; 116 -12.1; 128 -12.3; 141 -12.3; 155 -12.3; 170 -12.4; 187 -12.3; 206 -12.1; 227 -11.9; 249 -11.8; 274 -11.5; 302 -11.1; 332 -10.6; 365 -10.2; 402 -9.8; 442 -9.4; 486 -9.0; 535 -8.5; 588 -8.0; 647 -7.6; 712 -7.0; 783 -6.5; 861 -6.1; 947 -6.0; 1042 -6.2; 1146 -6.9; 1261 -7.5; 1387 -7.9; 1526 -7.9; 1678 -7.6; 1846 -7.2; 2031 -6.4; 2234 -5.2; 2457 -3.7; 2703 -2.3; 2973 -1.1; 3270 -0.5; 3597 -0.6; 3957 -1.4; 4353 -2.3; 4788 -3.3; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.4; 15026 -25.1; 16529 -32.1; 18182 -31.6; 20000 -17.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 custom sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 custom sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 0.3  | -2.3 dB  |
| Peaking | 190 Hz   | 0.47 | -4.8 dB  |
| Peaking | 5520 Hz  | 0.63 | 12.1 dB  |
| Peaking | 12412 Hz | 1.46 | 15.8 dB  |
| Peaking | 16792 Hz | 0.45 | -31.8 dB |
| Peaking | 923 Hz   | 1.64 | 2.5 dB   |
| Peaking | 1812 Hz  | 0.83 | -4.7 dB  |
| Peaking | 2986 Hz  | 1.03 | 4.9 dB   |
| Peaking | 4600 Hz  | 4.22 | -3.9 dB  |
| Peaking | 18417 Hz | 4.97 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 16000 Hz | 1.41 | -28.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M15%20custom%20sample%202/64%20Audio%20N8%20M15%20custom%20sample%202.png)