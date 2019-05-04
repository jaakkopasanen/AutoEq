# Beyerdynamic DT 880 32 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -0.8; 66 -1.1; 72 -1.5; 79 -1.9; 87 -2.4; 96 -2.9; 106 -3.4; 116 -3.9; 128 -4.3; 141 -4.7; 155 -5.0; 170 -5.2; 187 -5.4; 206 -5.4; 227 -5.4; 249 -5.5; 274 -5.6; 302 -5.6; 332 -5.6; 365 -5.7; 402 -5.9; 442 -6.2; 486 -6.0; 535 -5.9; 588 -6.0; 647 -6.0; 712 -5.9; 783 -5.9; 861 -5.6; 947 -5.5; 1042 -5.2; 1146 -5.0; 1261 -4.9; 1387 -4.9; 1526 -5.3; 1678 -6.2; 1846 -7.4; 2031 -8.1; 2234 -8.4; 2457 -8.1; 2703 -8.0; 2973 -7.7; 3270 -6.7; 3597 -5.5; 3957 -4.5; 4353 -4.6; 4788 -5.3; 5267 -6.8; 5793 -10.0; 6373 -9.8; 7010 -9.1; 7711 -12.5; 8482 -14.9; 9330 -12.9; 10263 -11.3; 11289 -12.0; 12418 -11.2; 13660 -10.0; 15026 -10.7; 16529 -12.9; 18182 -16.0; 20000 -17.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.39 | 6.4 dB  |
| Peaking | 1435 Hz  | 1.03 | 3.0 dB  |
| Peaking | 2090 Hz  | 1.85 | -2.3 dB |
| Peaking | 4298 Hz  | 1.82 | 6.5 dB  |
| Peaking | 19339 Hz | 0.05 | -6.7 dB |
| Peaking | 40 Hz    | 2.31 | -0.4 dB |
| Peaking | 67 Hz    | 2.9  | 0.4 dB  |
| Peaking | 7015 Hz  | 9.54 | 2.3 dB  |
| Peaking | 8447 Hz  | 5.71 | -3.7 dB |
| Peaking | 13876 Hz | 2.39 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.9 dB |
| Peaking | 16000 Hz | 1.41 | -8.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)