# Eartech Quad
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.4; 25 -4.7; 28 -5.1; 31 -5.5; 34 -5.9; 37 -6.2; 41 -6.6; 45 -6.9; 49 -7.2; 54 -7.5; 60 -8.0; 66 -8.4; 72 -8.9; 79 -9.4; 87 -9.9; 96 -10.5; 106 -10.9; 116 -11.3; 128 -11.7; 141 -12.0; 155 -12.3; 170 -12.4; 187 -12.4; 206 -12.4; 227 -12.3; 249 -12.2; 274 -12.0; 302 -11.7; 332 -11.4; 365 -10.9; 402 -10.6; 442 -10.1; 486 -9.6; 535 -9.0; 588 -8.3; 647 -7.6; 712 -6.8; 783 -6.0; 861 -5.2; 947 -4.6; 1042 -4.4; 1146 -4.6; 1261 -4.8; 1387 -4.8; 1526 -4.4; 1678 -3.8; 1846 -3.0; 2031 -2.2; 2234 -1.8; 2457 -2.1; 2703 -2.3; 2973 -2.0; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.2; 5793 -5.1; 6373 -5.3; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Eartech Quad GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Eartech Quad ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.35 | 3.1 dB  |
| Peaking | 199 Hz  | 0.41 | -6.1 dB |
| Peaking | 940 Hz  | 1.59 | 2.8 dB  |
| Peaking | 2202 Hz | 1.46 | 3.8 dB  |
| Peaking | 4081 Hz | 1.79 | 5.9 dB  |
| Peaking | 3325 Hz | 6.55 | 1.3 dB  |
| Peaking | 4920 Hz | 4.74 | 3.0 dB  |
| Peaking | 5324 Hz | 1.35 | -2.0 dB |
| Peaking | 6843 Hz | 7.87 | 2.3 dB  |
| Peaking | 9096 Hz | 4.5  | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Eartech%20Quad/Eartech%20Quad.png)