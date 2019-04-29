# NocturnaL Audio Atlantis
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.1; 25 -3.4; 28 -3.9; 31 -4.3; 34 -4.6; 37 -4.8; 41 -5.1; 45 -5.3; 49 -5.6; 54 -5.9; 60 -6.2; 66 -6.5; 72 -6.9; 79 -7.2; 87 -7.7; 96 -8.1; 106 -8.5; 116 -8.9; 128 -9.1; 141 -9.4; 155 -9.6; 170 -9.7; 187 -9.9; 206 -9.9; 227 -9.9; 249 -9.8; 274 -9.7; 302 -9.5; 332 -9.3; 365 -9.1; 402 -8.9; 442 -8.6; 486 -8.3; 535 -7.9; 588 -7.5; 647 -7.1; 712 -6.6; 783 -6.0; 861 -5.6; 947 -5.3; 1042 -5.4; 1146 -5.9; 1261 -6.4; 1387 -6.7; 1526 -6.5; 1678 -6.0; 1846 -5.2; 2031 -4.3; 2234 -3.9; 2457 -3.5; 2703 -2.2; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -1.3; 4788 -1.7; 5267 -3.9; 5793 -4.9; 6373 -7.6; 7010 -6.6; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NocturnaL Audio Atlantis GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NocturnaL Audio Atlantis ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.49 | 4.1 dB  |
| Peaking | 205 Hz  | 0.53 | -4.2 dB |
| Peaking | 1523 Hz | 4.19 | -1.4 dB |
| Peaking | 3601 Hz | 1.13 | 5.8 dB  |
| Peaking | 6482 Hz | 5.06 | -3.7 dB |
| Peaking | 463 Hz  | 2.31 | -0.5 dB |
| Peaking | 900 Hz  | 3.53 | 1.2 dB  |
| Peaking | 9675 Hz | 2.4  | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/NocturnaL%20Audio%20Atlantis/NocturnaL%20Audio%20Atlantis.png)