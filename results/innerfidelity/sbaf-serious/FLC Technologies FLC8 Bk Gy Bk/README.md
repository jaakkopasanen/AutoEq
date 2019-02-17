# FLC Technologies FLC8 Bk Gy Bk
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.7; 25 -8.8; 28 -9.0; 31 -9.1; 34 -9.1; 37 -9.1; 41 -9.1; 45 -9.1; 49 -9.2; 54 -9.2; 60 -9.2; 66 -9.3; 72 -9.3; 79 -9.4; 87 -9.6; 96 -9.6; 106 -9.6; 116 -9.5; 128 -9.4; 141 -9.4; 155 -9.3; 170 -9.1; 187 -8.9; 206 -8.8; 227 -8.5; 249 -8.3; 274 -8.0; 302 -7.7; 332 -7.4; 365 -7.2; 402 -6.9; 442 -6.5; 486 -6.4; 535 -6.2; 588 -5.7; 647 -5.6; 712 -5.7; 783 -5.3; 861 -5.5; 947 -6.1; 1042 -6.7; 1146 -7.0; 1261 -7.1; 1387 -7.1; 1526 -6.7; 1678 -6.0; 1846 -4.9; 2031 -4.2; 2234 -4.0; 2457 -3.6; 2703 -3.8; 2973 -1.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.7; 7010 -6.3; 7711 -10.0; 8482 -11.7; 9330 -11.9; 10263 -10.3; 11289 -6.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 Bk Gy Bk GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 Bk Gy Bk ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.63 | -1.9 dB  |
| Peaking | 119 Hz  | 0.48 | -2.8 dB  |
| Peaking | 629 Hz  | 2.53 | 1.2 dB   |
| Peaking | 5255 Hz | 0.77 | 8.6 dB   |
| Peaking | 8561 Hz | 1.79 | -10.6 dB |
| Peaking | 1355 Hz | 3.18 | -1.7 dB  |
| Peaking | 3236 Hz | 5.94 | 1.9 dB   |
| Peaking | 4996 Hz | 2.92 | -1.5 dB  |
| Peaking | 6328 Hz | 2.85 | 2.1 dB   |
| Peaking | 7179 Hz | 6.09 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20Bk%20Gy%20Bk/FLC%20Technologies%20FLC8%20Bk%20Gy%20Bk.png)