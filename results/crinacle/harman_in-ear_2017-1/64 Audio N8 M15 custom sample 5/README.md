# 64 Audio N8 M15 custom sample 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -12.0; 25 -12.2; 28 -12.3; 31 -12.4; 34 -12.5; 37 -12.5; 41 -12.5; 45 -12.5; 49 -12.5; 54 -12.5; 60 -12.5; 66 -12.5; 72 -12.6; 79 -12.7; 87 -12.8; 96 -12.8; 106 -12.7; 116 -12.8; 128 -12.7; 141 -12.6; 155 -12.4; 170 -12.2; 187 -12.1; 206 -11.8; 227 -11.5; 249 -11.2; 274 -10.9; 302 -10.6; 332 -10.1; 365 -9.8; 402 -9.5; 442 -9.2; 486 -8.8; 535 -8.4; 588 -8.0; 647 -7.6; 712 -7.1; 783 -6.6; 861 -6.2; 947 -6.0; 1042 -6.2; 1146 -6.7; 1261 -7.4; 1387 -7.8; 1526 -7.9; 1678 -7.6; 1846 -7.2; 2031 -6.5; 2234 -5.4; 2457 -4.0; 2703 -2.5; 2973 -1.3; 3270 -0.7; 3597 -0.8; 3957 -1.4; 4353 -1.8; 4788 -2.7; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.3; 13660 -15.6; 15026 -22.6; 16529 -27.0; 18182 -27.6; 20000 -13.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 custom sample 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 custom sample 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.47 | -4.6 dB  |
| Peaking | 139 Hz   | 0.37 | -5.5 dB  |
| Peaking | 5336 Hz  | 0.74 | 8.9 dB   |
| Peaking | 11925 Hz | 1.88 | 10.1 dB  |
| Peaking | 17071 Hz | 0.5  | -23.8 dB |
| Peaking | 941 Hz   | 1.43 | 3.0 dB   |
| Peaking | 1567 Hz  | 0.75 | -3.5 dB  |
| Peaking | 3047 Hz  | 1.82 | 3.7 dB   |
| Peaking | 4831 Hz  | 3.57 | -2.6 dB  |
| Peaking | 5946 Hz  | 4.45 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 16000 Hz | 1.41 | -24.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M15%20custom%20sample%205/64%20Audio%20N8%20M15%20custom%20sample%205.png)