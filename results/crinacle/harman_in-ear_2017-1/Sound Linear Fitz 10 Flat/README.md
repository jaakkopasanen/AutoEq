# Sound Linear Fitz 10 Flat
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -3.0; 25 -3.4; 28 -3.9; 31 -4.4; 34 -4.9; 37 -5.2; 41 -5.7; 45 -6.1; 49 -6.4; 54 -6.9; 60 -7.4; 66 -7.9; 72 -8.4; 79 -8.9; 87 -9.5; 96 -10.0; 106 -10.6; 116 -10.9; 128 -11.4; 141 -11.7; 155 -12.0; 170 -12.2; 187 -12.4; 206 -12.4; 227 -12.4; 249 -12.4; 274 -12.3; 302 -12.1; 332 -11.8; 365 -11.5; 402 -11.2; 442 -10.9; 486 -10.5; 535 -10.2; 588 -9.7; 647 -9.3; 712 -8.8; 783 -8.2; 861 -7.9; 947 -7.8; 1042 -8.0; 1146 -8.6; 1261 -9.0; 1387 -9.0; 1526 -8.6; 1678 -7.6; 1846 -6.2; 2031 -4.4; 2234 -2.4; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -1.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -3.0; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.6; 15026 -17.7; 16529 -21.7; 18182 -22.7; 20000 -20.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sound Linear Fitz 10 Flat GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sound Linear Fitz 10 Flat ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.27 | 4.7 dB   |
| Peaking | 204 Hz   | 0.24 | -6.0 dB  |
| Peaking | 4580 Hz  | 0.66 | 9.1 dB   |
| Peaking | 12369 Hz | 1.46 | 10.2 dB  |
| Peaking | 17674 Hz | 0.32 | -18.2 dB |
| Peaking | 921 Hz   | 1.12 | 3.7 dB   |
| Peaking | 1435 Hz  | 0.85 | -5.1 dB  |
| Peaking | 2439 Hz  | 1.83 | 4.4 dB   |
| Peaking | 3923 Hz  | 5.4  | -1.8 dB  |
| Peaking | 5780 Hz  | 8.29 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB   |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -17.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sound%20Linear%20Fitz%2010%20Flat/Sound%20Linear%20Fitz%2010%20Flat.png)