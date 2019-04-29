# Earsonics EM6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.9; 25 -7.1; 28 -7.3; 31 -7.5; 34 -7.6; 37 -7.7; 41 -7.8; 45 -7.9; 49 -7.9; 54 -8.0; 60 -8.1; 66 -8.3; 72 -8.5; 79 -8.8; 87 -9.1; 96 -9.4; 106 -9.6; 116 -9.9; 128 -10.1; 141 -10.3; 155 -10.5; 170 -10.6; 187 -10.6; 206 -10.6; 227 -10.5; 249 -10.4; 274 -10.3; 302 -10.1; 332 -10.0; 365 -9.7; 402 -9.5; 442 -9.2; 486 -8.9; 535 -8.6; 588 -8.3; 647 -7.9; 712 -7.5; 783 -7.1; 861 -6.8; 947 -6.8; 1042 -7.1; 1146 -7.9; 1261 -8.8; 1387 -9.5; 1526 -9.6; 1678 -9.3; 1846 -8.6; 2031 -7.6; 2234 -6.5; 2457 -5.2; 2703 -4.0; 2973 -3.1; 3270 -2.5; 3597 -2.8; 3957 -2.3; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.2; 6373 -2.5; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.8; 16529 -15.5; 18182 -15.4; 20000 -8.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics EM6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics EM6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 109 Hz   | 0.45 | -1.8 dB  |
| Peaking | 248 Hz   | 0.6  | -3.1 dB  |
| Peaking | 1580 Hz  | 2.29 | -3.8 dB  |
| Peaking | 4600 Hz  | 1.15 | 6.4 dB   |
| Peaking | 17533 Hz | 1.28 | -10.8 dB |
| Peaking | 891 Hz   | 5.22 | 0.9 dB   |
| Peaking | 3835 Hz  | 8.07 | -1.9 dB  |
| Peaking | 6477 Hz  | 0.85 | 1.2 dB   |
| Peaking | 7934 Hz  | 2.47 | -2.5 dB  |
| Peaking | 13825 Hz | 4.11 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -7.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Earsonics%20EM6/Earsonics%20EM6.png)