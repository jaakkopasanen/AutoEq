# Fender Thirteen 6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.4; 25 -2.6; 28 -2.8; 31 -3.0; 34 -3.2; 37 -3.3; 41 -3.6; 45 -3.9; 49 -4.1; 54 -4.3; 60 -4.6; 66 -4.9; 72 -5.3; 79 -5.7; 87 -6.1; 96 -6.7; 106 -7.2; 116 -7.7; 128 -8.2; 141 -8.6; 155 -8.9; 170 -9.2; 187 -9.5; 206 -9.8; 227 -9.9; 249 -9.9; 274 -10.1; 302 -10.2; 332 -10.2; 365 -10.3; 402 -10.3; 442 -10.4; 486 -10.4; 535 -10.6; 588 -10.7; 647 -10.8; 712 -10.8; 783 -10.6; 861 -10.2; 947 -9.7; 1042 -9.4; 1146 -9.6; 1261 -9.9; 1387 -9.9; 1526 -9.6; 1678 -9.2; 1846 -8.9; 2031 -8.7; 2234 -7.3; 2457 -4.6; 2703 -2.4; 2973 -1.6; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fender Thirteen 6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fender Thirteen 6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.54 | 2.0 dB  |
| Peaking | 41 Hz   | 0.39 | 3.6 dB  |
| Peaking | 421 Hz  | 0.2  | -4.4 dB |
| Peaking | 1868 Hz | 1.97 | -2.9 dB |
| Peaking | 3831 Hz | 0.88 | 8.0 dB  |
| Peaking | 2199 Hz | 7.09 | -1.1 dB |
| Peaking | 2690 Hz | 3.82 | 1.6 dB  |
| Peaking | 3922 Hz | 2.22 | -1.0 dB |
| Peaking | 6326 Hz | 2.37 | 5.2 dB  |
| Peaking | 7346 Hz | 1.49 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Fender%20Thirteen%206/Fender%20Thirteen%206.png)