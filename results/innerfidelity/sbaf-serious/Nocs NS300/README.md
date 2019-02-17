# Nocs NS300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.1; 45 -1.8; 49 -2.4; 54 -2.9; 60 -3.4; 66 -3.8; 72 -4.2; 79 -4.4; 87 -4.2; 96 -4.1; 106 -3.4; 116 -2.5; 128 -2.7; 141 -3.2; 155 -3.1; 170 -2.1; 187 -1.8; 206 -0.7; 227 -0.5; 249 -0.5; 274 -0.5; 302 -1.0; 332 -3.4; 365 -4.3; 402 -4.8; 442 -5.2; 486 -5.6; 535 -5.9; 588 -5.9; 647 -6.2; 712 -6.7; 783 -6.8; 861 -7.0; 947 -6.9; 1042 -6.0; 1146 -4.7; 1261 -3.6; 1387 -3.5; 1526 -2.2; 1678 -2.3; 1846 -1.7; 2031 -1.7; 2234 -2.3; 2457 -2.6; 2703 -3.6; 2973 -3.9; 3270 -4.5; 3597 -3.1; 3957 -1.7; 4353 -0.5; 4788 -1.8; 5267 -1.7; 5793 -0.5; 6373 -1.3; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.1  | 2.4 dB  |
| Peaking | 28 Hz   | 1.02 | 4.0 dB  |
| Peaking | 238 Hz  | 1.52 | 5.6 dB  |
| Peaking | 1865 Hz | 1.71 | 4.7 dB  |
| Peaking | 4983 Hz | 1.53 | 5.7 dB  |
| Peaking | 119 Hz  | 7.12 | 1.4 dB  |
| Peaking | 935 Hz  | 1.67 | -2.0 dB |
| Peaking | 1231 Hz | 2.79 | 1.9 dB  |
| Peaking | 6305 Hz | 5.33 | 3.3 dB  |
| Peaking | 7557 Hz | 1.49 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | 6.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS300/Nocs%20NS300.png)