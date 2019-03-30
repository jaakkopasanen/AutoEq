# Sennheiser HD 515
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.9; 37 -1.4; 41 -2.1; 45 -2.8; 49 -3.3; 54 -3.8; 60 -4.1; 66 -4.4; 72 -4.7; 79 -5.0; 87 -5.4; 96 -5.8; 106 -6.1; 116 -6.4; 128 -6.5; 141 -6.7; 155 -6.8; 170 -7.1; 187 -7.4; 206 -7.5; 227 -7.8; 249 -7.8; 274 -7.8; 302 -7.7; 332 -7.6; 365 -7.5; 402 -7.5; 442 -7.5; 486 -7.2; 535 -7.1; 588 -6.8; 647 -6.8; 712 -6.5; 783 -6.4; 861 -6.1; 947 -5.7; 1042 -4.9; 1146 -3.8; 1261 -2.3; 1387 -0.8; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.7; 2703 -4.0; 2973 -10.4; 3270 -13.6; 3597 -14.2; 3957 -12.7; 4353 -10.9; 4788 -9.4; 5267 -7.7; 5793 -6.3; 6373 -5.7; 7010 -7.9; 7711 -10.7; 8482 -11.5; 9330 -10.5; 10263 -9.7; 11289 -9.7; 12418 -9.0; 13660 -7.4; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 515 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 515 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 25 Hz   |  0.64 | 6.3 dB   |
| Peaking | 773 Hz  |  0.29 | -2.9 dB  |
| Peaking | 2298 Hz |  0.66 | 13.7 dB  |
| Peaking | 3431 Hz |  1.78 | -17.2 dB |
| Peaking | 9212 Hz |  1.53 | -5.3 dB  |
| Peaking | 2538 Hz | 12.5  | 1.8 dB   |
| Peaking | 4647 Hz |  3.17 | -1.6 dB  |
| Peaking | 5231 Hz |  3.35 | 0.4 dB   |
| Peaking | 6297 Hz |  3.52 | 2.5 dB   |
| Peaking | 7781 Hz |  5.87 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.1 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20515/Sennheiser%20HD%20515.png)