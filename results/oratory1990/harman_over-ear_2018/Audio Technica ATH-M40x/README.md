# Audio Technica ATH-M40x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.8; 60 -2.2; 66 -2.1; 72 -2.7; 79 -4.3; 87 -5.1; 96 -5.3; 106 -6.6; 116 -7.7; 128 -8.5; 141 -8.6; 155 -8.6; 170 -8.9; 187 -9.1; 206 -9.0; 227 -8.7; 249 -8.2; 274 -7.4; 302 -6.4; 332 -5.2; 365 -4.6; 402 -5.2; 442 -5.2; 486 -5.1; 535 -5.0; 588 -5.0; 647 -5.0; 712 -5.0; 783 -5.0; 861 -5.1; 947 -4.9; 1042 -5.0; 1146 -5.7; 1261 -6.1; 1387 -6.3; 1526 -6.0; 1678 -5.9; 1846 -5.6; 2031 -5.2; 2234 -5.2; 2457 -5.5; 2703 -5.8; 2973 -5.8; 3270 -5.5; 3597 -5.1; 3957 -5.6; 4353 -7.2; 4788 -6.0; 5267 -5.7; 5793 -6.0; 6373 -7.0; 7010 -8.6; 7711 -10.3; 8482 -10.2; 9330 -8.5; 10263 -6.7; 11289 -6.6; 12418 -9.9; 13660 -13.5; 15026 -12.5; 16529 -9.9; 18182 -9.8; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M40x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M40x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.36 | 6.7 dB  |
| Peaking | 162 Hz   | 0.72 | -6.5 dB |
| Peaking | 392 Hz   | 0.38 | 2.8 dB  |
| Peaking | 14223 Hz | 1.83 | -6.8 dB |
| Peaking | 20099 Hz | 1.01 | -8.6 dB |
| Peaking | 240 Hz   | 6.22 | -0.7 dB |
| Peaking | 3208 Hz  | 1.77 | 0.9 dB  |
| Peaking | 5780 Hz  | 3.37 | 1.5 dB  |
| Peaking | 7989 Hz  | 2.45 | -4.0 dB |
| Peaking | 10892 Hz | 3.58 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -6.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M40x/Audio%20Technica%20ATH-M40x.png)