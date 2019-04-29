# Eternal Melody EM6W
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.5; 25 -5.8; 28 -6.1; 31 -6.4; 34 -6.7; 37 -6.9; 41 -7.2; 45 -7.4; 49 -7.6; 54 -7.9; 60 -8.3; 66 -8.6; 72 -9.0; 79 -9.3; 87 -9.8; 96 -10.2; 106 -10.6; 116 -10.9; 128 -11.2; 141 -11.5; 155 -11.7; 170 -11.8; 187 -11.8; 206 -11.7; 227 -11.6; 249 -11.4; 274 -11.2; 302 -10.8; 332 -10.5; 365 -10.1; 402 -9.7; 442 -9.2; 486 -8.6; 535 -8.1; 588 -7.4; 647 -6.7; 712 -6.0; 783 -5.2; 861 -4.5; 947 -4.1; 1042 -4.0; 1146 -4.5; 1261 -5.2; 1387 -5.7; 1526 -5.8; 1678 -5.7; 1846 -5.2; 2031 -4.5; 2234 -3.8; 2457 -3.3; 2703 -3.0; 2973 -2.6; 3270 -2.0; 3597 -1.1; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -4.2; 5793 -3.5; 6373 -2.2; 7010 -4.0; 7711 -7.0; 8482 -8.5; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Eternal Melody EM6W GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Eternal Melody EM6W ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 109 Hz  | 0.97 | -1.6 dB |
| Peaking | 225 Hz  | 0.56 | -4.8 dB |
| Peaking | 919 Hz  | 1.88 | 3.1 dB  |
| Peaking | 3382 Hz | 1.1  | 3.7 dB  |
| Peaking | 4435 Hz | 2.17 | 3.4 dB  |
| Peaking | 18 Hz   | 1.8  | 1.4 dB  |
| Peaking | 4835 Hz | 8.03 | 1.2 dB  |
| Peaking | 5293 Hz | 5.53 | -2.4 dB |
| Peaking | 6465 Hz | 4.11 | 3.4 dB  |
| Peaking | 8223 Hz | 4.17 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Eternal%20Melody%20EM6W/Eternal%20Melody%20EM6W.png)