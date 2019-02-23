# Beyerdynamic DT 880 32 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -0.8; 60 -1.0; 66 -1.3; 72 -1.7; 79 -2.2; 87 -2.7; 96 -3.2; 106 -3.7; 116 -4.2; 128 -4.6; 141 -5.0; 155 -5.3; 170 -5.5; 187 -5.6; 206 -5.6; 227 -5.6; 249 -5.5; 274 -5.6; 302 -5.7; 332 -5.7; 365 -5.7; 402 -6.0; 442 -6.2; 486 -6.0; 535 -5.8; 588 -5.9; 647 -5.8; 712 -5.7; 783 -5.8; 861 -5.6; 947 -5.4; 1042 -5.1; 1146 -4.8; 1261 -4.7; 1387 -4.7; 1526 -5.0; 1678 -5.9; 1846 -7.1; 2031 -7.6; 2234 -7.6; 2457 -7.1; 2703 -7.5; 2973 -7.6; 3270 -6.9; 3597 -5.6; 3957 -4.8; 4353 -5.0; 4788 -4.9; 5267 -6.2; 5793 -10.0; 6373 -10.8; 7010 -9.0; 7711 -11.6; 8482 -15.2; 9330 -14.7; 10263 -11.9; 11289 -11.0; 12418 -11.0; 13660 -10.8; 15026 -11.1; 16529 -13.0; 18182 -16.1; 20000 -17.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.42 | 6.4 dB  |
| Peaking | 1483 Hz  | 0.89 | 3.2 dB  |
| Peaking | 1957 Hz  | 3.16 | -1.8 dB |
| Peaking | 4424 Hz  | 1.86 | 6.7 dB  |
| Peaking | 19719 Hz | 0.03 | -6.9 dB |
| Peaking | 36 Hz    | 2.06 | -0.5 dB |
| Peaking | 66 Hz    | 2.9  | 0.5 dB  |
| Peaking | 7190 Hz  | 8.49 | 2.7 dB  |
| Peaking | 8763 Hz  | 4.13 | -4.4 dB |
| Peaking | 12699 Hz | 1.42 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | -8.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)