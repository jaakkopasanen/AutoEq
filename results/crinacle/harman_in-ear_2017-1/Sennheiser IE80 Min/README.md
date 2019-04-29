# Sennheiser IE80 Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.3; 25 -3.0; 28 -3.8; 31 -4.5; 34 -5.1; 37 -5.7; 41 -6.3; 45 -6.8; 49 -7.3; 54 -7.7; 60 -8.2; 66 -8.7; 72 -9.2; 79 -9.6; 87 -10.1; 96 -10.5; 106 -10.9; 116 -11.1; 128 -11.3; 141 -11.5; 155 -11.6; 170 -11.5; 187 -11.5; 206 -11.3; 227 -11.1; 249 -10.9; 274 -10.7; 302 -10.3; 332 -9.9; 365 -9.5; 402 -9.3; 442 -9.1; 486 -8.8; 535 -8.5; 588 -8.2; 647 -7.9; 712 -7.5; 783 -7.1; 861 -6.8; 947 -6.5; 1042 -6.3; 1146 -6.5; 1261 -6.6; 1387 -6.2; 1526 -5.4; 1678 -4.4; 1846 -3.3; 2031 -2.0; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.9; 3957 -2.1; 4353 -4.1; 4788 -7.3; 5267 -10.7; 5793 -7.5; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.8; 15026 -25.3; 16529 -26.9; 18182 -24.3; 20000 -19.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80 Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80 Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.66 | 7.1 dB   |
| Peaking | 158 Hz   | 0.42 | -5.2 dB  |
| Peaking | 2814 Hz  | 1.04 | 9.2 dB   |
| Peaking | 11707 Hz | 0.51 | 23.3 dB  |
| Peaking | 15862 Hz | 0.38 | -35.8 dB |
| Peaking | 1342 Hz  | 6.6  | -0.8 dB  |
| Peaking | 3963 Hz  | 3.99 | 1.9 dB   |
| Peaking | 5310 Hz  | 4.51 | -6.2 dB  |
| Peaking | 6486 Hz  | 5.06 | 6.2 dB   |
| Peaking | 10435 Hz | 5.35 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB   |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 16000 Hz | 1.41 | -24.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sennheiser%20IE80%20Min/Sennheiser%20IE80%20Min.png)