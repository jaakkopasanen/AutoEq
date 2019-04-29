# Ultimate Ears UE7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.0; 25 -5.2; 28 -5.5; 31 -5.8; 34 -5.9; 37 -6.1; 41 -6.4; 45 -6.6; 49 -6.7; 54 -7.0; 60 -7.3; 66 -7.6; 72 -7.9; 79 -8.3; 87 -8.7; 96 -9.2; 106 -9.6; 116 -10.0; 128 -10.3; 141 -10.6; 155 -10.9; 170 -11.0; 187 -11.2; 206 -11.2; 227 -11.2; 249 -11.2; 274 -11.1; 302 -10.9; 332 -10.7; 365 -10.3; 402 -10.1; 442 -9.9; 486 -9.5; 535 -9.1; 588 -8.7; 647 -8.3; 712 -7.8; 783 -7.2; 861 -6.7; 947 -6.5; 1042 -6.5; 1146 -6.8; 1261 -6.9; 1387 -6.6; 1526 -5.7; 1678 -4.8; 1846 -4.0; 2031 -3.3; 2234 -2.6; 2457 -1.2; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -3.1; 5267 -3.3; 5793 -1.7; 6373 -2.2; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.4; 15026 -19.5; 16529 -13.9; 18182 -7.3; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 0.26 | 2.1 dB   |
| Peaking | 219 Hz   | 0.45 | -4.9 dB  |
| Peaking | 3239 Hz  | 1.03 | 6.7 dB   |
| Peaking | 6129 Hz  | 5.28 | 3.4 dB   |
| Peaking | 15254 Hz | 2.64 | -14.3 dB |
| Peaking | 904 Hz   | 3.36 | 0.8 dB   |
| Peaking | 1321 Hz  | 3.37 | -1.1 dB  |
| Peaking | 2139 Hz  | 2.14 | 0.4 dB   |
| Peaking | 9157 Hz  | 6.33 | -1.8 dB  |
| Peaking | 12575 Hz | 5.18 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB   |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -10.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ultimate%20Ears%20UE7/Ultimate%20Ears%20UE7.png)