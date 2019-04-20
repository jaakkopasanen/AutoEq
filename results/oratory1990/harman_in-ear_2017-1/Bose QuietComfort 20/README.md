# Bose QuietComfort 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -5.4; 25 -6.3; 28 -7.3; 31 -7.8; 34 -8.0; 37 -8.0; 41 -8.0; 45 -7.8; 49 -7.7; 54 -7.6; 60 -7.6; 66 -7.7; 72 -7.9; 79 -8.3; 87 -8.7; 96 -9.1; 106 -9.4; 116 -9.4; 128 -9.2; 141 -8.9; 155 -8.6; 170 -8.5; 187 -8.4; 206 -8.4; 227 -8.4; 249 -8.4; 274 -8.4; 302 -8.3; 332 -8.2; 365 -8.1; 402 -8.2; 442 -8.3; 486 -8.0; 535 -7.2; 588 -5.8; 647 -4.7; 712 -4.1; 783 -3.3; 861 -2.6; 947 -2.9; 1042 -3.9; 1146 -4.9; 1261 -5.7; 1387 -6.3; 1526 -8.5; 1678 -10.6; 1846 -10.6; 2031 -8.9; 2234 -7.2; 2457 -6.3; 2703 -5.6; 2973 -5.1; 3270 -5.2; 3597 -5.9; 3957 -7.4; 4353 -7.5; 4788 -5.0; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -5.0; 7711 -7.6; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.2; 16529 -14.5; 18182 -13.9; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 192 Hz   |  0.25 | -2.5 dB |
| Peaking | 864 Hz   |  1.55 | 5.2 dB  |
| Peaking | 1752 Hz  |  3.96 | -5.3 dB |
| Peaking | 5844 Hz  |  3.76 | 7.1 dB  |
| Peaking | 17889 Hz |  1.06 | -9.0 dB |
| Peaking | 471 Hz   |  6.83 | -0.9 dB |
| Peaking | 3069 Hz  |  3.2  | 1.6 dB  |
| Peaking | 4171 Hz  |  6.74 | -2.6 dB |
| Peaking | 7607 Hz  | 11.25 | -2.4 dB |
| Peaking | 13328 Hz |  3.18 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -7.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)