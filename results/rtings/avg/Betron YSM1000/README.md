# Betron YSM1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.5; 25 -5.6; 28 -5.8; 31 -5.9; 34 -6.0; 37 -6.1; 41 -6.2; 45 -6.3; 49 -6.5; 54 -6.8; 60 -7.3; 66 -7.8; 72 -8.2; 79 -8.7; 87 -9.3; 96 -10.0; 106 -10.6; 116 -11.3; 128 -11.9; 141 -12.3; 155 -12.7; 170 -12.8; 187 -12.8; 206 -12.9; 227 -12.8; 249 -12.6; 274 -12.2; 302 -11.6; 332 -11.1; 365 -10.4; 402 -9.8; 442 -9.0; 486 -8.2; 535 -7.2; 588 -6.2; 647 -5.1; 712 -4.2; 783 -3.4; 861 -2.8; 947 -2.6; 1042 -2.5; 1146 -2.2; 1261 -1.6; 1387 -0.8; 1526 -2.4; 1678 -4.3; 1846 -4.3; 2031 -3.6; 2234 -2.1; 2457 -0.8; 2703 -0.5; 2973 -1.3; 3270 -2.7; 3597 -4.5; 3957 -6.2; 4353 -8.5; 4788 -10.7; 5267 -11.1; 5793 -6.3; 6373 -2.3; 7010 -3.8; 7711 -6.1; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Betron YSM1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Betron YSM1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 209 Hz  | 0.6  | -7.1 dB |
| Peaking | 1041 Hz | 0.93 | 5.2 dB  |
| Peaking | 2782 Hz | 2.3  | 5.6 dB  |
| Peaking | 5060 Hz | 2.98 | -6.9 dB |
| Peaking | 6417 Hz | 4.64 | 6.1 dB  |
| Peaking | 22 Hz   | 0.21 | 1.1 dB  |
| Peaking | 111 Hz  | 1.59 | -1.0 dB |
| Peaking | 1143 Hz | 2.9  | -2.4 dB |
| Peaking | 1411 Hz | 1.87 | 3.6 dB  |
| Peaking | 1693 Hz | 3.52 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Betron%20YSM1000/Betron%20YSM1000.png)