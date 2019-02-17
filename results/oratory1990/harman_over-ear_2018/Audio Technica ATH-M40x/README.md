# Audio Technica ATH-M40x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.3; 49 -2.5; 54 -3.7; 60 -4.2; 66 -4.0; 72 -4.5; 79 -6.0; 87 -6.9; 96 -6.9; 106 -8.4; 116 -9.4; 128 -10.2; 141 -10.4; 155 -10.4; 170 -10.7; 187 -10.9; 206 -10.7; 227 -10.5; 249 -10.0; 274 -9.2; 302 -8.2; 332 -7.1; 365 -6.3; 402 -6.9; 442 -6.9; 486 -6.8; 535 -6.8; 588 -6.7; 647 -6.7; 712 -6.7; 783 -6.7; 861 -6.8; 947 -6.7; 1042 -6.7; 1146 -7.4; 1261 -7.8; 1387 -8.1; 1526 -7.8; 1678 -7.8; 1846 -7.4; 2031 -7.0; 2234 -6.9; 2457 -7.3; 2703 -7.6; 2973 -7.6; 3270 -7.4; 3597 -7.2; 3957 -7.5; 4353 -9.2; 4788 -7.9; 5267 -7.8; 5793 -7.9; 6373 -8.9; 7010 -10.2; 7711 -11.7; 8482 -11.4; 9330 -9.4; 10263 -7.4; 11289 -7.2; 12418 -10.7; 13660 -14.6; 15026 -14.5; 16529 -12.4; 18182 -12.7; 20000 -19.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M40x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M40x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.61 | 6.6 dB  |
| Peaking | 162 Hz   | 0.99 | -5.3 dB |
| Peaking | 1417 Hz  | 3.25 | -1.4 dB |
| Peaking | 13047 Hz | 0.29 | -3.3 dB |
| Peaking | 20620 Hz | 0.34 | -9.5 dB |
| Peaking | 360 Hz   | 6.79 | 1.5 dB  |
| Peaking | 8217 Hz  | 2.34 | -5.5 dB |
| Peaking | 11161 Hz | 0.94 | 6.3 dB  |
| Peaking | 13747 Hz | 2.12 | -7.4 dB |
| Peaking | 20431 Hz | 5.04 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -9.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M40x/Audio%20Technica%20ATH-M40x.png)