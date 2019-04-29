# Sennheiser IE800S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.9; 28 -10.1; 31 -10.3; 34 -10.4; 37 -10.5; 41 -10.7; 45 -10.7; 49 -10.8; 54 -10.9; 60 -11.1; 66 -11.3; 72 -11.4; 79 -11.6; 87 -11.8; 96 -12.0; 106 -12.1; 116 -12.2; 128 -12.3; 141 -12.2; 155 -12.2; 170 -12.1; 187 -11.9; 206 -11.7; 227 -11.4; 249 -11.1; 274 -10.8; 302 -10.5; 332 -10.1; 365 -9.6; 402 -9.4; 442 -9.2; 486 -8.9; 535 -8.6; 588 -8.4; 647 -8.2; 712 -7.9; 783 -7.7; 861 -7.6; 947 -7.7; 1042 -8.2; 1146 -8.8; 1261 -9.2; 1387 -8.8; 1526 -8.4; 1678 -7.5; 1846 -6.2; 2031 -4.2; 2234 -1.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -4.3; 5793 -5.9; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -7.5; 11289 -6.5; 12418 -8.6; 13660 -19.7; 15026 -29.8; 16529 -30.6; 18182 -25.4; 20000 -22.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE800S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE800S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 306 Hz   | 0.06 | -5.3 dB  |
| Peaking | 3618 Hz  | 0.39 | 20.4 dB  |
| Peaking | 12034 Hz | 0.67 | 24.2 dB  |
| Peaking | 15115 Hz | 0.32 | -43.4 dB |
| Peaking | 833 Hz   | 0.87 | 3.2 dB   |
| Peaking | 1390 Hz  | 0.87 | -4.3 dB  |
| Peaking | 2346 Hz  | 3.02 | 3.7 dB   |
| Peaking | 5629 Hz  | 8.93 | -4.3 dB  |
| Peaking | 6406 Hz  | 7.23 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 16000 Hz | 1.41 | -30.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sennheiser%20IE800S/Sennheiser%20IE800S.png)