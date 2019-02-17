# Beyerdynamic DT 100 2X2kOhm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.3; 25 -3.9; 28 -4.6; 31 -5.2; 34 -5.8; 37 -6.2; 41 -6.7; 45 -7.1; 49 -7.4; 54 -7.7; 60 -7.8; 66 -8.0; 72 -8.1; 79 -7.7; 87 -9.0; 96 -8.4; 106 -7.3; 116 -10.8; 128 -14.4; 141 -15.3; 155 -14.8; 170 -14.2; 187 -16.0; 206 -15.7; 227 -15.4; 249 -15.2; 274 -14.9; 302 -14.3; 332 -13.8; 365 -13.2; 402 -12.5; 442 -11.6; 486 -11.0; 535 -10.2; 588 -9.1; 647 -8.4; 712 -8.1; 783 -7.5; 861 -7.1; 947 -6.8; 1042 -5.9; 1146 -6.2; 1261 -6.2; 1387 -7.1; 1526 -8.8; 1678 -10.1; 1846 -10.8; 2031 -9.9; 2234 -8.6; 2457 -6.9; 2703 -4.3; 2973 -2.7; 3270 -2.4; 3597 -3.3; 3957 -3.8; 4353 -3.4; 4788 -1.7; 5267 -0.5; 5793 -0.6; 6373 -1.1; 7010 -4.0; 7711 -7.2; 8482 -11.1; 9330 -12.3; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 100 2X2kOhm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 100 2X2kOhm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.65 | 4.1 dB  |
| Peaking | 139 Hz  | 4.56 | -4.5 dB |
| Peaking | 245 Hz  | 0.79 | -9.1 dB |
| Peaking | 5646 Hz | 1.38 | 6.8 dB  |
| Peaking | 8842 Hz | 3.48 | -8.4 dB |
| Peaking | 107 Hz  | 6.26 | 4.6 dB  |
| Peaking | 112 Hz  | 2.91 | -2.0 dB |
| Peaking | 1274 Hz | 1.44 | 4.8 dB  |
| Peaking | 1759 Hz | 1.19 | -6.9 dB |
| Peaking | 2957 Hz | 2.85 | 4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -8.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20100%202X2kOhm/Beyerdynamic%20DT%20100%202X2kOhm.png)