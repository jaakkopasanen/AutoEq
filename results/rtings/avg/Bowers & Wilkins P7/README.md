# Bowers & Wilkins P7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.4; 25 -8.6; 28 -8.9; 31 -9.1; 34 -9.1; 37 -9.0; 41 -8.9; 45 -8.7; 49 -8.6; 54 -8.4; 60 -8.4; 66 -8.5; 72 -8.4; 79 -8.2; 87 -8.3; 96 -8.6; 106 -9.0; 116 -9.2; 128 -9.2; 141 -9.1; 155 -8.8; 170 -8.4; 187 -7.8; 206 -7.1; 227 -6.2; 249 -5.4; 274 -4.6; 302 -4.2; 332 -4.0; 365 -4.3; 402 -5.1; 442 -5.4; 486 -5.4; 535 -5.4; 588 -5.5; 647 -5.5; 712 -5.6; 783 -5.7; 861 -5.8; 947 -5.9; 1042 -5.7; 1146 -5.4; 1261 -6.1; 1387 -6.7; 1526 -7.5; 1678 -8.4; 1846 -9.0; 2031 -8.6; 2234 -5.6; 2457 -2.5; 2703 -2.0; 2973 -2.1; 3270 -3.1; 3597 -5.0; 3957 -5.7; 4353 -4.3; 4788 -2.6; 5267 -1.9; 5793 -1.8; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -7.6; 9330 -6.2; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -6.0; 16529 -7.9; 18182 -6.0; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.61 | -3.2 dB |
| Peaking | 129 Hz   | 1.97 | -3.1 dB |
| Peaking | 1917 Hz  | 2.89 | -5.0 dB |
| Peaking | 2644 Hz  | 2.46 | 5.2 dB  |
| Peaking | 5891 Hz  | 2.96 | 5.0 dB  |
| Peaking | 186 Hz   | 2.93 | -1.2 dB |
| Peaking | 311 Hz   | 1.85 | 2.3 dB  |
| Peaking | 1108 Hz  | 6.13 | 0.6 dB  |
| Peaking | 16491 Hz | 3.72 | -1.3 dB |
| Peaking | 16704 Hz | 2.15 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20P7/Bowers%20&%20Wilkins%20P7.png)