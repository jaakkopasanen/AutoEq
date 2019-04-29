# Sennheiser IE80 Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -12.0; 25 -12.2; 28 -12.4; 31 -12.5; 34 -12.6; 37 -12.7; 41 -12.9; 45 -13.0; 49 -13.0; 54 -13.1; 60 -13.2; 66 -13.4; 72 -13.5; 79 -13.7; 87 -13.9; 96 -14.0; 106 -14.1; 116 -14.1; 128 -14.1; 141 -14.0; 155 -13.9; 170 -13.7; 187 -13.4; 206 -13.0; 227 -12.6; 249 -12.1; 274 -11.7; 302 -11.1; 332 -10.5; 365 -9.9; 402 -9.4; 442 -8.9; 486 -8.5; 535 -8.0; 588 -7.5; 647 -7.1; 712 -6.6; 783 -6.1; 861 -5.7; 947 -5.3; 1042 -5.2; 1146 -5.5; 1261 -5.5; 1387 -5.2; 1526 -4.5; 1678 -3.6; 1846 -2.6; 2031 -1.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -2.0; 4353 -3.9; 4788 -7.1; 5267 -10.0; 5793 -6.1; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.7; 15026 -24.2; 16529 -25.4; 18182 -23.3; 20000 -22.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80 Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80 Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.31 | -5.2 dB  |
| Peaking | 168 Hz   | 0.53 | -5.5 dB  |
| Peaking | 2794 Hz  | 0.77 | 6.3 dB   |
| Peaking | 17735 Hz | 0.86 | -20.6 dB |
| Peaking | 844 Hz   | 4.61 | 0.7 dB   |
| Peaking | 5236 Hz  | 5.14 | -7.1 dB  |
| Peaking | 6386 Hz  | 5.27 | 5.4 dB   |
| Peaking | 12630 Hz | 1.59 | 8.6 dB   |
| Peaking | 14994 Hz | 2.33 | -11.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -5.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 16000 Hz | 1.41 | -23.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sennheiser%20IE80%20Max/Sennheiser%20IE80%20Max.png)