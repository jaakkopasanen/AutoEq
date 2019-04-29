# Ultimate Ears UE11
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.9; 25 -10.1; 28 -10.3; 31 -10.5; 34 -10.6; 37 -10.7; 41 -10.8; 45 -11.0; 49 -11.1; 54 -11.3; 60 -11.5; 66 -11.8; 72 -12.0; 79 -12.2; 87 -12.5; 96 -12.8; 106 -13.0; 116 -13.2; 128 -13.2; 141 -13.3; 155 -13.3; 170 -13.2; 187 -13.0; 206 -12.7; 227 -12.4; 249 -12.1; 274 -11.7; 302 -11.2; 332 -10.6; 365 -10.0; 402 -9.5; 442 -9.0; 486 -8.4; 535 -7.7; 588 -7.1; 647 -6.4; 712 -5.8; 783 -5.1; 861 -4.5; 947 -4.3; 1042 -4.4; 1146 -4.8; 1261 -5.1; 1387 -5.1; 1526 -4.6; 1678 -4.1; 1846 -3.4; 2031 -2.7; 2234 -2.2; 2457 -1.5; 2703 -0.5; 2973 -0.5; 3270 -0.9; 3597 -1.0; 3957 -0.5; 4353 -0.9; 4788 -3.8; 5267 -2.8; 5793 -1.5; 6373 -3.1; 7010 -4.0; 7711 -6.2; 8482 -7.1; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -16.6; 15026 -22.7; 16529 -15.4; 18182 -7.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE11 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 57 Hz    | 0.22 | -3.8 dB  |
| Peaking | 208 Hz   | 0.5  | -4.9 dB  |
| Peaking | 3333 Hz  | 1.09 | 4.2 dB   |
| Peaking | 4466 Hz  | 0.05 | 2.3 dB   |
| Peaking | 15088 Hz | 2.08 | -20.1 dB |
| Peaking | 875 Hz   | 4.79 | 1.2 dB   |
| Peaking | 6013 Hz  | 5.33 | 1.8 dB   |
| Peaking | 8841 Hz  | 3.9  | -2.9 dB  |
| Peaking | 12626 Hz | 3.94 | 5.3 dB   |
| Peaking | 15043 Hz | 3.88 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 16000 Hz | 1.41 | -13.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ultimate%20Ears%20UE11/Ultimate%20Ears%20UE11.png)