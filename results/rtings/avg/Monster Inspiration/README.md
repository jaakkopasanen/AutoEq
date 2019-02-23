# Monster Inspiration
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.3; 25 -2.1; 28 -3.4; 31 -4.6; 34 -5.6; 37 -6.4; 41 -7.3; 45 -8.3; 49 -9.1; 54 -9.9; 60 -10.7; 66 -11.4; 72 -12.0; 79 -12.4; 87 -12.9; 96 -13.2; 106 -13.5; 116 -13.6; 128 -13.5; 141 -13.3; 155 -13.0; 170 -12.4; 187 -11.7; 206 -10.8; 227 -9.8; 249 -8.8; 274 -7.6; 302 -6.3; 332 -4.6; 365 -2.7; 402 -1.6; 442 -0.8; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -1.1; 1146 -2.0; 1261 -3.2; 1387 -4.5; 1526 -5.4; 1678 -6.5; 1846 -8.0; 2031 -9.3; 2234 -10.4; 2457 -11.7; 2703 -13.3; 2973 -13.2; 3270 -12.8; 3597 -11.5; 3957 -9.5; 4353 -8.5; 4788 -10.0; 5267 -9.7; 5793 -5.0; 6373 -1.0; 7010 -4.0; 7711 -7.9; 8482 -9.5; 9330 -7.2; 10263 -6.5; 11289 -7.2; 12418 -11.1; 13660 -14.1; 15026 -14.3; 16529 -12.8; 18182 -8.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Inspiration GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Inspiration ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.91 | 7.1 dB   |
| Peaking | 160 Hz   | 0.38 | -11.3 dB |
| Peaking | 491 Hz   | 0.45 | 11.6 dB  |
| Peaking | 2743 Hz  | 1.48 | -8.7 dB  |
| Peaking | 15039 Hz | 1.53 | -8.9 dB  |
| Peaking | 998 Hz   | 6.13 | 1.1 dB   |
| Peaking | 5337 Hz  | 3.51 | -6.4 dB  |
| Peaking | 6243 Hz  | 3.3  | 9.8 dB   |
| Peaking | 8216 Hz  | 6.63 | -3.7 dB  |
| Peaking | 17208 Hz | 4.3  | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 6.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -9.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Monster%20Inspiration/Monster%20Inspiration.png)