# Shozy & Neo BG sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.2; 25 -5.6; 28 -6.1; 31 -6.4; 34 -6.7; 37 -6.9; 41 -7.2; 45 -7.5; 49 -7.8; 54 -8.1; 60 -8.4; 66 -8.7; 72 -9.0; 79 -9.3; 87 -9.7; 96 -10.1; 106 -10.5; 116 -10.8; 128 -11.0; 141 -11.2; 155 -11.2; 170 -11.4; 187 -11.4; 206 -11.4; 227 -11.2; 249 -11.0; 274 -10.8; 302 -10.5; 332 -10.0; 365 -9.5; 402 -9.1; 442 -8.7; 486 -8.2; 535 -7.7; 588 -7.2; 647 -6.6; 712 -6.1; 783 -5.6; 861 -5.2; 947 -5.2; 1042 -5.6; 1146 -6.3; 1261 -7.0; 1387 -7.5; 1526 -7.7; 1678 -8.1; 1846 -8.6; 2031 -7.7; 2234 -4.6; 2457 -1.2; 2703 -0.5; 2973 -0.5; 3270 -1.7; 3597 -2.2; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.5; 5793 -3.9; 6373 -5.5; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.9; 15026 -16.5; 16529 -24.6; 18182 -24.0; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy & Neo BG sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy & Neo BG sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 210 Hz   | 0.43 | -5.6 dB  |
| Peaking | 1893 Hz  | 1.38 | -10.6 dB |
| Peaking | 2524 Hz  | 1.16 | 7.7 dB   |
| Peaking | 3919 Hz  | 0.11 | 4.0 dB   |
| Peaking | 17365 Hz | 1.12 | -23.2 dB |
| Peaking | 20 Hz    | 1.65 | 2.1 dB   |
| Peaking | 4795 Hz  | 3.26 | 3.6 dB   |
| Peaking | 6835 Hz  | 0.79 | -2.2 dB  |
| Peaking | 13189 Hz | 2.09 | 4.9 dB   |
| Peaking | 15638 Hz | 3.18 | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB   |
| Peaking | 62 Hz    | 1.41 | -1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -17.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shozy%20&%20Neo%20BG%20sample%201/Shozy%20&%20Neo%20BG%20sample%201.png)