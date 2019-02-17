# Brainwavz S5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -11.9; 25 -12.0; 28 -12.1; 31 -12.2; 34 -12.3; 37 -12.3; 41 -12.4; 45 -12.5; 49 -12.6; 54 -12.6; 60 -12.8; 66 -12.9; 72 -13.0; 79 -13.1; 87 -13.3; 96 -13.4; 106 -13.3; 116 -13.2; 128 -13.1; 141 -12.9; 155 -12.7; 170 -12.3; 187 -11.9; 206 -11.5; 227 -10.9; 249 -10.4; 274 -9.8; 302 -9.2; 332 -8.5; 365 -7.9; 402 -7.2; 442 -6.5; 486 -6.0; 535 -5.3; 588 -4.3; 647 -3.7; 712 -3.2; 783 -2.6; 861 -2.4; 947 -2.5; 1042 -2.6; 1146 -2.6; 1261 -2.3; 1387 -2.8; 1526 -2.8; 1678 -2.7; 1846 -2.2; 2031 -1.7; 2234 -1.3; 2457 -0.5; 2703 -0.7; 2973 -1.0; 3270 -2.0; 3597 -4.3; 3957 -6.7; 4353 -9.8; 4788 -11.7; 5267 -14.0; 5793 -13.1; 6373 -9.2; 7010 -6.3; 7711 -6.8; 8482 -10.4; 9330 -11.2; 10263 -5.4; 11289 -2.6; 12418 -2.6; 13660 -4.4; 15026 -8.7; 16529 -6.5; 18182 -4.9; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz S5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.25 | -9.2 dB  |
| Peaking | 140 Hz   | 0.73 | -5.6 dB  |
| Peaking | 295 Hz   | 1.29 | -3.1 dB  |
| Peaking | 5371 Hz  | 2.75 | -11.2 dB |
| Peaking | 16321 Hz | 0.26 | -3.4 dB  |
| Peaking | 3408 Hz  | 1.02 | 4.6 dB   |
| Peaking | 4177 Hz  | 2.57 | -5.5 dB  |
| Peaking | 9106 Hz  | 4.27 | -7.9 dB  |
| Peaking | 11476 Hz | 2.61 | 4.6 dB   |
| Peaking | 20107 Hz | 3.32 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB |
| Peaking | 62 Hz    | 1.41 | -7.4 dB |
| Peaking | 125 Hz   | 1.41 | -8.7 dB |
| Peaking | 250 Hz   | 1.41 | -6.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB |
| Peaking | 8000 Hz  | 1.41 | -6.7 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S5/Brainwavz%20S5.png)