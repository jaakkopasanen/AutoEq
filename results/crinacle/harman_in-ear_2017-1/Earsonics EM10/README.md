# Earsonics EM10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.1; 25 -11.0; 28 -11.0; 31 -11.0; 34 -11.0; 37 -11.0; 41 -11.1; 45 -11.1; 49 -11.2; 54 -11.3; 60 -11.4; 66 -11.5; 72 -11.7; 79 -11.8; 87 -12.0; 96 -12.3; 106 -12.4; 116 -12.3; 128 -12.3; 141 -12.2; 155 -12.0; 170 -11.6; 187 -11.2; 206 -10.6; 227 -10.0; 249 -9.3; 274 -8.8; 302 -8.2; 332 -7.8; 365 -7.6; 402 -7.6; 442 -7.7; 486 -7.9; 535 -8.1; 588 -8.2; 647 -8.5; 712 -8.6; 783 -8.8; 861 -9.1; 947 -9.7; 1042 -10.5; 1146 -11.6; 1261 -12.5; 1387 -12.4; 1526 -11.3; 1678 -9.3; 1846 -6.7; 2031 -3.8; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -1.4; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.0; 6373 -3.1; 7010 -6.6; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.1; 15026 -22.4; 16529 -33.2; 18182 -33.7; 20000 -23.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics EM10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics EM10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 80 Hz    | 0.26 | -5.8 dB  |
| Peaking | 1318 Hz  | 0.92 | -15.2 dB |
| Peaking | 3503 Hz  | 0.27 | 17.0 dB  |
| Peaking | 12911 Hz | 1.28 | 17.7 dB  |
| Peaking | 16992 Hz | 0.37 | -36.6 dB |
| Peaking | 19 Hz    | 2.39 | -1.4 dB  |
| Peaking | 2312 Hz  | 7.4  | 2.2 dB   |
| Peaking | 3762 Hz  | 5.28 | -2.2 dB  |
| Peaking | 5390 Hz  | 4.62 | 1.6 dB   |
| Peaking | 7214 Hz  | 8.71 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | -6.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 16000 Hz | 1.41 | -27.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Earsonics%20EM10/Earsonics%20EM10.png)