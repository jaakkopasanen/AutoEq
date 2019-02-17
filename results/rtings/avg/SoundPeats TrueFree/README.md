# SoundPeats TrueFree
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.5; 25 -12.2; 28 -11.8; 31 -11.4; 34 -11.0; 37 -10.6; 41 -10.2; 45 -9.8; 49 -9.5; 54 -9.2; 60 -9.2; 66 -9.2; 72 -9.1; 79 -9.2; 87 -9.4; 96 -9.6; 106 -10.0; 116 -10.3; 128 -10.7; 141 -10.9; 155 -10.9; 170 -10.9; 187 -10.7; 206 -10.5; 227 -10.2; 249 -9.7; 274 -9.2; 302 -8.7; 332 -8.2; 365 -7.7; 402 -7.3; 442 -6.8; 486 -6.3; 535 -5.7; 588 -5.2; 647 -4.8; 712 -4.3; 783 -4.0; 861 -3.9; 947 -4.2; 1042 -4.8; 1146 -5.7; 1261 -6.6; 1387 -7.1; 1526 -7.7; 1678 -8.2; 1846 -8.7; 2031 -8.8; 2234 -8.1; 2457 -7.3; 2703 -7.5; 2973 -7.0; 3270 -5.2; 3597 -3.6; 3957 -2.8; 4353 -2.5; 4788 -1.6; 5267 -0.9; 5793 -0.5; 6373 -1.6; 7010 -3.4; 7711 -6.5; 8482 -8.1; 9330 -9.7; 10263 -12.0; 11289 -11.0; 12418 -6.1; 13660 -4.5; 15026 -4.5; 16529 -6.6; 18182 -10.4; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats TrueFree GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats TrueFree ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.82 | -8.1 dB |
| Peaking | 28 Hz    | 0.61 | -4.4 dB |
| Peaking | 170 Hz   | 0.59 | -6.1 dB |
| Peaking | 10411 Hz | 3.36 | -8.5 dB |
| Peaking | 18432 Hz | 1.81 | -6.7 dB |
| Peaking | 853 Hz   | 1.55 | 2.6 dB  |
| Peaking | 2018 Hz  | 0.86 | -5.0 dB |
| Peaking | 5824 Hz  | 1.04 | 6.4 dB  |
| Peaking | 8144 Hz  | 1.87 | -4.8 dB |
| Peaking | 14311 Hz | 2.98 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20TrueFree/SoundPeats%20TrueFree.png)