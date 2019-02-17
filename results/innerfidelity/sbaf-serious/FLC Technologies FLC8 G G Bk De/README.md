# FLC Technologies FLC8 G G Bk De
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.9; 25 -7.0; 28 -7.1; 31 -7.1; 34 -7.1; 37 -7.1; 41 -7.1; 45 -7.0; 49 -7.0; 54 -7.0; 60 -7.1; 66 -7.1; 72 -7.2; 79 -7.3; 87 -7.4; 96 -7.6; 106 -7.6; 116 -7.5; 128 -7.6; 141 -7.6; 155 -7.6; 170 -7.5; 187 -7.4; 206 -7.3; 227 -7.1; 249 -7.0; 274 -6.8; 302 -6.6; 332 -6.4; 365 -6.2; 402 -6.0; 442 -5.7; 486 -5.7; 535 -5.5; 588 -5.1; 647 -5.1; 712 -5.2; 783 -5.1; 861 -5.3; 947 -6.0; 1042 -6.9; 1146 -7.5; 1261 -7.7; 1387 -7.7; 1526 -7.1; 1678 -6.3; 1846 -5.1; 2031 -4.4; 2234 -4.2; 2457 -3.9; 2703 -4.3; 2973 -1.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.2; 7010 -7.0; 7711 -9.1; 8482 -8.9; 9330 -8.6; 10263 -8.7; 11289 -7.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 G G Bk De GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 G G Bk De ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 707 Hz  | 1.7  | 1.7 dB  |
| Peaking | 1300 Hz | 2.22 | -2.4 dB |
| Peaking | 4027 Hz | 1.01 | 6.7 dB  |
| Peaking | 6051 Hz | 2.98 | 5.9 dB  |
| Peaking | 7588 Hz | 1.43 | -6.0 dB |
| Peaking | 40 Hz   | 0.46 | -0.5 dB |
| Peaking | 137 Hz  | 1.03 | -1.0 dB |
| Peaking | 2022 Hz | 5.48 | 0.6 dB  |
| Peaking | 2819 Hz | 5.82 | -2.1 dB |
| Peaking | 3084 Hz | 7.47 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20G%20G%20Bk%20De/FLC%20Technologies%20FLC8%20G%20G%20Bk%20De.png)