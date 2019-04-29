# Lear NS-U1 NS On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.0; 23 -16.1; 25 -16.1; 28 -16.1; 31 -16.0; 34 -15.9; 37 -15.8; 41 -15.6; 45 -15.4; 49 -15.2; 54 -15.0; 60 -14.8; 66 -14.6; 72 -14.5; 79 -14.3; 87 -14.2; 96 -14.0; 106 -14.0; 116 -13.8; 128 -13.7; 141 -13.5; 155 -13.3; 170 -13.0; 187 -12.8; 206 -12.6; 227 -12.3; 249 -12.1; 274 -11.9; 302 -11.7; 332 -11.4; 365 -11.2; 402 -11.0; 442 -10.7; 486 -10.1; 535 -8.9; 588 -7.0; 647 -4.0; 712 -0.7; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.7; 1261 -3.1; 1387 -5.0; 1526 -6.2; 1678 -7.2; 1846 -8.1; 2031 -8.6; 2234 -8.4; 2457 -7.4; 2703 -6.7; 2973 -7.3; 3270 -8.9; 3597 -10.2; 3957 -11.6; 4353 -9.3; 4788 -4.4; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.3; 16529 -8.1; 18182 -9.3; 20000 -20.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lear NS-U1 NS On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lear NS-U1 NS On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.05 | -8.1 dB |
| Peaking | 889 Hz   | 1.29 | 9.9 dB  |
| Peaking | 1926 Hz  | 2.45 | -3.1 dB |
| Peaking | 3980 Hz  | 3.23 | -7.0 dB |
| Peaking | 5588 Hz  | 2.65 | 7.9 dB  |
| Peaking | 27 Hz    | 0.79 | -1.7 dB |
| Peaking | 275 Hz   | 0.34 | 0.8 dB  |
| Peaking | 473 Hz   | 2.76 | -2.3 dB |
| Peaking | 19917 Hz | 2.14 | -7.6 dB |
| Peaking | 20248 Hz | 0.66 | -6.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 8.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 16000 Hz | 1.41 | -3.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lear%20NS-U1%20NS%20On/Lear%20NS-U1%20NS%20On.png)