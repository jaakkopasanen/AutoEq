# Custom Art FIBAE 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.7; 25 -4.9; 28 -5.0; 31 -5.1; 34 -5.2; 37 -5.3; 41 -5.4; 45 -5.5; 49 -5.6; 54 -5.8; 60 -6.0; 66 -6.2; 72 -6.5; 79 -6.8; 87 -7.2; 96 -7.6; 106 -7.9; 116 -8.2; 128 -8.5; 141 -8.8; 155 -9.0; 170 -9.2; 187 -9.2; 206 -9.3; 227 -9.3; 249 -9.2; 274 -9.2; 302 -9.0; 332 -8.8; 365 -8.5; 402 -8.3; 442 -8.1; 486 -7.8; 535 -7.5; 588 -7.1; 647 -6.8; 712 -6.3; 783 -5.9; 861 -5.5; 947 -5.4; 1042 -5.7; 1146 -6.3; 1261 -6.7; 1387 -6.9; 1526 -6.7; 1678 -6.5; 1846 -6.6; 2031 -6.9; 2234 -7.7; 2457 -8.6; 2703 -7.6; 2973 -4.9; 3270 -2.9; 3597 -2.7; 3957 -4.7; 4353 -9.4; 4788 -7.5; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.9; 15026 -18.5; 16529 -17.3; 18182 -10.4; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art FIBAE 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art FIBAE 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.4  | 1.8 dB   |
| Peaking | 202 Hz   | 0.69 | -3.1 dB  |
| Peaking | 5979 Hz  | 3.53 | 7.2 dB   |
| Peaking | 12921 Hz | 1.84 | 6.7 dB   |
| Peaking | 15481 Hz | 1.39 | -15.6 dB |
| Peaking | 893 Hz   | 3.44 | 1.5 dB   |
| Peaking | 2527 Hz  | 3.42 | -3.5 dB  |
| Peaking | 3482 Hz  | 2.44 | 5.3 dB   |
| Peaking | 4487 Hz  | 4.93 | -6.8 dB  |
| Peaking | 5217 Hz  | 9.75 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB   |
| Peaking | 62 Hz    | 1.41 | 0.5 dB   |
| Peaking | 125 Hz   | 1.41 | -1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -12.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Custom%20Art%20FIBAE%201/Custom%20Art%20FIBAE%201.png)