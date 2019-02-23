# FLC Technologies FLC8 G G Bk De
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.3; 25 -8.4; 28 -8.5; 31 -8.5; 34 -8.5; 37 -8.5; 41 -8.5; 45 -8.5; 49 -8.4; 54 -8.5; 60 -8.5; 66 -8.5; 72 -8.6; 79 -8.7; 87 -8.8; 96 -9.0; 106 -9.0; 116 -8.9; 128 -9.0; 141 -9.0; 155 -9.0; 170 -8.9; 187 -8.8; 206 -8.7; 227 -8.5; 249 -8.4; 274 -8.2; 302 -8.0; 332 -7.8; 365 -7.6; 402 -7.4; 442 -7.1; 486 -7.1; 535 -6.9; 588 -6.5; 647 -6.5; 712 -6.7; 783 -6.5; 861 -6.7; 947 -7.4; 1042 -8.3; 1146 -8.9; 1261 -9.1; 1387 -9.1; 1526 -8.5; 1678 -7.7; 1846 -6.5; 2031 -5.9; 2234 -5.7; 2457 -5.3; 2703 -5.7; 2973 -3.3; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.7; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -3.6; 7010 -8.5; 7711 -10.5; 8482 -10.3; 9330 -10.0; 10263 -10.1; 11289 -8.7; 12418 -6.8; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 G G Bk De GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 G G Bk De ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 86 Hz    | 0.29 | -2.5 dB |
| Peaking | 1319 Hz  | 2.56 | -3.0 dB |
| Peaking | 3558 Hz  | 2.53 | 5.7 dB  |
| Peaking | 5730 Hz  | 1.88 | 9.7 dB  |
| Peaking | 7679 Hz  | 1.31 | -7.7 dB |
| Peaking | 21 Hz    | 1.97 | -0.5 dB |
| Peaking | 718 Hz   | 1.87 | 0.7 dB  |
| Peaking | 1050 Hz  | 6.33 | -0.8 dB |
| Peaking | 10719 Hz | 3.75 | -2.1 dB |
| Peaking | 12210 Hz | 1.32 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20G%20G%20Bk%20De/FLC%20Technologies%20FLC8%20G%20G%20Bk%20De.png)