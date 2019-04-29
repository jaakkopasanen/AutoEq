# qdc Gemini
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.3; 25 -7.4; 28 -7.5; 31 -7.6; 34 -7.7; 37 -7.8; 41 -7.9; 45 -8.0; 49 -8.0; 54 -8.1; 60 -8.3; 66 -8.4; 72 -8.6; 79 -8.8; 87 -8.9; 96 -9.2; 106 -9.4; 116 -9.4; 128 -9.5; 141 -9.6; 155 -9.5; 170 -9.4; 187 -9.2; 206 -9.0; 227 -8.7; 249 -8.5; 274 -8.2; 302 -7.9; 332 -7.5; 365 -7.2; 402 -7.0; 442 -6.8; 486 -6.7; 535 -6.6; 588 -6.6; 647 -6.7; 712 -6.8; 783 -6.9; 861 -7.1; 947 -7.5; 1042 -8.1; 1146 -8.8; 1261 -9.3; 1387 -9.1; 1526 -8.6; 1678 -7.9; 1846 -7.1; 2031 -6.2; 2234 -5.3; 2457 -4.3; 2703 -3.1; 2973 -2.0; 3270 -2.0; 3597 -2.6; 3957 -3.4; 4353 -5.0; 4788 -3.5; 5267 -0.5; 5793 -0.6; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -16.9; 15026 -25.7; 16529 -27.4; 18182 -27.1; 20000 -27.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Gemini GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Gemini ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 137 Hz   | 0.43 | -3.1 dB  |
| Peaking | 1343 Hz  | 1.19 | -5.6 dB  |
| Peaking | 5805 Hz  | 0.26 | 22.5 dB  |
| Peaking | 12244 Hz | 1.46 | 16.8 dB  |
| Peaking | 15084 Hz | 0.2  | -36.5 dB |
| Peaking | 3036 Hz  | 4.84 | 1.8 dB   |
| Peaking | 4475 Hz  | 4.32 | -4.7 dB  |
| Peaking | 5220 Hz  | 3.22 | 3.4 dB   |
| Peaking | 7676 Hz  | 5.74 | -1.4 dB  |
| Peaking | 19748 Hz | 3.11 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 16000 Hz | 1.41 | -27.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Gemini/qdc%20Gemini.png)