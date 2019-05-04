# Beyerdynamic T1 2nd Generation
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.9; 25 -3.1; 28 -3.3; 31 -3.5; 34 -3.7; 37 -3.8; 41 -4.0; 45 -4.1; 49 -4.2; 54 -4.4; 60 -4.6; 66 -4.9; 72 -5.2; 79 -5.6; 87 -6.0; 96 -6.5; 106 -6.9; 116 -7.3; 128 -7.7; 141 -8.0; 155 -8.2; 170 -8.3; 187 -8.4; 206 -8.3; 227 -8.3; 249 -8.2; 274 -8.2; 302 -8.2; 332 -8.2; 365 -8.1; 402 -8.0; 442 -7.7; 486 -7.8; 535 -7.7; 588 -7.5; 647 -7.2; 712 -6.9; 783 -6.7; 861 -6.5; 947 -6.2; 1042 -5.5; 1146 -4.6; 1261 -4.0; 1387 -2.8; 1526 -2.2; 1678 -2.7; 1846 -2.8; 2031 -2.6; 2234 -1.3; 2457 -0.9; 2703 -2.0; 2973 -3.9; 3270 -4.8; 3597 -4.8; 3957 -4.6; 4353 -3.0; 4788 -0.5; 5267 -2.3; 5793 -8.4; 6373 -11.0; 7010 -9.5; 7711 -12.2; 8482 -15.1; 9330 -12.3; 10263 -8.4; 11289 -9.1; 12418 -7.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 2nd Generation GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 2nd Generation ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.01 | 3.7 dB  |
| Peaking | 2156 Hz | 1.28 | 5.2 dB  |
| Peaking | 4609 Hz | 6.16 | 3.9 dB  |
| Peaking | 5064 Hz | 7.66 | 5.0 dB  |
| Peaking | 8306 Hz | 1.94 | -8.2 dB |
| Peaking | 63 Hz   | 0.91 | 3.0 dB  |
| Peaking | 149 Hz  | 0.26 | -2.4 dB |
| Peaking | 1389 Hz | 4.21 | 2.1 dB  |
| Peaking | 6199 Hz | 8.65 | -3.1 dB |
| Peaking | 7203 Hz | 7.59 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20T1%202nd%20Generation/Beyerdynamic%20T1%202nd%20Generation.png)