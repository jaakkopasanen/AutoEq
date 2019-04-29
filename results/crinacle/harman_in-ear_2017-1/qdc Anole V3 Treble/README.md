# qdc Anole V3 Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.1; 25 -9.2; 28 -9.4; 31 -9.6; 34 -9.7; 37 -9.8; 41 -10.0; 45 -10.1; 49 -10.2; 54 -10.3; 60 -10.5; 66 -10.7; 72 -11.0; 79 -11.3; 87 -11.6; 96 -11.9; 106 -12.2; 116 -12.4; 128 -12.6; 141 -12.7; 155 -12.8; 170 -12.8; 187 -12.7; 206 -12.6; 227 -12.4; 249 -12.2; 274 -11.9; 302 -11.5; 332 -11.1; 365 -10.6; 402 -10.1; 442 -9.6; 486 -9.1; 535 -8.4; 588 -7.7; 647 -7.0; 712 -6.2; 783 -5.4; 861 -4.6; 947 -4.1; 1042 -3.9; 1146 -4.0; 1261 -3.9; 1387 -3.5; 1526 -2.6; 1678 -1.7; 1846 -0.8; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -0.7; 5267 -1.6; 5793 -4.4; 6373 -7.1; 7010 -7.3; 7711 -8.4; 8482 -10.3; 9330 -10.1; 10263 -7.7; 11289 -6.5; 12418 -6.9; 13660 -15.1; 15026 -23.4; 16529 -22.2; 18182 -18.2; 20000 -21.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V3 Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V3 Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.13 | -2.4 dB  |
| Peaking | 213 Hz   | 0.38 | -4.5 dB  |
| Peaking | 8236 Hz  | 1.5  | -12.8 dB |
| Peaking | 9809 Hz  | 0.25 | 27.2 dB  |
| Peaking | 15750 Hz | 0.38 | -36.0 dB |
| Peaking | 4924 Hz  | 1.18 | 1.7 dB   |
| Peaking | 6277 Hz  | 4.99 | -2.9 dB  |
| Peaking | 7698 Hz  | 6.52 | 2.0 dB   |
| Peaking | 12428 Hz | 4.77 | 4.6 dB   |
| Peaking | 20150 Hz | 0.03 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -19.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20V3%20Treble/qdc%20Anole%20V3%20Treble.png)