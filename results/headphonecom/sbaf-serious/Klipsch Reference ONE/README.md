# Klipsch Reference ONE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.7; 25 -12.9; 28 -13.1; 31 -13.3; 34 -13.4; 37 -13.5; 41 -13.5; 45 -13.4; 49 -13.4; 54 -13.4; 60 -13.4; 66 -13.4; 72 -13.4; 79 -13.3; 87 -13.3; 96 -13.2; 106 -12.9; 116 -12.3; 128 -11.9; 141 -12.3; 155 -12.3; 170 -11.7; 187 -11.5; 206 -10.9; 227 -10.9; 249 -10.4; 274 -10.0; 302 -9.1; 332 -8.2; 365 -7.0; 402 -5.7; 442 -4.2; 486 -3.1; 535 -2.7; 588 -2.3; 647 -2.1; 712 -2.2; 783 -2.5; 861 -3.3; 947 -4.3; 1042 -5.3; 1146 -5.7; 1261 -6.3; 1387 -7.5; 1526 -8.9; 1678 -9.8; 1846 -10.1; 2031 -9.8; 2234 -9.8; 2457 -9.5; 2703 -9.4; 2973 -9.3; 3270 -8.4; 3597 -6.7; 3957 -4.4; 4353 -2.3; 4788 -0.5; 5267 -3.6; 5793 -5.6; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Reference ONE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Reference ONE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.42 | -5.4 dB |
| Peaking | 655 Hz  | 0.61 | 14.6 dB |
| Peaking | 708 Hz  | 0.14 | -9.7 dB |
| Peaking | 4859 Hz | 1.39 | 8.8 dB  |
| Peaking | 17 Hz   | 1.02 | -1.3 dB |
| Peaking | 1227 Hz | 7.53 | 1.4 dB  |
| Peaking | 4832 Hz | 4.46 | 4.2 dB  |
| Peaking | 5575 Hz | 2.44 | -5.5 dB |
| Peaking | 6464 Hz | 5.11 | 6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 4.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Reference%20ONE/Klipsch%20Reference%20ONE.png)