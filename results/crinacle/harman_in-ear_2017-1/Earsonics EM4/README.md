# Earsonics EM4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.9; 25 -10.0; 28 -10.2; 31 -10.4; 34 -10.5; 37 -10.6; 41 -10.8; 45 -10.8; 49 -10.9; 54 -11.0; 60 -11.1; 66 -11.3; 72 -11.5; 79 -11.7; 87 -12.0; 96 -12.2; 106 -12.4; 116 -12.6; 128 -12.7; 141 -12.9; 155 -13.0; 170 -13.0; 187 -13.0; 206 -12.8; 227 -12.7; 249 -12.5; 274 -12.3; 302 -12.0; 332 -11.6; 365 -11.2; 402 -10.9; 442 -10.5; 486 -10.1; 535 -9.7; 588 -9.2; 647 -8.8; 712 -8.3; 783 -7.8; 861 -7.6; 947 -7.6; 1042 -7.9; 1146 -8.6; 1261 -9.3; 1387 -9.7; 1526 -9.5; 1678 -9.2; 1846 -8.7; 2031 -7.5; 2234 -6.0; 2457 -4.3; 2703 -2.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -2.3; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.5; 15026 -23.9; 16529 -35.0; 18182 -33.2; 20000 -19.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics EM4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics EM4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 56 Hz    | 0.25 | -4.0 dB  |
| Peaking | 215 Hz   | 0.62 | -4.1 dB  |
| Peaking | 4500 Hz  | 0.58 | 16.1 dB  |
| Peaking | 12862 Hz | 0.59 | 28.4 dB  |
| Peaking | 16544 Hz | 0.3  | -48.0 dB |
| Peaking | 1714 Hz  | 2.62 | -2.4 dB  |
| Peaking | 2952 Hz  | 3.02 | 3.3 dB   |
| Peaking | 4021 Hz  | 3.95 | -2.4 dB  |
| Peaking | 6218 Hz  | 7.3  | 2.2 dB   |
| Peaking | 17976 Hz | 4.97 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 16000 Hz | 1.41 | -29.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Earsonics%20EM4/Earsonics%20EM4.png)