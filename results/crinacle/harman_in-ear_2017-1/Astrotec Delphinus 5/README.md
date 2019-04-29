# Astrotec Delphinus 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.7; 25 -4.0; 28 -4.4; 31 -4.7; 34 -4.9; 37 -5.1; 41 -5.4; 45 -5.6; 49 -5.8; 54 -6.1; 60 -6.4; 66 -6.7; 72 -7.2; 79 -7.6; 87 -7.9; 96 -8.4; 106 -8.8; 116 -9.2; 128 -9.5; 141 -9.9; 155 -10.1; 170 -10.3; 187 -10.5; 206 -10.6; 227 -10.6; 249 -10.6; 274 -10.6; 302 -10.6; 332 -10.4; 365 -10.3; 402 -10.3; 442 -10.4; 486 -10.4; 535 -10.4; 588 -10.6; 647 -10.8; 712 -11.2; 783 -11.6; 861 -12.2; 947 -13.0; 1042 -13.4; 1146 -13.0; 1261 -11.6; 1387 -9.6; 1526 -7.6; 1678 -5.9; 1846 -4.5; 2031 -3.6; 2234 -3.4; 2457 -3.9; 2703 -2.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -12.4; 16529 -18.1; 18182 -16.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec Delphinus 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec Delphinus 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.18 | 3.1 dB   |
| Peaking | 226 Hz   | 0.3  | -4.4 dB  |
| Peaking | 1058 Hz  | 1.71 | -6.7 dB  |
| Peaking | 3852 Hz  | 0.68 | 6.9 dB   |
| Peaking | 17249 Hz | 1.47 | -13.9 dB |
| Peaking | 1896 Hz  | 5.98 | 1.3 dB   |
| Peaking | 5859 Hz  | 2.75 | 4.0 dB   |
| Peaking | 6558 Hz  | 6.13 | 2.8 dB   |
| Peaking | 6778 Hz  | 1.44 | -4.1 dB  |
| Peaking | 13316 Hz | 3.75 | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB   |
| Peaking | 62 Hz    | 1.41 | 0.0 dB   |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -7.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -10.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Astrotec%20Delphinus%205/Astrotec%20Delphinus%205.png)