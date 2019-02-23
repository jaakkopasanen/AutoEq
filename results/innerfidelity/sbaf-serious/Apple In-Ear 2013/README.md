# Apple In-Ear 2013
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.5; 25 -5.5; 28 -5.5; 31 -5.5; 34 -5.6; 37 -5.6; 41 -5.7; 45 -5.9; 49 -6.0; 54 -6.1; 60 -6.3; 66 -6.6; 72 -6.9; 79 -7.2; 87 -7.6; 96 -8.1; 106 -8.3; 116 -8.5; 128 -8.8; 141 -9.1; 155 -9.2; 170 -9.3; 187 -9.5; 206 -9.5; 227 -9.5; 249 -9.4; 274 -9.4; 302 -9.3; 332 -9.1; 365 -8.9; 402 -8.7; 442 -8.4; 486 -8.3; 535 -7.9; 588 -7.1; 647 -6.9; 712 -6.9; 783 -6.5; 861 -6.6; 947 -6.7; 1042 -6.8; 1146 -6.9; 1261 -7.0; 1387 -7.3; 1526 -7.5; 1678 -7.5; 1846 -7.2; 2031 -6.8; 2234 -6.6; 2457 -6.2; 2703 -6.5; 2973 -5.4; 3270 -2.4; 3597 -0.5; 3957 -1.3; 4353 -3.7; 4788 -3.7; 5267 -1.7; 5793 -0.6; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple In-Ear 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple In-Ear 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.64 | 1.2 dB  |
| Peaking | 204 Hz   | 0.57 | -3.3 dB |
| Peaking | 3638 Hz  | 3.21 | 7.4 dB  |
| Peaking | 4484 Hz  | 0.55 | -2.1 dB |
| Peaking | 5906 Hz  | 2.54 | 7.7 dB  |
| Peaking | 479 Hz   | 1.5  | -1.5 dB |
| Peaking | 592 Hz   | 1.01 | 1.4 dB  |
| Peaking | 1548 Hz  | 3.82 | -0.8 dB |
| Peaking | 12233 Hz | 2.79 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20In-Ear%202013/Apple%20In-Ear%202013.png)