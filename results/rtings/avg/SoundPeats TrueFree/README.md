# SoundPeats TrueFree
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.2; 25 -11.9; 28 -11.5; 31 -11.1; 34 -10.7; 37 -10.3; 41 -9.9; 45 -9.5; 49 -9.2; 54 -8.9; 60 -8.8; 66 -8.8; 72 -8.8; 79 -8.9; 87 -9.0; 96 -9.3; 106 -9.6; 116 -10.0; 128 -10.3; 141 -10.5; 155 -10.6; 170 -10.5; 187 -10.4; 206 -10.2; 227 -9.8; 249 -9.4; 274 -8.9; 302 -8.4; 332 -7.9; 365 -7.4; 402 -7.0; 442 -6.4; 486 -5.9; 535 -5.4; 588 -4.9; 647 -4.4; 712 -4.0; 783 -3.7; 861 -3.5; 947 -3.8; 1042 -4.5; 1146 -5.4; 1261 -6.2; 1387 -6.8; 1526 -7.3; 1678 -7.9; 1846 -8.4; 2031 -8.5; 2234 -7.8; 2457 -7.0; 2703 -7.2; 2973 -6.7; 3270 -4.8; 3597 -3.3; 3957 -2.5; 4353 -2.2; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.3; 7010 -3.9; 7711 -6.3; 8482 -7.7; 9330 -9.4; 10263 -11.7; 11289 -10.7; 12418 -6.7; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -10.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats TrueFree GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats TrueFree ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.62 | -6.0 dB |
| Peaking | 166 Hz   | 0.83 | -4.1 dB |
| Peaking | 761 Hz   | 1.97 | 3.4 dB  |
| Peaking | 5436 Hz  | 1.84 | 7.0 dB  |
| Peaking | 10269 Hz | 2.55 | -6.2 dB |
| Peaking | 1026 Hz  | 3.14 | 1.4 dB  |
| Peaking | 1981 Hz  | 1.33 | -2.4 dB |
| Peaking | 3757 Hz  | 4.56 | 2.3 dB  |
| Peaking | 13423 Hz | 2.57 | 1.2 dB  |
| Peaking | 18342 Hz | 2.07 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20TrueFree/SoundPeats%20TrueFree.png)