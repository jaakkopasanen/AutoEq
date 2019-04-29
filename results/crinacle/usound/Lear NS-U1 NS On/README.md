# Lear NS-U1 NS On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.9; 23 -15.0; 25 -15.0; 28 -15.0; 31 -14.9; 34 -14.8; 37 -14.7; 41 -14.5; 45 -14.2; 49 -14.1; 54 -13.9; 60 -13.6; 66 -13.4; 72 -13.3; 79 -13.2; 87 -13.0; 96 -12.9; 106 -12.8; 116 -12.7; 128 -12.6; 141 -12.4; 155 -12.2; 170 -11.9; 187 -11.7; 206 -11.5; 227 -11.2; 249 -11.0; 274 -10.7; 302 -10.6; 332 -10.4; 365 -10.3; 402 -10.2; 442 -9.9; 486 -9.3; 535 -8.2; 588 -6.3; 647 -3.4; 712 -0.6; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -2.6; 1387 -4.8; 1526 -6.3; 1678 -7.4; 1846 -8.3; 2031 -9.2; 2234 -9.6; 2457 -9.1; 2703 -8.8; 2973 -9.6; 3270 -11.1; 3597 -12.2; 3957 -13.2; 4353 -10.5; 4788 -5.3; 5267 -1.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.8
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

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.06 | -6.9 dB |
| Peaking | 905 Hz  | 1.21 | 9.4 dB  |
| Peaking | 2011 Hz | 1.85 | -3.5 dB |
| Peaking | 3919 Hz | 2.27 | -8.5 dB |
| Peaking | 5591 Hz | 2.51 | 8.8 dB  |
| Peaking | 26 Hz   | 0.88 | -1.7 dB |
| Peaking | 464 Hz  | 2.3  | -2.7 dB |
| Peaking | 801 Hz  | 0.18 | 1.4 dB  |
| Peaking | 1742 Hz | 0.53 | -1.3 dB |
| Peaking | 8201 Hz | 4.24 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Lear%20NS-U1%20NS%20On/Lear%20NS-U1%20NS%20On.png)