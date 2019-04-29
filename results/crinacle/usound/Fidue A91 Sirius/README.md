# Fidue A91 Sirius
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.6; 25 -2.0; 28 -2.4; 31 -2.8; 34 -3.1; 37 -3.3; 41 -3.6; 45 -3.9; 49 -4.2; 54 -4.5; 60 -4.8; 66 -5.2; 72 -5.6; 79 -6.1; 87 -6.5; 96 -7.0; 106 -7.5; 116 -7.9; 128 -8.3; 141 -8.6; 155 -9.0; 170 -9.2; 187 -9.3; 206 -9.4; 227 -9.4; 249 -9.4; 274 -9.3; 302 -9.1; 332 -8.8; 365 -8.4; 402 -8.0; 442 -7.7; 486 -7.3; 535 -6.8; 588 -6.2; 647 -5.7; 712 -5.0; 783 -4.5; 861 -4.2; 947 -4.5; 1042 -5.6; 1146 -7.5; 1261 -9.4; 1387 -10.8; 1526 -11.5; 1678 -11.3; 1846 -10.2; 2031 -8.5; 2234 -6.9; 2457 -5.6; 2703 -4.9; 2973 -5.0; 3270 -5.3; 3597 -4.0; 3957 -2.4; 4353 -1.8; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -5.9; 7711 -8.1; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A91 Sirius GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A91 Sirius ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.25 | 5.4 dB  |
| Peaking | 208 Hz  | 0.58 | -3.4 dB |
| Peaking | 857 Hz  | 1.58 | 3.6 dB  |
| Peaking | 1520 Hz | 2.22 | -6.4 dB |
| Peaking | 4975 Hz | 1.85 | 6.7 dB  |
| Peaking | 1886 Hz | 5.9  | -1.0 dB |
| Peaking | 2590 Hz | 3.7  | 1.5 dB  |
| Peaking | 4908 Hz | 5.65 | -0.9 dB |
| Peaking | 6268 Hz | 4.66 | 3.6 dB  |
| Peaking | 7606 Hz | 3.13 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Fidue%20A91%20Sirius/Fidue%20A91%20Sirius.png)