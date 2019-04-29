# Fidue A91 Sirius custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.4; 45 -2.0; 49 -2.4; 54 -2.9; 60 -3.3; 66 -3.7; 72 -4.1; 79 -4.5; 87 -4.9; 96 -5.4; 106 -5.8; 116 -6.3; 128 -6.6; 141 -6.8; 155 -7.0; 170 -7.2; 187 -7.4; 206 -7.6; 227 -7.6; 249 -7.6; 274 -7.6; 302 -7.7; 332 -7.6; 365 -7.5; 402 -7.5; 442 -7.4; 486 -7.4; 535 -7.3; 588 -7.2; 647 -7.0; 712 -6.9; 783 -6.8; 861 -6.8; 947 -7.1; 1042 -7.8; 1146 -9.0; 1261 -10.3; 1387 -11.0; 1526 -10.6; 1678 -9.5; 1846 -8.1; 2031 -6.8; 2234 -5.8; 2457 -5.3; 2703 -5.3; 2973 -5.7; 3270 -5.9; 3597 -5.5; 3957 -5.2; 4353 -5.3; 4788 -4.2; 5267 -2.4; 5793 -0.6; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A91 Sirius custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A91 Sirius custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.48 | 6.2 dB  |
| Peaking | 215 Hz  | 0.62 | -1.5 dB |
| Peaking | 1442 Hz | 2.37 | -5.0 dB |
| Peaking | 2470 Hz | 2.09 | 1.7 dB  |
| Peaking | 5869 Hz | 3.26 | 6.3 dB  |
| Peaking | 879 Hz  | 2.47 | 1.4 dB  |
| Peaking | 896 Hz  | 1.37 | -0.8 dB |
| Peaking | 6724 Hz | 6.69 | 1.3 dB  |
| Peaking | 7785 Hz | 2.87 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Fidue%20A91%20Sirius%20custom/Fidue%20A91%20Sirius%20custom.png)