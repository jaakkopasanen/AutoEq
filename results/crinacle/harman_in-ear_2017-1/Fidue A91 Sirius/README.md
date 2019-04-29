# Fidue A91 Sirius
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.8; 25 -3.1; 28 -3.6; 31 -3.9; 34 -4.2; 37 -4.5; 41 -4.8; 45 -5.1; 49 -5.3; 54 -5.6; 60 -6.0; 66 -6.4; 72 -6.8; 79 -7.2; 87 -7.7; 96 -8.2; 106 -8.6; 116 -9.1; 128 -9.4; 141 -9.8; 155 -10.1; 170 -10.3; 187 -10.5; 206 -10.6; 227 -10.6; 249 -10.5; 274 -10.5; 302 -10.2; 332 -9.7; 365 -9.2; 402 -8.9; 442 -8.6; 486 -8.1; 535 -7.5; 588 -6.9; 647 -6.3; 712 -5.7; 783 -5.2; 861 -4.9; 947 -5.3; 1042 -6.4; 1146 -8.3; 1261 -9.9; 1387 -11.0; 1526 -11.4; 1678 -11.2; 1846 -10.0; 2031 -7.9; 2234 -5.7; 2457 -3.9; 2703 -2.8; 2973 -2.7; 3270 -3.1; 3597 -2.0; 3957 -0.8; 4353 -0.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.1; 15026 -13.7; 16529 -14.6; 18182 -17.7; 20000 -22.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A91 Sirius GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A91 Sirius ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.57 | 4.2 dB   |
| Peaking | 199 Hz   | 0.77 | -4.5 dB  |
| Peaking | 1610 Hz  | 2.54 | -6.7 dB  |
| Peaking | 3281 Hz  | 1.09 | 4.3 dB   |
| Peaking | 5418 Hz  | 2.36 | 5.1 dB   |
| Peaking | 861 Hz   | 2.56 | 2.6 dB   |
| Peaking | 1258 Hz  | 5.31 | -1.9 dB  |
| Peaking | 6400 Hz  | 5.21 | 2.3 dB   |
| Peaking | 12354 Hz | 1.97 | 4.6 dB   |
| Peaking | 20059 Hz | 0.29 | -14.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB   |
| Peaking | 62 Hz    | 1.41 | 0.2 dB   |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -10.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Fidue%20A91%20Sirius/Fidue%20A91%20Sirius.png)