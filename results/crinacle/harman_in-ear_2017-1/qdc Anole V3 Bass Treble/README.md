# qdc Anole V3 Bass Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -11.0; 25 -11.1; 28 -11.3; 31 -11.4; 34 -11.5; 37 -11.6; 41 -11.7; 45 -11.8; 49 -11.9; 54 -12.0; 60 -12.1; 66 -12.3; 72 -12.5; 79 -12.8; 87 -13.0; 96 -13.3; 106 -13.5; 116 -13.6; 128 -13.8; 141 -13.8; 155 -13.9; 170 -13.8; 187 -13.7; 206 -13.5; 227 -13.2; 249 -12.9; 274 -12.6; 302 -12.1; 332 -11.6; 365 -10.9; 402 -10.4; 442 -9.9; 486 -9.2; 535 -8.5; 588 -7.7; 647 -6.9; 712 -6.0; 783 -5.1; 861 -4.3; 947 -3.7; 1042 -3.5; 1146 -3.4; 1261 -3.3; 1387 -2.8; 1526 -1.9; 1678 -0.9; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.8; 4788 -0.5; 5267 -1.3; 5793 -4.3; 6373 -7.0; 7010 -7.3; 7711 -8.5; 8482 -9.6; 9330 -8.6; 10263 -6.7; 11289 -6.5; 12418 -6.7; 13660 -14.5; 15026 -22.7; 16529 -22.4; 18182 -19.4; 20000 -22.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V3 Bass Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V3 Bass Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.66 | -3.0 dB  |
| Peaking | 77 Hz    | 0.43 | -3.3 dB  |
| Peaking | 220 Hz   | 0.47 | -5.7 dB  |
| Peaking | 2677 Hz  | 0.39 | 6.9 dB   |
| Peaking | 17698 Hz | 0.55 | -16.4 dB |
| Peaking | 4989 Hz  | 2.93 | 3.5 dB   |
| Peaking | 7690 Hz  | 1.09 | -5.3 dB  |
| Peaking | 11968 Hz | 1.23 | 8.4 dB   |
| Peaking | 15096 Hz | 2.62 | -9.2 dB  |
| Peaking | 21716 Hz | 4.82 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB  |
| Peaking | 250 Hz   | 1.41 | -5.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -19.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20V3%20Bass%20Treble/qdc%20Anole%20V3%20Bass%20Treble.png)