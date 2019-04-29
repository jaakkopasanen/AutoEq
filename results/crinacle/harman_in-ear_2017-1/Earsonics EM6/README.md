# Earsonics EM6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.0; 25 -8.2; 28 -8.4; 31 -8.6; 34 -8.8; 37 -8.9; 41 -9.0; 45 -9.0; 49 -9.1; 54 -9.2; 60 -9.3; 66 -9.5; 72 -9.7; 79 -9.9; 87 -10.2; 96 -10.6; 106 -10.8; 116 -11.1; 128 -11.3; 141 -11.4; 155 -11.6; 170 -11.7; 187 -11.7; 206 -11.7; 227 -11.7; 249 -11.6; 274 -11.5; 302 -11.2; 332 -10.9; 365 -10.6; 402 -10.3; 442 -10.0; 486 -9.7; 535 -9.3; 588 -8.9; 647 -8.6; 712 -8.2; 783 -7.7; 861 -7.5; 947 -7.5; 1042 -7.9; 1146 -8.6; 1261 -9.3; 1387 -9.6; 1526 -9.5; 1678 -9.1; 1846 -8.4; 2031 -7.0; 2234 -5.3; 2457 -3.5; 2703 -1.9; 2973 -0.8; 3270 -0.5; 3597 -0.8; 3957 -0.9; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.8; 15026 -26.2; 16529 -34.4; 18182 -31.9; 20000 -20.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics EM6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics EM6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 0.17 | -1.5 dB  |
| Peaking | 286 Hz   | 0.32 | -4.8 dB  |
| Peaking | 1575 Hz  | 1.3  | -8.2 dB  |
| Peaking | 8326 Hz  | 0.18 | 19.8 dB  |
| Peaking | 16998 Hz | 0.47 | -43.4 dB |
| Peaking | 362 Hz   | 2.83 | 0.1 dB   |
| Peaking | 6439 Hz  | 1.91 | 2.5 dB   |
| Peaking | 7721 Hz  | 2.26 | -5.2 dB  |
| Peaking | 13048 Hz | 2.44 | 9.2 dB   |
| Peaking | 15195 Hz | 2.8  | -8.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 16000 Hz | 1.41 | -29.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Earsonics%20EM6/Earsonics%20EM6.png)