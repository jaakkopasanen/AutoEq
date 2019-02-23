# Beyerdynamic DT 100 2X2kOhm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.5; 31 -3.1; 34 -3.7; 37 -4.1; 41 -4.6; 45 -5.0; 49 -5.3; 54 -5.6; 60 -5.7; 66 -5.9; 72 -6.0; 79 -5.7; 87 -6.9; 96 -6.3; 106 -5.2; 116 -8.7; 128 -12.3; 141 -13.2; 155 -12.7; 170 -12.1; 187 -13.9; 206 -13.6; 227 -13.4; 249 -13.1; 274 -12.8; 302 -12.2; 332 -11.7; 365 -11.1; 402 -10.4; 442 -9.5; 486 -8.9; 535 -8.1; 588 -7.1; 647 -6.3; 712 -6.0; 783 -5.4; 861 -5.0; 947 -4.7; 1042 -3.8; 1146 -4.1; 1261 -4.1; 1387 -5.0; 1526 -6.8; 1678 -8.1; 1846 -8.7; 2031 -7.8; 2234 -6.5; 2457 -4.8; 2703 -2.2; 2973 -0.8; 3270 -0.8; 3597 -1.2; 3957 -1.7; 4353 -1.4; 4788 -0.8; 5267 -0.8; 5793 -0.8; 6373 -1.3; 7010 -4.3; 7711 -6.5; 8482 -9.0; 9330 -10.2; 10263 -6.8; 11289 -6.8; 12418 -6.8; 13660 -6.8; 15026 -6.8; 16529 -6.8; 18182 -6.8; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 100 2X2kOhm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 100 2X2kOhm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 140 Hz  | 4.51 | -4.8 dB |
| Peaking | 235 Hz  | 1.24 | -7.2 dB |
| Peaking | 3251 Hz | 2.43 | 5.9 dB  |
| Peaking | 5358 Hz | 2.41 | 6.2 dB  |
| Peaking | 15 Hz   | 0.57 | 7.5 dB  |
| Peaking | 105 Hz  | 7.83 | 3.2 dB  |
| Peaking | 1125 Hz | 1.54 | 3.4 dB  |
| Peaking | 1816 Hz | 3.24 | -3.8 dB |
| Peaking | 8985 Hz | 6    | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20100%202X2kOhm/Beyerdynamic%20DT%20100%202X2kOhm.png)