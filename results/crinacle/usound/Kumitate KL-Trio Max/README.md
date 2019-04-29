# Kumitate KL-Trio Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -5.7; 25 -5.6; 28 -5.6; 31 -5.7; 34 -5.7; 37 -5.8; 41 -5.9; 45 -6.0; 49 -6.0; 54 -6.0; 60 -6.1; 66 -6.2; 72 -6.4; 79 -6.5; 87 -6.7; 96 -7.0; 106 -7.0; 116 -6.9; 128 -6.9; 141 -6.8; 155 -6.7; 170 -6.4; 187 -6.1; 206 -5.7; 227 -5.3; 249 -4.9; 274 -4.3; 302 -3.9; 332 -3.3; 365 -2.8; 402 -2.2; 442 -1.7; 486 -1.2; 535 -0.7; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -1.4; 1261 -3.9; 1387 -7.5; 1526 -10.4; 1678 -10.7; 1846 -9.8; 2031 -9.6; 2234 -10.8; 2457 -12.9; 2703 -12.7; 2973 -10.1; 3270 -7.9; 3597 -6.9; 3957 -6.4; 4353 -6.1; 4788 -5.9; 5267 -6.3; 5793 -7.4; 6373 -9.4; 7010 -14.8; 7711 -21.2; 8482 -21.1; 9330 -18.2; 10263 -15.6; 11289 -12.2; 12418 -9.7; 13660 -8.1; 15026 -8.3; 16529 -13.4; 18182 -20.3; 20000 -25.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Trio Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Trio Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 2.24 | 1.0 dB   |
| Peaking | 1600 Hz  | 3.63 | -8.1 dB  |
| Peaking | 2614 Hz  | 1.64 | -13.4 dB |
| Peaking | 4687 Hz  | 0.21 | 27.4 dB  |
| Peaking | 8151 Hz  | 0.41 | -36.6 dB |
| Peaking | 164 Hz   | 0.87 | -1.7 dB  |
| Peaking | 709 Hz   | 1.03 | 1.6 dB   |
| Peaking | 6283 Hz  | 8    | 2.7 dB   |
| Peaking | 14614 Hz | 1.04 | 12.1 dB  |
| Peaking | 19779 Hz | 0.33 | -16.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | 0.2 dB   |
| Peaking | 125 Hz   | 1.41 | -1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.8 dB   |
| Peaking | 500 Hz   | 1.41 | 5.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -12.9 dB |
| Peaking | 16000 Hz | 1.41 | -6.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Trio%20Max/Kumitate%20KL-Trio%20Max.png)