# Sennheiser IE80S Half
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.6; 25 -9.9; 28 -10.2; 31 -10.5; 34 -10.7; 37 -10.9; 41 -11.0; 45 -11.2; 49 -11.3; 54 -11.5; 60 -11.7; 66 -11.8; 72 -12.0; 79 -12.2; 87 -12.3; 96 -12.5; 106 -12.6; 116 -12.6; 128 -12.6; 141 -12.5; 155 -12.4; 170 -12.2; 187 -11.9; 206 -11.5; 227 -11.1; 249 -10.7; 274 -10.2; 302 -9.6; 332 -9.0; 365 -8.4; 402 -7.9; 442 -7.4; 486 -6.9; 535 -6.4; 588 -5.9; 647 -5.5; 712 -5.0; 783 -4.5; 861 -4.2; 947 -4.1; 1042 -3.9; 1146 -4.2; 1261 -4.7; 1387 -4.6; 1526 -4.1; 1678 -3.5; 1846 -2.8; 2031 -2.1; 2234 -1.4; 2457 -1.2; 2703 -1.4; 2973 -1.9; 3270 -2.5; 3597 -3.2; 3957 -4.4; 4353 -6.8; 4788 -10.1; 5267 -7.9; 5793 -2.1; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.1; 13660 -14.1; 15026 -18.7; 16529 -18.6; 18182 -21.2; 20000 -27.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80S Half GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80S Half ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 0.43 | -4.8 dB  |
| Peaking | 136 Hz   | 0.95 | -4.1 dB  |
| Peaking | 252 Hz   | 1.6  | -2.5 dB  |
| Peaking | 2305 Hz  | 1.38 | 5.0 dB   |
| Peaking | 6319 Hz  | 7.78 | 6.0 dB   |
| Peaking | 885 Hz   | 2.36 | 1.9 dB   |
| Peaking | 3440 Hz  | 2.48 | 1.8 dB   |
| Peaking | 4820 Hz  | 7.36 | -5.8 dB  |
| Peaking | 10495 Hz | 0.81 | 8.6 dB   |
| Peaking | 20107 Hz | 0.16 | -19.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 16000 Hz | 1.41 | -18.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sennheiser%20IE80S%20Half/Sennheiser%20IE80S%20Half.png)