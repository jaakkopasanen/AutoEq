# Beats BeatsX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.8; 25 -4.8; 28 -4.8; 31 -4.8; 34 -4.8; 37 -4.8; 41 -4.8; 45 -4.8; 49 -4.8; 54 -4.9; 60 -5.3; 66 -5.6; 72 -5.7; 79 -5.8; 87 -5.8; 96 -5.7; 106 -5.8; 116 -5.9; 128 -5.9; 141 -6.0; 155 -5.9; 170 -5.8; 187 -5.5; 206 -5.3; 227 -5.1; 249 -4.9; 274 -4.9; 302 -4.8; 332 -4.6; 365 -4.4; 402 -4.3; 442 -4.2; 486 -4.1; 535 -4.0; 588 -3.9; 647 -3.9; 712 -4.0; 783 -4.5; 861 -5.2; 947 -6.0; 1042 -6.7; 1146 -7.3; 1261 -7.5; 1387 -7.5; 1526 -7.5; 1678 -7.5; 1846 -7.7; 2031 -7.9; 2234 -7.5; 2457 -6.8; 2703 -5.5; 2973 -3.4; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -1.9; 5267 -3.8; 5793 -4.5; 6373 -2.9; 7010 -2.2; 7711 -4.4; 8482 -4.7; 9330 -6.3; 10263 -9.6; 11289 -9.7; 12418 -12.4; 13660 -12.9; 15026 -6.9; 16529 -4.7; 18182 -6.1; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats BeatsX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats BeatsX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 115 Hz   | 1.13 | -1.4 dB |
| Peaking | 1974 Hz  | 1.03 | -4.2 dB |
| Peaking | 3691 Hz  | 1.83 | 6.2 dB  |
| Peaking | 6917 Hz  | 6.39 | 3.3 dB  |
| Peaking | 12816 Hz | 1.84 | -8.9 dB |
| Peaking | 648 Hz   | 1.23 | 1.4 dB  |
| Peaking | 1112 Hz  | 3.02 | -1.6 dB |
| Peaking | 8849 Hz  | 6.68 | 1.7 dB  |
| Peaking | 10029 Hz | 6.58 | -2.4 dB |
| Peaking | 15979 Hz | 4.77 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20BeatsX/Beats%20BeatsX.png)