# Musical Fidelity MF200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.9; 25 -4.5; 28 -5.3; 31 -6.0; 34 -6.5; 37 -6.9; 41 -7.4; 45 -7.7; 49 -8.0; 54 -8.2; 60 -8.3; 66 -8.6; 72 -8.8; 79 -8.9; 87 -9.0; 96 -8.9; 106 -9.1; 116 -9.0; 128 -8.8; 141 -8.3; 155 -8.4; 170 -7.9; 187 -7.6; 206 -7.4; 227 -6.9; 249 -6.5; 274 -5.8; 302 -5.0; 332 -4.4; 365 -4.0; 402 -3.8; 442 -3.0; 486 -2.5; 535 -1.9; 588 -1.9; 647 -3.5; 712 -4.7; 783 -5.4; 861 -6.4; 947 -6.5; 1042 -6.0; 1146 -6.4; 1261 -5.6; 1387 -5.2; 1526 -5.1; 1678 -5.3; 1846 -5.4; 2031 -5.7; 2234 -6.1; 2457 -6.1; 2703 -5.9; 2973 -6.1; 3270 -6.2; 3597 -6.3; 3957 -5.4; 4353 -6.7; 4788 -9.0; 5267 -5.7; 5793 -2.4; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -6.3; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Musical Fidelity MF200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Musical Fidelity MF200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.43 | 3.8 dB  |
| Peaking | 66 Hz   | 0.69 | -2.3 dB |
| Peaking | 132 Hz  | 1.05 | -1.8 dB |
| Peaking | 505 Hz  | 1.81 | 4.3 dB  |
| Peaking | 6346 Hz | 6.49 | 6.4 dB  |
| Peaking | 321 Hz  | 5.71 | 0.9 dB  |
| Peaking | 916 Hz  | 3.74 | -1.3 dB |
| Peaking | 1546 Hz | 3.82 | 0.8 dB  |
| Peaking | 4828 Hz | 8.38 | -3.7 dB |
| Peaking | 5934 Hz | 8.32 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Musical%20Fidelity%20MF200/Musical%20Fidelity%20MF200.png)