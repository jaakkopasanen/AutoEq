# Audio Technica ATH-M40x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.9; 54 -2.0; 60 -2.5; 66 -2.3; 72 -2.8; 79 -4.2; 87 -5.1; 96 -5.2; 106 -6.6; 116 -7.7; 128 -8.5; 141 -8.6; 155 -8.7; 170 -8.9; 187 -9.1; 206 -9.0; 227 -8.8; 249 -8.2; 274 -7.4; 302 -6.4; 332 -5.3; 365 -4.6; 402 -5.2; 442 -5.1; 486 -5.1; 535 -5.0; 588 -5.0; 647 -5.0; 712 -4.9; 783 -4.9; 861 -5.0; 947 -4.9; 1042 -4.9; 1146 -5.7; 1261 -6.1; 1387 -6.4; 1526 -6.1; 1678 -6.1; 1846 -5.6; 2031 -5.2; 2234 -5.2; 2457 -5.5; 2703 -5.8; 2973 -5.8; 3270 -5.6; 3597 -5.4; 3957 -5.8; 4353 -7.5; 4788 -6.1; 5267 -6.1; 5793 -6.2; 6373 -7.1; 7010 -8.4; 7711 -10.0; 8482 -9.7; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -8.9; 13660 -12.9; 15026 -12.7; 16529 -10.7; 18182 -11.0; 20000 -17.3
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
| Peaking | 33 Hz    | 0.37 | 6.6 dB  |
| Peaking | 165 Hz   | 0.77 | -6.2 dB |
| Peaking | 398 Hz   | 0.35 | 2.6 dB  |
| Peaking | 17436 Hz | 0.41 | -5.1 dB |
| Peaking | 20052 Hz | 2.43 | -6.4 dB |
| Peaking | 2984 Hz  | 1.99 | 0.6 dB  |
| Peaking | 5837 Hz  | 4.47 | 0.8 dB  |
| Peaking | 8051 Hz  | 2.3  | -5.0 dB |
| Peaking | 12158 Hz | 0.8  | 6.0 dB  |
| Peaking | 13777 Hz | 1.96 | -8.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -7.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M40x/Audio%20Technica%20ATH-M40x.png)