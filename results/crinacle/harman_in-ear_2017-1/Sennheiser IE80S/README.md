# Sennheiser IE80S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.7; 25 -3.3; 28 -4.0; 31 -4.7; 34 -5.2; 37 -5.7; 41 -6.2; 45 -6.6; 49 -7.0; 54 -7.5; 60 -7.9; 66 -8.3; 72 -8.8; 79 -9.2; 87 -9.5; 96 -9.9; 106 -10.2; 116 -10.4; 128 -10.6; 141 -10.7; 155 -10.8; 170 -10.6; 187 -10.5; 206 -10.3; 227 -10.1; 249 -9.8; 274 -9.5; 302 -9.1; 332 -8.6; 365 -8.2; 402 -7.9; 442 -7.5; 486 -7.1; 535 -6.8; 588 -6.4; 647 -6.0; 712 -5.6; 783 -5.2; 861 -4.9; 947 -4.9; 1042 -4.7; 1146 -4.9; 1261 -5.3; 1387 -5.2; 1526 -4.7; 1678 -4.0; 1846 -3.2; 2031 -2.4; 2234 -1.7; 2457 -1.3; 2703 -1.4; 2973 -1.9; 3270 -2.5; 3597 -3.2; 3957 -4.5; 4353 -6.9; 4788 -10.4; 5267 -8.8; 5793 -3.0; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -14.0; 15026 -19.8; 16529 -20.1; 18182 -22.4; 20000 -26.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.27 | 4.2 dB   |
| Peaking | 146 Hz   | 0.57 | -5.0 dB  |
| Peaking | 2490 Hz  | 1.3  | 5.6 dB   |
| Peaking | 10361 Hz | 0.64 | 13.0 dB  |
| Peaking | 18640 Hz | 0.18 | -20.3 dB |
| Peaking | 4960 Hz  | 5.91 | -6.4 dB  |
| Peaking | 6253 Hz  | 5.72 | 6.3 dB   |
| Peaking | 14857 Hz | 5.32 | -4.3 dB  |
| Peaking | 17768 Hz | 2.3  | 1.7 dB   |
| Peaking | 22049 Hz | 1.29 | 0.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB   |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 16000 Hz | 1.41 | -19.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sennheiser%20IE80S/Sennheiser%20IE80S.png)