# Oriveti New Primacy
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.1; 25 -6.5; 28 -6.8; 31 -7.2; 34 -7.4; 37 -7.6; 41 -7.9; 45 -8.1; 49 -8.3; 54 -8.5; 60 -8.8; 66 -9.1; 72 -9.4; 79 -9.8; 87 -10.1; 96 -10.5; 106 -10.8; 116 -11.1; 128 -11.4; 141 -11.6; 155 -11.8; 170 -11.9; 187 -11.9; 206 -11.9; 227 -11.9; 249 -11.9; 274 -11.7; 302 -11.5; 332 -11.2; 365 -10.9; 402 -10.8; 442 -10.6; 486 -10.4; 535 -10.1; 588 -9.9; 647 -9.5; 712 -9.0; 783 -8.3; 861 -7.7; 947 -7.1; 1042 -6.9; 1146 -6.9; 1261 -6.8; 1387 -6.4; 1526 -5.8; 1678 -5.3; 1846 -4.7; 2031 -3.1; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -3.9; 5267 -3.5; 5793 -1.3; 6373 -1.4; 7010 -5.8; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -7.9; 16529 -9.8; 18182 -13.9; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriveti New Primacy GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriveti New Primacy ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.56 | 1.4 dB  |
| Peaking | 101 Hz   | 0.51 | -1.2 dB |
| Peaking | 248 Hz   | 0.39 | -4.8 dB |
| Peaking | 2402 Hz  | 2.46 | 4.0 dB  |
| Peaking | 3797 Hz  | 1.11 | 5.6 dB  |
| Peaking | 616 Hz   | 3.41 | -0.4 dB |
| Peaking | 949 Hz   | 4.39 | 0.8 dB  |
| Peaking | 6140 Hz  | 9.19 | 3.9 dB  |
| Peaking | 18926 Hz | 0.94 | -6.9 dB |
| Peaking | 20229 Hz | 0.91 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Oriveti%20New%20Primacy/Oriveti%20New%20Primacy.png)